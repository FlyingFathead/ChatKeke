model_files_dir = './model_data_files/'

"""
Above: Set the directory path for the model's files.

These files are
===============
model-<model checkpoint number>.data-00000-of-00001
model-<model checkpoint number>.index
model-<model checkpoint number>.meta
vocab.bpe
checkpoint
counter
encoder.json
hparams.json
"""

model_py_dir = './model_py_files/'

"""
Above: Set the directory path for the model's python files

These files are
===============
encoder.py
sample.py
model.py
"""

# chat prefix // the text prefix added _before_ every line that's input to the model
# (this can be i.e.: `<user>` or `User: `, etc...)
chat_prefix = '\n|kysymys|'

# chat suffix // the suffix added _after_ every line that's input to the model
# (this can be i.e.: `<AI>` or `ChatBot: `, etc...)
chat_suffix = '\n|vastaus|'

# maximum chat context / message history memory
# note that the higher the count is, the more computationally intensive the model will be
# no context memory means that the model will treat each query as a new random input
context_memory_length = 1  # Make sure this is an integer

# what to answer if the answer is empty
# you can also set the model to try to regenerate an answer if it returns empty; this may increase response time
answer_on_empty = "Anteeksi, nyt en ymmärtänyt. Voisitko täsmentää?"

# pieces of text upon which the model should stop generating its answer
breakpoints = ['\n','|','|v','|k','|ky','|kys','|kysy', '|kysymys|', '|vastaus|', '---', '###', '|' '<|', '<|endoftext|>']  # Add any other desired breakpoints here
