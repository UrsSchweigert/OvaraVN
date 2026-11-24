#!/bin/zsh
# usage: gen4.sh name purpose chapter-file-prompt ref1 ref2 ... ; writes new4/name.png (raw) 
cd /Users/ursschweigert/Documents/GitHub/OvaraVN
name=$1; purpose=$2; shift 2
args=(); for x in "$@"; do args+=(--ref $x); done
./vn image nano-banana-2 --purpose $purpose --chapter 18 --aspect 16:9 --out art/refs/ch18/new4/$name.png --prompt-file art/refs/ch18/new4/$name.txt $args 2>&1 | tail -3
python3 - <<PY
from PIL import Image
im=Image.open("art/refs/ch18/new4/$name.png"); print(im.size)
PY
