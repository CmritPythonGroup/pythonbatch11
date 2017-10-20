class Menu:
  def __init__(self):
    self.d = {'vada' : 10, 'idly' : 20}
    
  def __contains__(self, key):
    return key in self.d
    
  def __getitem__(self, i):
    try:
      return self.d[i]
    except Exception as error:
      print 'not in menu. error - ' + repr(error)
        
  def __setitem__(self, key, item): 
    self.d[key] = item
    
  def show(self):
    print 'menu :'
    for i in self.d.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
      
  def add(self, a, b):
    self.d[a] = b
    
class Order:
  d = Menu()
  def __init__(self, m):
    self.d = m
    self.ord = {}
      
  def __getitem__(self, i):
    try:
      return self.ord[i]
    except Exception as error:
      print 'not in menu. error - ' + repr(error)
      
  def __setitem__(self, key, item): 
    try:
      #if self.d[key] == item:
      if key in self.d:
        self.ord[key] = item
      else:
        print 'wrong price'
    except Exception as error:
      print 'not in menu. error - ' + repr(error)
      
  def show(self):
    print 'order :'
    for i in self.ord.items():
      print '\t' + str(i[0]) + ' costs ' + str(i[1])
    
  
c = Menu()
c['idly'] = 20
print c['i']
c.show()
o1 = Order(c)
o2 = Order(c)
o1['vada'] = 10
o2['idly'] = 20
print o1['vada']
o1.show()
o2.show()
