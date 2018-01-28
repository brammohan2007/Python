#Write a program that does – Loop through [1..100], if a number is divisible by 3, print “fizz”,
#divisible by 5 print “buzz”, divisible by 3 & 5, print “fizzbuzz”
list1=list(range(1,100))
for i in list1:
    if (i%3==0) & (i%5==0):
        print("fizzbuzz",i)
    elif i%3 ==0:
        print("fizz",i)
    elif i%5==0:
        print("buzz",i)
