import tiktoken

class TokenUtils(object):
    def __init__(self, encoding_name: str = 'gpt2') -> None:
        self.encoding = tiktoken.get_encoding(encoding_name)
    
    def encode(self, text: str) -> list[int]:
        return self.encoding.encode(text)
    
    def decode(self, tokens: list[int]) -> str:
        return self.encoding.decode(tokens)




