#!/bin/zsh
cd /Users/ursschweigert/Documents/GitHub/OvaraVN
name=$1; purpose=$2; shift 2
args=(); for x in "$@"; do args+=(--ref $x); done
./vn image nano-banana-2 --purpose $purpose --chapter 18 --aspect 16:9 --out art/refs/ch18/new5/$name.png --prompt-file art/refs/ch18/new5/$name.txt $args 2>&1 | tail -2
