#euclid's algorithm

def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n==0):
        return(n)
    else:
        return(gcd(max(n,m-n),min(n,m-n)))
print(gcd(int(input()),int(input())))