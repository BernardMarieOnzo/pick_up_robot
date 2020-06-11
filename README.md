# Execution file: 
    main.py

# Change of instance:
To change the instance of the problem, it is necessary, in the main.py file, at the line def getInput(id = 0), to replace the value of id by the number of the instance to execute.
id = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19 } }.

Running the main.py file:
At the line result = processing('DFS_G', inputs), replace the value between dimensions by the search algorithm you want to execute
BFS_T for Breadth-First Tree Search
BFS_G for Breadth First Graph Search
DFS_T for Depth First Tree Search
DFS_G for Depth First Graph Search
UCS_G for Uniform-Cost Search
IDS_G for Iterative Deepening Search
GS_G for Greedy Best-First Search
Astar_G for Astar Search

# Presentation of results
  You have 4 ways of presenting the results
  * solution in terms of robot motion (decomment line 20 main.py file) [print(resultat.solution()]
  * solution in terms of path of the different states from the beginning to the solution (decomment line 21 main.py file) [print(resultat.path()]
  * console graphics solution (decomment line 23 file main.py) [curses_console_display(resultat.path())]
    -- please enlarge your cosole for the runtime to see the end animation:
  * GUI solution (uncomment line 23 main.py file) [pySimple_display(resultat.path()]
    -- for this one the code is not yet well optimized so please be patient while it is running it works fine once started

NB: 
  -it is possible to change the array dimensions in the 'pick_up_robot.py' file (line 12).
    And the instances will be adapted and the out of range will be ignored.

________________________
#environment requirement
___________________________

"python3

"pip install animation

"pip install curses

"pip install --upgrade PySimpleGUI
