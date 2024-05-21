
'''

    Sokoban assignment


The functions and classes defined in this module will be called by a marker script. 
You should complete the functions and classes according to their specified interfaces.

No partial marks will be awarded for functions that do not meet the specifications
of the interfaces.

You are NOT allowed to change the defined interfaces.
In other words, you must fully adhere to the specifications of the 
functions, their arguments and returned values.
Changing the interfacce of a function will likely result in a fail 
for the test of your code. This is not negotiable! 

You have to make sure that your code works with the files provided 
(search.py and sokoban.py) as your code will be tested 
with the original copies of these files. 

Last modified by 2022-03-27  by f.maire@qut.edu.au
- clarifiy some comments, rename some functions
  (and hopefully didn't introduce any bug!)

'''

# You have to make sure that your code works with
# the files provided (search.py and sokoban.py) as your code will be tested
# with these files
import search
import sokoban
import os
import sys
import time


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)

    '''
    return [(2020338038, 'Rj', 'Avro')]
    # raise NotImplementedError()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def taboo_cells(warehouse):
    '''  
    Identify the taboo cells of a warehouse. A "taboo cell" is by definition
    a cell inside a warehouse such that whenever a box get pushed on such 
    a cell then the puzzle becomes unsolvable. 

    Cells outside the warehouse are not taboo. It is a fail to tag an 
    outside cell as taboo.

    When determining the taboo cells, you must ignore all the existing boxes, 
    only consider the walls and the target  cells.  
    Use only the following rules to determine the taboo cells;
     Rule 1: if a cell is a corner and not a target, then it is a taboo cell.
     Rule 2: all the cells between two corners along a wall are taboo if none of 
             these cells is a target.

    @param warehouse: 
        a Warehouse object with the worker inside the warehouse

    @return
       A string representing the warehouse with only the wall cells marked with 
       a '#' and the taboo cells marked with a 'X'.  
       The returned string should NOT have marks for the worker, the targets,
       and the boxes.  
    '''
    # "INSERT YOUR CODE HERE"
    # raise NotImplementedError()

    X, Y = zip(*warehouse.walls)
    x_size, y_size = 1+max(X), 1+max(Y)

    vis = [[" "] * x_size for y in range(y_size)]

    for (x, y) in warehouse.walls:
        vis[y][x] = "#"

    inner_cells = [(x, y) for y in range(1, warehouse.nrows - 1)
                   for x in range((''.join(vis[y]).index('#')), (''.join(vis[y]).rindex('#')))
                   if (vis[y][x] == " ")]
    inner_cells.sort()
    # print(inner_cells)

    corner_cells = [(x, y) for (x, y) in inner_cells
                    if ((vis[y-1][x] == '#' and vis[y][x-1] == '#')
                        or (vis[y-1][x] == '#' and vis[y][x+1] == '#')
                        or (vis[y+1][x] == '#' and vis[y][x-1] == '#')
                        or (vis[y+1][x] == '#' and vis[y][x+1] == '#'))]
    # print(corner_cells)

    # Rule:1
    taboo_cells = [(x, y) for (x, y) in corner_cells if (x, y)
                   not in warehouse.targets]

    # Rule:2
    # print(list(zip(*corner_cells)))

    for (x, y) in taboo_cells:
        vis[y][x] = 'X'

    return "\n".join(["".join(line) for line in vis])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class SokobanPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.

    Your implementation should be fully compatible with the search functions of 
    the provided module 'search.py'. 

    '''

    #
    #         "INSERT YOUR CODE HERE"
    #
    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to
    #     complete this class. For example, a 'result' method is needed
    #     to satisfy the interface of 'search.Problem'.
    #
    #     You are allowed (and encouraged) to use auxiliary functions and classes

    def __init__(self, warehouse):
        # raise NotImplementedError()
        # Static part
        self.walls = warehouse.walls
        self.targets = warehouse.targets
        self.weights = warehouse.weights

        # state part
        self.initial = tuple((warehouse.worker, tuple(warehouse.boxes)))
        self.goal = tuple((warehouse.worker, tuple(warehouse.targets)))

    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.

        """
        # raise NotImplementedError
        L = []
        x, y = state[0]

        if ((x-1, y) not in self.walls and (x-1, y) not in state[1]):
            L.append('Left')
        elif ((x-1, y) in state[1]):
            # print('box hit')
            if ((x-2, y) not in self.walls and (x-2, y) not in state[1]):
                L.append('Left')

        if ((x+1, y) not in self.walls and (x+1, y) not in state[1]):
            L.append('Right')
        elif ((x+1, y) in state[1]):
            if ((x+2, y) not in self.walls and (x+2, y) not in state[1]):
                L.append('Right')

        if ((x, y-1) not in self.walls and (x, y-1) not in state[1]):
            L.append('Up')
        elif ((x, y-1) in state[1]):
            if ((x, y-2) not in self.walls and (x, y-2) not in state[1]):
                L.append('Up')

        if ((x, y+1) not in self.walls and (x, y+1) not in state[1]):
            L.append('Down')
        elif ((x, y+1) in state[1]):
            # print('box hit')
            if ((x, y+2) not in self.walls and (x, y+2) not in state[1]):
                L.append('Down')

        return L

    def result(self, state, action):

        worker = list(state[0])
        boxes = list(state[1])

        # print('\n',state[1], '\n',self.goal[1], end='')
        # if(set(state[1]) == set(self.goal[1])):
        #     print(' => Goal Found !\n')
        # else:
        #     print('\n')

        assert action in self.actions(state)

        x, y = find_move(action)
        worker[0] += x
        worker[1] += y

        for idx, box in enumerate(boxes):
            if box == (worker[0], worker[1]):
                box_x = box[0] + x
                box_y = box[1] + y
                boxes[idx] = (box_x, box_y)

        cur_state = tuple((tuple(worker), tuple(boxes)))

        return cur_state

    def goal_test(self, state):
        return set(state[1]) == set(self.goal[1])

    def path_cost(self, cost, state1, action, state2):
        assert self.result(state1, action) == state2

        worker = list(state1[0])
        boxes = list(state1[1])

        x, y = find_move(action)
        worker[0] += x
        worker[1] += y

        if((worker[0],worker[1]) in boxes):
            weight = self.weights[boxes.index((worker[0],worker[1]))]
            return cost + 1 + weight
        
        return cost + 1

    def h(self, node):
        state = node.state
        player_x, player_y = state[0]
        boxes, goals = state[1], self.targets
        boxes_cost = 0
        player_cost = 0
        for box_x, box_y in boxes:
            boxes_cost += (min(abs(box_x - goal_x) + abs(box_y - goal_y)
                              for goal_x, goal_y in goals)) * (
                                  self.weights[boxes.index((box_x,box_y))])
            
        player_cost = min(abs(box_x - player_x) + abs(box_y - player_y)
                          for box_x, box_y in boxes) if boxes else 0
        return boxes_cost + player_cost

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def check_elem_action_seq(warehouse, action_seq):
    '''

    Determine if the sequence of actions listed in 'action_seq' is legal or not.

    Important notes:
      - a legal sequence of actions does not necessarily solve the puzzle.
      - an action is legal even if it pushes a box onto a taboo cell.

    @param warehouse: a valid Warehouse object

    @param action_seq: a sequence of legal actions.
           For example, ['Left', 'Down', Down','Right', 'Up', 'Down']

    @return
        The string 'Impossible', if one of the action was not valid.
           For example, if the agent tries to push two boxes at the same time,
                        or push a box into a wall.
        Otherwise, if all actions were successful, return                 
               A string representing the state of the puzzle after applying
               the sequence of actions.  This must be the same string as the
               string returned by the method  Warehouse.__str__()
    '''

    # "INSERT YOUR CODE HERE"
    x, y = warehouse.worker

    # message for invalid action sequence
    failed = 'Impossible'

    # iterate through each move in the action_seq checking if valid
    for data in action_seq:
        if data == 'Left':
            # next location for left
            next_x = x - 1
            next_y = y
            # see if able to move the player in this direction
            if (next_x, next_y) in warehouse.walls:
                return failed  # impossible move, player was blocked
            elif (next_x, next_y) in warehouse.boxes:
                if (next_x - 1, next_y) not in warehouse.walls and (
                        next_x - 1, next_y) not in warehouse.boxes:  # double box condition
                    # can move the box
                    # move successful
                    warehouse.boxes.remove((next_x, next_y))
                    warehouse.boxes.append((next_x - 1, next_y))
                    x = next_x
                else:
                    return failed  # box was blocked
            else:
                x = next_x
        elif data == 'Right':
            next_x = x + 1
            next_y = y
            if (next_x, next_y) in warehouse.walls:
                return failed  # impossible move
            elif (next_x, next_y) in warehouse.boxes:
                if (next_x + 1, next_y) not in warehouse.walls and (
                        next_x + 1, next_y) not in warehouse.boxes:
                    # can move the box!
                    # move successful
                    warehouse.boxes.remove((next_x, next_y))
                    warehouse.boxes.append((next_x + 1, next_y))
                    x = next_x
                else:
                    return failed  # box was blocked
            else:
                x = next_x
        elif data == 'Up':
            next_y = y - 1
            next_x = x
            if (next_x, next_y) in warehouse.walls:
                return failed  # impossible move
            elif (next_x, next_y) in warehouse.boxes:
                if (next_x, next_y - 1) not in warehouse.walls and (
                        next_x, next_y - 1) not in warehouse.boxes:
                    # can move the box!
                    # move successful
                    warehouse.boxes.remove((next_x, next_y))
                    warehouse.boxes.append((next_x, next_y - 1))
                    y = next_y
                else:
                    return failed  # box was blocked
            else:
                y = next_y
        elif data == 'Down':
            next_y = y + 1
            next_x = x
            if (next_x, next_y) in warehouse.walls:
                return failed  # impossible move
            elif (next_x, next_y) in warehouse.boxes:
                if (next_x, next_y + 1) not in warehouse.walls and (
                        next_x, next_y + 1) not in warehouse.boxes:
                    # can move the box!
                    # move successful
                    warehouse.boxes.remove((next_x, next_y))
                    warehouse.boxes.append((next_x, next_y + 1))
                    y = next_y
                else:
                    return failed  # box was blocked
            else:
                y = next_y
        else:
            raise ValueError("No action sequence")

    # new state after applying the action sequence
    warehouse.worker = x, y

    X, Y = zip(*warehouse.walls)
    x_size, y_size = 1 + max(X), 1 + max(Y)

    vis = [[" "] * x_size for z in range(y_size)]
    for (x, y) in warehouse.walls:
        vis[y][x] = "#"
    for (x, y) in warehouse.targets:
        vis[y][x] = "."
    # Note y is worker[1], x is worker[0]
    if vis[warehouse.worker[1]][warehouse.worker[0]] == ".":
        vis[warehouse.worker[1]][warehouse.worker[0]] = "!"
    else:
        vis[warehouse.worker[1]][warehouse.worker[0]] = "@"
    # if a box is on a target display a "*"
    # exploit the fact that Targets has been already processed
    for (x, y) in warehouse.boxes:
        if vis[y][x] == ".":  # if on target
            vis[y][x] = "*"
        else:
            vis[y][x] = "$"
    warehouse = "\n".join(["".join(line) for line in vis])

    # print(str(warehouse))
    return str(warehouse)

    # raise NotImplementedError()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_weighted_sokoban(warehouse):
    '''
    This function analyses the given warehouse.
    It returns the two items. The first item is an action sequence solution.
    The second item is the total cost of this action sequence.

    @param
     warehouse: a valid Warehouse object

    @return

        If puzzle cannot be solved
            return 'Impossible', None

        If a solution was found,
            return S, C
            where S is a list of actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
            C is the total cost of the action sequence C

    '''

    puzzle = SokobanPuzzle(warehouse.copy())
    sol = search.astar_graph_search(puzzle)
    if sol is None:
        return 'Impossible', None
    
    pth = sol.path()
    ac = []
    for nod in pth:
        if nod.action is not None:
            ac.append(nod.action)

    return ac, sol.path_cost


def find_move(action):
    '''
    Helper function to find the position of x and y with particular action

    @param action: the type of action. For example :['Left','Right','Up','Down']

    @return
            x : x value  should be added one. For example, if the action is Right, 
            y : y value should be added one. For example, if the action is Down
    '''
    x = 0
    y = 0
    if (action == "Up"):
        y -= 1
    elif (action == "Down"):
        y += 1
    elif (action == "Left"):
        x -= 1
    elif (action == "Right"):
        x += 1

    return x, y


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    wh = sokoban.Warehouse()
    wh.load_warehouse("./warehouses/warehouse_8a.txt")

    # print(taboo_cells(wh))

    puzzle = SokobanPuzzle(wh.copy())
    print(wh.copy())
    sol = search.astar_graph_search(puzzle)
    # print(puzzle.actions(puzzle.initial))
    print(sol)
    # print(puzzle.initial)
    # state_1 = puzzle.result(puzzle.initial, 'Up')
    # print(state_1)
    # print(puzzle.actions(state_1))
    # state_2 = puzzle.result(state_1, 'Left')
    # print(state_2)
    # print(puzzle.actions(state_2))
    # state_3 = puzzle.result(state_2, 'Down')
    # print(state_3)
    # state_4 = puzzle.result(state_3, 'Down')
    # print(state_4)

    # print(puzzle.actions(state_1))

    pth = sol.path()
    ac = []
    for nod in pth:
        # print(nod.state)
        if nod.action is not None:
            ac.append(nod.action)

    # # ac.reverse()
    print(ac)
    print(sol.path_cost)
    # print(puzzle.initial)
    # for ac in puzzle.actions(puzzle.initial):
    #     print(ac, ' => ',puzzle.result(puzzle.initial, ac))

    # print(puzzle.goal)
