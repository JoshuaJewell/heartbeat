#!/bin/bash

git checkout -b new-branch
start_date=$(date -d "2023-01-01" +%s)
end_date=$(date -d "2023-12-31" +%s)

i=$start_date
while [ $i -le $end_date ]; do
  date_str=$(date -d "@$i" +"%Y-%m-%d")
  git commit --allow-empty -m "Daily commit on $date_str"
  i=$((i + 86400))
done

git checkout main
git reset --hard new-branch
git branch -D new-branch
