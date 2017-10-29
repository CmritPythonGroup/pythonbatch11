class ITEMNOTINMENU(Exception):
  pass
class WrongPrice(Exception):
  pass

class Help(object):
  def getitem(self, i, a):
    if i in a:
      return a[i]
    else:
      raise ITEMNOTINMENU
      
  def show(self, a):
    for i in a.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])

class Menu(Help):
  def __init__(self):
    self.d = {'vada' : 10, 'idly' : 20}
    
  def __getitem__(self, i):
    return super(Menu, self).getitem(i, self.d)
  
  def __contains__(self, key):
    return key in self.d
      
  def __setitem__(self, key, item): 
    self.d[key] = item
    
  def show(self):
    print 'menu :'
    super(Menu, self).show(self.d)
      
  def add(self, a, b):
    self.d[a] = b
    
class Order(Help):
  def __init__(self, m):
    self.d = m
    self.ordL = {}
      
  def __getitem__(self, i):
    return super(Order, self).getitem(i, self.ordL)
      
  def __setitem__(self, key, item): 
    if key in self.d:
      if self.d[key] == item:
        self.ordL[key] = item
      else:
        raise WrongPrice
    else:
      raise ITEMNOTINMENU
      
  def show(self):
    print 'order :'
    super(Order, self).show(self.ordL)
    
  
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