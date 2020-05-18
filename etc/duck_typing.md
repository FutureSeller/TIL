# Duck Typing

> 동적 타이핑의 한 종류로, 객체의 변수 및 메소드의 집합이 객체의 타입을 결정하는 것
>> 객체가 어떤 타입에 걸맞은 변수와 메소드를 지니면 객체를 해당 타입에 속하는 것으로 간주함

즉, 타입을 미리 정하는 것이 아니라 실행되었을 때, 프로퍼티와 메소드들을 확인

- 장점: dynamic. runtime-based
- 단점: runtime-based로부터 오는 단점들

---

인상 깊은 문구: 
> 만약 어떤 새가 오리처럼 걷고, 헤엄치고, 꽥꽥거리는 소리를 낸다면 나는 그 새를 오리라고 부를 것이다.

```python
class Duck:
        def quack(self): print u"꽥꽥!"
        def feathers(self): print u"오리에게 흰색, 회색 깃털이 있습니다."

class Person:
        def quack(self): print u"이 사람이 오리를 흉내내네요."
        def feathers(self): print u"사람은 바닥에서 깃털을 주어서 보여 줍니다."

def in_the_forest(duck):
        duck.quack()
        duck.feathers()

def game():
        donald = Duck()
        john = Person()
        in_the_forest(donald)
        in_the_forest(john)
```


---
## Reference
- https://ko.wikipedia.org/wiki/%EB%8D%95_%ED%83%80%EC%9D%B4%ED%95%91
