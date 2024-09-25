# def outer_fun(fun):
#     def inner_fun(a,b):
#         a=a+10
#         b=b+10
#         return fun(a,b)
#         fun(a,b)
#         print("main function call")
#     return inner_fun

# def main_fun(a,b):
#     return a+b    

# @outer_fun
# def main_fun(a,b):
#     return  a+b
# a=main_fun(5,6)
# print(a)

# basics of decoratores:

 # nested_function....
# def fun1(x):
#     def fun2(y):
#         return x+y
#     return fun2
# var1 = fun1(5)
# var2 = var1(5)
# print(var2)

# function pass as a argument....
# def add(x,y):
#     return x+y

# def cal(func,x,y):
#     return func(x,y)

# var1 = cal(add,4,5)
# print(var1)

# function that returns a function.......
# def fun1(num):
#     def fun2(x):
#         x=num+x
#         return x
#     return fun2

# var1 = fun1(5)
# var2 = var1(10)

# print(var2)

def outer_fun(fun):
    def inner_fun():
     return fun()
    return inner_fun

@outer_fun
def display():
    print("This is from abhishek kumar")
display()
