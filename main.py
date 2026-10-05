import tools.stack_class as stack
from tools.check_brackets import check_brackets as cb

if __name__ == '__main__':
    stack = stack.Stack()
    brackets = input('Введите скобки: ')
    print(cb(brackets))