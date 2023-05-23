import math
points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
dis = list(range(len(points)))
print(dis)
a = 0
#your code goes here
for x, y in points:
    dis[a]=math.sqrt(x**2+y**2)
    a += 1
print(min(dis))












contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}
#your code goes here
name = "James"
#name = input()
if name in contacts:
    a = contacts.get(name)
    print(a[1])
    #print(contacts.get(name))
else:
    print("Not found")