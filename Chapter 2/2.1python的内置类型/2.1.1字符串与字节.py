"""
1.python3中只有一种能够保存文本信息的数据类型，就是str字符串，它是不可变序列，保存的是Unicode码位。
2.字符串可以保存的数据类型就是Unicode文本；
3.字符串：所有没有前缀的字符串都是Unicode，被''、""、''''''包围且没有前缀的值都是str数据类型；
4.字节：被,''、""、'''''' 包围但必须有一个b或B前缀都是bytes字节；
"""

print(bytes([102,111,111]))

list1 = list(b'foo bar')
print(list1)

tuple1 = tuple(b'foo bar')
print(tuple1)

print(type(b'some bytes'))
print(type('string'))

#一、字符串和字节的转换：
# 1.str(字符串)encode()为bytes(字节)：encode()\bytes(source,encoding='字节序列则需要指定该参数')
string1 = 'i am coming!'
bytes1 = str.encode(string1)
print(bytes1)
print(type(bytes1))
print(bytes(string1,encoding='utf-8'))

# 2.bytes(字节)decode()为str(字符串)：decode()/str(source,encoding='字节序列则需要指定该参数')
bytes2 = b'i am bytes!'
string2 = bytes.decode(bytes2)
print(string2)
print(str(bytes2,encoding='utf-8'))
# 二、python字符串是不可变的，字节序列也是不可变的。
# 三、字符串拼接
# 1、str.join()方法接受可迭代的字符串作为参数，返回合并后的字符串
list = ['i','am','coming','!']
string3 = ' '.join(list)
print(string3)
tuple1 = ('i','am','coming','!')
string4 = ' '.join(tuple1)
print(string4)
# 2、使用+拼接字符串
a = '123'
b = '456'
print(a+b)
# 3、字符串格式化可以用str.format()或%运算符
