def sets(a,b):
    inter=a.intersection(b)
    uni=a.union(b)
    print("Intersection:",inter)
    print("Union:",uni)
a={1,2,3,4,5}
b={4,5,6,7,8}
sets(a,b)