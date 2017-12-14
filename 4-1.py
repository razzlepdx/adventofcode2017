# Advent of Code 2017 - Problem 1, Day 4
########################################
# A new system policy has been put in place that requires all 
# accounts to use a passphrase instead of simply a password. A 
# passphrase consists of a series of words (lowercase letters) 
# separated by spaces.

# To ensure security, a valid passphrase must contain no 
# duplicate words.

# The system's full passphrase list is available as your 
# puzzle input. ***How many passphrases are valid?***

def validate_pass(file):

    # set up counter variable
    valid_pass = 0
    input = open(file, "r")
    # iterate over lines in input file
    for line in input:
        current_passphrase = line
        words = current_passphrase.split()
        unique_list = set(words)
        if len(unique_list) == len(words):
            valid_pass += 1

    return valid_pass


# For testing:
#################
print(validate_pass("day-4-input.txt"))