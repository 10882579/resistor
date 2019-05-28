"""

  Author: Bahodirov Botir

  Description: 
  This program is meant to calculate the resistivity 
  of a resistor with the color codes



"""

import sys
from resistor import Resistor

def main():

  data = ""

  if sys.version_info[0] < 3:
    data = raw_input("Enter color codes: ").upper()
  else:
    data = input("Enter color codes: ").upper()

  resistor = Resistor(data.split(" "))
  resistor.output()


if __name__ == "__main__":

    try:
      while(True):
        main()
    except KeyboardInterrupt:
      print("")