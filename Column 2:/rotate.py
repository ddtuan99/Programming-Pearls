# Problem B is to rotate the n-element vector x left by i positions in time proportional to n and with just a few dozen bytes of extra space.
# "abcdefgh", i = 3
# -> "defghabc"

def reverse(str):
    return str[::-1] #slicing 

def rotate(str, i):
    tmp = reverse(str[:i]) + reverse(str[i:])
    return reverse(tmp)

str = input("string: ")
i = int(input("position: "))
print(rotate(str, i))