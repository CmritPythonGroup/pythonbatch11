import cmath

def root(a, b, c):
	  return (-b + cmath.sqrt(b * b - 4 * a * c)) / (2 * a), (-b - cmath.sqrt(b * b - 4 * a * c)) / (2 * a)

print root(2, 3, 5)
