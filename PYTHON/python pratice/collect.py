from collections import *

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)

import collections 
print("collections list:",dir(collections))

od = OrderedDict()
od['apple'] = 3
od['banana'] = 2
od['orange'] = 5
print("OrderedDict:", od)

dd = defaultdict(int)
dd['apples'] += 1
dd['bananas'] += 2
dd["c"] #this will take zero
print("defaultdict:", dd)

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
cm = ChainMap(d1, d2)
print("ChainMap:", cm)
print("ChainMap keys:", list(cm.keys()))
print("ChainMap values:", list(cm.values()))

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print("deque after append and appendleft:", dq)
dq.pop()
dq.popleft()
print("deque after pop and popleft:", dq)

c = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print("Counter:", c)

class CustomDict(collections.UserDict):
    def popitem(self):
        raise RuntimeError("popitem is not allowed. Deletion is forbidden.")

cd = CustomDict()
for i in range(3):
    cd[f'key{i}'] = i * 10
print("CustomDict after adding values in loop:", cd)




