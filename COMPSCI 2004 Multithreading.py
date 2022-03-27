#code for multithreading a list of numbers and finding the average of those number, the maximum and minim
from threading import Thread
AVG = 0
MAX = 0
MIN = None
def FindAvg(L):#function to find the average
    global AVG
    for i in L:
        AVG += i
    AVG = int(AVG/(len(L)))
def FindMax(L):#function to find the max
    global MAX
    for i in L:
        if MAX<i:
            MAX = i
def FindMin(L):# Function to find the min
    global MIN
    MIN = L[0]
    for i in L:
        if MIN > i:
            MIN = i

def SetValues(L):#main function where you give the argument in a list
    #The function then creates threads to find the average, minimum, and Maximum.
    LIST = L
    #AVG = FindAvg(LIST)
    #MAX = FindMax(LIST)
    #MIN = FindMin(LIST)
    t1 = Thread(target=FindAvg,args=(LIST,))
    t2 = Thread(target=FindMax,args=(LIST,))
    t3 = Thread(target=FindMin,args=(LIST,))
    t1.start()
    t2.start()
    t3.start()
    print("The average value is: ",AVG)
    print("The minimum value is: ",MIN)
    print("The maximum value is: ",MAX)
    
    
