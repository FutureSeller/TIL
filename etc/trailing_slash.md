# Trailing Slash

> URL 끝에 붙이는 슬래시

/ 로 끝나는 URL은 도메인 + 파일과 정확히 매칭되지 않는다면 당연히 '디렉토리'라고 생각하고 있었다.
directory listing이라는 엄청난 취약점이 머릿속 깊이 박혀있었기 때문이다.

fundamental한 동작을 간과했었던 것 같고, 잘못 알고 있었던 부분이 있어 정리하고자 한다.
(https://djkeh.github.io/articles/Why-do-we-put-slash-at-the-end-of-URL-kor/ 를 참고했다.)

### Basic
``` bash
https://www.example.com/path  # file
https://www.example.com/path/ # directory
```

### 클라이언트 입장 (도메인을 통해 접속)
구글이나 네이버에 접속할 때 우리는 `https://www.google.com`이라고 브라우저의 address bar에 입력하지 `https://www.google.com/`이라고 입력하진 않는다.

그런데 url scheme을 다시 생각해보면 리소스가 파일인지 디렉토리인지 결정하는 요소는 host가 아니라 path 이다.

```
scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
```

`https://www.google.com/` 이 좀더 명시적으로 루트 경로인 `/`을 지정한 것과 다름 없다.

사용자 입장에서 trailing slash를 붙이기 귀찮으니까 브라우저에서 붙여준다고 한다.

### 서버의 입장

#### Trailing slash가 없는 URL: 우선 파일로 간주
- 해당 이름의 파일이 존재하는지를 먼저 확인
- 없을 경우, 해당 이름의 디렉토리를 확인
- 디렉토리가 있으면, 그 안의 기본 파일(`index.html`)을 확인

#### Trailing slash가 있는 URL: 우선 디렉토리로 간주
- 해당 이름의 디렉토리를 확인
- 디렉토리가 있으면, 그 안의 기본 파일(`index.html`)을 확인
  - 이 부분이 내가 잘못 알고 있던 부분이다.
  - 당연히 디렉토리로 인식해서 존재하지 않으면 **모든 서버가 404를 내려줄 것**이라고 생각했다.
  - 그러나, **서버가 이 로직을 어떻게 해소할 것이냐**에 따라 달라질 수 있다는 것을 간과했다.

> Tip: 디렉토리 리소스를 요청하는 경우, trailing slash를 명시하면 파일 확인하는 동작을 생략할 수 있음

> (Security): 디렉토리를 보여준다 === Information disclosure가 발생할 수 있다는 점에서 권장하진 않음

### 검색 엔진 봇의 입장 (Google)

```
http://example.com/foo/ (with trailing slash, conventionally a directory)
http://example.com/foo (without trailing slash, conventionally a file)
```

> Google treats each URL above separately (and equally) regardless of whether it’s a file or a directory, or it contains a trailing slash or it doesn’t contain a trailing slash.

그냥 둘 다 개별적으로 동등한 입장에서 처리한다고 한다.

> Don't both return a 200 response code, but that one version redirects to the other

이 문구를 보면 뭔가 손해가 있지 않을까라는 생각을 하게 될 수 밖에 없다.

#### 혹시 SEO에 영향을 주나?

다른 article의 문구를 발췌한 내용은 아래와 같다.

> The slashes play an important role in search engine optimization, especially in the area of duplicate content.

- 왜?
  - 위의 봇 입장에서보면 둘 다 개별적으로 동등한 입장에서 처리됨
  - 조금 풀어서 말하자면 동일한 컨텐츠임에도 불구하고 inbound가 다를 수 있어 url 들이 각각 rank가 매겨짐. 분산되는 손해가 있을 수 있음
  - 예가 적절할진 모르겠지만, 대선에서 같은 정당인데 후보자 두 명이 나오는 느낌(?)
- 그럼 어떻게 하나? 
  - 근본적인 해결: **Avoiding duplicate content**
  - 그게 어렵다면?
    - trailing slash 여부와 관계없이 동일한 리소스를 내려준다면 둘 중 하나에 `301 redirect` 응답을 내려주면 됨
    - `<link rel="canonical" href=.... />`
    - robots.txt 를 사용하여 적절히 제한
    - 등등... [[link](https://webmasters.googleblog.com/2009/08/optimize-your-crawling-indexing.html)]

그런데, 구글 웹마스터 article에는 또 아래와 같은 문구가 있다(!)

> Leave it as-is. Many sites have duplicate content. Our indexing process often handles this case for webmasters and users.

즉, 너네가 해결해주면 좋겠지만 가능한 수준에서 우리가 해줄게라는 얘기다.

---
## Reference
- https://djkeh.github.io/articles/Why-do-we-put-slash-at-the-end-of-URL-kor
- https://en.ryte.com/wiki/Trailing_Slashes
- https://ko.wikipedia.org/wiki/URL
- https://stackoverflow.com/questions/42212122/why-django-urls-end-with-a-slash
- https://webmasters.googleblog.com/2010/04/to-slash-or-not-to-slash.html
- https://www.seroundtable.com/google-trailing-slashes-url-24943.html