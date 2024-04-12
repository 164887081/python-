# 元组
"""
t1 = (10, 20, 30)
# print(t1)
# print(type(t1))

dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}
print(dict1)
print(type(dict1))
# 字典不支持下标 字典是
# 创建空字典
dict2 = {}
print(type(dict2))

dict3 = dict()
print(type(dict3))

str1 = 'lu si '
str2 = 'hello'
str3 = str1 + str2
print(str3)
"""
"""
# 创建一个列表
my_list = [1, 2, 3, 4, 5]

# 将列表转换为迭代器
my_iterator = iter(my_list)

# 使用迭代器遍历列表
try:
    while True:
        element = next(my_iterator)
        print(element)
except StopIteration:
    pass

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# upe1 = dict1.items()
# print(upe1[0])
for item in dict1.items():
    print(item[1])

[dict1, dict2] = [2, (2, 3, 4, 4)]
print(dict1)
print(dict2)

list1 = []
for i in range(1, 3):
    for j in range(4):
        list1.append([i, j])
print(list1)

# 列表推导式
list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)
"""
"""
# 字典推导式目标：快速合并列表为字典或者是提取字典中的目标数据
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, '男']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}  # i必须是可迭代对象，因此使用range返回的也是可迭代对象
print(dict1)
# print(range(len(list1)))
# 假如说两个列表数据个数不同
# 如果两个列表长度相同，那么len统计任何一个列表长度都可，若不同，统计列表多的，报错，统计少的不报错
dict1 = {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}
"""
"""
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)
print(type(dict1))
sets1 = {1, 2, 3}
print(sets1)
print(type(sets1))

count = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
list1 = count.keys()  # 通过keys函数得到的依然是字典的key，本质上依然是字典，需要显示的转化为列表，才能按照列表方式使用
list2 = list(list1)
list3 = count.values()
list4 = list(list3)
print(list1)
print(list2[0])
print(list3)
print(list4)
print(type(list1))
print(type(list2))
print(type(list3))  # <class 'dict_values'>
print(type(list4))
#  items函数理解  返回是可迭代对象，每个键值对构成一个元组
print(count.items())  # dict_items([('MBP', 268), ('HP', 125), ('DELL', 201), ('Lenovo', 199), ('acer', 99)])
list5 = list(count.items())
print(list5[0])
# print(count.keys())

# test = count.items()
# print(test.)
# print(count.items())
# print(type(count.items()))

count = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 希望提取字典中的目标数据--提取销售量大于200的键值对--由于要饭返回的一对数据，因此使用字典推导式
# 由于字典返回的是迭代器，其中内部是元组，因此需要用到拆包，两个临时变量拆包去接收
dict1 = {keys: values for keys, values in count.items() if values >= 200}
# print(dict1)

print(count.items())  # dict_items([('MBP', 268), ('HP', 125), ('DELL', 201), ('Lenovo', 199), ('acer', 99)])
# 根据上面输出的迭代器，可以得到，每个键值对构成一个元组，那么如果for循环过程中不拆包，使用一个变量接收，那么每次接收一个元组元素，然后存入到列表中
dict1 = [values for values in count.items()]
print(dict1)  # [('MBP', 268), ('HP', 125), ('DELL', 201), ('Lenovo', 199), ('acer', 99)]
#  这么做其实就相当于将元组构成的键值对构成一个集合，每个键值对作为一个整体
list1 = {key for key in count.items()}
print(list1)

# 集合推导式
list1 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)  # 集合具有去重功能

# 实现函数
def user_info(name, age, gender):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')


user_info('Tom', 20, '男')  # 位置参数
user_info('Tom', gender='男', age=20)  # 位置参数必须在关键字参数之前，但关键字参数不存在先后顺序
help(user_info)

# 缺省参数--所有位置参数在默认参数之前，函数调用时，如果缺省参数传值则修改默认参数
def user_info(name, age, gender='男'):
    print(f'您的名字是{name},年龄是{age},性别是{gender}')

user_info('Tom', 18)  # 使用默认值
user_info('ROSS', 18, '女')

# 不定长参数
def user_info(*args):
    # 包裹位置参数实现不定长参数
    # 传进去所有参数通过args变量收集，根据传进参数的位置合并为一个元组
    # args是元组类型
    print(args)
user_info('Tom')
user_info('Tom', 20)
user_info()

def user_info(**kwargs):
    # kwargs输出是一个字典的形式--收集所有关键字返回一个字典
    print(kwargs)
# 无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程
user_info()
user_info(name='Tom', age=20)

# 拆包与组包正反两方面
# 拆包字典
dict1 = {'name': 'Tom', 'age': 20}
a, b = dict1
# 对字典拆包，取出来的是字典的key
print(a)
print(b)
print(dict1[a])
print(dict1[b])

c, d = 10, 82
print(c, d)
c, d = d, c
print(c, d)

aa = [1, 2, 3]
bb = aa
print(id(aa))
print(id(bb))
aa.append(4)
# aa.extend([10, 12])
print(aa)
print(id(aa))
print(id(bb))

a = [1, 2, 3]
b = [9, 3, 4]
a = [a[i] + b[i] for i in range(len(a))]
print(a)
"""


def info_print():
    print('请选择功能-----------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出系统')
    print('-' * 20)


# 等待存储所有学员的信息
info = []


# 添加学员信息
def add_info():
    """添加学员函数"""
    global info
    # 接收信息
    new_id = input('请输入学号: ')
    new_name = input('请输入姓名: ')
    new_phone = input('请输入手机号: ')
    # 判断学员姓名是否存在
    for i in info:
        if new_name == i['name']:
            print('该用户已存在')
            return  # return 的作用是退出当前函数，后面添加信息不执行

    # 为每一位新学员准备一个空字典,然后把这个字典追加到列表中
    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_phone
    # print(info_dict)
    # 将该学员信息的字典添加到列表
    info.append(info_dict)
    # print(info)


while True:
    info_print()
    user_num = int(input('请输入功能序号：'))
    if user_num == 1:
        print('添加')
        add_info()
    elif user_num == 2:
        print('删除')
    elif user_num == 3:
        print('修改')
    elif user_num == 4:
        print('查询')
    elif user_num == 5:
        print('显示所有')
        print(info)
    elif user_num == 6:
        print('退出系统')
        break
    else:
        print('输入有误')

# 学员信息采用字典存储，然后每个班级有多个学员，可以采用列表存储，列表内是字典
# 由于各个函数要对列表进行操作，那么这个列表应该是全局变量
