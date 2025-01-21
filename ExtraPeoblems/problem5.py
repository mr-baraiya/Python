# [-2,3,4,5,-1,3,-4,-3] => [3,-2,4,-1,5,-4,3,-3]

def interleave_pos_neg(arr):
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    result = []
    
    # Interleave positive and negative numbers
    while pos or neg:
        if pos:
            result.append(pos.pop(0))
        if neg:
            result.append(neg.pop(0))
    
    return result

# Input array
l = [-2,3,4,5,-1,3,-4,-3]
# Transform the array
output = interleave_pos_neg(l)
print(output)