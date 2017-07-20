def _range(stop):
    num=0
    while num<stop:
        print str(num)
        num +=1

def _range2(start,stop,step):
    while start>=stop:
        print str(start)
        start = start-step

_range(4)
print ""
_range2(3,0,1)
print ""
_range2(8,2,2)
