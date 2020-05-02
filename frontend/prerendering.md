# Pre-rendering

> To generate the site in advance

## 이 기술이 왜 필요했고 어떻게 동작하는가?
- Why: preload all elements on the page for a web cralwer to see it
- How
  - UA를 보다가 bot임을 알게 되면, prerender middleware가 statically 캐싱된 버전을 서빙해 줌
  - HTTP Caching 헤더를 통해 만료기간 등을 제어할 수 있음

## Advantages
- Speed: 기존에 요청 시, data + template > markup 생성하던 걸 생략하고 바로 asset들을 내려줌
- Security: pre-rendering된 static asset들만 서빙하기 때문에 ~부가적 연산으로 인한 개입이 없음~
- Scale: 기존 구조에선 각 계층 사이마다 Caching layer를 두어야하는데, CDN이 알아서 해줌
- Certainty
  > But by pre-rendering our sites we can be certain that our pages are correct before we deploy them

---
## Reference
- https://www.hawksworx.com/blog/prerendering/
- https://www.netlify.com/blog/2016/11/22/prerendering-explained/
- https://docs.netlify.com/site-deploys/post-processing/prerendering/#external-services
