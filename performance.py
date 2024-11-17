import time
import timeit
from tokenUtil import TokenUtils

tutils = TokenUtils()

text = "Hello world! I am the highest performing tokenization library in the world!"

tokens = tutils.encode(text)

encode_time = timeit.timeit(lambda: tutils.encode(text), number=1000) / 1000
decode_time = timeit.timeit(lambda: tutils.decode(tokens), number=1000) / 1000

print(f"Encoding time: {encode_time} seconds")
print(f"Decoding time: {decode_time} seconds")