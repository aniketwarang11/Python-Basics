s = set()
"""
s_from_list = set([1,2,3,4,5])
print(s_from_list)
print(type(s_from_list))
"""
s.add(1)
s.add(2)
s.add(3)
#s1 = s.union([4,5,6])
#s1 = s.intersection([4,5,3])
s.remove(3)
print(s)
s1 = {4,5}
print(s.isdisjoint(s1))
