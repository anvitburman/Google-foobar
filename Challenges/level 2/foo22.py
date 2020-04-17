# Hey, I Already Did That!
# ========================
# Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep her minions on their toes. But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a case for your next promotion. 
# You have worked out that the algorithm has the following process: 
# 1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
# 2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
# 3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
# 4) Assign n = z to get the next minion ID, and go back to step 2
# For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.
# Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.
# Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function answer(n, b) which returns the length of the ending cycle of the algorithm above starting with n. For instance, in the example above, answer(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.
# Languages
# =========
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
# Test cases
# ==========
# Inputs:
#     (string) n = "1211"
#     (int) b = 10
# Output:
#     (int) 1
# Inputs:
#     (string) n = "210022"
#     (int) b = 3
# Output:
#     (int) 3
def countdigits(n):
    return len(str(n))

def decitobase(n,b):
    temp=n
    res=0
    while(temp>0):
        rem=temp%b
        res=res*10+rem
        temp=int(temp/b)
    res=str(res)
    return(int(res[::-1]))


  
def bastodec(n,b): 
    l=len(str(n))
    temp=n
    res=0
    for i in range(0,l):
        rem=temp%10
        res=rem*(b**i)+res
        temp=int(temp/10)
    return res
    

def solution(n , b):
    flag=True
    list=[]
    count=0
    dig=countdigits(n)
    while(flag):
        asc="".join(sorted(str(n)))
        des="".join(sorted(str(n),reverse=True))
        
        x=bastodec(int(asc),b)
        y=bastodec(int(des),b)
      
        z=decitobase(y-x,b)
        if(countdigits(z)!=dig):
            z=str(z*(10**(dig-countdigits(z))))
        else:
            z=str(z)

        for ind,item in enumerate(list):
            if(item==z):
                return ind+1
                break
        list=[z]+list
        n=z
        

x=solution('210022',3)
print(x)


