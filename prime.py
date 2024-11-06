def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_prime(n):
    count = 0
    candidate = 2
    while True:
        if prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1

n = int(input("찾고 싶은 소수의 순서를 입력하세요."))
print(f"{n_prime(n)}입니다.")
