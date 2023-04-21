def divisors(n):
    results = []
    i = 1
    while i < 500000 :
        i+=1
        if n % i == 0:
            results.append(str(i))
    return "\n".join(results)
    
test = divisors(6500)
print(test)