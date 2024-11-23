"""1), 2), 3)"""
example = "123456789"
print(f'{example[0]}\n{example[-1]}')

"""4)"""

if len(example) // 2 == 0:
    i: int = len(example) / 2 - 1
    print(example[i])
else:
    i = (len(example) // 2)
    print(example[i:])

'''5)'''
print(example[::-1])

'''6)'''
print(example[1::2])



