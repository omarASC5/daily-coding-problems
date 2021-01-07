def findAllSteps(N, X):
    all_subsets = []

    def helper(N, X, subset):
        if N == 0:
            all_subsets.append(subset)
        elif N < 0:
            return

        for i in range(len(X)):
            old_subset = subset[:]
            subset = subset + [X[i]]
            remaining_sum = N - X[i]
            if remaining_sum < N:
                helper(remaining_sum, X, subset)
            subset = old_subset

    helper(N, X, [])

    return all_subsets

assert findAllSteps(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert findAllSteps(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]
