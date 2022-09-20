import math

 
#Input Prime Numbers
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
 
#Check if Input's are Prime
def prime_check(a):
    if(a==2):
        return True
    elif((a<2) or ((a%2)==0)):
        return False
    elif(a>2):
        for i in range(2,a):
            if not(a%i):
                return False
    return True
 
check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p==False)or(check_q==False))):
    p = int(input("Enter a prime number for p: "))
    q = int(input("Enter a prime number for q: "))
    check_p = prime_check(p)
    check_q = prime_check(q)
 
#RSA Modulus
n = p * q
print("n=p*q is: ",n)
 
#Eulers Toitent
r= (p-1)*(q-1)
print("phi(n)=(p-1)*(q-1) is: ",r)
 
#GCD
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
#Euclid's Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        return s%r
 
#e Value Calculation
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print("gcd is:",e)
 
#Private and Public Keys
eugcd(e,r)
d = mult_inv(e,r)
public = (e,n)
private = (d,n)
print("\n\nPrivate Key: ",private)
print("Public Key: ",public)
 
#Encryption
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            x.append(400)
    return x
     
 
#Decryption
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
#Message
message = input("Enter message: ")
print("Your message is:",message)
 
#Choose Encrypt or Decrypt and Print
choose = input("for encryption 1 and for decrytion 0: ")
if(choose=='1'):
    enc_msg=encrypt(public,message)
    print("Your encrypted message is:",enc_msg)
elif(choose=='0'):
    print("Your decrypted message is:",decrypt(private,message))
else:
    print("ERROR!!.")
