def root(a, b, c):
  sq = b * b - 4 * a * c
  if sq < 0:
    r1 = str(pow(abs(b * b - 4 * a * c), 0.5)) + 'i'
    r2 = -b / 2 * a
    return str(r2) + ' + ' + r1, str(r2) + ' - ' + r1
  else:
	  return (-b + pow(b * b - 4 * a * c, 0.5)) / (2 * a), (-b - pow(b * b - 4 * a * c, 0.5)) / (2 * a)

print root(2, 3, 5)