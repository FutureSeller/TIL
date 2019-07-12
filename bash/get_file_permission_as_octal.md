## `man stat`
```
-c  --format=FORMAT
              use the specified FORMAT instead of the default; output a newline after each use of FORMAT
%a     access rights in octal
%n     file name
```

``` bash
$ stat -c "%a %n" test.txt
644 text.txt
```

---
## Reference
- https://askubuntu.com/questions/152001/how-can-i-get-octal-file-permissions-from-command-line
