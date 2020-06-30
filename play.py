

def mutate(a):
    a += "b"
    print(id(a))


a = ""
print(id(a))
mutate(a)
print(a)