import tools.stack_class as Stack

def check_brackets(string):
    """Проверяет сбалансированность скобок в строке"""

    stack = Stack.Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in pairs.values():          # открывающая скобка
            stack.push(char)
        elif char in pairs:                 # закрывающая скобка
            if stack.is_empty():
                return 'Несбалансированно'
            if stack.peek() != pairs[char]:
                return 'Несбалансированно'
            stack.pop()                     # убираем совпавшую открывающую

    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'                 # в конце стек должен быть пуст
