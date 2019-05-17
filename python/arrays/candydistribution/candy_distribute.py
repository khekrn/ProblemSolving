'''
Given an array of n integers where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:

Each student gets one packet.
The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
Examples:

Input : arr[] = {7, 3, 2, 4, 9, 12, 56} 
        m = 3
Output: Minimum Difference is 2
We have seven packets of chocolates and
we need to pick three packets for 3 students
If we pick 2, 3 and 4, we get the minimum
difference between maximum and minimum packet
sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} 
        m = 5
Output: Minimum Difference is 6
The set goes like 3,4,7,9,9 and the output 
is 9-3 = 6
'''

def candy_distribute(arr, m):
    n = len(arr)
    if n == 0 or m == 0:
        return 0
    
    if m > len(arr):
        return -1
    
    arr.sort()
    
    
    return 0