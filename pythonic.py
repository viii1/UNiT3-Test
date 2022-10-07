#zen of python
#from concurrent.futures.thread import _threads_queues
#import this


#one statement per line
# print("hello")
# print("vivek")
# print("hello",end=" ");print("dhruvi")




# true_value=True
# false_value=False
# none_value=None

# if true_value:
#     print("truthy")
# if false_value:
#     print("Falsey")


# #Testing for  None
# if none_value is None:
#     print(None)





#Ex. to swap variables you can use

# tmp = b
# b = a 
# a = tmp
# print(a);print(b)

# a,b = b,a







#To initialise a list with even numbers up to 2*n, 
# you can write it the following way :

l = [] 
i = 0 
n=5
while (i <= n): 
    l.append(i*2) 
    i += 1 # No ++ available :\ 
    print(l)
print(l)

#pythonic 
l = [2*x for x in range(0, n+1)]
print(l)
