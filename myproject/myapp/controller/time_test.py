import time;
ticks = time.time()
print "now time is ",ticks


a = "2018-03-1"
timeArray = time.strptime(a, "%Y-%m-%d")
timeStamp = int(time.mktime(timeArray))
print(timeStamp)
day=time.strftime("%Y-%m-%d",time.localtime(timeStamp-7*86400))
print day

print time.strftime("%Y-%m-%d", time.localtime()) 
def binary_search(li,num,day):  
    low = num  
    high = len(li)-1   
    print "max",high
    while low <= high:  
        middle = (low + high) /2
        if li[middle] == day :
            while li[middle] == day :
                print "press",middle
                if middle == len(li)-1:
                    middle = middle+1
                    break;
                middle=middle+1
            return middle-1
        elif li[middle] > day:  
            high = middle - 1  
        elif li[middle] < day:  
            low = middle + 1  
    if middle==0 :
        if li[middle]>day:
            return -1
    elif middle == len(li)-1:
        print "123",middle
        if li[middle]<day:
            return -1
    else:
        return middle

#num=[1,2,3,4,4,5,5,7,7,7,7,8,8,8,8]
#sub=binary_search(num,0,7)
#print sub

