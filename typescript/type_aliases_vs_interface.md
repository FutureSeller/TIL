# Type Aliases vs. Interface

TypeScript의 공식문서를 읽다가 Type Aliases와 Interface의 차이에 대한 본문을 보게되었다.

**As we mentioned, type aliases can act sort of like interfaces; however there are some subtle differences.**

> One difference is that interfaces create a new name that is used everywhere. Type aliases don’t create a new name
> - for instance, error messages won’t use the alias name.
> - hovering over interfaced in an editor will show that it returns an Interface, but will show that aliased returns object literal type.

처음 읽고 든 생각은 ????????? 였다. ~그래서 뭐 어쩌라는 거지, 큰 의미 없어보이는데...

> In older versions of TypeScript, type aliases couldn’t be extended or implemented from (nor could they extend/implement other types). 

> As of version 2.7, type aliases can be extended by creating a new intersection type

여기 찾아보니 공식문서가 outdated 라고 한다. 좀 충격이였다. ~wow~

그럼 도대체 어떤 차이를 가지고 사용해야할까?

공식 문서를 과감히 접고 우선 stackoverflow 내용들을 적당히 추려봤다.

#### Diff 1. Syntax
이걸로 type과 interface를 가려쓸 이유는 못되는 것 같다.

``` typescript
interface Point {
  x: number;
  y: number;
}

interface SetPoint {
  (x: number, y: number): void;
}

type Point = {
  x: number;
  y: number;
};

type SetPoint = (x: number, y: number) => void;
```

#### Diff 2. Other types: primitives, unions, and tuples
type alias는 보통 primitive나 union, 그리고 tuple을 정의하는데 쓰인다고 한다.
아니 그런데(!), interface도 약간 성격 그리고 가독성 차원에서 다르지만 tuple이 가능하다고 한다.

``` typescript
// primitive
type Name = string;

// object
type PartialPointX = { x: number; };
type PartialPointY = { y: number; };

// union: type
type PartialPoint = PartialPointX | PartialPointY;

// union: 

// tuple: type
type Data = [number, string];

// typle: interface
interface Data {
  0 : number,
  1 : string
}
```

#### Diff 3. Extend: 이것도 결국 Syntax
두 개가 `not mutually exclusive` 하다고 함. 결국 각각 extend가 가능하다.
interface는 `extends`, type alias는 `&` 를 쓴다.
이것도 역시 type과 interface를 가려쓸 이유는 못되는 것 같다.

``` typescript
// Interface extends interface
interface PartialPointX { x: number; }
interface Point extends PartialPointX { y: number; }

// Type alias extends type alias
type PartialPointX = { x: number; };
type Point = PartialPointX & { y: number; };

// Interface extends type alias
type PartialPointX = { x: number; };
interface Point extends PartialPointX { y: number; }

// Type alias extends interface
interface PartialPointX { x: number; }
type Point = PartialPointX & { y: number; };
```

#### Diff 4. Implements
둘 다 implements 가능함. 
그런데, **they can not implement / extend a type alias that names a union type.** 이렇다고 한다.


``` typescript
interface Point {
  x: number;
  y: number;
}

class SomePoint implements Point {
  x: 1;
  y: 2;
}

type Point2 = {
  x: number;
  y: number;
};

class SomePoint2 implements Point2 {
  x: 1;
  y: 2;
}

type PartialPoint = { x: number } | { y: number };

// ERROR: can not implement a union type
class SomePartialPoint implements PartialPoint {
  x: 1;
  y: 2;
}
```

#### Diff 5. Declaration Merging
이게 그나마 제일 큰 차이 인 것 같고, 유용한 혹은 경우에 따라 사용하기 매우 까다로운 특징일 것 같다.
같은 이름의 interface는 나중에 알아서 merge가 된다.

**an interface can be defined multiple times, and will be treated as a single interface**

``` typescript
interface Point { x: number; }
interface Point { y: number; }

const point: Point = { x: 1, y: 2 };
```

#### Summary
- type이 union 되면: class에서 implements할 수 없고 interface에서 extends 할 수 없음. 약간 좀 더 static 한 느낌
- 확장성 및 가변성이 강한 것을 정의할 때 `interface`, 불변성이 강한 것들을 정의할 때 `type`을 쓰는 것이 좋아보임
- React in Props & State 에서는?
  - interface를 사용해도 상관 없음.
  - declaration merging이나 implements는 필요 없어 `type`이 좀 더 나을 수 있음.

***사실 오류만 안내고 일관성 있게 그냥 취향 껏 잘 정의해서 쓰면 될 것 같다.***


---
## Reference
- http://www.typescriptlang.org/docs/handbook/advanced-types.html#interfaces-vs-type-aliases
- https://medium.com/@martin_hotell/interface-vs-type-alias-in-typescript-2-7-2a8f1777af4c
- https://joonsungum.github.io/post/2019-02-25-typescript-interface-and-type-alias
- https://codingblast.com/typescript-tuples
