'''
Let’s say we have a whole bunch of people in line waiting to see a baseball game. They are all hometown fans and each person is wearing a team cap. However, not all of them are wearing the caps in the same way—some are wearing their caps in the normal way, and some are wearing them backward.
People have different definitions of normal and backward, but you think the cap on the left (see below) is being worn normally, and the one on the right is being worn backward.

You are the gatekeeper and can only let the fans into the stadium if the entire group has their caps on the same way—either all forward or all backward. Because everyone has different definitions of forward and backward, you can’t tell them to wear their caps forward or backward. You can only tell them to flip their caps. The good news is that each person knows what position they are in the line, with the first person having position 0 and the last one position n − 1. You can say things like:

Person in position i, please flip your cap.
People in positions i through j (inclusive), please flip your caps.

But what you would like to do is minimize the number of requests you have to shout, to save your voice. Here is an example:

['F','F','B','B','B','F','B','B','B','F','F','B','F']

We have thirteen people standing in line in positions 0 through 12, inclusive. Since there are six people with caps on forward, we could shriek out six commands, for example:
Person in position 0, please flip your cap.

and repeat for the people in positions 1, 5, 9, 10, and 12. A voice-saving measure would exploit the second type of command and only yell out four commands:

People in positions 0 through 1, please flip your caps.
Person in position 5, please flip your cap.
People in positions 9 through 10, please flip your caps.
Person in position 12, please flip your cap.

and this will get everyone to have caps on backward.
However, in this example, we can do one better. If we scream out:
People in positions 2 through 4, please flip your caps.
People in positions 6 through 8, please flip your caps.
Person in position 11, please flip your cap.

this will get everyone with caps on forward.

How can we generate the minimum number of commands? A harder question: Can you think of a way of generating the commands as you walk down the line for the first time?

'''

def all_confirm(seq):
    # seq = seq + ['END']
    forward = []
    backward = []
    last_item = seq[0]
    last_start, last_index = 0, 0
    for index in range(1, len(seq)):
        if last_item is not seq[index]:
            range_index = [last_start, index - 1]
            if seq[index] == 'END':
                if seq[index] == 'B':
                    backward.append(range_index)
                else:
                    forward.append(range_index)
                break   
            if seq[index] == 'B':
                forward.append(range_index)
            else:
                backward.append(range_index)
            last_start = index
            last_index = index-1
        last_item = seq[index]
    # if last_index != len(seq) - 1:
    #     range_index = [last_index+1, len(seq) - 1]
    #     if seq[last_index+1] == 'B':
    #         backward.append(range_index)
    #     else:
    #         forward.append(range_index)
    print("Forward Range = ", forward)
    print("Backward Range = ", backward)

x = ['F','F','B','B','B','F','B','B','B','F','F','B','F', 'END']
all_confirm(x)
# x = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
# all_confirm(x)