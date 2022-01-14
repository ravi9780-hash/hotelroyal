
# from threading import *
# import threading
# class hello(Thread):
#     def run(self):
#         for i in range(10):
#             print("hello")

# class hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("hi")
# p1=hello()
# p1.start()  
# p2=hi() 
# p2.start()
# p1.join()
# p2.join()
# print("bye")
# def dis():
#     for i in range(5):
#         print("hello")

# def dish():
#     for i in range(5):
#         print("hi")



# t1=Thread(target=dis)
# t1.start()
# t2=Thread(target=dish)
# t2.start()
# class p:
#     def __init__(self,t):
#         self.t=t

#     def go(self):
#         for i in range(5):
#             print(self.t,"happening",i)
# h1=p("Take order")
# t1=Thread(target=h1.go)
# t1.start()
# h2=p("deliver order")
# t2=Thread(target=h2.go)
# t2.start()
# thread race confition

# class p:
#     def __init__(self,avs):
#         self.av=avs
#         self.l=Lock()
#     def book(self,need):
#         self.l.acquire(blocking=True,timeout=-1)
#         if self.av>need:
           
#             self.av=self.av-need
#             print(self.av)
#             print("seats are book for ",current_thread().name)
#         else:
#             print("sorry no seats available for this",current_thread().name)
#         self.l.release()


# g=p(10)

# t1=Thread(target=g.book,args=(8,),name="suresh")
# t2=Thread(target=g.book,args=(3,),name="mahesh")
# t1.start()
# t2.start()
# k=open("my.txt","r")
# if k:
#     print("opened")
print("hello")