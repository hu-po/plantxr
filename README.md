# plantxr

Comes from 
https://github.com/immersive-web/webxr-samples.git

```
sudo npm install http-server -g
http-server
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
http-server -S -C cert.pem -K key.pem
```