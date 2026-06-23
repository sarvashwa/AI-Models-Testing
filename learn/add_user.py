import tiktoken  # OpenAI's tokenizer

enc = tiktoken.encoding_for_model("gpt-4o")
tokens = enc.encode("Hello, how are you?")
print(len(tokens))        # 6
print(tokens)             # [15496, 11, 1128, 527, 499, 30]
print(enc.decode(tokens)) 