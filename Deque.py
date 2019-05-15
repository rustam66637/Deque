class Deque:
    def __init__(self):
        self.deque = [] # инициализация внутреннего хранилища

    def addFront(self, item):
        self.deque.insert(0, item) # добавление в голову

    def addTail(self, item):
        self.deque.append(item) # добавление в хвост

    def removeFront(self):
        if len(self.deque) == 0:
            return None # если очередь пуста
        return self.deque.pop(0)# удаление из головы

    def removeTail(self):
        if len(self.deque) == 0:
            return None # если очередь пуста
        return self.deque.pop()# удаление из хвоста

    def size(self):
        return len(self.deque)# размер очереди
