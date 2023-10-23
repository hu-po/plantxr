# plantxr

Comes from 
https://github.com/immersive-web/webxr-samples.git

Using webxr directly

```
sudo npm install http-server -g
http-server
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
http-server -S -C cert.pem -K key.pem
```

https://developer.oculus.com/documentation/web/webxr-overview/
https://immersive-web.github.io/webxr/explainer.html

Trying to use Python and flask

```
conda create -n plantxr python=3.7
conda activate plantxr
pip install Flask

FLASK_APP=flaskapp.py FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 flask run --cert=cert.pem --key=key.pem
```