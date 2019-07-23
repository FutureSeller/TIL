# VSCode
VSCode가 어떻게 동작하는 지 파는 것은 아니고, 오로지 사용자의 입장에서 남기는 기록. 
새롭게 나오는 기능이나 사용해 볼만한 익스텐션 등등을 점진적으로 업데이트할 예정

## 사용하게 된 계기
- mac이나 linux에서 vim을 쓰고 있었는데, window 환경에서 쓸 게 좀 애매했었음
- 몇몇 세미나들을 듣을 때나, 참석한 이런저런 스터디에 VSCode를 많이 쓰고 있음
- 터미널을 선호하는데, 따로 띄울 필요가 없음. powershell에서 지원하지 않는 command가 많아 살짝 불편
- default인 dark theme이 너무 마음에 듬

## Shortcuts
- (개인적으로) 에디터/터미널/브라우저를 사용할 때, 마우스 사용을 매우 귀찮아함 (파일 생성, 탭 이동 같은 것들)
- (개인적으로) 쓸만한 것들을 정리
- 추가 혹은 변경할 것이 있으면, 추후에 `keybindings.json` 만들 예정

| Component(dest) | Keybindings | Description |
| - | - | - |
| Sidebar |  Ctrl + Shift + E | 
| Sidebar |  Ctrl + Shift + F | 
| Sidebar |  Ctrl + Shift + G |
| Editor | Alt + [0-9] |
| Editor | Ctrl + [0-9] | 
| Editor | Ctrl + [0-9] [0-9] |
| Editor | Ctrl + N |
| Editor | Ctrl + W |
| Editor | Ctrl + Tab |
| Workspace | Ctrl + K Ctrl + O |
| Workspace | Ctrl + K F |
| Terminal | Ctrl + ` |

## code
1. open a file by using terminal
```
$ code -r /path/to/file
```