# a = 1
# b = 2
# c = a + b
# print(c)

# msg = "helloworld"
# print(msg[:5:3])


# msg = 'abcaaaadefga'
# print(msg.strip('a'))

# msg = 'abcdefga'
# print(msg.strip('a'))


# info='lilei 18 male'
# res=info.split()
# print(res) 


# info='egon:18:male'
# for x in info:
#     print(x)


# print(tuple('hello'))
# print(tuple([1,2,3]))
# print(tuple({'a1':111,'a2':333}))

# l1 = [111, 222, 333]
# l2 = ['aaa', 'bbb']
# # l1.append(l2)
# # print(l1)
# l1.insert(0, l2)
# print(l1)
# l1.extend(l2)
# print(l1)

# res = list(range(10))
# print(res[1.5])


# mls = list(range(10))
# print(mls)
# print(mls[1:4])
# print(mls[1:4:2])
# print(mls[-5:-1])
# print(mls[-5:-1:-1])
# print(mls[-1:-5])   # 反向取，这里的


# mls = list(range(10))
# print(mls[::-1]) #输出[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]，只是输出逆序结果，mls本身不变
# print(mls.reverse()) #对列表的inplace操作，无返回值，但执行后mls变为[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(mls)



# a = [1, 2, 3, 4, 5, 6]
# b = a[:]
# a[0] = 100
# print(b[0])

# import sys

# x = '张三' # 10的引用计数为1
# y = x  # 10的引用计数为2
# z = x  # 10的引用计数为3
# print("'张三'的引用次数为：", sys.getrefcount('张三'))

# a = input("请输入一个数字，你将得到它的10倍：")
# b = int(a)
# c = b * 10
# print(f'{a}的10倍是', c)

# a = int(input("请输入一个数字，你将得到它的10倍："))
# print(f'{a}的10倍是', a*10)

# print('my age is %s' % 18)
# print('my age is %s' % [1,23])
# print('my age is %s' % {'a.txt':333})
# print('my age is %d' % 18) # %d只能接收int
# print('my age is %d' % "18")


print('{0:*<10}'.format('开始执行')) # 开始执行******