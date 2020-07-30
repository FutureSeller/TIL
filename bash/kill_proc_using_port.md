```bash
$ lsof -i:8080

# To kill any process listening to the port 8080
$ kill $(lsof -t -i:8080)

# To kill any process listening to the port 8080 more violently
$ kill -9 $(lsof -t -i:8080)
```

---
## Reference
- https://stackoverflow.com/questions/11583562/how-to-kill-a-process-running-on-particular-port-in-linux
