# Hoisting (호이스팅)

크게 착각을 하고있었던 부분이 있었고, 다시 한번 정리가 필요하다고 생각했다.

> Hoisting: 변수를 선언하고 초기화했을 때 선언 부분이 최상단으로 끌어올려지는 현상

> 스코프 안에서 선언된 변수는 최상위에서 선언된 것과 동등함

> 선언 코드가 최상단으로 옮겨진다고 표현하지만, 실제 메모리에서는 변화가 없다고 함

### 왜 이런 현상이 발생할까?

> 인터프리터가 코드를 해석할 때 변수 및 함수의 선언 처리, 실제 코드 실행의 두단계로 나눠서 처리하기 때문

이 문장을 보고 처음 든 생각은 파서가 변수를 처리할 때 
scope을 기준으로 파싱해놓고 (symtab을 만들어 놓는다던지)
실제 코드 실행할 때 바인딩하는 듯 한 느낌을 받았다.

### JavaScript 인터프리터 내부에서 변수는 총 3단계에 걸쳐 생성된다고 한다.
- 선언 (Declaration): 스코프와 변수 객체가 생성되고 스코프가 변수 객체를 참조
- 초기화 (Initalization): 변수 객체가 가질 값을 위해 메모리에 공간을 할당. 이 때 초기화되는 값은 undefined
- 할당 (Assignment): 변수 객체에 값을 할당

### var vs. let & const: "TDZ"
var는 선언, 초기화가 동시에 이루어짐. 즉, 메모리에 공간 할당함.
let, const는 선언은 되어있지만 메모리 할당은 안된 상태임. 
이를 TDZ(Temporary Dead Zone)에 들어가 있다고 한다.

TDZ는 바인딩이 되기 전까지 변수에 access할 수 없는 현상을 의미함.

즉, let과 const도 hoisting이 발생하는데 TDZ에 있어 access가 불가능함.

---
## Reference
- https://developer.mozilla.org/ko/docs/Glossary/Hoisting
- https://www.zerocho.com/category/JavaScript/post/5741d96d094da4986bc950a0
- https://medium.com/@Dongmin_Jang/javascript-closure-hoisting-7bf8eb5062b9
- https://evan-moon.github.io/2019/06/18/javascript-let-const
