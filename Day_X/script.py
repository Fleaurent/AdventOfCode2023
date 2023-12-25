from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DAY                = 3
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

def part_1(data: str) -> int:
    return 0

def part_2(data: str) -> int:
    return 0

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
