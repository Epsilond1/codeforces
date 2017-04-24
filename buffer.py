class Buffer:
    def __init__(self):
        self.sequence = []

    def add(self, *a):
        index = 0
        while index < len(a):
            self.sequence.append(a[index])
            index += 1
        if len(self.sequence) >= 5:
            while len(self.sequence) >= 5:
                print(sum(self.sequence[0:5]))
                del self.sequence[0:5]

    def get_current_part(self):
        return self.sequence


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]