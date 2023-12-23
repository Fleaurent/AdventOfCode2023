from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE         = PROJECT_DIR / "Day_1" / "input.txt"
EXAMPLE_INPUT_FILE = PROJECT_DIR / "Day_1" / "example_input.txt"
EXAMPLE_INPUT_FILE2 = PROJECT_DIR / "Day_1" / "example_input2.txt"


def get_input(filepath: Path) -> list:
    """ read lines into list of strings """
    data = []

    with open(filepath, "r") as f:
        lines = f.readlines()

        for line in lines:
            data.append(line.strip())
                
    return data


def part_1(data: list) -> int:
    """
    1. combine the first digit and the last digit (in that order) to form a single two-digit number.
    2. Adding these together produces
    """
    result = 0
    
    for line in data:
        first_num = None
        second_num = None
        
        for character in line:
            if character.isdigit():
                if first_num is None:
                    first_num = int(character)
                    second_num = first_num
                else:
                    second_num = int(character)
            
        calibration_value = first_num * 10 + second_num
        result += calibration_value
        
    return result

def part_2(data: list) -> int:
    """ find top 3 largest sum """
    number_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = 0
    
    for line in data:
        # find the first_num
        first_num = None
        
        for character_index, character in enumerate(line):
            # 1. check for number 
            if character.isdigit():
                first_num = int(character)
            
            # 2. check for ascii num
            temp_line_str = line[character_index:]
            for i, num in enumerate(number_list):
                if temp_line_str.startswith(num):
                    first_num = i
                    break
            
            # check if number already found
            if first_num is not None:
                break
        
        
        # find last valid num
        last_num = None
        
        for reversed_character_index, character in enumerate(reversed(line)):
            character_index = len(line) - reversed_character_index
            
            # 1. check for number 
            if character.isdigit():
                last_num = int(character)
            
            # 2. check for ascii num
            temp_line_str = line[:character_index]
            for i, num in enumerate(number_list):
                if temp_line_str.endswith(num):
                    last_num = i
                    break
                
            # check if number already found
            if last_num is not None:
                break
        
        # calculate calibration value
        calibration_value = first_num * 10 + last_num
        result += calibration_value
        
    # return top_3_sum
    return result

if __name__ == '__main__':
    print(INPUT_FILE)

    example_data = get_input(EXAMPLE_INPUT_FILE)
    print(example_data)
    
    example_data2 = get_input(EXAMPLE_INPUT_FILE2)
    print(example_data2)

    data = get_input(INPUT_FILE)
    print(f"Number of lines: {len(data)}")

    # Part 1
    print(part_1(example_data))
    print(part_1(data))

    # Part 2
    print(part_2(example_data2))
    print(part_2(data))
