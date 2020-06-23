# WebP (웹피, weppy)

> 구글이 개발한 손실/비손실 압축 이미지 파일을 위한 이미지 포맷

- 확장자: `.webp`
- 미디어 타입: `image/webp`
- 목적: 웹사이트의 트래픽 감소 및 로딩 속도 단축을 겨냥. 압축 효과가 높은 것으로 알려져있음
- 손실 압축(JPEG) 화질 저하를 최소화하면서 파일 크기를 축소l 25-34%
- 비손실 압축(PNG, GIF)도 용량을 줄여줌; 26% smaller
- 브라우저마다 지원여부가 갈림
  - IE는 당연히 안되고, Safari 진영에서 조만간 지원하는 듯함
  - https://caniuse.com/#search=webp 여길 확인해보니 조만간 최신버전들에선 다 지원하는 듯 함.

## Using WebP in HTML
```html
<img src="img/path-to-image.webp" alt="...">

<picture>
  <source srcset="img/path-to-image.webp" type="image/webp">
  <source srcset="img/path-to-image.jpg" type="image/jpeg">
  <img src="img/creakyOldJPEG.jpg" alt="Alt Text!">
</picture>
```

## Using WebP Images in CSS
```css
.no-webp .elementWithBackgroundImage {
  background-image: url("image.jpg");
}

.webp .elementWithBackgroundImage{
  background-image: url("image.webp");
}
```

이렇게 두고 JS로 제어하면 됨.

## 단점은?
- 이전 브라우저를 위해 다른 미디어 타입의 여러벌의 이미지를 가지고 있어야 함
- WebP로 변환해야할 이미지가 너무 많으면 전환을 하지 않는 결정을 할 수 있음
- CSS에서 WebP 이미지를 사용해야 하는 경우, JS를 관리해줘야 함.

---
## Reference
- https://developers.google.com/speed/webp
- https://ko.wikipedia.org/wiki/WebP
- https://css-tricks.com/using-webp-images/
