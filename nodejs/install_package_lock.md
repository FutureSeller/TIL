> only update the package-lock.json, instaed of checking node_modules and downloading dependencies.

```bash
$ npm isntall --package-lock-only
```

> prevent npm from creating a package-lock.json. will not automatically prune your node modules when installing
```bash
$ npm install --no-package-lock
```

---
## Reference
- https://docs.npmjs.com/cli/install.html
