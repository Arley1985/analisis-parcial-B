## punto 3
import marth

def sieve(n):
    
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

def primes_in_intervals(intervals):
    max_b = max(b for a, b in intervals)
    is_prime = sieve(max_b)
    
    prefix = [0] * (max_b + 1)
    for i in range(1, max_b + 1):
        prefix[i] = prefix[i-1] + (1 if is_prime[i] else 0)
   
    result = []
    for a, b in intervals:
        count = prefix[b] - prefix[a-1] if a > 1 else prefix[b]
        result.append(count)
    return result

if __name__ == "__main__":
    N = int(input())
    intervals = []
    for _ in range(N):
        a, b = map(int, input().split())
        intervals.append((a, b))
    counts = primes_in_intervals(intervals)
    for c in counts:
        print(c)


## punto 2
import math

def find_threshold():
    for n in range(1, 1000):
        t1 = 5 * n**2 + 10 * n
        t2 = 6 * n * math.log2(n) + 300
        if t1 > t2:
            return n
    return None

print(find_threshold())
import math

def compare_thresholds():
    # T1 vs T2
    for n in range(1, 10000):
        t1 = 5 * n**2 + 10 * n
        t2 = 6 * n * math.log2(n) + 300
        if t1 > t2:
            print(f"T1(n) supera a T2(n) cuando n = {n}")
            break

    # T2 vs T3
    for n in range(1, 10000):
        t2 = 6 * n * math.log2(n) + 300
        t3 = 0.01 * n**3
        if t3 > t2:
            print(f"T3(n) supera a T2(n) cuando n = {n}")
            break

     # T3 vs T4
    for n in range(1, 100):
        t3 = 0.01 * n**3
        t4 = 1.5 ** n
        if t4 > t3:
            print(f"T4(n) supera a T3(n) cuando n = {n}")
            break

if __name__ == "__main__":
    
    compare_thresholds()


    ## punto 2
    









