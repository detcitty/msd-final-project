#!/bin/bash
file_name="../data/us_billboard_25.psv"
cut -d'|' -f1 $file_name | sort -nr | uniq -c > this_week_position_distribution.txt
cut -d'|' -f5 $file_name | sort -nr | uniq -c | sort -nr > song_counts.txt
cut -d'|' -f5 $file_name | sort -nr | uniq > song_names.txt
