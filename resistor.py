class Resistor:

  def __init__(self, res):

    self.colors = ["B", "BR", "R", "O", "Y", "G", "BL", "P", "S", "W"]
    self.resistor = res


  def four_band(self):

    for i, color in enumerate(self.colors):
      if self.resistor[0] == color:
        self.first = i

      if self.resistor[1] == color:
        self.second = i

      if self.resistor[2] == color:
        self.third = ((i+1)/(i+1)) * (10**i)

    return int("{}{}".format(self.first, self.second)) * self.third

  def five_band(self):

    for i, color in enumerate(self.colors):
      if self.resistor[0] == color:
        self.first = i

      if self.resistor[1] == color:
        self.second = i
      
      if self.resistor[2] == color:
        self.third = i

      if self.resistor[3] == color:
        self.fourth = ((i+1)/(i+1)) * (10**i)
    
    return int("{}{}{}".format(self.first, self.second, self.third)) * self.fourth
      

  def tolerance(self):

    color = self.resistor[len(self.resistor)-1]
    tolerance = 1

    if color == 'BR':
      tolerance = 1
    elif color == 'R':
      tolerance = 2
    elif color == 'GD':
      tolerance = 5
    elif color == 'S':
      tolerance = 10

    return tolerance

  def output(self):

    if len(self.resistor) == 4:
      print(
        "Resistivity: %d %c%d%% ohms" % (self.four_band(), u"\u00B1", self.tolerance()) 
      )
    elif len(self.resistor) == 5:
      print(
        "Resistivity: %d %c%d%% ohms" % (self.five_band(), u"\u00B1", self.tolerance()) 
      )
    else:
      print("Enter a valid resistor color code")
