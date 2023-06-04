# requires gunicorn; install it with:
# pip install gunicorn

gunicorn -b 0.0.0.0:5000 local_web_backend:app
