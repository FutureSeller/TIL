CI를 구축하다가 .env.local이 모든 파일을 dominate 해버려서 골치아픈 도중 공식문서를 찾게 되었다.
물론 레포에는 .env.local이 없지만, 사정상 로컬에서 dev환경 도커 이미지를 만들어 올려야했기 때문에 꽤 귀찮은 일이 아닐 수 없었다.

env-cmd 같은 녀석들을 써도 된다.

다른 방법을 없을 까 찾아보다가 약간의 편법을 쓰긴했다. 
썩 좋다고 생각하진 않지만 팀내 공유가 되어있다면 공감대를 얻었다면 꽤 괜찮은 방법이긴하다. [링크](https://nextjs.org/docs/pages/building-your-application/configuring/environment-variables#test-environment-variables)

`NODE_ENV=test yarn build`

어찌보면 좀 당연하다. test 환경에서 local 상태를 바라보는게 말이 안되니까. 요러면 환경변수 로드하는 우선순위가 바뀌면서 .env.local을 무시할 수 있긴하다.
