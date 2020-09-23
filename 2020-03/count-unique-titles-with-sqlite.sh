#!/bin/sh
# 2020-03 author: Ian Lessing.
# using a "here-doc" to pass commands from shell script to sqlite
# as suggested https://unix.stackexchange.com/questions/445612/sqlite3-command-line-how-to-set-mode-and-import-in-one-step
echo "Number of unique titles from authors-table.csv: "
sqlite3 <<END_COMMANDS
.mode csv
.import authors-table.csv authors
select count(distinct(title)) from authors;
END_COMMANDS
