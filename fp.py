# fungsi yang menghitung nilai kuadrat
def square(x):
    return x * x

# fungsi yang menghitung nilai faktorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# pemanggilan fungsi
hasil = square(5)
print(hasil) 

hasil = factorial(5)
print(hasil) 
