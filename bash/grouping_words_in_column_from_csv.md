csv file에서 특정 column의 값들을 grouping하여 count할 상황이 있다.
코드를 작성해도 상관없지만 복잡하지 않은 간단한 작업이라면 아래와 같이 확인할 수 있다.

``` bash
# download a simple csv file
$ wget -q https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv

# remove trailing newline
$ cat biostats.csv | head -c -1 > biostats.csv
"Name",     "Sex", "Age", "Height (in)", "Weight (lbs)"
"Alex",       "M",   41,       74,      170
"Bert",       "M",   42,       68,      166
"Carl",       "M",   32,       70,      155
"Dave",       "M",   39,       72,      167
"Elly",       "F",   30,       66,      124
"Fran",       "F",   33,       66,      115
"Gwen",       "F",   26,       64,      121
"Hank",       "M",   30,       71,      158
"Ivan",       "M",   53,       72,      175
"Jake",       "M",   32,       69,      143
"Kate",       "F",   47,       69,      139
"Luke",       "M",   34,       72,      163
"Myra",       "F",   23,       62,       98
"Neil",       "M",   36,       75,      160
"Omar",       "M",   38,       70,      145
"Page",       "F",   31,       67,      135
"Quin",       "M",   29,       71,      176
"Ruth",       "F",   28,       65,      131

# number of users those are grouped by sex
$ tail -n +2 biostats.csv | cut -d',' -f2 | sort | uniq -c
      7        "F"
     11        "M"
```
