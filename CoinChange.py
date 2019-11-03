class CoinChange:
    def NumberofCoins(self, arr, n):
        table = [[0 for _ in range(n + 1)] for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(n + 1):
                if i > 0:
                    if j >= arr[i]:
                        table[i][j] = min(table[i - 1][j], table[i][j - arr[i]] + 1)
                    else:
                        table[i][j] = table[i - 1][j]
                else:
                    table[i][j] = j
        return table[-1][-1]