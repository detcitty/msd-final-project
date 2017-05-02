#~/bin/bash
cut -d'|' -f1 us_billboard.psv | sort -nr | uniq -c > this_week_position_distribution.txt
cut -d'|' -f5 us_billboard.psv | sort -nr | uniq -c | sort -nr > song_counts.txt
