class Menu:
  def __init__(self):
    self.d = {'vada' : 10}
    
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
  d = {}
  def __getitem__(self, i):
    return self.d[i]
      
  def __setitem__(self, key, item): 
    Mobj = Menu()
    if Mobj[key] is not None:
      if Mobj[key] == item:
        self.d[key] = item
      else:
        print 'wrong price'
      
  def show(self):
    print 'order'
    for i in self.d.items():
      print str(i[0]) + ' costs ' + str(i[1])
    
  
c = Menu()
c['idly'] = 20
c.show()
o = Order()
o['vaa'] = 10
o.show()
