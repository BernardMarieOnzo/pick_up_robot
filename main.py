#/usr/bin/python3
from pick_up_robot import processing
from curses_formating import curses_console_display
from PySimple import pySimple_display

def getInput(id=0):
  file = open("inputs/input"+str(id)+".txt", "r+")
  data = eval(file.read())
  file.close()
  return data

inputs = getInput()

result = processing('GS_G', inputs)

# results
print('Solution cost: ', result.path_cost)

print(result.solution())
#print(result.path())

#curses_console_display(result.path()) # console animation with curses

pySimple_display(result.path())  # graphic interface with avec PySimpleGUI
