#lst = [99, 333, 44, 'type', 55]
#
#def foo(lst):
#    return [i for i in lst if isinstance(i, int)]
#
#print(foo(lst))


#lst = [33, 1, 22, 44, -10, 16, -74, 33]
#def foo(lst):
#    return [i for i in lst if i > 0]
#
#print(foo(lst))


#lst =[33, 19, 'next', 22]
#def foo(lst):
#    return[i if not isinstance(i, str) else 0 for i in lst]
#
#print(foo(lst))


lst = [3.3, 1.1, 2.1, 9.2]
def foo(lst):
    return sum([float(i) for i in lst])

print(foo(lst))