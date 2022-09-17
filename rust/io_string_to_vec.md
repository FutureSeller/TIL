# 공백 구분 input string 정수로 바꾸기

```rust
use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer);

    let number: Vec<i32> = buffer.split_whitespace().map(|s| s.trim().parse().unwrap()).collect::<Vec<i32>>();
    println!("{:?}", number);
}
~
```

# 문자열 그대로 정수 배열로 바꾸기

```rust
use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();

    let number: Vec<usize> = buffer.trim().chars().map(|c| c as usize  - '0' as usize  ).collect::<Vec<_>>();
    println!("{:?}", number);
}
```

---
## Reference

- https://comb.tistory.com/9
