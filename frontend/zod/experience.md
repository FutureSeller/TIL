# Zod experience

## ~ 2023-07-20

최근 프로덕트에 zod를 점진적으로 적용해보고 있는데 경험이 꽤 괜찮다. 

이걸 도입하고 팀 내에서 가장 많이 바뀐 것은 `schema first`로 생각하고 일을 진행한다는 것이다.
우리가 그려야 할 화면은 결국 모델간 의존성/제약사항까지 동반되는 경우가 대부분이고, 이것들이 흩어져있거나 재정의가 되어야할때마다 우리의 부채는 쌓여가는 구조였다.

https://tkdodo.eu/blog/type-safe-react-query 요 글의 예시 중 하나가 가장 와닿는데,

```javascript
const fetchTodo = async (id: number) => {
  const response = await axios.get(`/todos/${id}`)
  // 🎉 parse against the schema
  return todoSchema.parse(response.data)
}
```

schema.parse를 통해서 response가 스키마에 맞게 들어오고있는지 런타임에 검증해준 다음, 에러를 뱉거나 응답을 주기 때문이다.
(물론 런타임 오버헤드는 측정해보지 않아서 정확히는 모르는데, 애초에 응답이 그렇게 복잡하지 않기 때문에 오버헤드가 클거라고는 생각하지 않는다)

개발을 하면서 심리적인 안정감도 조금 가질 수 있는 것 같고, 무엇보다 꽤 괜찮은 장점 중 하나는 에러의 원인을 파악하는데 들이는 시간을 꽤나 줄일 수 있다는 점이다.
정의한 스키마에 따른 에러 메시지를 정의할 수 있고, 어떤 필드가 제약사항을 어겼는지 뱉어주기 때문이다.

약간의 불편한 점은 조금 유연하게 스키마를 가져가려면 `nullable`, `nullish` 같은 녀석들이 붙기 마련인데, 이것들이 덕지덕지 붙게되면 좀 오묘하다.
