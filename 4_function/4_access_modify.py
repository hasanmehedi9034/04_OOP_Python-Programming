balance = 500

def total_cost(price, quantity):
    global balance
    cost = price * quantity
    balance = balance - cost
    return cost

print(balance)
print(total_cost(2, 5))
print(balance)