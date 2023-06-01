result = (lambda x,y: x(y))(lambda i: i**2, 10)
print(result)