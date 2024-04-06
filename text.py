print("hellow world!")
age = 18
name = 'TOM'
weight = 60.3
stu_id = 1
# 今年我的年龄是多少岁
print('今年我的年龄是%d岁' % age)
# 我的名字是
print('我的名字是%s' % name)
# 我的体重是
print('我的体重是%.3f' % weight)
print('我的体重是%f' % weight)
# 我的学号
print('我的学号是%04d' % stu_id)
# 我的名字是x,今年x岁了
print('我的名字是%s,今年%d岁了' % (name, age))
# 我的名字是x，明年x岁了
print('我的名字是%s,明年%d岁了' % (name, age + 1))

# 我的名字是x,今年x岁了,体重是x
print(f'我的名字是{name}, 今年{age}岁了，体重是{weight}')
print('我的名字是%s,今年%s岁了,体重是%s' % (name, age, weight))

print('hello\npython')
print('\tabcd')

print('输出的内容', end="\n")

print('hello', end="\n")
print('world', end="\t")
print('hello', end="...")  # 以"..."作为结束并输出
print('python')

# password = input('请输入')
# print(f'输入为{password}')

str1 = '10'
print(float(str1))
print(type(str(age)))
list1 = '[10, 20, 30]'
tuple1 = '(20, 23, 45)'
print(list1)
print(tuple(list1))
print(list(tuple1))

a = 12
b = 15
c = a - b if a > b else b - a
print(c)
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print('媳妇我错了')
        j += 1
    print('每天一次刷碗')
    i += 1

str2 = '0123456'
print(str2[2:5])
