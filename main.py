#1 - misol
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


# 2 - misol
numbers = [-5, -2, 0, 3, 5, 7]
positive = list(filter(lambda x: x > 0, numbers))
doubled = list(map(lambda x: x * 2, positive))
print(doubled)

# 3 -  misol
strings = ["salom", "dunyo", "python"]
upper_case = list(map(lambda s: s.upper(), strings))
print(upper_case)


#4 -  misol
numbers = [3, 4, 6, 7, 9, 10, 12]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3)


# 5 -  misol
import math
ebob = lambda a, b: math.gcd(a, b)
print(ebob(36, 60))
