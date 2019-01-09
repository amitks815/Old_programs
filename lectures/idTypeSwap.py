a=10
b=20
print a,b
print id(a),id(b)
b,a=a,b
print a,b
print id(a),id(b)
a=b=20
print a,b
print id(a),id(b)

a = 10
b = "Ten"
print type(a), a
print type(b), b
