"""
looks like some leetcode problem

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
"""


"""
testing floor division

revX = 897
x = 89798
y = 3
print(1 // 10)
"""


"""
testing logic ??? idk 

s = "examples243"
for i in range(len(s) - 1):
    print(s[i])
"""


"""testing for lp(leetcode problem)#14

strs = ["flower", "flowing", "floful"]

lcp = ""
for i in range(len(strs) - 1):
    print(len(strs[i]))
    for j in range(len(strs[i])):
        if strs[i][j] == strs[i + 1][j]:
            lcp = strs[i][:j + 1]
        else:
            lcp = 
print(lcp)
        
"""
