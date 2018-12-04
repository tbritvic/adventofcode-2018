import sys


def calculate_frequency(file_name):
    f = open(file_name, "r")
    freq_sum = 0

    for line in f.readlines(): 
        if line[0] == '+':
            freq_sum += int(line[1:])
        else:
            freq_sum -= int(line[1:])
    
    return freq_sum


def main():
    print(calculate_frequency(sys.argv[1]))


if __name__ == "__main__":
    main()
