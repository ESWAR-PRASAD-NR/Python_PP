a = 10 # global scope
print(type(a))
b = 5
a,b = b,a 
print(a,b)
def update():
    """
    desc:
    Update value of a
    """
    global a
    a=20 # local to this function
update()
c=100
d=150
print(a, b,c, sep=",",end=" ", file=open('out.txt', 'w'))
print(d)

try:
    a = int(input("Enter input:"))
except Exception as e:
    print(str(e))
print(type(a))
