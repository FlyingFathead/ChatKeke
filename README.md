# ChatKeke

ChatKeke - a simple GPT-2 web chat interface w/ front+backend (Python+Flask+any Nginx-type microserver setup you have)

![ChatKeke screenshot](https://github.com/FlyingFathead/ChatKeke/blob/main/chatkeke.png)

ChatKeke is a straightforward and easy-to-deploy web chat interface (front+back end) for GPT-2, a powerful language model developed by OpenAI. The project is designed to provide a seamless and user-friendly way to interact with the GPT-2 model, making it an excellent choice for those looking to quickly set up a chatbot interface.

# Features

- Simplicity: ChatKeke is designed with simplicity in mind. The project consists of a single HTML file for the frontend and a Python script for the backend, making it easy to understand and deploy.

- GPT-2 Integration: ChatKeke is powered by a GPT-2 model, which is capable of generating human-like text based on the input it receives. The model is integrated into the backend server, which handles requests from the frontend and sends back the generated responses.

- Local Backend Server: The backend server is built with Python and Flask, and it uses TensorFlow to interact with the GPT-2 model. The server can be run locally, making it easy to set up and manage.

- Cross-Origin Resource Sharing (CORS): The backend server is configured to allow CORS, making it possible to host the frontend and backend on different domains or ports.

# Usage

To deploy ChatKeke, simply clone the repository, install the required Python packages, and run the backend server script. The frontend can be opened in any web browser and will connect to the backend server to send and receive chat messages. There are examples included on how to set up the backend either as a local or remote instance.

**NOTE:** although quite easy and quick to deploy, ChatKeke isn't necessarily the most secure way to set up a web interface for your GPT-2 model; it's highly recommended to use this for small scale testbed purposes only. Don't run anything too serious on it! No warranty, no guarantees.

# Future Work / TODO

ChatKeke is open to contributions and improvements. Potential areas of development include enhancing the user interface, optimizing the backend server, and integrating with other AI models or services.

- Context memory and other chat mode tweaks are still to be implemented, as well as a potential hyperparameter user panel, etc.

# License

ChatKeke is open-source software and is licensed under MIT.

# Author

ChatKeke is developed and maintained by [FlyingFathead](https://github.com/FlyingFathead), a developer with a keen interest in neural networks and AI. Kind thanks to ChaosWhisperer for the help, may the wind be on your back!
