#!/bin/bash
# usage: run.sh name model purpose outdir [refs...]
cd /Users/ursschweigert/Documents/GitHub/OvaraVN
n=$1; m=$2; pu=$3; d=$4; shift 4
ch=${n#c}; ch=${ch%%_*}
args=(); for r in "$@"; do args+=(--ref "$r"); done
./vn image $m --prompt-file art/refs/stage_b/$d/$n.prompt "${args[@]}" --out art/refs/stage_b/$d/$n.png --purpose $pu --size 1920x1080 --chapter $ch > art/refs/stage_b/$d/$n.log 2>&1
