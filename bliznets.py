count = int(input())
coins = [int(x) for x in input().split(' ')]

coins.sort(reverse=True)
fullsum = sum(coins)
left_money = 1
take_money = [coins[0]]

while sum(take_money) <= fullsum - sum(take_money):
    take_money.append(coins[left_money])
    left_money += 1

print(len(take_money))
