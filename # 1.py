# # 1. 变量定义：学习如何存储不同类型的数据
# name = "你的名字"
# age = 25
# hobbies = ["阅读", "编程", "旅行"] # 列表(List)
# is_learning_ai = True # 布尔值(Boolean)

# # 2. 交互逻辑：简单的 if-else 判断
# print(f"你好！我叫 {name}。")

# if age < 30:
#     print("我目前处于职业发展的黄金期。")
# else:
#     print("我正在探索人生新的可能性。")

# # 3. 循环练习：遍历列表中的内容
# print("我的爱好包括：")
# for hobby in hobbies:
#     print(f"- {hobby}")

# # 4. 简单数据计算：输出基础结论
# if is_learning_ai:
#     print("目前 AI 学习进度：已启动！")

# name =  input("输入名字：")
# age = int(input("输入年龄："))

# print(f"hi{name}!you are {age}.")
# print(f"five year pass you are {age+5}")

# height  =   float(input("输入身高："))
# weight  =   float(input("输入体重："))
# bmi = weight/(height**2)

# print(f"you BMI is {bmi:.2f}")

# if bmi < 18.5:
#     status = "偏瘦"
# elif 18.5 <= bmi <24:
#     status = "正常"
# else:
#     status = "偏胖"

# print(f"根据bmi，身体评估为：{status}")

# use_role = "admin1"

# if use_role == "admin":
#     print("welcome!!")
# else:
#     print("sorry")

# baddate = [120, 85, -5, 200, "Missing", 45]

# cleaned = []

# for item in baddate:
#     if isinstance(item,int) and item > 0:
#         cleaned.append(item)

# print(f"old data :{baddate}")
# print(f"useful data :{cleaned}")
# print(f"平均值: {sum(cleaned) / len(cleaned)}")

# 2026.3.4 关键字详解：

# 1. and、or、not （逻辑运算符）
# and：如果两个语句都返回True，则返回值将仅为True，否则它将返回False。
# or：如果其中一条语句返回True，则返回值为True，否则它将返回False。
# not：如果语句不是True，则返回值为True，否则返回False。
# # 1. and、or、not （逻辑运算符）
# a = 5 > 3 and 1 < 2
# b = 5 > 3 or 1 > 2
# c = not (5 < 3)
# print(a, b, c)

# 2. if、elif、else（条件语句）

# if：用于创建条件语句（if语句），并且仅当条件为True时，才允许执行if代码块。
# elif：在条件语句（if语句）中使用，是else if的缩写。
# else：在条件语句（if语句）中使用，并确定在if条件为False时该执行的代码。

# age = int(input("请输入您的年龄："))
# if age < 18:
#     print(f"您的岁数是{age},是一个未成年人")
# elif age < 40:
#     print(f"您的岁数是{age},是一个青年人")
# else:
#     print(f"您的岁数是{age},是一个中老年人")

# 3. for、while（循环语句）

# for：用于创建一个for循环，它可以用来遍历序列，例如列表，元组等。
# while：用于定义while循环，while循环将继续，直到while的条件为False。

# languages = ["python","java","ruby","golang"]

# for i in languages:print(i,end="|")
# print("________分隔符________")

# a = 0
# while a <= 20:
#     print(a,end="--")
#     a += 1

# 4. True、False（布尔变量）

# True：关键字True与1相同。
# False：关键字False与0相同。

# print(1 < 3)
# print(5 < 2)
# print("p" in "python")


# 5. continue、break（循环控制）
#continue 跳过。break 中断？
# continue：continue关键字用于在for循环（或while循环）中结束当前迭代，并继续进行下一个迭代。
# break：break关键字用于中断for循环或while循环。

# for i in range(10):
#     if i == 5 :
#         continue
#     print(i,end="|")
# print("unuse")

# for i in range(10):
#     if i == 5 :
#         break
#     print(i,end="|")

# 6. pass（代码的占位符）
# 循环，函数定义，类定义或if语句中不允许使用空代码，则可以使用pass；当执行pass语句时，不会有任何影响，只是占位作用代表空白代码

# def fun1():
#     pass

# if 5 > 3:
#     pass

# 7. try、except、finally、raise（异常）

# try：在try…except块中使用，它定义了一个代码块，并在没有问题的情况下执行块。如果包含任何错误，可以为不同的错误类型定义不同的块。
# except：在try… except块中使用。 如果try块引发错误，并在有问题的情况下执行对应的代码块。
# finally：在try…except块中使用。它定义了一个代码块，当try…except…else块结束时，该代码块将运行。无论try块是否引发错误，都将执行finally代码块。
# raise：raise关键字用于引发异常，可以定义引发哪种错误，以及向用户显示错误信息。

# def div(x, y):
#     result = None
#     if (not isinstance(x, int)) and (not isinstance(x, float)) and (not isinstance(y, int)) and (
#             not isinstance(y, float)):
#         raise Exception("抛出一个异常,输入非数字!")
#     result = x / y
#     return result

# div("哈哈", "我")

# def div(x, y):
#     result = None
#     try:
#         result = x / y
#         print(f"运算结果为{result}")
#     except Exception:
#         print("除数为0，异常！")
#     finally:
#         print("此语句必定指定")
#     return result

# div(1, 2)
# print("split")
# div(1,0)

# 8.  import、from、as（模块导入）

# import：用于导入模块。
# from：用于从模块中导入指定的部分，按需要导入指定子类或函数，减少不必要的资源浪费。
# as：用于创建别名。
