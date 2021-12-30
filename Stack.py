myStr = '(((([{}]))))'
myStr1 = '[([])((([[[]]])))]{()}'
myStr2 = '{{[()]}}'
myStr3 = '}{}'
myStr4 = '{{[(])]}}'
myStr5 = '[[{())}]'


# def check():
myString = '(((([{}]))))'
list_stack = []
for item in myString:
    if item == '(' or item == '{' or item == '[':
        list_stack.append(item)
    elif len(list_stack) > 0 \
            and item == ')' or item == '}' or item == ']' \
            and (list_stack[-1] + item) == '()' or (list_stack[-1] + item) == '{}' or (list_stack[-1] + item) == '[]':
        list_stack.pop()
if list_stack == 0:
    print("Cбалансированно")
else:
    print("Несбалансированно")



# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def isEmpty(self):
#         if len(self.stack) == 0:
#             return False
#         else:
#             return True
#
#     def push(self, item):
#         self.stack.append(item)
#         return self.stack
#
#     def pop(self):
#         if len(self.stack) == 0:
#             return "Список пуст"
#         else:
#             removed = self.stack.pop()
#             return removed
#
#     def peek(self):
#         if len(self.stack) == 0:
#             return "Список пуст"
#         else:
#             last_item = self.stack[-1]
#             return last_item
#
#     def size(self):
#         sizeStack = len(self.stack)
#         return sizeStack
#
#
# s = Stack()
#
# print(s.isEmpty())
# print(s.push(1))
# print(s.push(2))
# print(s.push(3))
# print(s.push(4))
# print(s.isEmpty())
# print(s.size())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.size())
# print(s.peek())
# print(s.size())

# print(check(myStr))
# print(check(myStr1))
# print(check(myStr2))
# print(check(myStr3))
# print(check(myStr4))
# print(check(myStr5))
