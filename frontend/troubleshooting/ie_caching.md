트러블 슈팅 중, IE에서 어떤 요청들이 캐싱되기 때문에 변경사항이 반영되지 않고 이전 결과물들이 렌더링되는 기괴한 현상을 겪게 되었다.

구글에 검색해보니 역시 나와 같은 현상을 겪는 사람이 이전부터 많았던 것 같다.

## 혼자 분석해 봤을 때...
어떤 XHR 요청이 처음에는 서버로 가다가, 위의 현상을 겪고 개발자 도구의 네트워크 탭을 보니 **(시작 캐시)**로 부터 도착했다는 문구가 있었다.
이유는 모르겠지만 요청에 대한 응답을 IE가 캐싱하고 있다는 의미이다.

캐싱 문제임을 확신한 이유는 개발자 도구의 네트워크 탭에 항상 서버로부터 가져오기라는 설정을 활성화시키니, 
매번 서버로 요청을 하게되었고 변경사항들이 그때그때 잘 반영되고 있었다.

여기저기 글을 찾아보니 IE가 AJAX Get request에 대한 응답을 캐싱하고 있고, 이런 현상을 겪는 사람이 꽤 있었던 것 같다.
여기서 멈추지 않고 왜 그럴까가 궁금했다.

IE의 설정을 보면 **웹 사이트 데이터 설정** 이라는 것이 있는데, 아래에 이러한 문구가 쓰여있다.

> 웹 페이지를 빠르게 불러오기 위해 Internet Explorer에서 웹 페이지, 이미지 및 미디어 복사본을 저장합니다.
> 저장된 페이지의 새 버전 확인 옵션이 존재한다.
>> default는 자동으로

저장된 페이지의 새 버전 확인 옵션에는 아래와 같은 것들이 더 존재한다.

1\. 웹 페이지를 열 때 마다
2\. Internet Explorer를 시작할 때 마다
3\. 자동으로
4\. 안 함

웹 페이지를 열 때마다로 활성화 시키면 implicit하게 캐싱하지않고 매번 새로 요청하게 되었고,
IE를 시작할 때마다는 IE를 다 닫고 창을 열기 전까지는 계속 캐싱된 상태를 유지하였고, 
자동으로는 잘 모르겠지만 어떤 것은 캐싱이 되고 어떤 것은 안되는 괴이함을 느꼈고,
안 함의 경우는 그냥 계속 캐싱이 되는 것 같았다. (확실하진 않음)

개발자가 유저의 브라우저 설정을 건드리는 건 권한 밖의 일이라 개발자 입장에서 해결 방법을 찾아야했다.


## 보통의 해결법들
#### url 마지막에 timestamp를 쿼리스트링으로 붙인다.
```
axios.get(`https://example.com/some_path?&timestamp=${new Date().getTime()}`)
```

서버의 구현 마다 다른데 불필요한 쿼리를 붙이면 에러를 뱉는 서버도 있다고 한다. 하지만 드문 행동일 것 같다.

#### `'Cache-Control': 'no-cache, no-store'` 를 헤더에 붙인다.
흠.. IE 하나를 대응하자고 서버의 Cache 정책을 무너뜨리고 싶진 않다. 다른 브라우저에선 멀쩡하기 때문이다.

#### POST 메소드를 사용
요것은 REST에 부합하지 않은 것 같아 사용하고 싶지 않다.

---
## Reference
- https://stackoverflow.com/questions/32261000/how-to-avoid-ajax-caching-in-internet-explorer-11-when-additional-query-string-p
- https://stackoverflow.com/questions/54567654/ie-11-issue-automatically-cache-responses-from-get-requests-reactjs
- https://jeonghwan-kim.github.io/dev/2019/08/12/ie-cache.html
- https://thisinterestsme.com/ajax-request-internet-explorer-cache/
