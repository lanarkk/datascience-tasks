text = '''Имя: Иван, Группа А123, Средний балл: 4.75
Имя: Максимб Группа: Б123, Средний балл: 3.33
'''.strip()

with open('data.txt', 'w') as f:
  f.write(text)


def parse_file(filename):
  data = dict()
  with open(filename, 'r') as file:
    text = [line.strip().split(',') for line in file.readlines()]
  for i in range(len(text[0])):
    for pair in text:
      data[i] = pair.split(':')[0]
      data[i][pair.split(':')[0]] = pair.split(':')[1]
  return data

print(parse_file('data.txt'))
