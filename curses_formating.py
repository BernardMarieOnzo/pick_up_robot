#/usr/bin/python3
from curses import wrapper
import time,sys


def main(stdscr, path):
    # Clear screen
    stdscr.clear()

    for node in path:
      stdscr.refresh()
      time.sleep(0.5)
      for i in range(len(node.state)):
        # stdscr.addstr(i, 0, ' '.join([str(elem) for elem in node.state[i]]))
        try:
            stdscr.addstr(i, 0, ' '.join([str(elem)for elem in node.state[i]]))
        except:
            stdscr.getkey()
            print("Veuillez agrandir votre console")
            time.sleep(0.9)
            # sys.exit()
            break
        else:
            # print ("Written content in the file successfully")
            pass




    stdscr.refresh()
    stdscr.addstr(len(node.state) + 4, 0, 'Appuyez une touche pour quitter')
    stdscr.getkey()

def curses_console_display(path) :
    wrapper(main, path)
