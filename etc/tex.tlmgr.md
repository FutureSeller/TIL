LaTex으로 작업할 일이 조금 있는데, 다른 환경에서 작업하려고 하니 package들이 꼬여있었다.

``` bash
$ xelatex ...
...
! LaTeX Error: File `fullpage.sty' not found.
...
```

처음부터 다시 하나씩 잡아주려고 의존성을 찾기위해, [CTAN:fullpage](https://www.ctan.org/pkg/fullpage)을 방문
>The package is part of the preprint bun­dle.

bash로는 아래와 같이 검색
``` bash
$ tlmgr info fullpage
tlmgr: cannot find package fullpage, searching for other matches:

Packages containing `fullpage' in their title/description:
context-fullpage - Overfull pages with ConTeXt
dpfloat - Support for double-page floats
phffullpagefigure - Figures which fill up a whole page
preprint - A bundle of packages provided "as is"
```

해당 의존성 해소를 위해 package 설치
``` bash
$ tlmgr install preprint
```
