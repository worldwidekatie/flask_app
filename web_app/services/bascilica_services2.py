import basilica

import os
from dotenv import load_dotenv
load_dotenv()

BASCILICA_API_KEY=os.getenv("BASCILICA_API_KEY", default="oops")
sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
with basilica.Connection(BASCILICA_API_KEY) as connection:
#connection = Connection(BASCILICA_API_KEY)
    print(type(connection))


embeddings = list(connection.embed_sentences(sentences))
for embed in embeddings:
    print("---------")
    print(embed) # a list of 786 floats from -1 to 1

breakpoint()

embedding = connection.embed_sentence("Hello World")
print(embedding)