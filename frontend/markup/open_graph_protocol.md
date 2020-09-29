# Open Graph protocol

> Open Graph protocol enables any web page to become a rich object in social graph.

페이스북에서 최초로 정의한 메타 태그 유약. 프리뷰에 활용.
특정 정보를 웹사이트에서 미리 간략하게 정리하면 일관된 정보를 전달할 수 있음.
`<head>` 영역에 추가하면 페이스북 봇이 해당 메타데이터를 읽어서 내용을 표시함.

## Basic Metadata

- `og:title`: the title of your object as it should appear within the graph
- `og:type`: the type of your object; `video. movie`
- `og:image`: ad image url which should represent your object within the graph
- `og:url`: canonical url of your object that will be used as its permanent ID in the graph

```html
<html prefix="og: https://ogp.me/ns#">
  <head>
    <title>The Rock (1996)</title>
    <meta property="og:title" content="The Rock" />
    <meta property="og:type" content="video.movie" />
    <meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
    <meta
      property="og:image"
      content="https://ia.media-imdb.com/images/rock.jpg"
    />
    ...
  </head>
  ...
</html>
```

추가로 아래와 같은 것들이 있음.

- `og:description`: one to two sentence description of your object
- `og:locale`: the locale these tags are marked up in. (default is en_US)
- `og:locale:alternate`: array of other locales
- `og:site_name`: the name which should be displayed for the overall site

각각의 메타 데이터에 attribute를 붙이는 방식으로 사용될 수 있음.

- `og:image:url`: `og:image`와 같음
- `og:image:scure_url`: https
- `og:image:type`, `og:image:width`, `og:image:height`, `og:image:alt`

만약 다수의 값을 가지고 싶다면 같은 맥락의 `<meta>` 태그를 아래애 추가하면 됨.

이녀석도 TTL이 있고 `og:ttl`로 제어하며 이 값은 페이스북 크롤러가 다시 스크랩하는 주기를 나타냄.

## 테스트 및 pros and cons

- 테스트 해보려면 https://developers.facebook.com/tools/debug/ 에 가서 해보면됨
  - 웹문서 상 오픈그래프가 바뀌었어도 바로 반영되지 않을 수 있음
  - CDN캐싱이 되어 있으면 TTL이 있기 때문에 리로드가 가끔 필요함
- pros
  - 링크 프리뷰에 알맞는 이미지와 제목을 부여해 줄 수 있음
  - 특히 마케팅에 유용하며 링크가 복잡해도 정확한 정보를 전달할 수 있음
- cons
  - 대다수의 서비스들이 이에 준하는 마크업을 작성하고 있으나 표준은 아님; 예를 들면 트위터는 자체적인 메타데이터 표기법을 가지고 있음
  - 유저입장에서 불필요한 정보를 로드하게 됨
  - 페이스북에 너무 많은 데이터를 제공해 주게 됨

---

## Reference

- https://ogp.me/
- https://www.facebook.com/notes/response-media/pros-and-cons-of-facebooks-open-graph-initiative/118232828216869/
- https://devtalk.kakao.com/t/topic/22238
