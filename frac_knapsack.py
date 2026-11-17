def fractional_knapsack(W, wt, val, n):
    ratio = []

    for i in range(n):
        ratio.append((val[i] / wt[i], wt[i], val[i]))

    ratio.sort(reverse=True)

    profit = 0

    for r, w, v in ratio:
        if W >= w:
            profit += v
            W -= w
        else:
            profit += r * W
            break

    return profit

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print("Maximum Profit:", fractional_knapsack(W, wt, val, n))
