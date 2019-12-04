#/usr/bin/python3
import PySimpleGUI as sg
import time


# Create a standard window
form = sg.FlexForm('Pick up Robot')

# define basics params
background = '#F0F0F0'
robo_image = './images/robot.png'
blank_image = './images/blank.png'
green_image = './images/green.png'
yellow_image = './images/yellow.png'


# form.Layout(layout)
def getLayout(state):
  tab = []
  tab.append([sg.T(' ' * 65), sg.Button('START', button_color=('#FFFFFF', '#60BC88'),
                                        image_subsample=8, border_width=0, key=('start'))])
  tab.append([sg.T(' ' * 65)])
  for i in range(len(state)):
    subTab = []
    # for j in state[i]:
    for jnd, j in enumerate(state[i]):
      if (j == 'V'):
          newElem = sg.Button('', button_color=(background, background),image_filename=green_image, image_size=(60, 60), image_subsample=15, border_width=0, key=('case_' + str(i) + '_' +str(jnd)))
      elif (j == 'J'):
          newElem = sg.Button('', button_color=(background, background), image_filename=yellow_image, image_size=(60, 60), image_subsample=10, border_width=0, key=('case_' + str(i) + '_' +str(jnd)))
      elif (j == '@'):
          newElem = sg.Button('', button_color=(background, background),image_filename=robo_image, image_size=(60, 60), image_subsample=8, border_width=0, key=('case_' + str(i) + '_' +str(jnd)))
      else:
          newElem = sg.Button('', button_color=(background, background),image_filename=blank_image, image_size=(60, 60), image_subsample=8, border_width=0, key=('case_' + str(i) + '_' +str(jnd)))

      subTab.append(newElem)
    tab.append(subTab)
  return tab


def makeMove(path):
  for k, kk in enumerate(path):

    for i, ii in enumerate(kk.state):
      for j, jj in enumerate(ii):
        # print(jj)
        # form.Refresh()
        if (jj == 'V'):
            form.FindElement('case_' + str(i) + '_' + str(j)).Update('', button_color=(background, background),
                                                                     image_filename=green_image, image_size=(60, 60), image_subsample=15)
        elif (jj == 'J'):
            form.FindElement('case_' + str(i) + '_' + str(j)).Update('', button_color=(background, background),
                                                                     image_filename=yellow_image, image_size=(60, 60), image_subsample=10)
        elif (jj == '@'):
            form.FindElement('case_' + str(i) + '_' + str(j)).Update('', button_color=(background, background),
                                                                     image_filename=robo_image, image_size=(60, 60), image_subsample=8)
        elif (jj == '_'):
            form.FindElement('case_' + str(i) + '_' + str(j)).Update('', button_color=(background, background),
                                                                     image_filename=blank_image, image_size=(60, 60), image_subsample=8)
    form.Refresh()
    # time.sleep(0.1)
  form.FindElement('start').Update(
      'RESTART', button_color=('#FFFFFF', '#60BC88'), image_subsample=8)

  



def pySimple_display (path):
  layout_ = getLayout(path[0].state)
  form.Layout(layout_)

  while True:
      button, values = form.Read()
      # print(button)
      if button == 'start':
        print('action')
        makeMove(path)
        # form.Refresh()
      elif button == 'Quit' or button is None:
          break
