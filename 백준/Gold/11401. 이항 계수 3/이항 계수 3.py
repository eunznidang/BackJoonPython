def factorial(N, mod):
    res=1
    for i in range(1, N+1):
        res=(res*i)%mod
    return res

# 모듈러 역원: a**(mod-2)%mod
def modular(a, mod):
    return pow(a, mod-2, mod)

N, K=map(int, input().split())
mod=1000000007

a=factorial(N, mod)
b=(factorial(K,mod)*factorial(N-K,mod))%mod
# a/b를 a * modular(b)로 변환
result=(a * modular(b,mod))%mod

print(result)