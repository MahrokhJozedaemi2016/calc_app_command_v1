from calculator.commands import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            return "Cannot divide by zero!"
        return self.a / self.b

def register():
    return DivideCommand
