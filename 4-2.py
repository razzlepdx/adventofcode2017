# Advent of Code 2017 - Problem 1, Day 4
########################################
# For added security, yet another system policy has been put 
# in place. Now, a valid passphrase must contain no two words 
# that are anagrams of each other - that is, a passphrase is 
# invalid if any word's letters can be rearranged to form any 
# other word in the passphrase.

# Under this new system policy, how many passphrases are valid?

def find_valid_passphrases(file):
    # set up counter variable
    valid_pass = 0
    input = open(file, "r")
    # iterate over lines in input file
    for line in input:
        passphrase = line.split()
        sorted_pass = []
        for word in passphrase:
            sorted_word = ''.join(sorted(word))
            sorted_pass.append(sorted_word)
        unique_list = set(sorted_pass)
        if len(unique_list) == len(sorted_pass):
            valid_pass += 1
    
    return valid_pass


# For testing:
#################
print(find_valid_passphrases("testfile2.txt")) #should return 3
print(find_valid_passphrases("day-4-input.txt"))