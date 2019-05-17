'''
Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install radio
transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to all
houses within that number of units distance away.
Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every
house is within range of at least one transmitter. Each transmitter must be installed on top of an existing house.

For example, assume houses are located at x = [1,2,3,5,9] and the transmission range k=1.
3 antennae at houses 2 and 5 and 9 would provide complete coverage

Function Description
--------------------
Complete the hackerlandRadioTransmitters function in the editor below. It must return an integer that denotes the
minimum number of transmitters to install.
hackerlandRadioTransmitters has the following parameter(s):

x: integer array that denotes the locations of houses
k: an integer that denotes the effective range of a transmitter

Input Format
------------
The first line contains two space-separated integers and , the number of houses in Hackerland and the range of each transmitter.
The second line contains space-separated integers describing the respective locations of each house x[i].

Constraints
-----------
1 <= n, k <= 10^5
1 <= x[i] <= 10^5
There may be more than one house at the same location.

Output Format
-------------
Print a single integer denoting the minimum number of transmitters needed to cover all of the houses.


'''

def radioTransmitters(x, k):
    x.sort()
    index = 0
    loc = 0
    size = len(x)
    res = 0
    while index < size:
        res += 1
        loc = x[index] + k
        while index < size and x[index] <= loc:
            index += 1
        index -= 1
        if index < size:
            loc = x[index] + k
        while index < size and x[index] <= loc:
            index += 1
    return res

x = [1,2,3,5,9]
k = 1
print(radioTransmitters(x, k))

x = [7,2,4,6,5,9,12,11]
k = 2
print(radioTransmitters(x, k))

x = [7,2,9,5,4,2,6,15,12]
k = 2
print(radioTransmitters(x, k))