class ITEMNOTINMENU(Exception):
  pass
class WrongPrice(Exception):
  pass

class Menu(dict):
  def __init__(self):
    self.d = {'vada' : 10, 'idly' : 20}
    
  def __getitem__(self, i):
    return dict.__getitem__(self.d, i)
  
  def __contains__(self, key):
    return key in self.d
      
  def __setitem__(self, key, item): 
    dict.__setitem__(self.d, key, item)
    
  def show(self):
    print 'menu :'
    for i in self.d.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
      
  def add(self, a, b):
    self.d[a] = b
    
class Order(dict):
  def __init__(self, m):
    self.d = m.d
    self.ordL = {}
    
  def __getitem__(self, i):
    return dict.__getitem__(self.ordL, i)
      
  def __setitem__(self, key, item): 
    if key in self.d:
      if self.d[key] == item:
        self.ordL[key] = item
      else:
        raise WrongPrice
    else:
      raise ITEMNOTINMENU
    pass
      
  def show(self):
    print 'order :'
    for i in self.ordL.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
    
  
c = Menu()
c['idly'] = 30
print c['idly']
try:
  print c['unknown']
except KeyError:
  print 'not in menu'
  
c.show()
o1 = Order(c)
o2 = Order(c)
try:
  o1['vada'] = 10
  o2['idly'] = 30
except ITEMNOTINMENU:
  print 'not in menu'
except WrongPrice:
  print 'wrong price'
  
o1.show()
o2.show()