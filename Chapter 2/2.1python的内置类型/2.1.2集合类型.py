# 一、列表和元组
# 列表是动态的，元组是不可变，一旦创建则不可修改。
# 1.列表推导
events = []
events_ = []
for i in range(10):
    if i % 2 ==0:
        events.append(i)
    else:
        events_.append(i)
print(events_)
print(events)
# 高效写法
events1 = [i for i in range(10) if i % 2 ==0]
print(events1)
# 2.enumerate枚举，在循环中使用序列时，可以很方便获取其索引
i = 0
for element in ['one','two','three']:
    print(i,element)
    i = i +1
# 高效写法：
for j,element in enumerate(['one','two','three']):
    print(j,element)
# 3.一个一个合并多个列表中的元素zip()
for a in zip(['1','2','3'],[4,5,6]):
    print(a)
# zip()函数返回的结果再次调用zip()可将其恢复原状：
for b in zip(*zip([1,2,3],[4,5,6])):
    print(b)
# 4.序列解包,适用任意序列类型，只要=左边的变量数目和序列中元素数目相等都可以使用该方法将元素序列解包到另一组变量中
a,b,c = 1,2,3
print(a,b,c)
# 解包还可以通过带*号的表达式获取单个变量中的多个元素：
# 带*号表达式可以获取序列剩余部分
d,e,*f = 1,3,4,5,6
print(f)
# 带*号表达式可以获取序列中间部分
ab ,*cd,ef =1,2,3,4,5,6
print(cd)
# 嵌套解包
(a_,b_),(c_,d_) = (1,2),(3,4)
print(a_,b_,c_,d_)

# 二、字典与集合