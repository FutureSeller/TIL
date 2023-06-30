폰트 로딩으로 인해 CRP에 영향을 주게 되는데, 이때 종종 쓰이는것이 preload이다.

아주 단적으로 https://web.dev/codelab-preload-web-fonts/ 이 페이지에 있는 방법을 쓰면 된다. 코드를 가져와보면 아래와 같다.

```html
<head>
 <link rel="preload" href="/assets/Pacifico-Bold.woff2" as="font" type="font/woff2" crossorigin>
</head>
```

`link`가 다른 리소스는 CORS를 보는 몇개 중 하나의 에셋이 폰트인데, 요 녀석이 safari와 만나면 아주 골치가 아프다.

font-face의 url의 경우, CORS 요청이기 때문에 preload 시 캐싱된 녀석을 사용하려면 crossorigin이 필요하다.

safari는 참... 이게 캐싱된걸 안가져오는데, 먼저 preload 할 때 요청헤더를 보면 `Vary: Origin, 기타 등등`이 있다. 
Origin을 캐시의 키중 하나로 보겠다는건데, 곤란한게 font-face url에 있는 폰트를 가져올 때 CORS 요청을 하지 않는다.
헤더를 보니 Origin이 없었다. 이로 인해 캐싱된걸 가져올 수 없는 상황이 생기게 되었다. (쩝..)

[뱅크샐러드](https://blog.banksalad.com/tech/font-preload-on-safari/)의 해소 방법을 보니 Cloudfront와 같이 cdn이 있고, 앞에 edge-function에서 강제로 헤더를 심는 방법으로 해결했는데, 뭔가 다른 방법이 없을까를 계속 고민해보고있는 중이다.
(결국 헤더를 심어야해서 중간 proxy가 필요해보이는데 말이다.)
