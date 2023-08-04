## exports
- Node.js ESM 시스템에서 모듈 로딩을 정의

## publishConfig - exports
- npm에 패키지를 배포할 때 해당 패키지의 exports 필드 값을 변경하는 데 사용

결론: exports가 모듈 로딩을 정의하는거고. puslishConfig의 exports는 현재 패키지의 exports를 npm에 배포할 때 덮어쓰는 용도

### @toss/storage를 예로들자면.

- 배포전 코드
```js
{
  "exports": {
    ".": "./src/index.ts",
    "./typed": "./src/typed/index.ts",
    "./package.json": "./package.json"
  },
  "publishConfig": {
    "access": "public",
    "exports": {
      ".": {
        "require": {
          "types": "./dist/index.d.ts",
          "default": "./dist/index.js"
        },
        "import": {
          "types": "./esm/index.d.mts",
          "default": "./esm/index.mjs"
        }
      },
      "./typed": {
        "require": {
          "types": "./dist/typed/index.d.ts",
          "default": "./dist/typed/index.js"
        },
        "import": {
          "types": "./esm/typed/index.d.mts",
          "default": "./esm/typed/index.mjs"
        }
      },
      "./package.json": "./package.json"
    },
    "main": "./dist/index.js",
    "module": "./esm/index.mjs",
    "types": "./dist/index.d.ts"
  },
}
```

- 배포후 다운로드 받고 node_modules에 있는 package.json
```js
{
"exports": {
    ".": {
      "require": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      },
      "import": {
        "types": "./esm/index.d.mts",
        "default": "./esm/index.mjs"
      }
    },
    "./typed": {
      "require": {
        "types": "./dist/typed/index.d.ts",
        "default": "./dist/typed/index.js"
      },
      "import": {
        "types": "./esm/typed/index.d.mts",
        "default": "./esm/typed/index.mjs"
      }
    },
    "./package.json": "./package.json"
  },
  "main": "./dist/index.js",
}
```
