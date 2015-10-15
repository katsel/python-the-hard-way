numbers = []

def loopfun(number, change):
    i = 0
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += change
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

numbers2 = []
def loopfun_2(number, change):
    for i in range(0,number,change):
        print "\tAt the top i is %d" % i
        numbers2.append(i)
#        i += change
        print "\tNumbers now: ", numbers2
        print "\tAt the bottom i is %d" % i

loopfun(6,2)
loopfun_2(6,2)

print "The numbers: "

for num in numbers:
    print num

for num in numbers2:
    print "\t", num
