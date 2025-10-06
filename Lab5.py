# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result =""
    
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                result += "*"
            else:
                result += " "
        result = result.rstrip()
        result += "\n"
    
    return result.rstrip()

print(hollow_square(5))




# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n+1):
            for j in range(1, i +1):
                result += str(j)
            result += "\n"
    return result.rstrip()
        
print(number_pattern(4))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
     result = n*(n+1)/2   
     return result

print(sum_of_natural_numbers(5))


# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    if n <=0:
        return""
    result=""
    for i in range(n):
        for j in range(n-i-1):
            result+=" "
        for k in range(2*i+1):
            result+="*"
        result+="\n"
    return result.rstrip()
        
print(centered_star_pyramid(4)) 


    