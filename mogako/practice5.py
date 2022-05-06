def answer(n):
    arr = []
    for i in range(n/2):
        if n % i == 0:







# 에라토스테네스의 체
# import time
#
# def print_prime_by_range(n):
#     prime_range = n+1
#     prime_list = [True]*prime_range
#
#     sqrt = int(n**0.5)
#     for i in range(2, sqrt+1):
#         if prime_list[i]:
#             for j in range(i+i, prime_range, i):
#                 prime_list[j] = False
#     return prime_list.count(True)-2
#
# start = time.time()
# prime_count = print_prime_by_range(50000)
# print(f"소수의 개수 : {prime_count}")
#
# end = time.time()
# print(f'실행시간(초) : {end-start}')



# import time
# import math
#
# def is_prime(n):
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
#
# def print_prime(n):
#     cnt=0
#     for i in range(2, n+1):
#         if is_prime(i):
#             cnt += 1
#     print(f'소수의 개수 : {cnt}')
#
# start = time.time()
# print_prime(5555)
# end = time.time()
# print(f'실행시간(초) : {end - start}')

# import time
# # 소수
# def is_prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#         return True
#
# def print_prime(n):
#     cnt = 0
#     for i in range(2, n+1):
#         if is_prime(i):
#             cnt += 1
#     print(f"소수의 개수 : {cnt}")
#
#
# n = int(input('1000000 이하의 자연수를 입력해주세요 : '))
# start = time.time()
# print_prime(n)
# end = time.time()
# print(f'실행시간(초) : {end-start}')
