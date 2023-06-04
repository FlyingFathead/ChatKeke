# ChatKeke

ChatKeke - a simple GPT-2 web chat interface w/ front+backend

(Python+Flask+gunicorn => to any Nginx-type [micro]server setup you have)

![ChatKeke screenshot](https://github.com/FlyingFathead/ChatKeke/blob/main/chatkeke.png)

ChatKeke is a straightforward and easy-to-deploy web chat interface (front+back end) for TensorFlow-based local GPT-2 models from OpenAI.

You can get your base model from i.e.: https://github.com/openai/gpt-2/ and start fine-tuning from that.

The project is designed to provide a seamless and user-friendly way to interact with the GPT-2 model, making it a feasible choice for those looking to quickly set up a chatbot interface.

# Features

- Simplicity: ChatKeke is designed with simplicity in mind. The project consists of a single HTML file for the frontend and a Python script for the backend, making it easy to understand and deploy.

- GPT-2 Integration: ChatKeke is powered by a GPT-2 model, which is capable of generating human-like text based on the input it receives. The model is integrated into the backend server, which handles requests from the frontend and sends back the generated responses.

- Local Backend Server: The backend server is built with Python and Flask, and it uses TensorFlow to interact with the GPT-2 model. The server can be run locally, making it easy to set up and manage.

- Cross-Origin Resource Sharing (CORS): The backend server is configured to allow CORS, making it possible to host the frontend and backend on different domains or ports.

# Usage

To deploy ChatKeke, simply clone the repository, install the required Python packages, i.e. by using the included `requirements.txt` file:

```
pip install -r requirements.txt
```

The backend script can be run with i.e.:

```
./gunicorn_run.sh
```

... if you're using `gunicorn`; you can also run the backend directly with `python3 local_web_backend.py` or `python local_web_backend.py`; depending on how your Python 3.x is set up.

In case you are operating to a remote frontend, you can set up a remote reverse SSH tunnel with `./remote_reverse_tunnel.sh` (be sure to configure it properly first!). In a local backend-remote front end-scenario, depending on your remote web server, you might also need to take a look at the `proxypasses.txt` for possible ways to set up the reverse tunnel from the remote server to your local backend.

After deployment, the frontend (once it's been configured to your needs; again, look through the configuration files and source code) can be opened in any web browser and will connect to the backend server to send and receive chat messages. 

In this repository, there are examples included on how to set up the backend either as a local or remote instance.

**NOTE:** although being quite easy and fast to deploy, ChatKeke isn't necessarily the most secure way to set up a web interface for your GPT-2 model; it's highly recommended to use this for small scale testbed purposes only. Don't run anything too serious on it! No warranty, no guarantees.

# Future Work / TODO

ChatKeke is open to contributions and improvements. Potential areas of development include enhancing the user interface, optimizing the backend server, and integrating with other AI models or services.

- Context memory has been added but the functionality needs to be observed further.
- Other chat mode tweaks are still to be implemented, as well as a potential hyperparameter user panel, etc.

# License

ChatKeke is open-source software and is licensed under MIT.

# Author

ChatKeke is developed and maintained by [FlyingFathead](https://github.com/FlyingFathead). Multiple aspects have been developed in kind collaboration from ChaosWhisperer, whom I thank greatly for all the help. May the wind be on your back!
