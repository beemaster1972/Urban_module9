first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(el[0])-len(el[1]) for el in zip(first,second) if len(el[0])!=len(el[1]))
second_result = (len(el)==len(second[_]) for _,el in enumerate(first))
print(*first_result)
print(*second_result)