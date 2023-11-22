# evoscript
#!/usr/bin/env python

from evo_lexer import EvoLexer
from evo_parser import EvoParser
from evo_interpreter import EvoInterpreter
import sys

def execute_evoscript(code):
    lexer = EvoLexer(code)
    tokens = lexer.tokenize()

    parser = EvoParser(tokens)
    ast = parser.parse()

    interpreter = EvoInterpreter(ast)
    interpreter.interpret()

def main():
    if len(sys.argv) != 2:
        print("Usage: evoscript <filename.es>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".es"):
        print("Error: The file must have a .es extension")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            evoscript_code = file.read()
            execute_evoscript(evoscript_code)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()
