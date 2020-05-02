# Headless CMS(Content Management System)

들어가기 앞서, CMS란 무엇인지, decoupled CMS와 headless CMS는 무엇이고 차이점이 무엇인지 알아보자.

## 들어가기 앞서, (Traditional) CMS란?
> a software application that can be used to manage the creation and modification of digital content

#### 컴포넌트
- CMA(Content Management Application)
  - 컨텐츠를 등록, 수정 삭제 가능하도록 하는 유저 인터페이스
  - 쉽게 생각하면 컨텐츠 매니저가 개발자 필요 없이 컨텐츠를 등록하고 관리 할 수 있도록 해주는 친구
- CDA(Content Delivery Application)
  - back-end + front-end 을 의미
  - 컨텐츠를 쌓아놓고(back-end), 웹 사이트(front-end)를 변경하는 녀석

#### 특징
- indexing, search and retrieval
- format management: 다른 문서 형식으로부터 HTML 또는 PDF로 변환시켜줄 수 있는 기능
- revision control: content의 revision control을 의미
- management: 기타 등등 (e.g., font management)
- SEO-friendly URLs
- Group-based permission systems
- Full template support and customisable templates

#### 잘 알려진, 많이 쓰는 CMS
WordPress, Wix, and Squarespace 등

## Decoupled CMS
- backend와 frontend를 나눈 것 (우리가 흔히 알고있는 구조)
- CMS의 관점에서 보면
  - content들이 DB에 관리 되는 것 (backend)
  - content들을 frontend에서 사용할 수 있게 API를 뚫어 줘야함(backend)
  - 뚫려있는 API를 가지고 어드민/프로덕션에 서빙할 interface를 만들어 두어야 함(frontend)
- 통상적으로 같은 망(방화벽) 뒤에서 생성된 컨텐츠를 sync하고 delivery environment에 추가하는 형식

## Headless CMS
> a back-end only content management system (CMS) built from the ground up as a content repository 
> that makes content accessible via a RESTful API for display on any device.

즉, CMS는 뚫어둔 API를 통해 데이터만 서빙하고 front-end 쪽(presentation layer)을 더 이상 관여하지 않겠다는 의미 

---
## Reference
- https://en.wikipedia.org/wiki/Content_management_system
- https://en.wikipedia.org/wiki/Headless_content_management_system
- https://www.businessnewsdaily.com/5148-content-management-systems.html
- https://www.brightspot.com/blog/decoupled-cms-and-headless-cms-platforms
