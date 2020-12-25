
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




