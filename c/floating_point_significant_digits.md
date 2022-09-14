float은 유효 자리수가 6-7 이고, double은 15-16 자리수까지 유효하다.
기본적으로 double 형은 소수점 6자리까지 출력하게 되어있어 유의해야함. 출력 시 하위 자리수까지 찍으려면 `printf("%.12lf");` 이런식으로 자릿수를 나타내면 됨.

---

## Reference

https://docs.microsoft.com/ko-kr/cpp/c-language/type-float?view=msvc-170

