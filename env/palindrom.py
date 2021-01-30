s = 'potop'

s == s[::-1]
print(s == s[::-1])

def is_palindrome(test_string):
    test_string = test_string.lower().replace('.','').replace(' ','')
    return test_string == test_string[::-1]
    
    

is_palindrome(s)