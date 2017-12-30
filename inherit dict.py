
class ITEMNOTINMENU(Exception):
  pass
class WrongPrice(Exception):
  pass

class Menu(dict):
  def __getitem__(self, i):
    if self.get(i) is None:
      raise ITEMNOTINMENU
    else:
      return self.get(i)
    
class Order(dict):
  def __init__(self, m):
    self.d = m
    dict.__init__(self)
      
  def __setitem__(self, key, item): 
    if key in self.d:
      if self.d[key] == item:
        self.update({key : item})
      else:
        raise WrongPrice
    else:
      raise ITEMNOTINMENU
      
  def show(self):
    print 'order :'
    for i in self.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
    
  
c = Menu()
c['vada'] = 10
c['idly'] = 30
print c['vada']
try:
  print c['unknown']
except ITEMNOTINMENU:
  print 'not in menu'
  
o1 = Order(c)
o2 = Order(c)
try:
  o1['vada'] = 10
except ITEMNOTINMENU:
  print 'not in menu'
except WrongPrice:
  print 'wrong price'

try:
  o2['idly'] = 30
except ITEMNOTINMENU:
  print 'not in menu'
except WrongPrice:
  print 'wrong price'
 
o1.show()
o2.show()
