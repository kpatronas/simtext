# simtext
Give a file, create a json report of how similiar is each line of the file to the others in a rating between 0: Not similar at all 1:Exact match

Example:
simtext.py --file ./test_file.txt
{"1": {"1": 1.0, "2": 1.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.0, "10": 0.0}, "2": {"1": 1.0, "2": 1.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.0, "10": 0.0}, "3": {"1": 0.0, "2": 0.0, "3": 1.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.0, "10": 0.0}, "4": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 1.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.3333333333333333, "10": 0.0}, "5": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 1.0, "6": 0.3333333333333333, "7": 0.0, "8": 0.2, "9": 0.6666666666666666, "10": 0.6666666666666666}, "6": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.3333333333333333, "6": 1.0, "7": 0.0, "8": 0.0, "9": 0.0, "10": 0.6666666666666666}, "7": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 1.0, "8": 0.0, "9": 0.0, "10": 0.0}, "8": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.2, "6": 0.0, "7": 0.0, "8": 1.0, "9": 0.2, "10": 0.15384615384615385}, "9": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 0.3333333333333333, "5": 0.6666666666666666, "6": 0.0, "7": 0.0, "8": 0.2, "9": 1.0, "10": 0.4444444444444444}, "10": {"1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.6666666666666666, "6": 0.6666666666666666, "7": 0.0, "8": 0.15384615384615385, "9": 0.4444444444444444, "10": 1.0}}

The key is the number of line, the values of the keys are lines of the files also and their values are a rating between 0-1 which indicates how similiar each line is to the others.