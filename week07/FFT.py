import math
def FFT(a,invert) :
    n = len(a) # n = 2^k
    j = 0
    for i in range(1,n) :
        bit = n >> 1
        while j >= bit : j -= bit ; bit >>= 1
        j += bit
        if i < j : a[i] , a[j] = a[j] , a[i]
    L = 2
    while L <= n :
        ang = ( 2 * math.pi / L ) * ( -1 if invert else 1 )
        wL = complex( math.cos(ang) , math.sin(ang) )
        for i in range(0,n,L) :
            w = complex(1,0)
            for j in range( 0 , L//2 ) :
                u = a[i+j] ; v = a[i+j+L//2] * w
                a[ i+j        ] = u + v
                a[ i+j + L//2 ] = u - v
                w *= wL
        L <<= 1
    if invert :
        for i in range(n) : a[i] /= n

def FFTMultiply(a,b,res) :
    n = 1
    while n < max( len(a) , len(b) ) : n <<= 1
    n *= 2
    a += [0] * ( n - len(a) )
    b += [0] * ( n - len(b) )
    FFT(a,False)
    FFT(b,False)
    for i in range(n) : a[i] *= b[i]
    FFT(a,True)
    for i in range(n) : a[i] = a[i].real
    res += [0] * ( n - len(res) )
    for i in range(n) :
        if a[i] > 0 : p = 0.5
        else : p = -0.5
        res[i] = int( a[i].real + p )

import sys ; input = sys.stdin.readline

u , u_list = int(input()) , list(map(int,input().strip().split()))
m , m_list = int(input()) , list(map(int,input().strip().split()))
l , l_list = int(input()) , list(map(int,input().strip().split()))
minimum , maximum = min( u_list+m_list+l_list ) , max( u_list+m_list+l_list )

u_FFT , l_FFT = [0] * (maximum-minimum+1) , [0] * (maximum-minimum+1)
for ul in u_list : u_FFT[ul-minimum] = 1
for ll in l_list : l_FFT[ll-minimum] = 1

result = []
FFTMultiply(u_FFT,l_FFT,result)

cnt = 0
for ml in m_list :
    if (ml-minimum)*2 < len(result) and result[(ml-minimum)*2] != 0 : cnt += result[(ml-minimum)*2]
print(cnt)
"""
해결 방법
1. 기본적으로 바늘이 3개의 선분을 지나가기 위해선 u점과 m점을 지날 때의 기울기와 m점과 l점의 기울기가 같아야 하고, 동시에 이때, m의 위치가 같아야 한다. 
2. 즉, u+l = 2 * m 를 만족한다. 
3. u+l를 구하기 위해 convolution 합성곱을 이용하는데 더 빠르게 하기 위해 단순히 모든 원소를 곱해주는 것이 아닌 고속 푸리에 변환을 사용한다.
4. 그 후 u와 l의 합성곱을 m의 원소와 비교해준다. 
"""

"""
수행시간 분석
1. u_list를 생성하는 시간 O(u), m_list를 생성하는 시간 O(m), l_list를 생성하는 시간 O(l)
2. 세 리스트에서 minimum 값과, maximum 값을 구해주는 시간 O(u+m+l)
3. u와 l의 합성곱을 구하는 FFT 함수는 n개 수열의 이산 푸리에 변환 문제를 n/2개 수열의 이산 푸리에 변환 x 2 로 환원시켜 T(n) = 2*T(n/2) + O(n)의 점화식이 나오게 되는데 이를 전개하면 O(nlogn)이 나온다.
4. 마지막에 u와 l의 합성곱으로 나온 것과 m_list을 비교하는 시간은 O(m)
5. 수행시간은 O(nlogn)
"""