import math

def algo2(n):
    minr = 2
    r = True
    while r == True:
        for k in range(1,int(math.log(n,2)**2)):
                if n**k % minr > (math.log(n))**2 :
                    m = minr
                    r = False
                    return m
                    #print(r)
                    #break
        minr = minr + 1

def phi(n):
    phi = 1                         # 1 because the range is 1 - minr 
    for a in range(1,algo2(n)):
        if math.gcd(a,algo2(n)) == 1:
            phi = phi + 1
            return phi


def algo4(n):
    #Step 1: If n = a^b for integers a > 1 and b > 1, output composite.
    for a in range(2,math.ceil(math.log(n,2))):  #log of base 2 is used because the least is a square number so need ot check atmost sqrt(n)
        b = math.log(n)/math.log(a)
        #print(b)
        if b == int(b): 
            return False
            # break
            # sys.exit('Coposit')

    for a in range(2,algo2(n)):
        #print(a)
        if math.gcd(a,n) > 1 and math.gcd(a,n) < n:
            return False
            #break
            #quit()

    #Step 4: If n ≤ r, output prime.
    if n <= algo2(n):
        return True
        #quit()



def algo5(n):
    index = 0
    for i in range(1,int(math.sqrt(phi(n))*math.log(n))):
        multiple = i**n - i 
        #print(multiple)
        #print(i)
        if multiple%n == 0: 
            index = index + 1
        else:
            break
    if index == int(math.sqrt(phi(n))*math.log(n)) - 1:
        return True
    else:
        return False

def aks(n):
    if algo5(n) is True or algo4(n) is True:
        return f"{n} is prime"
    elif algo4(n) is False or algo5(n) is False:
        return f"{n} is not prime"


print(aks(3166))

