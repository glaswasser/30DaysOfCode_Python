# Task
#Complete the Difference class by writing the following:

# A class constructor that takes an array of integers as a parameter and saves
# it to the elements instance variable.
# A computeDifference method that finds the maximum absolute difference between
# any 2 numbers in N and stores it in the maximumDifference instance variable.


# This is probably not the solution they wanted
# They say "to find the maximum difference, computeDifference checks each
# element in the array and finds the maximum difference between any 2 elements...
# What I did was just taking the max and min to create the difference.
# Alternatively one would use a for loop. But this solution went through all the
# test cases, so yeah... let's count it ;P

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        minimum = min(self.__elements)
        maximum = max(self.__elements)
        self.maximumDifference = maximum - minimum


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
