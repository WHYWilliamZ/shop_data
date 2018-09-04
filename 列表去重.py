#1. 使用python将列表数据去重。比如，[2, 1, 2, 3]  => [2, 1, 3]， [2, [1, 2], 3] => [2, [1, 2,], 3]


a = [2, [1, 2], 3,3,[1,2]]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)




from functools import reduce

a = [2, [1, 2], 3,3,[1,2]]
func = lambda x,y:x if y in x else x + [y]
result = reduce(func, [[], ] + a)
print(result)