def print_numbers1(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)*i
    return result
        
print(print_numbers1(5))
