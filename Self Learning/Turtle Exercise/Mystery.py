def paradox(riddle, poser):
    return riddle + [poser[0]] #b, c

def mystery(puzzle, cont = ['b']):
    return [puzzle[1]] + paradox(cont, puzzle)

result = mystery(['c', 'a'])

print(result)