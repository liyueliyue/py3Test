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

# 字符串和字节的转换：