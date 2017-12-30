D = {}

def makeD(s):
  a = s.split(";")
  for i in a:
    key, val = i.split("=")
    D[key] = val

def makeDshort(s):
    return dict([i.split("=") for i in s.split(";")])
  
def dictocs(d):
  s = ''
  for i in d:
    s += str(i) + '=' + str(d[i])
  return s

makeD("a=bc;d=efg;h=ijkl;m=n")
print D
print dictocs({'a': 'bc', 'h': 'ijkl', 'm': 'n', 'd': 'efg'})