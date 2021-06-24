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


# print('{0:*<10}'.format('开始执行')) # 开始执行******

# your_score = input("请输入你的考试分数：")
# your_score = int(your_score)
# if your_score > 60:
#     print("奖励手机一部")
# else:
#     print("不及格还想要手机？回去学习！")


# your_score = input("请输入你的考试分数：")
# your_score = int(your_score)
# if your_score > 60:
#     print("奖励手机一部")
# if your_score > 80:
#     print("奖励自行车一辆")
# print("这是if以外的代码")



# your_score = input("请输入你的考试分数：")
# your_score = int(your_score)

# # 这回奖励要缩水了，只有一个奖励，但是价值越来越高^_^
# if your_score > 90:
#     print("优秀！奖励手机一部")
# elif your_score > 80:
#     print("还行吧，奖励手环一个")
# elif your_score > 60:
#     print("刚及格，奖励鲜花一朵")
# else:
#     print("不及格还想要手机？回去学习！")

# while True:
    # print("正在运行！")

# lst = [1, 2, 'aaa', 'bbb']
# for i in lst:
#     print(i)

# for i in range(10):
    # print("正在运行第%s次" % i)

# f = open('a.txt')
# res = f.read()
# print(res)
# f.close()

# with open('c.txt', mode='rt', encoding='utf-8') as f:
#     print("第一次读".center(50, '*'))
#     res = f.read()
#     print(res)
# print("执行完毕")

# input_username = input("请输入用户名： ").strip()
# input_password = input("请输入密码： ").strip()

# with open('c.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         username, password = line.strip().split(':')
#         if input_username == username and input_password == password:
#             print("登陆成功")
#             break
#     else:
#         print("用户名或密码错误")

# with open('d.txt', mode='wt', encoding='utf-8') as f:
#     f.write("这是一句话\n")
#     f.write("这是另一句话\n")
#     f.write("这是还一句话\n")

src_file = input("请输入源文件地址：").strip()
des_file = input("请输入目标文件地址：").strip()

with open(r'{}'.format(src_file),mode='rt',encoding='utf-8') as f1,\
    open(r'{}'.format(des_file),mode='wt',encoding='utf-8') as f2:
    res=f1.read()
    f2.write(res)


src_file = input("  ")



