numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    out_num = numbers.pop(0)
    if out_num == 1:
       numbers.append(out_num)
    elif (out_num % 2 != 0 or out_num == 2) and out_num != 0 and (out_num % 3 != 0 or out_num == 3):
        primes.append(out_num)
    else:
        not_primes.append(out_num)

print(primes)
print(not_primes)
