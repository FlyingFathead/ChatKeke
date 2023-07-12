# requires gunicorn; install it with:
# pip install -U gunicorn

# recommended to use `firejail`
# install it with i.e. `sudo apt-get install firejail`

export backend_dir="./"

# run in loop w/ firejail
while true; do
  cd "$backend_dir" &&

  # non-verbose variant;
  # firejail gunicorn -b 0.0.0.0:5000 local_web_backend:app &&

  # verbose; debug
  firejail gunicorn -b 0.0.0.0:5000 local_web_backend:app --log-level debug --access-logfile access.log

  echo "Connection lost. Retrying in 5 seconds..."
  sleep 5
done
