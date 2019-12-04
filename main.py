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

resultat = processing('BFS_G', inputs)
print('cout de la solution: ', resultat.path_cost)
# présentation ds résultats

# print(resultat.solution())
# print(resultat.path())

#curses_console_display(resultat.path()) # animation console avec curses

pySimple_display(resultat.path())  # interface graphique avec PySimpleGUI
