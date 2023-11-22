class EvoInterpreter:
    def __init__(self, ast):
        self.ast = ast

    def interpret(self):
        for statement in self.ast:
            if statement.startswith("evoprint"):
                self.handle_print(statement)
            # Add more handling for other types of statements

    def handle_print(self, statement):
        # Extract the content inside the parentheses
        content = statement.split('(', 1)[1].rsplit(')', 1)[0]
        # Split the content by commas and remove quotes
        elements = [arg.strip('\'"') for arg in content.split(',')]
        # Print each argument with a space in between
        print(" ".join(str(arg) for arg in elements))