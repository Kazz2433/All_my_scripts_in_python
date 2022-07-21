from numpy import number


def my_sum(numbers, extra=0):
    soma = 0
    for i in numbers:
        soma += i
    media = len(numbers)
    media = soma / media
    if (extra):
        print(f"Media is {media} soma is {soma}")
    else:
        print(f"soma is {soma}")

print(my_sum([1,2,3]))