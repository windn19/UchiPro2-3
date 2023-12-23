# Создай класс Queue (очередь) и реализуй в нем следующие методы:
#     • push(item) – добавляет элемент в очередь (в конец),
#     • pop() – выводит на экран значение элемента из очереди (с начала) и удаляет его, если очередь пуста,
#     то вывести «error».
#     • size() – выводит на экран размер очереди (количество элементов).
#
# Методы push() и pop() должны выполняться за O(1), для этого очередь реализуй на односвязном списке.
# Кроме указателя на начало очереди (head), потребуется также указатель на конец очереди (tail).
#
# С клавиатуры вводится одно целое число - количество команд. Затем вводятся сами команды в формате:
# push x – команда добавляет элемент в очередь и ничего не выводит,
# pop – выводит на экран значение элемента из очереди и удаляет его, если очередь пуста, то вывести «error»,
# size – выводит на экран размер очереди.
#
# Входные данные:
# Вводится одно целое число n - количество команд, затем n строк с командами.
#
# Выходные данные:
# Выводятся строки.
#
# Пример ввода 1:
# 6
# push 1
# push 2
# push 3
# size
# pop
# size
#
# Пример вывода 1:
# 3
# 1
# 2
#
# Пример ввода 2:
# 6
# push 1
# pop
# pop
# size
# push 2
# pop
#
# Пример вывода 2:
# 1
# error
# 0
# 2

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def pop(self):
        if not self.queue_size:
            print('error')
        else:
            print(self.head.value)
            self.head = self.head.next
            self.queue_size -= 1

    def push(self, x):
        if not self.head:
            self.head = Node(x, None)
            self.tail = self.head
        else:
            new = Node(x, None)
            self.tail.next = new
            self.tail = new
        self.queue_size += 1

    def size(self):
        print(self.queue_size)


n = int(input())
queue = Queue()
for i in range(n):
    commands = input().split()
    if commands[0] == 'size':
        queue.size()
    elif commands[0] == 'pop':
        queue.pop()
    elif commands[0] == 'push':
        queue.push(int(commands[1]))
