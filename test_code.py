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

# import json
# l = [1, 222, 'aaa']
# res = json.dumps(l)
# print(res, type(res))

# class Student:
#     def __init__(self, name, age, gender)
#     def tell_stu_school(self, stu_name):
#         print(stu_name)

# # print(Student.__dict__['stu_name'])
# # print(Student.__dict__['tell_stu_school'])

# # print(Student.stu_name)
# # print(Student.tell_stu_school())

# # stu1_obj = Student()
# # stu2_obj = Student()
# stu1_obj = Student('abc', 18, 'male')
# stu2_obj = Student('efg', 19, 'female')
# print(stu1_obj.)

# class Student:
#     stu_school = 'nau'
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def set_info(self, x, y, z):
#         self.name = x
#         self.age = y
#         self.gender = z

# stu1_obj = Student('lilei', 18, 'male')
# stu2_obj = Student('hanmeimei', 19, 'female')  
# stu3_obj = Student('poly', 17, 'male')  

# print(stu1_obj.stu_school)
# print(stu2_obj.stu_school)
# print(stu3_obj.stu_school)

# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))


# Student.stu_school = 'NAU'
# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))  # id相同，指向同一地址


# stu1_obj.stu_school = 'nnn'
# print(id(Student.stu_school))
# print(id(stu1_obj.stu_school))
# print(id(stu2_obj.stu_school))
# print(id(stu3_obj.stu_school))  # id相同，指向同一地址

# print(Student.set_info)
# print(stu1_obj.set_info)

# print(stu2_obj.set_info) # 地址不同
# print(stu3_obj.set_info) # 地址不同

# 大学管理系统：
# 学校类：决定一个学校开设多少个年级(暂时固定为4个)，一个年级有多少个班级，增减学院
# 年级类：开设哪些学科，主要是公共学科
# 学院类：开设哪些课程，主要是专业学科
# 学生类：选修哪些具体课程，必修是固定的，无法选择



dic1 = {"name": "xiaoming", "age": 27}
dic2 = {"gender": "male"}
dic1.update(dic2)
print(dic1)
# dic2["gender"] = "female"
print(dic1.get("gender"))
print(dic2.get("gender"))
print(id(dic1.get("gender")))
print(id(dic2.get("gender")))


