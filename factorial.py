def factorial(n):
    if n <= 1:
        return 1
    
    count = 1

    for i in range(n, 1, -1):
        count *= i
   
    return count

def prettify_number(n):
    if n < 1000:
        return str(n)
    else:
        return prettify_number(n // 1000) + ',' + str(n % 1000).zfill(3)

while True:
    n = int(input("Enter a number and I'll tell you it's factorial\n"))
    # n_factorial = factorial(n)
    # n_pretty = prettify_number(n_factorial)
    # print(n_pretty)
    print(prettify_number(n))

