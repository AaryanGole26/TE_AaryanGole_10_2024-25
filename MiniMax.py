import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case: targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# Driver code
scores_input = input("Enter the scores separated by spaces: ")
scores = list(map(int, scores_input.split()))

# Ensure the length of scores is a power of 2
num_scores = len(scores)
if (num_scores & (num_scores - 1)) != 0 or num_scores == 0:
    raise ValueError("The number of scores must be a power of 2.")

treeDepth = int(math.log2(num_scores))
print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))

''' 
Output : 
 Enter the scores separated by spaces: 3 5 6 9 1 2 0 -1
 The optimal value is: 5
'''
