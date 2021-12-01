# Import the data file and split it into lines
data = open("input.txt")
lines = data.readlines()

# PART TWO

def repeat_freq(freq_file):
    import itertools
    frequency = 0
    my_set = set()
    finish = 0

    freq_cycle = itertools.cycle(freq_file)

    while finish == 0:

        for i in freq_cycle:
            i_int = int(i)
            frequency += i_int

            if frequency in my_set:
                print(f"I have already seen {frequency}.")
                finish = 1
                break
            elif frequency == 0:
                print("I have already seen 0.")
                finish = 1
                break
            else:
                my_set.add(frequency)


repeat_freq(lines)
