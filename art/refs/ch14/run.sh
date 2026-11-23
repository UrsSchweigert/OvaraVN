#!/bin/zsh
# usage: run.sh model purpose out txtfile refs...
cd /Users/ursschweigert/Documents/GitHub/OvaraVN
m=$1; p=$2; out=$3; txt=$4; shift 4
args=(); for r in "$@"; do args+=(--ref $r); done
./vn image $m --purpose $p --chapter 14 --out $out --prompt-file <(sed '1,/^$/d' $txt) $args
