# iOS build and Xcode Cloud

Setup copied from the DerSchweigert repo (`sites/lesen/ios/RELEASING.md`): team `2F695PTZC6`, bundle ids `de.derschweigert.<app>`, manual-start workflow, automatic signing, TestFlight.

## What is in git
`ios/` is the Xcode project made by Ren'Py (`renpy.sh launcher ios_create`), with these changes:
- Bundle id `de.derschweigert.ovaravn`, team `2F695PTZC6`, automatic signing, iPhone only.
- Version comes from `MARKETING_VERSION` (1.0) and `CURRENT_PROJECT_VERSION` (1). Xcode Cloud raises the build number itself.
- Shared scheme `TheManTheTideBroughtIn` (Release archive).

Not in git (about 740 MB, gitignored): `ios/base/` (the packaged game), `ios/prebuilt/` and `ios/Frameworks/` (Ren'Py engine).
`ios/ci_scripts/ci_post_clone.sh` downloads Ren'Py 8.6.1 and its iOS add-on and rebuilds those three folders. Run it by hand to build locally.

## Verified
- Unsigned simulator build succeeds (`xcodebuild ... CODE_SIGNING_ALLOWED=NO build`).
- `ci_post_clone.sh` runs to the end on this Mac and produces all three folders.

## Not verified
- That the script runs on Xcode Cloud's machines (Ren'Py's launcher headless, download time).
- Signing, archive, TestFlight, and a run on a real iPhone.
- The app icon is still the Ren'Py placeholder. Add `game/ios-icon.png` (1024x1024), then rerun the script.

## One-time steps for the owner (Apple side)
1. Push this branch to GitHub.
2. App Store Connect: create an iOS app with bundle id `de.derschweigert.ovaravn`.
3. Xcode: open `ios/TheMantheTideBroughtIn.xcodeproj`, sign in, confirm Signing & Capabilities shows the team.
4. Product > Xcode Cloud > Create Workflow. Authorize GitHub for `UrsSchweigert/OvaraVN`.
5. Workflow: manual start; action Archive, iOS, scheme `TheManTheTideBroughtIn`, Release; post-action TestFlight (internal).
6. Start the first build. If it fails, read `ci_post_clone.log` first.
