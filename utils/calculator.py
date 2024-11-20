def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        print(f"Ошибка при вычислении выражения: {e}")
        return None