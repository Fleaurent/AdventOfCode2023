from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DAY                = 2
INPUT_FILE         = PROJECT_DIR / f"DAY_{DAY}" / "input.txt"

EXAMPLE_INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def get_input(filepath: Path) -> str:
    """ read input into string """
    with open(filepath, 'r') as f:
        data = f.read().strip()  
    return data

def parse_line_part_1(line: str) -> bool:
    """
    parse line '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    check if valid game i.e. if number of cubes per color is smaller than in bag_dict
    """
    bag_dict = {'red': 12, 'green': 13, 'blue': 14}
    
    # remove game number
    game_str = line.split(':')[1].strip()        

    for game_set in game_str.split(';'):
        # run through each game set
        for game_set_cubes in game_set.strip().split(','):
            # check each cube if valid
            number, color = game_set_cubes.strip().split(' ')            
            
            if(bag_dict[color] < int(number)):
                return False
    
    return True

def parse_line_part_2(line: str) -> dict:
    """ 
    parse line '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    find largest number of each color 
    return dict
    """
    game_dict = {'red': 0, 'blue': 0, 'green': 0}
    
    # remove game number
    game_str = line.split(':')[1].strip()
    
    for game in game_str.split(';'):
        
        for round in game.strip().split(','):
            # extract number and color: add to dict
            number, color = round.strip().split(' ')  
            
            if(game_dict[color] < int(number)):
                game_dict[color] = int(number)

    return game_dict


def part_1(data: str) -> int:
    """
    sum of ids of valid games
    """
    sum_ids = 0
    
    for index, game in enumerate(data.strip().split('\n')):
        # run through each game
        game_valid = parse_line_part_1(game)

        if(game_valid):
            sum_ids += (index + 1)          

    return sum_ids

def part_2(data: str) -> int:
    """
    sum of power of maximum number of cubes per color
    """
    power = 0

    for game in data.strip().split('\n'):
        # run through each game        
        game_dict = parse_line_part_2(game)     
        
        power_i = game_dict['red'] * game_dict['blue'] * game_dict['green']
        power += power_i

    return power

if __name__ == '__main__':
    print(EXAMPLE_INPUT)
    
    print(INPUT_FILE)
    input_str = get_input(INPUT_FILE)

    # Part 1
    print(part_1(EXAMPLE_INPUT))
    print(part_1(input_str))

    # Part 2
    print(part_2(EXAMPLE_INPUT))
    print(part_2(input_str))
