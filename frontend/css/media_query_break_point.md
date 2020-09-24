# Media Queries for Standard Devices

> If you think responsive’s simple, I feel bad for you son. We got 99 viewports, but the iPhone’s just one. — Josh Brewer, March 10, 2010

음. 어떤 기준으로 break point를 정하는 게 좋을지 참고가 될 줄 알았는데 각종 디바이스들의 리스트와 해당 media query들이 나열된 곳이였음.

당연히 모든 디바이스들의 화면 크기를 각각 break point로 지정하고 싶지 않고... decision을 내릴 수 있을 만한 요소들이 필요해보임. 

decision point들을 경험적으로 분류해 놓은 것이나, 이것을 통계적으로 데이터를 수집해서 분석한 연구가 있을까?

리서치는 못찾은 것 같고 경험적으로 분류해 놓은 것 같은 것들을 모아보고자한다.

#### tailwindcss
> There are four breakpoints by default, inspired by common device resolutions:

```css
/* Small (sm) */
@media (min-width: 640px) { /* ... */ }

/* Medium (md) */
@media (min-width: 768px) { /* ... */ }

/* Large (lg) */
@media (min-width: 1024px) { /* ... */ }

/* Extra Large (xl) */
@media (min-width: 1280px) { /* ... */ }
```

어떤 디바이스가 common한지는 잘 모르겠지만 tailwindcss는 default로 4가지를 쓰고 있으며 물론 개발자가 커스터마이징 할 수 있는 것 같다.

#### bootstrap

```css
// Extra small devices (portrait phones, less than 576px)
// No media query for `xs` since this is the default in Bootstrap

// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }

// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }

// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }

// Extra large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
```

단순히 range 뿐만 아니라 landscape/portrait을 고려하는 것 같기도 하다.

#### Materialize

```
Small screens are defined as having a max-width of 600px
Medium screens are defined as having a max-width of 992px
Large screen are defined as having a min-width of 993px
Extra Large screen are defined as having a min-width of 1200px
```

#### Foundation
default로 core한 breakpoint들은 아래와 같다고 한다.

```
Small: any screen.
Medium: any screen 640 pixels or larger.
Large: any screen 1024 pixels or larger.
```

sass를 사용하고 있을 경우엔 아래와 같다고 한다.
```
$breakpoints: (
  small: 0px,
  medium: 640px,
  large: 1024px,
  xlarge: 1200px,
  xxlarge: 1440px,
);
```

---

다 찾아보고 정리하자니 크게 의미가 없는 것 같고 각각 나름대로 inspiration을 가지고 나누는 것 같다. (어떤 기준인지는 잘 모르겠지만)

기준이 너무 궁금해서 [Designing for Large Screen Smartphones](https://www.lukew.com/ff/entry.asp?1927)과 
[How Do Users Really Hold Mobile Devices?](https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php)를 
읽어보니 뭔가 힌트를 얻은 것 같기도하다. (아닌것 같기도 하고 말이지..)

> In his analysis of 1,333 observations of smartphones in use, 
> Steven Hoober found about 75% of people rely on their thumb and 49% rely on a one-handed grip to get things done on their phones.

디바이스들의 크기에 따라 사용자들이 디바이스를 다루는 방법이 다르고 이에 따라 인터랙션 패턴이 달라진다고 한다.
예를 들면 어떤 것들은 한손으로 디바이스를 들고 엄지만으로 가능하고, 한 손위에 올려놓고 다른 손으로 터치를 할 수 있다. 혹은 데스크탑은 키보드와 마우스로 제어한다.
이에 따라 보여줘야할 컨텐츠의 크기와 배치가 달라지기 마련일테고, 사용자의 인터랙션 범위에 따라 불편한 지점들의 분포를 분석한 데이터가 있어 저런식으로 나눈게 아닐까라는 생각도 해본다.
~사실 잘 모르겠다~

---
## Reference
- https://css-tricks.com/snippets/css/media-queries-for-standard-devices/
- https://css-tricks.com/css-media-queries/
- https://tailwindcss.com/docs/responsive-design
- https://getbootstrap.com/docs/4.1/layout/overview/
- https://materializecss.com/sass.html
- https://get.foundation/sites/docs/media-queries.html
- https://responsivedesign.is/articles/why-you-dont-need-device-specific-breakpoints/
- https://www.lukew.com/ff/entry.asp?1927
