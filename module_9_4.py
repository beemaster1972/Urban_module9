from random import choice


class MysticBall:
    def __init__(self, *args):
        self.__words = args

    def __call__(self, *args, **kwargs):
        return choice(self.__words)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')

    return write_everything


# Task 1 lambda
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(*map(lambda x, y: x == y, first, second))

# Task 2 Closure
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Task 3 OOP
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())