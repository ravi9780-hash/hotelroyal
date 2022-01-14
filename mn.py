# k=open("my.txt","w")
# k.write("hello my name is ravi refh" )
# k.seek(5)

# if k:
#     print("done")

# j=open("my.txt","r")
# k=j.readlines()
# print(k)
# n=j.read(10)
# print(n)
# j.close()
from os import error


def k():
    print("something happend")
# try:
#     a=10
#     b=0
#     c=a/b
# except Exception as e:
#     print("can not be done")
#     k()


# try :
#     k=int(input("enter age"))
#     if k<18:
#         raise ValueError
#     else:
#         print("valid age")
# except ValueError:
#     print("age is not above 18")


# custome exception

class cu(Exception):
    def __init__(self,p):
        self.p=p
    def __str__(self) :
        return repr(self.p)
try:
    raise cu(30)
except cu as e:
    print("error",e.p)
