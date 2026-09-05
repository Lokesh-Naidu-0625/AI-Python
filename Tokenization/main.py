#first for tokenization we need to import tiktoken
import tiktoken

#we need to assign a model name for this tiktoken 
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey please encode the following text"
# we are encoding the given text 
tokens = enc.encode(text)

print(text)
print(tokens)

# we are decoding the generated encoded tokens to normal text
dec = enc.decode(tokens)
print(dec)
