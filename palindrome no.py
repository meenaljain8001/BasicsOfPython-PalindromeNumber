# palindrome numbers

def palindromeNumbers(list_a):
    c = 0
    
    for i in list_a:
        t = i
        rev = 0
        while t>0:
            rev = rev*10+t%10
            t = t/10
            
            if rev == i:
                print(i)
                c = c+1
                
    print
    print "total pallindrome numbers are", c
    print

def main():
    list_a = [10,121,133,155,141]
    palindromesNumbers(list_a)
    list_b = [111,220,151,363,454]
    palindromeNumbers(list_b)

if_name_=="_main_":
    main()            