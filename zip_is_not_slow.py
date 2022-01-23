import timeit


print(timeit.timeit('''
sum = 0
a = range(100000000)
b = range(100000000)
for _ in a:
    sum += _
    
for _ in b:
    sum += _
    
print(sum)
''', number=1))

print(timeit.timeit('''
sum = 0
a = range(100000000)
b = range(100000000)
for e1, e2 in zip(a, b):
    sum += e1
    sum += e2

print(sum)
''', number=1))


'''
result
====================
9999999900000000
8.0715322
9999999900000000
8.7490618
====================
'''
