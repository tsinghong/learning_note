
# def func():
#     print('第一次')
#     yield 1
#     print('第二次')
#     yield 2
#     print('第三次')
#     yield 3
#     print('第四次')

# g=func() # --> 这个g就是生成器
# # print(g)



# res1=g.__next__()
# print(res1)
# res2=g.__next__()
# print(res2)
# res3=g.__next__()
# print(res3)
# res4=g.__next__()

# a = 'abcdefg'
# res = a.__len__()
# print(res)


# def my_range(start,stop,step=1):
#     # print('start...')
#     while start < stop:
#         yield start
#         start+=step
#     # print('end....')


# # g=my_range(1,10,3) # 1 3
# # print(next(g))
# # print(next(g))
# # print(next(g))


# for n in my_range(1,10,2):
#     print(n)


# def dog(name):
#     print('道哥%s准备吃东西啦...' %name)
#     while True:
#         # x拿到的是yield接收到的值
#         x = yield # x = '肉包子'
#         print('道哥%s吃了 %s' %(name,x))


# g=dog('alex')
# # g.send('肉包子')

# g.send(None) # 等同于next(g)

# g.send(['一根骨头','aaa'])
# g.send('肉包子')
# g.send('一同泔水')
# g.close()
# g.send('1111') # 关闭之后无法传值


# with open('note_of_git.md', mode='rt', encoding='utf-8') as f:
    # res = 0
    # for line in f:
    #     res += len(line)
    # print(res)
    # size_of_line = [len(line) for line in f]
    # print(size_of_line)
    # res = sum([len(line) for line in f])
    # print(res)

        
# def func1(n):
#     if n == 10:
#         return
#     print(n)
#     n += 1
#     func1(n)

# func1(0)

# def func1():
#     pass

# print(func1)

# print(lambda x, y : x + y)


# from functools import reduce
# res = reduce(lambda x, y:x+y, [1, 2, 3], 10)
# print(res)

# from mol_1 import func1
# print(func1)
# print(mol_1)

# import sys
# print(sys.path)
# print(sys.modules)


# def func(a: int, b: int) -> int:
#     c = a + b
#     return c

# res = func(1, 2)
# print(res)
# print(func.__annotations__)

# import sys
# print(__file__)


# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X'))
# print(time.localtime())
# print(time.gmtime())

# import random
# print(random.random())
# print(random.sample([1, 'a', 'b', 2,[1, 2, 3]], 3))

# import os
# print(os.listdir('.'))
# print(os.getcwd())
# res = os.path.normpath('E:\\learning_note')
# print(res)

import sys
# sys.argv()

# for f in (sys.stdin, sys.stdout, sys.stderr):
    # print(f)

import time

# res = ''
# for i in range(50):
#     res += '#'
#     time.sleep(0.1)
#     print('\r[%-50s]' % res, end='')
# print()



# num_rec = 0
# num_tot = 1025
# while num_rec < num_tot:
#     time.sleep(0.1)
#     num_rec += 1024
#     percentage = num_rec / num_tot
#     res = int (50 * percentage) * '#'
#     # print('\r[%-50s]' % res, end='')

#     print('\r[%-50s] %d%%' % (res, int(100*percentage)), end='') # 更进一步，在最后显示百分比

# print()

# def progress_bar():
#     for i in range(1, 101):
#         print("\rDownload progress: {}%: ".format(i), "#" * i, end='')
        # sys.stdout.flush()
        # time.sleep(0.05)

# progress_bar()

# import time 
# scale = 50
# print("执行开始，祈祷不报错".center(scale // 2, "-"))
# start = time.perf_counter()
# for i in range(scale + 1):
#     a = "*" * i
#     b = "." * (scale - i)
#     c = (i / scale) * 100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
#     time.sleep(0.1)
# print("\n"+"执行结束，万幸".center(scale // 2, "-"))

# import time
# def func():
#     # time.sleep(1)
#     a=time.perf_counter()#第一次调用perf_counter,所以a值应该为零,但是他不是刚好为零
#     print(a)
#     print(round(a))#把a四舍五入验证下
#     print(type(a))#验证a是浮点数
#     time.sleep(5)
#     b=time.perf_counter()#sleep5秒后,b的值就应该是5
#     print(b)
# func()


import json
l = [1, 'aaa', True, False]
res = json.dumps(l)
# print(res, type(res))
l_back = json.loads(res)
print(l_back, type(l_back))