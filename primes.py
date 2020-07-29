
def genPrimes():
    
    'Yield generator of prime numbers'
    
    p=[]
    x=2
    while True: 
        while True:
            prime=True
            for i in p:
                if x%i==0:
                    prime=False
                    break
            if prime==False:
                x+=1
            else:
                next=x
                break
        yield next
        p.append(x)
        x=next+1

primes=genPrimes()

def getPrimes():
    
    while True:
        n=input('How many prime numbers do you want to generate? ')
        try:
            for i in range(int(n)):
                print(primes.__next__())
            break
            
        except ValueError:
            print('Please choose a positive integer')
            
    
    