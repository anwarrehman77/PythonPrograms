# given a set of coins of certain denominations and an amount
# find all the ways you can get the amount using the coins
# assume unlimited number of coins are available for each denomination

amount = 30
coins = [1, 5, 10, 25]
print("Coin changer application")
print("Coins=" + str(coins))
print("Amount=" + str(amount))

x = len(coins)

# Recursive function that prints and counts solutions
def print_change(startindex, totalnow, strchange):
    # add coin(startindex) to the solution
    totalnow += coins[startindex]
    if strchange != "":
        strchange += ","
    strchange += str(coins[startindex])

    soln = 0
    if totalnow == amount:
        print (strchange) #We got a solution. print and return
        soln = 1
    elif totalnow < amount:
        # OK lets try a solution by adding one more coin
        # lets start with the same denomination and
        # then every other denomination that comes after this one.
        for i in range (startindex, x):
            # let us print if this works
            soln += print_change(i, totalnow, strchange)
    return soln

solncount = 0
for i in range(0, x):
    solncount += print_change(i, 0, "")

print("Found " + str(solncount) + " solutions!!!")
