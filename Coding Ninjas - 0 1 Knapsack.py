

def maxValue(values, weights, currIndex, w, memo):
    if currIndex==len(values) or w==0:
        return 0
    if memo[currIndex][w] != -1:
        return memo[currIndex][w]
    result=0
    if weights[currIndex]<=w:
        include = values[currIndex] + maxValue(values, weights, currIndex+1, w-weights[currIndex], memo)

        exclude = maxValue(values, weights, currIndex+1, w, memo)

        result=max(include, exclude)
    else:
        result=maxValue(values, weights, currIndex+1, w, memo)
    memo[currIndex][w] = result
    return result

def maxProfit(values, weights, n, w):
    memo = [[-1 for _ in range(w + 1)] for _ in range(n)]
    return maxValue(values, weights, 0, w, memo)
    
