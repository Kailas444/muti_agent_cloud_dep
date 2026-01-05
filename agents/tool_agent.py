
class ToolAgent:
    def calculator(self, expression):
        try:
            return str(eval(expression))
        except:
            return "Calculation error"
