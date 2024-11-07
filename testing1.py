def maximumWealth(self, accounts):
        wealth = []
        sum = 0
        richest = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum += j
            wealth.append(sum)
        for i in range(len(wealth)):
            richest = max(richest, wealth[i])
        print(richest)