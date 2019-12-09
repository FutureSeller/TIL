# Mixin (믹스인)

> 다른 클래스를 상속받을 필요 없이, 클래스에 구현되어있는 메서드를 담고 있는 클래스

> 메서드를 제공하는데 단독으로 쓰이지 않고 다른 클래스의 행동을 더해주는 용도

- 자바스크립트 클래스는 다중 상속이 불가능함
- 슈퍼클래스를 인자로 받고, 이 슈퍼클래스를 확장하는 서브 클래스를 생성하여 반환하는 함수를 사용하여 구현할 수 있음

#### Example: MDN; Using HOC

```javascript
const calculatorMixin = Base =>
  class extends Base {
    calc() {
      return "calc";
    }
  };

const randomizerMixin = Base =>
  class extends Base {
    randomize() {
      return "randomize";
    }
  };

class Foo {}
class Bar extends calculatorMixin(randomizerMixin(Foo)) {}

const bar = new Bar();
console.log(bar.calc()); // calc
console.log(bar.randomize()); // randomize
```

#### Example: javascript.info; Using `Object.assign`

```javascript
let sayHiMixin = {
  sayHi() {
    alert(`Hello ${this.name}`);
  },
  sayBye() {
    alert(`Bye ${this.name}`);
  }
};

class User {
  constructor(name) {
    this.name = name;
  }
}

Object.assign(User.prototype, sayHiMixin);
new User("Dude").sayHi(); // Hello Dude!
```

---

## Reference

- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes#Mix-ins
- https://ko.javascript.info/mixins
