from random import choice as c

s = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"

p = c(s) + c(s) + c(s) + c(s) + c(s) + c(s) + c(s) + c(s) + c(s) + c(s)
print(p)

