# Probability of "HELLO" Math Problem

## Program
The program solves the following problem by going through every possible scenario and finding the highest probability. The alternative is to solve the problem mathematically but that requires a bit more... pizzazz.

The console output shows a list of five coins `[['H', 'E'], ...]` where `'H'` is the letter on one side of the coin and `'E'` is the letter on the other side of the coin. Under each list of coins, the probability that "HELLO" is drawn is shown. To avoid printing all $4^{10} = 1,048,576$ different coin combinations, only the coins with the highest probability are shown.

### Usage
Run the python file in a console
```
python HelloProblem.py
```

## Problem Statement
The problem was found at https://math.bot/q/probability-spelling-hello-marked-coins-3ii8RT1

A set of five quarters was marked with a permanent marker. A random English language letter was written on the face of each coin. On the back of each coin, a different random English language letter was written. All of the letters written on the coins are upper-case.


Each of the five quarters was marked using the same process, so it is possible to have duplicate letters within the set of five coins. No coin has the same letter written on both sides.


After marking the coins, they are placed in an opaque cloth bag. You reach into the bag and select a coin using a blind draw. Once selected, you flip the coin and place it on a table. You repeat this process for each coin, drawing it at random from the cloth bag, flipping it, and then placing it on the table. You do not have any special coin-flipping skill; the coin flip causes a random side of the coin to be selected. After the coins have all been drawn and flipped, the coins are arranged in a neat row in the order in which they were drawn.


Suppose you were hopeful that the result would spell the word "HELLO" after the selection and flipping process was completed. Furthermore, suppose that by random chance the marking of the coins coincidentally maximized the odds that you would get a favorable outcome. Keep in mind that the order in which the coins are drawn from the bag is still entirely random.


In this favorable scenario, what is the probability that the letters on the coins spell the word "HELLO"?

## Solution
The result from the console output shows that in a scenario where the coin markings result in a favorable (highest) probability, the probability is $\dfrac{12}{3840} = 0.003125$.

When first attempting to solve the problem, one might think that they should determine which specific coin markings would result in a favorable scenario. However there are many different coin markings that cause such a scenario and as seen in the brute force approach that the program took, there are 960 favorable scenarios out of 1,048,576 scenarios. Instead the solution involves finding the characteristic that a favorable scenario entails.

The characteristic is that in a favorable scenario, there are 12 ways of rearranging the coins to obtain HELLO. Five coins have $5! = 120$ permutations. Thus, the probability that the coins are drawn in the right order is $\dfrac{12}{120} = \dfrac{1}{10}$. The probability that a coin is flipped to the side with the correct letter is $\dfrac{1}{2}$. So the probability that all coins are flipped to the correct side is $\dfrac{1}{2^5}$. So the probability of HELLO --coins drawn in correct order and with correct side up-- is $\dfrac{1}{10} * \dfrac{1}{2^5} = \dfrac{1}{320} = 0.003125$. This result matches what the program outputted.

Now the problem I am stuck on is proving where 12 came from in a mathematical way without the brute force approach.
