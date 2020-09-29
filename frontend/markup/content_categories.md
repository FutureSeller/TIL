# Content categories

모든 HTML 요소는 특성을 공유하는 요소끼리 묶는 콘텐츠 카테고리 한 가지 이상에 속합니다.
이는 공유하는 동작이나 관련 규칙을 정의하고 설명할 때, 특히 복잡한 세부사항을 포함할 때 도움이 됩니다.
요소가 아무런 카테고리에 속하지 않는 것 역시 가능합니다.

- 메인 콘텐츠 카테고리: 여러 요소가 서로 공유하는 일반적인 콘텐츠 규칙
- 폼 관련 콘텐츠 카테고리: 입력 폼 관련 요소가 공통으로 가지는 규칙
- 특정 콘텐츠 카테고리: 소수 요소만 공유. 특정 문맥에서만 유효함

## Main content categories

#### Metadata content

- 문서의 표현이나 동작을 수정하거나 다른 문서를 가리키는 링크를 설정하는 등 기타 대역외 정보를 전달
- `<base>`
- `<link>`
- `<meta>`
- `<noscript>`
- `<script>`
- `<style>`
- `<title>`

#### Flow content

- 보통 텍스트나 내장 콘텐츠를 포함합니다. (너무 많아서 생략)
- 대부분 body 요소 안에서 사용하는 요소들입니다.

#### Sectioning content

- 현재 개요에서 `<header>`, `<footer>`, 제목 콘텐츠의 범위를 정의하는 구역을 생성합니다.
- `<article>`, `<aside>` `<nav>`, `<section>`

#### Heading content

- 섹션의 제목을 정의합니다.
- `<h1> ~ <h6>`
- `<header>`는 보통 제목을 포함하지만 제목 콘텐츠는 아닙니다.

#### Phrasing content

- 텍스트와 텍스트가 포함한 마크업을 정의합니다. 구문 콘텐츠가 모여 문단을 형성합니다.

#### Embedded content

- 다른 리소스를 가져오거나 콘텐츠를 다른 마크업 언어나 네임스페이스로부터 문서에 삽입합니다.
- `<audio>`, `<canvas>`, `<iframe>`, `<img>`, `<object>`, `<picture>`, `<video>`

#### Interactive content

- 사용자와의 상호작용을 위해 특별하게 설계된 요소
- `<a>`, `<button>`, `<details>`, `<embed>`, `<iframe>`, `<label>`, `<select>`, `<textarea>`
- `<input>`에서 type이 hidden이 아닌 경우
- `<audio>`, `<video>`가 controls 속성을 가진 경우

#### Palpable content

- 내용이 비어있거나 숨겨지지 않은 경우를 의미함
- 렌더링 되며 실질적인 콘텐츠

#### Form-associated content

- `<form>` 특성이 소유자를 노출함.
- `<button>`, `<fieldset>`, `<input>`, `<label>` ...

## Secondary categories

스크립트 지원 요소는 문서의 렌더링 결과에 바로 기여하지 않는 요소로, 스크립트가 사용할 데이터를 지정하는 방식으로 지원하는 요소입니다. `<script>`, `<template>`이 있습니다.

---

## Reference

- https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories
