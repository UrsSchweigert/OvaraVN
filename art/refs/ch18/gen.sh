#!/bin/zsh
# usage: gen.sh art/refs/ch18/places/name   (reads name.txt, writes name.png)
cd /Users/ursschweigert/Documents/GitHub/OvaraVN
b=$1
m=$(sed -n 's/^model: //p' $b.txt); p=$(sed -n 's/^purpose: //p' $b.txt); r=$(sed -n 's/^refs: *//p' $b.txt)
case $m in fal-ai/flux-2/edit) mm=flux-2;; fal-ai/flux-2) mm=flux-2-t2i;; *) mm=$m;; esac
args=(); for x in ${(s:, :)r}; do [ -n "$x" ] && args+=(--ref $x); done
./vn image $mm --purpose $p --chapter 18 --size 1920x1088 --out $b.png --prompt-file <(sed '1,/^$/d' $b.txt) $args 2>&1 | tail -2
