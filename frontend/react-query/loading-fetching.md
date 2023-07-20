팀 내 스터디를 하다가 나왔던 내용. `isLoading과 isFetching은 무슨 차이일까?`

결론:

> 좀 더 자세히 이야기를 하면 isLoading, isFetching은 그 쿼리에 cacheData가 있는지 없는지로 결정 되는데욤
> 쿼리 기본 cacheTime이 5분인데, 5분동안 fetch가 일어나지 않은 경우 cacheData도 날립니다. 그래서 5분이 지난 이후 사용자가 다시 fetch시도를 하면 캐싱된 데이터도 없어서 다시 isLoading 상태가 true가 되지만, cacheTime이 지나기 전 fetch가 다시 일어나면 isFetching 상태가 true가 됩니다

짧게 요약하자면
```
isLoading: 첫 진입 상태. fetch가 일어난 적이 없는 상태에서 비동기 처리 상태
isFetching: 한번 이상 로딩이 되어 캐시된 데이터가 있는 상태에서 비동기 처리 나타내는 상태
```
