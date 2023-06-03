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

chat_prefix = '\n|kysymys|'
chat_suffix = '\n|vastaus|'
breakpoints = ['\n','|','|v','|k','|ky','|kys','|kysy', '|kysymys|', '|vastaus|', '---', '###', '|' '<|', '<|endoftext|>']  # Add any other desired breakpoints here

# maximum chat context message history memory
context_memory_length = 3  # Make sure this is an integer

# what to answer if the answer is empty
answer_on_empty = "Anteeksi, nyt en ymmärtänyt. Voisitko täsmentää?"
