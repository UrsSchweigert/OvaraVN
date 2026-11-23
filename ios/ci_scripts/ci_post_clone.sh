#!/bin/bash
# Xcode Cloud post-clone hook.
# The Xcode project in ios/ is committed, but the Ren'Py engine libraries
# (prebuilt/, Frameworks/) and the packaged game (base/) are too big for git.
# This script downloads the pinned Ren'Py SDK, packages the game, and fills them in.
set -euo pipefail
trap 'status=$?; echo "OvaraVN preparation failed at line $LINENO (exit $status)." >&2; exit "$status"' ERR

RENPY_VERSION="8.6.1"
RENPY_SHA256=""   # optional: pin the tarball hash here once recorded

if [[ -n "${CI_PRIMARY_REPOSITORY_PATH:-}" ]]; then
    ROOT="$CI_PRIMARY_REPOSITORY_PATH"
else
    ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
fi
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

cd "$WORK"
curl -fsSL -o sdk.tar.bz2 "https://www.renpy.org/dl/${RENPY_VERSION}/renpy-${RENPY_VERSION}-sdk.tar.bz2"
if [[ -n "$RENPY_SHA256" ]]; then
    echo "$RENPY_SHA256  sdk.tar.bz2" | shasum -a 256 -c -
fi
tar -xjf sdk.tar.bz2
SDK="$WORK/renpy-${RENPY_VERSION}-sdk"
# The iOS add-on (renios) is a separate download; it unpacks to renios/ in the SDK.
curl -fsSL -o renios.zip "https://www.renpy.org/dl/${RENPY_VERSION}/renpy-${RENPY_VERSION}-renios.zip"
unzip -q renios.zip -d "$SDK"

# Build a throwaway Xcode project, then copy only the heavy parts into ios/.
# Images ship as WebP to keep the app small; the PNG masters in git stay as they are.
command -v cwebp >/dev/null 2>&1 || HOMEBREW_NO_AUTO_UPDATE=1 brew install webp
python3 "$ROOT/tools/webp_game.py" "$ROOT/game" "$WORK/game_webp"

export SDL_VIDEODRIVER=dummy
cd "$SDK"
./renpy.sh launcher ios_create "$WORK/game_webp" "$WORK/ios"
for d in base prebuilt Frameworks; do
    rm -rf "$ROOT/ios/$d"
    cp -R "$WORK/ios/$d" "$ROOT/ios/$d"
done
# MetalANGLE ships a 32-bit armv7 slice that no supported iPhone uses. Drop it (saves about 8 MB).
XCF="$ROOT/ios/Frameworks/MetalANGLE.xcframework"
LIB="$XCF/ios-arm64_armv7/MetalANGLE.framework/MetalANGLE"
if lipo -info "$LIB" 2>/dev/null | grep -q armv7; then
    lipo -remove armv7 "$LIB" -output "$LIB"
    /usr/libexec/PlistBuddy -c "Delete :AvailableLibraries:0:SupportedArchitectures:1" "$XCF/Info.plist" || true
fi
echo "Ren'Py $RENPY_VERSION payload ready in ios/."
