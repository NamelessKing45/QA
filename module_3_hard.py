data_structure = [[1, 2, 3],{'a': 4,'b': 5},(6,{'cube': 7,'drum': 8}),'Hello',[(),[{(2,'Urban','Urban2',35)}]]]
summ = [0, 0]


def suma(data):
    if isinstance(data, list):[suma(item) for item in data];
    elif isinstance(data, tuple):[suma(item) for item in data];
    elif isinstance(data, str):summ[1] += len(data);
    elif isinstance(data, (int, float)):summ[0] += data;
    elif isinstance(data, dict): [(suma(key), suma(value)) for key, value in data.items()];
    elif isinstance(data, set): [suma(item) for item in data];
    else: pass


for i in data_structure:suma(i);
print(f'Сумма всех чисел = {summ[0]};\nCумма всех строковых '
      f'элементов = {summ[1]};\n'
      f'Количество всех строковых элементов + сумма всех чисел = {sum(summ)};.')
