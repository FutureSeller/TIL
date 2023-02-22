src 라는 디렉토리를 옮길때 쓴 커맨드

`find . -name "src" -type d | xargs -I{} mv {} /Users/jihoon/Workspaces/somewhere/{}`
