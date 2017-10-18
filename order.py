class Menu:
  def __init__(self):
    self.d = {'vada' : 10, 'idly' : 20}
    
  def __getitem__(self, i):
    try:
      return self.d[i]
    except:
      print('not in menu')
        
  def __setitem__(self, key, item): 
    self.d[key] = item
    
  def show(self):
    print 'menu'
    for i in self.d.items():
      print str(i[0]) + ' costs ' + str(i[1])
      
  def add(self, a, b):
    self.d[a] = b
    
class Order:
  def __init__(self, m):
    self.d = {}
    self.ord = {}
    for i in m.d:
      self.d[i] = m.d[i]
      
  def __getitem__(self, i):
    return self.d[i]
      
  def __setitem__(self, key, item): 
    try:
      if self.d[key] == item:
        self.ord[key] = item
      else:
        print 'wrong price'
    except:
      print 'not in menu'
      
  def show(self):
    print 'order'
    for i in self.ord.items():
      print str(i[0]) + ' costs ' + str(i[1])
    
  
c = Menu()
c['idly'] = 20
c.show()
o = Order(c)
o2 = Order(c)
o['vada'] = 10
o.show()
o2.show()
