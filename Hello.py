class Hello:

  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello and welcome, {name}".format(name=self.name))
