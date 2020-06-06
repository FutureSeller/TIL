# Properly Size Images

> all images in your page that aren't appropriately sized, along with the potential savings in kibibytes(KiB).

> Resize these images to save data and improve page load time

- 페이지 로딩 시, 요소에게 정의된 width/height보다 이미지의 크기가 커서 요소의 크기에 맞게
  사이즈가 조정되는 현상이 발생할 수 있음.
- 이 때, 브라우저는 요소의 크기에 맞게 적절히 이미지 사이즈를 조정하게 됨.
- 네트워크 상에서 이미지를 땡겨올 때 렌더링될 때와 달리 불필요하게 큰 용량을 가져오기때문에 데이터 사용량 + 페이지 로딩 시 퍼포먼스 저하를 일으킴

![Example](https://webdev.imgix.net/uses-responsive-images/uses-responsive-images.png)

Lighthouse를 통해 점검하면 위와 같이 개선될 수 있음을 알려줌

## How Lighthouse calculates oversized images

- 실제 네트워크 상 가져온 이미지의 크기와, 렌더링된 이미지의 크기를 비교
- 물론, 기기의 해상도와 관련이 있음.

## Strategies for properly sizing images

> 가장 이상적인 것은 서버나 CDN에서 이미지 요소의 크기와 동일한 이미지를 제공하는 것

### Serve reponsive images

> Serving desktop-sized images to mobile devices can use 2–4x more data than needed. Instead of a "one-size-fits-all" approach to images, serve different image sizes to different devices.

#### Resize images using tools

- `sharp`: 웹 사이트의 모든 비디오를 대상으로 다양한 크기의 thumbnail을 생성
- `ImageMagick`: CLI를 통해 하나하나 이미지 크기를 조정
- 얼마나 많은 이미지들을 생성해야하는지의 문제가 발생할 수 있음
  - 정답은 없고 보통 3-5개의 이미지를 서빙
  - 서버의 capacity와 기타 비지니스 로직에 영향을 받음
- On Demand tools: 사용자가 크기를 입력 값으로 줬을 때 알아서 crop, resizing, flipping을 해줌
  - [Thumbor](https://github.com/thumbor/thumbor)
  - [Cloudinary](https://cloudinary.com/)

#### Serve multiple image versions

> 여러개의 이미지 버전을 명시해놓고 브라우저가 알아서 선택하도록 함

`img` 태그의 src, srcset, sizes attribute를 사용하여 각 이미지 중 현재 뷰포트 너비에 최적화된 이미지를 선택해 출력

```html
<img
  src="flower-large.jpg"
  srcset="flower-small.jpg 480w, flower-large.jpg 1080w"
  sizes="(max-width: 500px) 444px,
         (max-width: 800px) 777px,
         1222px"
  alt="flower"
/>
```

- `src`: 브라우저의 버전에 따라 `srcset`, `sizes` attribute를 사용할 수 없을 때가 있어서 fallback 대책을 마련해 둠
- `srcset`: 이미지들의 경로와 해당 이미지의 원본 크기를 지정
  - comma로 구분되며 `${filename} ${width | density}`로 정의
  - 작은 크기 이미지부터 순서대로 입력 해야함
  - 이렇게 함으로써 적절한 크기의 이미지를 땡겨올 수 있음
- `sizes`: 브라우저에게 출력될 이미지 크기를 지정

### Image CDNs: CDN에 맞기는 거지뭐

### Vector-based image formats: SVG; SVG를 통해 scaling

---

## Reference

- https://web.dev/uses-responsive-images/
- https://web.dev/serve-responsive-images/
- https://web.dev/codelab-serve-images-correct-dimensions/
- https://github.com/GoogleChrome/lighthouse/blob/master/lighthouse-core/audits/byte-efficiency/uses-responsive-images.js
