서버를 두개 띄워서 같은 도메인으로 두고 route를 갈라줘야할 경우가 있었음. dev, prod 환경은 API Gateway가 갈라주고 있는 상황.

매번 배포해서 확인하는게 귀찮은지라... 아주 간단하게 reverse proxy 하나 만들어서 사용했었음.

두개 서버가 같은 도메인을 바라보게 되어있어 HTTPS 인증서를 reverse_proxy에 넣어버렸음.

```Dockerfile
FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY cert.key /etc/nginx/cert.key
COPY cert.pem /etc/nginx/cert.pem

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 9000
```

```conf
events {}

http {
        ssl on;
        ssl_certificate cert.pem;
        ssl_certificate_key cert.key;

        upstream server1 {
                server host.docker.internal:3000;
        }

        upstream server2 {
                server host.docker.internal:4000;
        }


        server {
                listen       9000;
                server_name  local.example.com;

                location / {
                        proxy_pass http://server1;
                        proxy_http_version 1.1;
                }


                location /webview/payment/ {
                        proxy_pass http://server2;
                        proxy_redirect off;
                }

                location /payment/ {
                        proxy_pass http://server2;
                        proxy_redirect off;
                }

                location /_next/ {
                        proxy_pass http://server2;
                        proxy_redirect off;
                        proxy_set_header Upgrade $http_upgrade;
                        proxy_set_header Connection "upgrade";
                }
        }
}
```
