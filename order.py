class ITEMNOTINMENU(Exception):
  pass
class WrongPrice(Exception):
  pass

class Menu:
  def __init__(self):
    self.d = {'vada' : 10, 'idly' : 20}
    
  def __contains__(self, key):
    return key in self.d
    
  def __getitem__(self, i):
    if i in self.d:
      return self.d[i]
    else:
      raise ITEMNOTINMENU
      
  def __setitem__(self, key, item): 
    self.d[key] = item
    
  def show(self):
    print 'menu :'
    for i in self.d.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
      
  def add(self, a, b):
    self.d[a] = b
    
class Order():
  d = Menu()
  def __init__(self, m):
    self.d = m
    self.ord = {}
      
  def __getitem__(self, i):
    if i in self.ord:
      return self.ord[i]
    else:
      raise ITEMNOTINMENU
      
  def __setitem__(self, key, item): 
      if key in self.d:
        if self.d[key] == item:
          self.ord[key] = item
        else:
          raise WrongPrice
      else:
        raise ITEMNOTINMENU
      
  def show(self):
    print 'order :'
    for i in self.ord.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
    
  
c = Menu()
c['idly'] = 20
try:
  print c['unknown']
except ITEMNOTINMENU:
  print 'not in menu'
  
c.show()
o1 = Order(c)
o2 = Order(c)
try:
  o1['vada'] = 10
  o2['idly'] = 20
except ITEMNOTINMENU:
  print 'not in menu'
except WrongPrice:
  print 'wrong price'
  
o1.show()
o2.show()
