# with open('aaa.txt', mode='wt', encoding='utf-8') as f:
#     l = ['aaa', 'bbb', 'ccc']
#     for i in l:
#         f.write(i)

# def func(x, y, z):
#     return x+y+z
# res = func(1, 2, x=3)
# print(res)


# def func(x, y, z=1):
#     return x+y+z
# res = func(2, 3)
# print(res)


# m=2
# print(id(m))

# def func(x,y=m): # y=>2的内存地址
#     print(x,y)
#     print(id(y))

# m=3333333333333333333
# print(id(m))
# func(1)

# import sys
# print(sys.path)

# import mol_package.mol1
# from mol_package import mol2
# from mol_package.mol3 import func3

# mol_package.mol1.func1()
# mol2.func2()
# func3()

# import mol_package as f1
# from mol_package import *
# mol_package.func1()
# mol_package.func2()
# mol_package.func3()

# func1()
# func2()
# func3()

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())
# print(__file__)

import json
l = [1, 222, 'aaa']
res = json.dumps(l)
print(res, type(res))








