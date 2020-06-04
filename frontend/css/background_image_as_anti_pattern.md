# The CSS background-image property as an anti-pattern

## Cons
#### 1. SEO 
- 구글 봇이 크롤링하거나 색인하지 않음
- 구글 검색의 33%는 이미지 검색
- `alt`를 통한 이미지 설명과 컨텍스트를 구글 봇에 제공 할 수 없음

#### 2. Accessibility
- 스크린 리더가 background-image를 무시함
- 무시하지 않았더라도 부가적으로 전달 할 수 있는 설명과 컨텍스트의 부재

#### 3. Performance
- 디바이스 화면 너비나 해상도를 고려하지 않고 이미지가 사용되기 때문
- 우리는 반응형을 사용하여 브라우저가 다른 크기의 이미지를 로드하도록 하고픈 이상이 있음
- 일반적으로 이미지는 전송되는 데이터 중 큰 청크
- media 쿼리를 적절히 사용할 수 있지만, 이미지 변경시 귀찮을 수 있음. 이미지가 CSS 에 포함 되어 있기 때문
- 브라우저가 CSS를 다운로드하고 파싱하기 전까지 이미지 다운로드를 할 수 없음

#### 4 CMS's & CDN's
- 즉, CSS에 이미지 URL이 박혀있는 이상, 이미지 관리 측면에서 귀찮은 점이 생긴다는 것

## Pros
- 배경 이미지를 사용해야 할 경우 좋음
- `image-set()`을 `background-image`와 함께 사용

## 대안: `object-fit` 속성과 함께 `<PICTURE>`를 사용
- `alt`로 SEO를 챙김
- native image lazy loading


```html
<picture>
    <source
        srcset="/some/_1170x658_crop_center-center/man-with-a-dog.webp 1170w,
                /some/_970x545_crop_center-center/man-with-a-dog.webp 970w,
                /some/_750x562_crop_center-center/man-with-a-dog.webp 750w,
                /some/_320x240_crop_center-center/man-with-a-dog.webp 320w"
        sizes="100vw"
        type="image/webp"
    />
    <source
        srcset="/some/_1170x658_crop_center-center/man-with-a-dog.jpg 1170w,
                /some/_970x545_crop_center-center/man-with-a-dog.jpg 970w,
                /some/_750x562_crop_center-center/man-with-a-dog.jpg 750w,
                /some/_320x240_crop_center-center/man-with-a-dog.jpg 320w"
        sizes="100vw"
    />
    <img
        src="/some/man-with-a-dog-placeholder.jpg"
        alt="Man with a dog"
        style="object-fit: cover;"
        loading="lazy"
    />
</picture>
```

---
## Reference
- https://nystudio107.com/blog/the-css-background-image-property-as-an-anti-pattern
