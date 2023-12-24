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

def parse_line(line: str) -> dict:
    """ 
    parse line '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    find largest number of each color 
    return dict
    """
    game_dict = {'red': 0, 'blue': 0, 'green': 0}
    for game in line.split(';'):
        
        for round in game.strip().split(','):
            # extract number and color: add to dict
            number, color = round.strip().split(' ')  
            
            if(game_dict[color] < int(number)):
                game_dict[color] = int(number)

    return game_dict


def part_1(data: str) -> int:
    bag_dict = {'red': 12, 'green': 13, 'blue': 14}
    sum_ids = 0
    
    for index, game in enumerate(data.strip().split('\n')):
        # run through each game
        game_valid = True
        
        game_str = game.split(':')[1].strip()
        
        for game_set in game_str.split(';'):
            # run through each game set
            for game_set_cubes in game_set.strip().split(','):
                # check each cube if valid
                number, color = game_set_cubes.strip().split(' ')            
                
                if(bag_dict[color] < int(number)):
                    game_valid = False
                    break
                
        if(game_valid):
            sum_ids += (index + 1)          

    return sum_ids

def part_2(data: str) -> int:
    """
    TEST
    """
    for index, game in enumerate(data.strip().split('\n')):
        # run through each game
        game_str = game.split(':')[1].strip()
        
        game_dict = parse_line(game_str)       
        print(game_dict)

    return 0

if __name__ == '__main__':
    print(INPUT_FILE)

    print(EXAMPLE_INPUT)
    input_str = get_input(INPUT_FILE)
    # print(input_str)

    # Part 1
    #print(part_1(EXAMPLE_INPUT))
    #print(part_1(input_str))

    # Part 2
    print(part_2(EXAMPLE_INPUT))
    #print(part_2(data))
