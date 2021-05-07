import matplotlib.pyplot as plt
import math as m
#save(fname,fo) fname = name of fun ,fo is format path is path return notsave fun , save fun
def save(path, fname, fo):
    fil = path + "/" + fname +"."+ fo
    
    try:
        plt.savefig(fil , dpi = 250 , bbox_inches = "tight")
        
    
    except Exception() as e:
        print(e)


def gen(limit):

    a = str(input("path "))
    b = str(input("format "))
    for i in range(1,limit+1):
        li = list()
        x = 1
        for j in range(0,200):
        #function
            
            
            fun = (x-i)**i
            li.append(fun)
            x +=1
        print(i)
        tit =" Function == math.sqrt(x**" + str(i) + ")"
        plt.plot(li)
        plt.title(tit)
        plt.xlabel("Domain")
        plt.ylabel("Range")
        try:
            save(a,tit,b)
            plt.close()
        except Exception() as e:
            print(e)