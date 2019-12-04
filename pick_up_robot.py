#!/usr/bin/python3
"""
this pick_up_robot classs
"""
from search import *
import animation
import time
import sys


class PickUpRobot(Problem):
    def __init__(self, dataset, dimention = [9, 9]):
        """ Dimention est un tableau a 2 dimention en perspective 
        nous voudrions aller vers un tableau à 3 dimention mais 
        hors du contest de ce tp ;)
        """
        if (isinstance(dimention, int)):
            dimention = [dimention, dimention]
        if (not isinstance(dimention, list)):
            print('ERROR please give a dimention in a list or int')


        self.dimention = dimention
        self.max_index_row = dimention[0] - 1
        self.max_index_col = dimention[1] - 1
        self.nbrElement = 0
        self.maxEndTime = time.time() + 600000

        self.display_state(self.get_initial(dataset)) # uncom
        print('\n')
        
        # animation
        self.anWait = animation.Wait('bar', text='THINKING...  ')
        self.anWait.start()
        Problem.__init__(self, self.get_initial(dataset), self.get_goal())

    def actions(self, state):
        """  """
        action_possible = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        robot_position = self.find_robot(state)
        
        if robot_position[1] == 0:
            action_possible.remove('LEFT')
        if robot_position[0] == 0:
            action_possible.remove('UP')
        if robot_position[1] == self.max_index_col:
            action_possible.remove('RIGHT')
        if robot_position[0] == self.max_index_row:
            action_possible.remove('DOWN')

        return action_possible

    def result(self, state, action):
        """is the index of the blank square"""
        # print(action)
        robot_position = self.find_robot(state)
        new_state = list(state)

        neighbor = robot_position

        delta = {
            'UP': [robot_position[0] - 1,robot_position[1]],
            'DOWN': [robot_position[0] + 1,robot_position[1]],
            'LEFT': [robot_position[0],robot_position[1] - 1],
            'RIGHT': [robot_position[0],robot_position[1] + 1]
        }
        neighbor = delta[action]
        # new_state[robot_position[0]][robot_position[1]] = '_'
        new_state[robot_position[0]] = list(new_state[robot_position[0]])
        new_state[robot_position[0]][robot_position[1]] = '_'
        new_state[robot_position[0]] = tuple(new_state[robot_position[0]])

        # new_state[neighbor[0]][neighbor[1]] = '@'   
        new_state[neighbor[0]] = list(new_state[neighbor[0]])
        new_state[neighbor[0]][neighbor[1]] = '@'
        new_state[neighbor[0]] = tuple(new_state[neighbor[0]])

        return tuple(new_state)

    def goal_test(self, state):
        if (self.maxEndTime < time.time()):
            self.anWait.stop()
            print("pas de solution avant la fin du temps (10min)")
            sys.exit()

        abot = self.find_robot(state)
        fresh_state = list(state)
        
        # fresh_state[abot[0]][abot[1]] = '_'
        fresh_state[abot[0]] = list(fresh_state[abot[0]])
        fresh_state[abot[0]][abot[1]] = '_'
        fresh_state[abot[0]] = tuple(fresh_state[abot[0]])
        
        fresh_state = tuple(fresh_state)
        self.nbrElement += 1
        # print()

        if (fresh_state == self.goal):
            pass
            self.anWait.stop()
            print('*************************************') #uncom
            self.display_state(state) # uncom
            print("trouvé en ", time.time() - (self.maxEndTime - 600000), ' secondes')
            print(self.nbrElement, ' elements visités')

        return fresh_state == self.goal

    def path_cost(self, c, state1, action, state2):
        # print()
        return c + 1 + abs(self.get_state_static_cost(state1) - self.get_state_static_cost(state2))

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        # return sum(s != g for (s, g) in zip(node.state, self.goal))

        return self.get_rest_element(node.state)


    def find_robot(self, state):
        """Return the index of the robot Abot in a given state"""
        i = -1
        j = -1
        finded = 0
        for ind, row in enumerate(state):
            for jnd, col in enumerate(row):
                if (col == '@'):
                    i = ind
                    j = jnd
                    find = 1
                    break
            if (finded == 1):
                break
        return [i, j]

    def get_goal(self):
        m = self.dimention[1]
        n = self.dimention[0]
        a = ['_'] * n
        for i in range(n):
            a[i] = ['_'] * m
            a[i] = tuple(a[i])
        a = tuple(a)

        return a

        # return tuple((("_") * self.dimention[1] for i in range(self.dimention[0])))

    def get_dataset_element_index(self, elem):
        if(elem < (self.dimention[1] * self.dimention[0])):
            return [int(elem)//self.dimention[1], int(elem)%self.dimention[1]]
        else:
            return [self.max_index_row, self.max_index_col]

    def get_initial(self, dataset):
        initial = list(self.get_goal())
        for key, value in dataset.items():
            coord = self.get_dataset_element_index(key)

            # initial[coord[0]][coord[1]] = value
            initial[coord[0]] = list(initial[coord[0]])
            initial[coord[0]][coord[1]] = value
            initial[coord[0]] = tuple(initial[coord[0]])

        initial[self.max_index_row] = list(initial[self.max_index_row])
        initial[self.max_index_row][0] = '@'
        initial[self.max_index_row] = tuple(initial[self.max_index_row])

        # initial[0] = list(initial[0])
        # initial[0][0] = '@'
        # initial[0] = tuple(initial[0])

        return tuple(initial)


    def display_state(self, state):
        for row in state:
            print(' '.join([str(elem) for elem in row]))
            sys.stdout.write('\r')
            # sys.stdout.write('\r '.join([str(elem) for elem in row]))
        return


    def get_state_static_cost(self, state):
        cost = 0
        for i in range(self.dimention[0]):
            for j in range(self.dimention[1]):
                # if (state[i][j] == 'V' or state[i][j] == 'J'):
                #     elem += 1
                if (state[i][j] == 'J'):
                    cost += 4
                elif (state[i][j] == 'V'):
                    cost += 2
        return cost

    def get_rest_element(self, state):
        elem = 0
        manhattanDistances = []
        abot = self.find_robot(state)
        for i in range(self.dimention[0]):
            for j in range(self.dimention[1]):
                if (state[i][j] == 'V' or state[i][j] == 'J'):
                    elem += 1
                    dist = abs(i-abot[0]) + abs(j-abot[1])
                    manhattanDistances.append(dist)
        if (len(manhattanDistances)):
            return elem + min(manhattanDistances)
        return elem



    def check_solvability(self, state):
        """ Checks if the given state is solvable(have at least one elemnt J or V) """
        inversion = 0
        for i in range(dimention[0]):
            if (state[i].index('V') or state[i].index('J')):
                return 1
        return 0
    

defaultInput = {
    74: 'V',
}


def processing(algo='Astar_G', inputs=defaultInput):
    instance = PickUpRobot(inputs)
    if (algo == 'DFS_G'):
        return depth_first_graph_search(instance)
    if (algo == 'DFS_T'):
        return depth_first_tree_search(instance)
    if (algo == 'BFS_G'):
        return breadth_first_graph_search(instance)
    if (algo == 'BFS_T'):
        return breadth_first_tree_search(instance)
    if (algo == 'UCS_G'):
        return uniform_cost_search(instance)
    if (algo == 'UCS_T'):
        pass
    if (algo == 'IDS_G'):
        iterative_deepening_search(instance)
    if (algo == 'IDS_T'):
        pass
    if (algo == 'GS_G'):
        return greedy_best_first_graph_search(instance, instance.h)
    if (algo == 'GS_T'):
        pass
    if (algo == 'Astar_G'):
        return astar_search(instance, instance.h)
    if (algo == 'Astar_T'):
        pass
    
    




def display_node(node):
        for row in node:
            print(' '.join([str(elem) for elem in row]))
        return


# resultat = processing()
# print(resultat.solution)
