class Menu:
  def __init__(self):
    self.d = {'vada' : 10}
  def show(self):
    for i in self.d.items():
      print str(i[0]) + ' costs ' + str(i[1])
  def add(self, a, b):
    self.d[a] = b
  
c = Menu()
c.add('idly', 20)
c.show()