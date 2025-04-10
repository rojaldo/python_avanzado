from ollama import chat
from ollama import ChatResponse
import ollama
import numpy as np

# get embedding for a text
embedding = ollama.embed(model='llama3.2', input='perro')
# print(embedding['embeddings'][0])

# create a function to create numpy array from the text
def create_numpy_array(text):
    # get the embedding for the text
    embedding = ollama.embed(model='llama3.2', input=text)
    # create a numpy array from the embedding
    array = np.array(embedding['embeddings'][0])
    return array

# a function that returns cosine similarity between two numpy arrays
def cosine_similarity(array1, array2):
    # calculate the cosine similarity between two numpy arrays
    dot_product = np.dot(array1, array2)
    norm_a = np.linalg.norm(array1)
    norm_b = np.linalg.norm(array2)
    return dot_product / (norm_a * norm_b)

word_1 = 'tocino'
word_2 = 'velocidad'

cat_embedding = create_numpy_array(word_1)
dog_embedding = create_numpy_array(word_2)

similarity = cosine_similarity(cat_embedding, dog_embedding)
print(f"similarity between {word_1} and {word_2}: {similarity}")