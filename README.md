

# Fichier d'execution: 
    main.py

# Changement d'instance:
Pour changer l'instance du problème, il faut, dans le fichier main.py, à la ligne def getInput(id = 0), remplacer la valeur de id par le numéro de l'instance à executer.
id = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12, 13, 14, 15, 16, 17, 18, 19 }

Exécution du fichier principal main.py:
A la ligne resultat = processing('DFS_G', inputs), remplacer la valeur entre cotes par l'algorithme de recherche que vous souhaitez exécuter
BFS_T pour Breadth-First Tree Search
BFS_G pour Breadth First Graph Search
DFS_T pour Depth First Tree Search
DFS_G pour Depth First Graph Search
UCS_G pour Uniform-Cost Search
IDS_G pour Iterative Deepening Search
GS_G pour Greedy Best-First Search
Astar_G pour Astar Search

# Présentation ds résultats
  Vous disposez de 4 formes de pésentation des résultats
  * solution en terme de mouvement du robot (decommenter ligne 20 fichier main.py) [print(resultat.solution())]
  * solution en terme de chemin des différents états du début à la solution  (decommenter ligne 21 fichier main.py) [print(resultat.path())]
  * solution en graphique console (decommenter ligne 23 fichier main.py) [curses_console_display(resultat.path())]
    -- veulliez bien agrandir votre cosole pour l'execution afin de voir l'animation de fin:
  * solution en interface graphique (decommenter ligne 23 fichier main.py) [pySimple_display(resultat.path())]
    -- pour celui ci le code n'est pas encore bien optimisé donc veuillez patienter pendant son exécution il marche bien une fois demarré

NB: 
  -il est possible de changer les dimentions de tableau dans le fichier 'pick_up_robot' (ligne 12)
    Et les instances seront adaptées et les "out of range" seront ignoré

________________________
#environment requirement
___________________________

» python3
» pip install animation
» pip install curses
» pip install --upgrade PySimpleGUI
