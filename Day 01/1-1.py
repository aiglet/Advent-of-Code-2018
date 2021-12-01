# Import the data file and split it into lines
data = open("input.txt")
lines = data.readlines()


# PART ONE

def add_freq(freq_file):
    total = 0

    for i in freq_file:
        i_num = int(i)
        total += i_num

    print(f"The total is {total}.")


add_freq(lines)
