#!/bin/bash
# Taken from: https://askubuntu.com/questions/475694/awk-command-to-print-all-the-lines-except-the-last-three-lines


for i in db_lyrics/*; do
    awk '{l[NR] = $0} END {for (i=1; i<=NR-3; i++) print l[i]}' i > i
done
