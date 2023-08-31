# -*- coding: utf-8 -*-


def prime(num):
    for k in range(2,num):
        if int(num)% int(k)==0:
            return False
    return True

def main(a,b):
    ans={}
    for num in range(a,b):
            c=prime(num)
            if c:
                ans[num]=bin(num)[2:]
            else:
                divisors=[]
                for j in range(1,num+1):
                    if int(num)%int(j)==0:
                        divisors.append(j)
                    ans[num]=divisors
    return ans
                        
a=int(input("Enter start no:"))
b=int(input("Enter end no.:"))
                    
result_ans=main(a,b)
print(result_ans)
   