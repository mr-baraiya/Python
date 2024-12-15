s = set()
s.add(20)
s.add(20.0)
# python programing 1 == 1.0 true
# therefore here 20 == 20.0
# 20.0 can not added in s
s.add('20')

print(s)
print(len(s)) # 2