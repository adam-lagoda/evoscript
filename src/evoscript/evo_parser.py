class EvoParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ast = None

    def parse(self):
        # Your parsing logic here
        # For simplicity, let's just return the tokens as the AST
        self.ast = self.tokens
        return self.ast

    def parse(self):
        # Your parsing logic here
        # print("Parsing tokens:", self.tokens)
        self.ast = self.tokens  # Simplified for debugging
        # print("AST:", self.ast)
        return self.ast