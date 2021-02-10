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

class college:
    def __init__(self, class_num):
        self.class_num = class_num
        self.academy = []
    
    def academy_manipulate(self):
        while True:
            choice_input = input("""
            请输入需要的操作：
            1. 增加学院
            2. 删除学院
            0. 退出
            """)
            if choice_input = '1':
                academy_name = input(""" 
                请输入学院名：
                """)
                self.academy.append(academy_name)
                if academy_name in self.academy:
                    print("添加成功！")
                else:
                    print("添加失败，请重新添加！")
                    # continue
            elif choice_input = '2':
                pass
            elif choice_input = '0':
                break
            else:
                print("输入的编号错误，请重新输入！")
                continue
        
        

    def tell_info(self, choice):
        while True:
            choice_input = input(""" 
            请选择要查看的信息：
            1. 查看班级数
            2. 查看公共科目
            0. 退出
            """)
            if choice_input = '1'
                choice_input = input(
                """
                请选择要查看的年级:
                1. 大一
                2. 大二
                3. 大三
                4. 大四
                0. 退出
                """)
                # 好像可以用switch语句
                if choice_input == '1':
                    print(f"大一有{self.class_num}班级")
                elif choice_input == '2':
                    print(f"大二有{self.class_num}班级")
                elif choice_input == '3':
                    print(f"大三有{self.class_num}班级")
                elif choice_input == '4':
                    print(f"大四有{self.class_num}班级")
                elif choice_input == '0':
                    print("已退出")
                    break
                else:
                    print("输入的数字有误，请重新输入！")
                    continue
            elif choice_input = '2':
                if self.academy:
                    for acad in self.academy:
                        print(acad)
                else:
                    print("尚未设置学院！")
            elif choice_input = '0':
                break
            else:
                print("输入的编号有误，请重新输入！")
                continue

college_1 = college()







