class EvoLexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        # Your tokenization logic here
        # For simplicity, let's consider whitespace-separated tokens
        self.tokens = self.code.split()
        return self.tokens

    def tokenize(self):
        # Your tokenization logic here
        # print("Tokenizing:", self.code)
        self.tokens = self.code.split()
        # print("Tokens:", self.tokens)
        return self.tokens