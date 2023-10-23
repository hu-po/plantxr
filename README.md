# plantxr

Comes from 
https://github.com/immersive-web/webxr-samples.git

```
sudo npm install http-server -g
http-server
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
http-server -S -C cert.pem -K key.pem
```

## Sources

https://developer.oculus.com/documentation/web/webxr-overview/
https://immersive-web.github.io/webxr/explainer.html

## Conda environment

```
conda create -n plantxr python=3.7
conda activate plantxr
pip install Flask
```