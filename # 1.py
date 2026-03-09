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
# import time
# from time import sleep as s
# print(time.ctime())
# s(3)
# print(time.ctime())

# 9. def、return（函数）

# def：用于创建（或定义）一个函数。

# return：用于结束所定义的函数，并返回值。

# def mysum(a,b):
#     return a+b

# mysumuse = mysum(9,21)

# print(mysumuse)

# print(mysum(12,23))

# 10. class（类）

#  class关键字用于创建（或定义）一个类。
# class Zhao:
#     name = "fermis"
#     age = 20
#     height = 1.80
#     weight = 70

# s = Zhao()
# name = s.name
# age = s.age
# print(name,age)
# height = s.height
# weight = s.weight
# print(name,age,height,weight)

# 11. lambda（匿名函数）

#  lambda关键字用于创建一个 特殊的“匿名函数”

# g = lambda z:z**64

# print(g(2))

# 12. del（删除对象）

# 在Python中，一切皆对象。del关键字主要用于删除对象，还可以用于删除变量，列表或列表的一部分等

# x = 1

# del x

# listl = [1,2,3,4,5,6,7,8,9,10]

# del listl[0]

# print(listl)

# 13. global、nonlocal（声明变量作用域）

#  global关键字用于创建一个全局变量。nonlocal关键字用于声明一个非局部变量，用于标识外部作用域的变量。

# x = 10
# def global_test():
#     global x
#     x = 21
#     return x

# def nonlocal_test():
#     count = 0
#     def test2():
#         nonlocal count
#         count += 1
#         return count
#     return test2

# num1 = global_test()
# print(num1)
# print(x)
# print("fffffffffff分隔线ffffffffffffff")

# val = nonlocal_test()
# print(val())
# print(val())
# print(val())


# 14. in、is（判断语句）

# print("z"in"zhao")
# print("z"not in "zhao")

# l1 = [1, 2, 3]
# l2 = l1.copy()
# l3 = l1
# print(l1 is l2)
# print(l1 is l3)


# 15. None（空值）

#  None关键字用于定义一个空值（根本没有值），与0，False或空字符串不同。 None是其自身的数据类型（NoneType）

# x = None

# print(x)

# y = [1,3,4,].reverse()
# z = [1,24,55,55,33]
# print(y)

# print(z)
# 16. assert（测试代码）

#  调试代码时，使用assert关键字。主要用于测试代码中的条件是否为True，如果为False，将引发AssertionError

# f-string与其他格式化方式对比
# 格式化方式	语法示例	特点
# f-string	f"Hello {name}!"	简洁、直观、支持表达式
# str.format()	"Hello {}!".format(name)	兼容性好（Python 2.6+），但代码较长
# % 操作符	"Hello %s!" % name	传统方式，可读性差，不支持复杂表达式
# str.join()	"Hello " + name + "!"	字符串拼接，代码冗长，易出错

# x = 10

# try:
#     assert x == 10
#     print(f"x == 10","赵江波")
#     assert x == 11
# except :
#     print(f"test fail x right={x}")


# 17. with（文件处理）

# with常和open使用，用于读取或写入文件
# with语句：

# 语法：with 上下文管理器 as 变量:
# 作用：创建一个上下文环境，在进入和退出时自动执行特定操作
# 优势：确保资源（如文件）在使用完毕后被正确释放，即使发生异常
# open()函数：

# 语法：open(file, mode)
# 参数：
# file：文件路径
# mode：打开模式（"r"表示只读）
# 返回值：文件对象
# 文件读取：

# f.read()：读取文件的全部内容并返回字符串
# 自动资源管理：

# 当with块执行完毕时，无论是否发生异常，文件都会被自动关闭
# 这避免了手动调用f.close()的需要，减少了资源泄露的风险
# with open("data.txt","r") as f:
#     print(f.read())
# 18. yield（生成器）

#  yield关键字结束一个函数，返回一个生成器，用于从函数依次返回值。

# 第340-341行：定义了一个生成器函数 yieldtest()

# 使用 yield 关键字，使其成为生成器函数
# 当被迭代时，会产生值 10
# 第342行：print(yieldtest)

# 打印函数对象本身，而不是调用函数
# 输出：函数的内存地址表示，如 <function yieldtest at 0x...>
# 第343行：print(yieldtest())

# 调用生成器函数，返回一个生成器对象
# 输出：生成器对象的内存地址表示，如 <generator object yieldtest at 0x...>
# 注意：此时函数体并未执行，只是创建了生成器对象
# 第344行：print(next(yieldtest()))

# 调用 yieldtest() 创建新的生成器对象
# 调用 next() 函数获取生成器的第一个值
# 执行函数体到 yield 10，返回值 10
# 输出：10

# def yieldtest():
#     yield 10
# print(yieldtest)
# print(yieldtest())
# print(next(yieldtest()))


# 19. async、await（多线程）

# （1）协程（Coroutine），也可以被称为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行

# yield，生成器，借助生成器的特点也可以实现协程代码

# async & awiat，在Python3.5中引入的两个关键字，结合asyncio模块可以更方便的编写协程代码

#  （2）async 用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，去执行其他异步函数，等到挂起条件（假设挂起条件是sleep(5)）消失后，也就是5秒到了再回来执行

# （3）await 用来用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异步程序。await 后面只能跟异步程序或有__await__属性的对象，因为异步程序与一般程序不同

# （4）举例说明：

# 假设有两个异步函数async a，async b，a中的某一步有await，当程序碰到关键字await b()后，异步程序挂起后去执行另一个异步b程序，就是从函数内部跳出去执行其他函数，当挂起条件消失后，不管b是否执行完，要马上从b程序中跳出来，回到原程序执行原来的操作。如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，无法在b执行的过程中返回。如果要在b执行完才返回，也就不需要用await关键字了，直接调用b函数就行。所以这就需要await后面跟的是异步函数了。在一个异步函数中，可以不止一次挂起，也就是可以用多个await。
# import time
# import requests
# import asyncio

# async def test2(i):
#     r = await other_test(i)
#     print(i, r)


# async def other_test(i):
#     r = requests.get(i)
#     print(i)
#     await asyncio.sleep(4)
#     print(time.time() - start)
#     return r


# url = ["https://segmentfault.com/p/1210000013564725",
#        "https://www.jianshu.com/p/83badc8028bd",
#        "https://www.baidu.com/"]

# loop = asyncio.get_event_loop()
# task = [asyncio.ensure_future(test2(i)) for i in url]
# start = time.time()
# loop.run_until_complete(asyncio.wait(task))
# endtime = time.time() - start
# print(endtime)
# loop.close()

# print("end")

#软关键字
# match（软关键字，3.10 + 引入的模式匹配）
# 作用：根据不同的模式匹配数据，有点像升级版的 switch-case，更灵活。
# 常用场景：处理不同结构的数据，比如解析 API 返回的不同状态。
# 错误点：后面必须跟表达式；case 块里的模式要写对，比如用_表示任意值。
# 基础案例：简单模式匹配
# case（软关键字，和 match 配对使用）
# 作用：定义 match 中的具体匹配模式，每个 case 对应一种情况。
# 常用场景：和 match 一起用，写不同的匹配分支。
# 错误点：不能单独使用，必须在 match 块里；模式语法要正确，比如用|表示或关系。
# 基础案例：多个模式匹配

# status = "success"
# match status:
#    case "success":
#        print("操作成功！")  # 匹配成功，执行这里
#    case "fail":
#        print("操作失败！")
#    case _:  # 匹配其他任意值
#        print("未知状态")

# num = 5
# match num:
#    case 1 | 2 | 3:  # 匹配1或2或3
#        print("小数字")
#    case 4 | 5 | 6:
#        print("中数字")  # 匹配5，执行这里
#    case _:
#        print("大数字")

# 软关键字：_（下划线，在模式匹配中作为通配符）
# 作用：在 match-case 中表示匹配任意值，相当于 "随便什么都行"。
# 常用场景：模式匹配中不想处理的情况，用_来占位。
# 错误点：平时可以当变量名用（虽然不推荐），但在 match-case 中是软关键字。
# value = "任意值"
# match value:
#    case _:  # 匹配所有情况
#        print("不管是什么，都执行这里")  # 会执行
# 软关键字：*（在模式匹配中表示收集多个元素）
# 作用：在 match-case 中，匹配多个元素并收集到列表中，类似函数的 * args。
# 常用场景：匹配可变数量的元素，比如元组中的多个值。
# 错误点：只能在模式匹配的解构中使用，比如case (a, *rest):。
# numbers = (1, 2, 3, 4, 5)
# match numbers:
#    case (first, *rest):  # first是1，rest是[2,3,4,5]
#        print(f"第一个数是{first}，剩下的是{rest}")  # 会执行
# 软关键字：...（Ellipsis，在模式匹配中表示占位符）
# 作用：在模式匹配中，暂时不处理的情况，作为占位符，类似 pass。
# 常用场景：编写模式匹配时，先占位，后续再补充代码。
# 错误点：平时是一个内置对象，在模式匹配中作为软关键字。
# def handle_value(value):
#    match value:
#        case 1:
#            print("处理1")
#        case 2:
#            print("处理2")
#        case ...:  # 其他情况暂时不处理
#            pass


# import sys
# print("Python解释器路径:", sys.executable)
# print("Python版本:", sys.version)


