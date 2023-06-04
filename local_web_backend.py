#  Local Backend (Python Flask + TensorFlow)
#  v1.312 / written by FlyingFathead & ChaosWhisperer

from flask import Flask, request, jsonify
from flask import send_from_directory
from flask_cors import CORS
import sys
import os
import glob
import numpy as np
import json
import logging

# chatlog
logging.basicConfig(filename='chat.log', level=logging.INFO, format='%(asctime)s %(message)s')

# see backend_config.py for directory configuration
import backend_config
model_files_dir = backend_config.model_files_dir
model_py_dir = backend_config.model_py_dir
chat_prefix = backend_config.chat_prefix
chat_suffix = backend_config.chat_suffix
breakpoints = backend_config.breakpoints
answer_on_empty = backend_config.answer_on_empty
context_memory_length = backend_config.context_memory_length  # Number of interactions to remember

sys.path.insert(0, model_py_dir)  # Add the python files directory to the system path

import model, sample, encoder
import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

model_files = glob.glob(os.path.join(model_files_dir, 'model-*'))
model_file = max(model_files, key=os.path.getctime)
model_name = model_file.split('/')[-1].split('.')[0]

# Modify the get_encoder function to look for the encoder.json file directly in the model_files_dir directory
def get_encoder(model_name, models_dir):
    with open(os.path.join(models_dir, 'encoder.json'), 'r') as f:
        encoder_dict = json.load(f)
    with open(os.path.join(models_dir, 'vocab.bpe'), 'r', encoding="utf-8") as f:
        bpe_data = f.read()
    bpe_merges = [tuple(merge_str.split()) for merge_str in bpe_data.split('\n')[1:-1]]
    return encoder.Encoder(
        encoder=encoder_dict,
        bpe_merges=bpe_merges,
    )

enc = get_encoder(model_name, model_files_dir)

hparams = model.default_hparams()
with open(os.path.join(model_files_dir, 'hparams.json')) as f:
    hparams.override_from_dict(json.load(f))

# Define the graph
with tf.Graph().as_default():
    context = tf.placeholder(tf.int32, [1, None])
    output = sample.sample_sequence(
        hparams=hparams, length=450,
        context=context,
        batch_size=1,
        temperature=1, top_k=40
    )
    saver = tf.train.Saver()
    # Create the session inside the graph context
    sess = tf.Session()  # Assign the session to a variable
    ckpt = tf.train.latest_checkpoint(model_files_dir)
    saver.restore(sess, ckpt)

chat_history = []  # Initialize chat history

@app.route('/')
def home():
    print("Current working directory:", os.getcwd())
    print("Absolute path to index.html:", os.path.abspath('index.html'))
    return send_from_directory('.', 'index.html')

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

def parse_response(output_text):
    next_delimiter_index = None

    for breakpoint in breakpoints:
        breakpoint_index = output_text.find(breakpoint)
        if breakpoint_index >= 0:
            if next_delimiter_index is None or breakpoint_index < next_delimiter_index:
                next_delimiter_index = breakpoint_index

    if next_delimiter_index is not None:
        output_text = output_text[:next_delimiter_index].strip()

    return output_text

@app.route('/api', methods=['POST'])
def generate_text():
    try:
        global sess  # Add this line to access the global session variable
        global chat_history  # Add this line to access the global chat history variable
        data = request.get_json()
        input_text = chat_prefix + data['input'] + chat_suffix

        # Prepend chat history
        for history in chat_history:
            input_text = history + input_text

        logging.info('User input: %s', input_text)  # Log the user input

        context_tokens = enc.encode(input_text)
        output_text = ""

        # Loop until the model generates a non-empty response
        while output_text.strip() == "":
            out = sess.run(output, feed_dict={
                context: [context_tokens]
            })[:, len(context_tokens):]
            output_text = enc.decode(out[0])
            for breakpoint in sorted(breakpoints, key=len):
                breakpoint_index = output_text.find(breakpoint)
                if breakpoint_index >= 0:
                    output_text = output_text[:breakpoint_index]
                    break

        logging.info('Model output: %s', output_text)  # Log the model output

        # Prepend chat history
        chat_history.insert(0, chat_prefix + data['input'] + chat_suffix)
        input_text = chat_prefix + data['input'] + chat_suffix + ''.join(chat_history)

        # Limit the chat history to the last n interactions
        chat_history = chat_history[:context_memory_length]

        return jsonify({'output': output_text})
    except Exception as e:
        logging.error('Error: %s', str(e))
        return jsonify({'error': str(e)}), 500

@app.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', '*') # only enable if local
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(port=5000)
