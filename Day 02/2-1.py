# Import the data file and split it into lines
data = open("input.txt")
lines = data.readlines()


# Define a function to return the character counts in a string as a dictionary by character
def check_freq(x):
    freq = {}
    for c in set(x):
        freq[c] = x.count(c)
    return freq


# Define the function to calculate the desired checksum
def checksum(datafile):

    # Set up variables to note whether this is a two-repeat or a three-repeat
    two_letter = 0
    three_letter = 0

    # For each line in the data file
    for line in datafile:
        two_count = 0
        three_count = 0

        # Set up the line as a dictionary
        test = check_freq(line.strip())

        # Go through the values in dictionary and increment the counters if there is a two or three repeat
        for value in test.values():
            if value == 2:
                two_count += 1
            if value == 3:
                three_count += 1
        # Since each item only counts once even if there are multiple two or three repeats, check this
        # before incrementing the counters
        if two_count > 0:
            two_letter += 1
        if three_count > 0:
            three_letter += 1

    # Calculate the checksum
    checksum_tot = two_letter * three_letter

    # Print the results
    print(f"The checksum is {checksum_tot}.")


checksum(lines)
