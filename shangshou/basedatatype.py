#coding:utf-8

# dict基本操作
x = {"a":1,"b":2,"c":3}
print(x)
print(x["a"])
print(x.get("x"))

# 修改内容
x["c"] = "d"
print(x)

g = lambda x,y : x + y
print(g(3,5))


#list 列表
l = range(5)

print(l[2])

# tuple
z = ("a","b","c","d")
print(z[0])