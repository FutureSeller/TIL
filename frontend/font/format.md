# Font format

## 임베디드 오픈 타입 / EOT (Embedded Open Type)

- 과거 microsoft (@font-face의 최초 사용자)가 작성했음. IE에서 지원.
- IE8 이하에서 @font-face를 사용할 때 인식할 수 있는 유일한 포맷

## 트루 타입 / TTF (TrueType Font)

- OSX, Windows 모두에서 가장 일반적인 글꼴 형식
- 모든 브라우저에서 지원되지만 IE 9 이상에서 임베디드 비트가 설치 가능으로 설정된 경우에만 작동

## OTF (OpenType Font)

## 웹 오픈 폰트 형식 / WOFF (Web Open Font Format)

- 웹에서 사용하기 위해 만들어지고, 다른 조직과 함께 모질라에서 개발됨
- OTF, TTF의 압충 버전을 사용. 빠르게 로드되는 경우가 많음
- 메타 데이터를 사용하면 저작권 문제를 해결하기 위해 글꼴 파일에 라이센스 데이터를 포함 할 수 있음
- 모든 주요 브라우저가 지원함

## WOFF2 (Web Open Font Format2)

- 차세대 WOFF. WOFF 1.0 보다 평균 30%의 압축률. 경우에 따라 최대 50%

---

## Reference
- https://knulab.com/archives/1191
- https://medium.com/@aitareydesign/understanding-of-font-formats-ttf-otf-woff-eot-svg-e55e00a1ef2
