
def pow(a,n,ti):

    if n==0:
        ti=1
        return 1
    if n==1:
        ti = 1
        return a
    if n%2==0:
        res=pow(a,n/2,ti)
        ti += 1
        return res*res
    else:
        res = pow(a, n -1,ti)
        ti += 1
        return a * res
a=3
n=12
ti=10
print(pow(a,n,ti))
print(ti)


long long int ipow(long long int a, unsigned int n, unsigned int * depth)
{
    long long int res=0;
    if (n==0)
        *depth=1;
        return 1;
    if (n==1)
        *depth=1;
        return a;
    if (n%2==0)
        res=ipow(a,n/2,depth);
        *depth+=1;
        return res*res;
    if (n%2==1)
        res=ipow(a,n-1,depth);
        *depth+=1;
        return a*res;
}

