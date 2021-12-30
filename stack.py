class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    def push(self, item):
        self.stack.append(item)
        return self.stack

    def pop(self):
        if len(self.stack) == 0:
            return "Список пуст"
        else:
            removed = self.stack.pop()
            return removed

    def peek(self):
        if len(self.stack) == 0:
            return "Список пуст"
        else:
            last_item = self.stack[-1]
            return last_item

    def size(self):
        sizeStack = len(self.stack)
        return sizeStack

    def check(self, myString):
        for item in myString:
            if item == '(' or item == '{' or item == '[':
                self.stack.append(item)
            elif len(self.stack) > 0 \
                    and (item == ')'
                         or item == '}'
                         or item == ']') \
                    and (self.stack[-1] + item == '()'
                         or self.stack[-1] + item == '{}'
                         or self.stack[-1] + item == '[]'):
                self.stack.pop()
            else:
                return "Несбалансированно"
        if len(self.stack) == 0:
            return "Cбалансированно"


s = Stack()
print(s.isEmpty())
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.isEmpty())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.size())
print(s.peek())
print(s.size())
print(s.check('(((([{}]))))'))
print(s.check('[([])((([[[]]])))]{()}'))
print(s.check('{{[()]}}'))
print(s.check('}{}'))
print(s.check('{{[(])]}}'))
print(s.check('[[{())}]'))
