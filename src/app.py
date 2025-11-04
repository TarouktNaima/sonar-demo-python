def add(a,b):
    return a+b
def is_palindrome(s):
    s=s.lower().replace(" ","")
    return s== s[::-1]