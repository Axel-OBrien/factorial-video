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

GRASS_LENGTH = 1 + (8 / 9) # inches

while True:
    n = int(input("Enter a number and I'll tell you how many feet tall that many blades of grass factorial would be\n"))
    n_factorial = round((factorial(n) * GRASS_LENGTH) / 12)
    n_pretty = prettify_number(n_factorial)
    print(n_pretty)
