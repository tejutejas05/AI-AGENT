def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Error in calculation"
        
