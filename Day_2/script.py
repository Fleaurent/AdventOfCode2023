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

def parse_game(line: str) -> dict:
    """ 
    parse line '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    into dict: {{'red': 4}, {'blue': 9}, {'green': 4}} 
    return dict
    """
    game_dict = {'red': 0, 'blue': 0, 'green': 0}
    for game in line.split(';'):
        
        for round in game.strip().split(','):
            # extract number and color: add to dict
            number, color = round.strip().split(' ')            
            game_dict[color] += int(number)

    return game_dict

def check_game(bag_dict: dict, game_dict: dict) -> bool:
    """ compare that all colors in bag_dict are larger than game_dict """
    for color in bag_dict.keys():
        if(bag_dict[color] < game_dict[color]):
            return False
    return True

def part_1(data: str) -> int:
    """
    1. 
    """
    bag_dict = {'red': 12, 'green': 13, 'blue': 14}
    sum_ids = 0
    
    for index, line in enumerate(data.strip().split('\n')):
        game_dict = parse_game(line.split(':')[1].strip())
        print(f"Game {index + 1}: {game_dict}")
        
        if(check_game(bag_dict, game_dict)):
            sum_ids += (index + 1)
            print("is valid")            

    return sum_ids

def part_2(data: list) -> int:
    """ find top 3 largest sum """
    number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = 0
    
    # return top_3_sum
    return result

if __name__ == '__main__':
    print(INPUT_FILE)

    print(EXAMPLE_INPUT)
    input_str = get_input(INPUT_FILE)
    # print(input_str)

    # Part 1
    print(part_1(EXAMPLE_INPUT))
    print(part_1(input_str))

    # Part 2
    #print(part_2(example_data2))
    #print(part_2(data))
