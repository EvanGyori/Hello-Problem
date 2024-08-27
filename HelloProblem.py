# This program goes through every possible scenario in order to solve the following problem
# in a brute force manner rather than a mathematical approach.

"""
A set of five quarters was marked with a permanent marker. A random English language letter
was written on the face of each coin. On the back of each coin, a different random English
language letter was written. All of the letters written on the coins are upper-case.


Each of the five quarters was marked using the same process, so it is possible to have
duplicate letters within the set of five coins. No coin has the same letter written on both
sides.


After marking the coins, they are placed in an opaque cloth bag. You reach into the bag and
select a coin using a blind draw. Once selected, you flip the coin and place it on a table.
You repeat this process for each coin, drawing it at random from the cloth bag, flipping it,
and then placing it on the table. You do not have any special coin-flipping skill; the coin flip
causes a random side of the coin to be selected. After the coins have all been drawn and flipped,
the coins are arranged in a neat row in the order in which they were drawn.


Suppose you were hopeful that the result would spell the word "HELLO" after the selection and
flipping process was completed. Furthermore, suppose that by random chance the marking of the
coins coincidentally maximized the odds that you would get a favorable outcome. Keep in mind
that the order in which the coins are drawn from the bag is still entirely random.


In this favorable scenario, what is the probability that the letters on the coins spell the word "HELLO"?
"""

def probability(coins):
    """
    Returns the number of ways the coins can be arranged to spell HELLO
    assuming that the correct side is picked.
    
    :param coins: a list of length 5 whose elements are lists of length 2 containing the letter on each side of the coin
    """
    prob = 0
    for coin1 in coins:
        if coin1[0] == 'H' or coin1[1] == 'H':
            coins2 = coins.copy()
            coins2.remove(coin1)
            for coin2 in coins2:
                if coin2[0] == 'E' or coin2[1] == 'E':
                    coins3 = coins2.copy()
                    coins3.remove(coin2)
                    for coin3 in coins3:
                        if coin3[0] == 'L' or coin3[1] == 'L':
                            coins4 = coins3.copy()
                            coins4.remove(coin3)
                            for coin4 in coins4:
                                if coin4[0] == 'L' or coin4[1] == 'L':
                                    coins5 = coins4.copy()
                                    coins5.remove(coin4)
                                    for coin5 in coins5:
                                        if coin5[0] == 'O' or coin5[1] == 'O':
                                            prob += 1
    #prob *= 1 / (10 * 8 * 6 * 4 * 2)
    return prob

def is_valid(coins):
    """
    Returns whether the coins is valid given the problem statement.
    True if no coin has the same letter on both sides.
    
    :param coins: a list of length 5 whose elements are lists of length 2 containing the letter on each side of the coin
    """
    for coin in coins:
        if coin[0] == coin[1]:
            return False
            
    return True

def next_case(coins):
    """
    Goes to that next possible set of coins (goes through invalid sets as well).
    There are 4 ** 10 possible sets
    
    :param coins: a list of length 5 whose elements are lists of length 2 containing the letter on each side of the coin
    """
    for i in range(len(coins)):
        for j in range(len(coins[i])):
            if coins[i][j] == 'H':
                coins[i][j] = 'E'
                return
            elif coins[i][j] == 'E':
                coins[i][j] = 'L'
                return
            elif coins[i][j] == 'L':
                coins[i][j] = 'O'
                return
            elif coins[i][j] == 'O':
                coins[i][j] = 'H'
                
def copy(coins):
    """
    Returns a copy of a list of lists
    so that each element is a copy rather than the original reference.
    """
    coins_copy = coins.copy()
    for i in range(len(coins)):
        coins_copy[i] = coins[i].copy()
    return coins_copy

coins = [['H', 'H'], ['H', 'H'], ['H', 'H'], ['H', 'H'], ['H', 'H']]
best_prob = 0
best_coins = []
counter = 0
# Goes through every possible arrangement of coins
for x in range(4 ** 10):
    next_case(coins)
    
    # No coin can have the same letter on both sides
    if is_valid(coins):
        prob = probability(coins)
        if (prob >= best_prob):
            best_prob = prob
            best_coins = copy(coins)
            print(best_coins)
            print("Probability:", best_prob, "/ 3840 =", (best_prob / 3840))
            print()
            if prob == 12:
                counter += 1

print(counter, "result in highest probability of", best_prob, "/ 3840 =", (best_prob / 3840))