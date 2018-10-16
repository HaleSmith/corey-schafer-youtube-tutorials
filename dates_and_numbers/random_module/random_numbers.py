# References https://www.youtube.com/watch?v=KzqSDvzOFNA
# Should not be used for security/cryptography

# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


import random  # Use secrets.py if need to do passwords/encryption

# Note that 0 is inclusive, 1 is not (could be 0, but only 0.9999)
new_section("Random number between 0 and 1")
value = random.random()
print(value)

new_section("Random float in range 1 - 10")
value = random.uniform(1, 10)
print(value)

new_section("Random integer")
value = random.randint(1, 6)  # Includes 1 and 6
print(value)

new_section("Random choice from a list")
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
print(value + ', Corey')

new_section("Roulette, equal probabilities")
colors = ['Red', 'Black', 'Green']
# Simulate 10 spins
results = random.choices(colors, k=10)
print(results)

new_section("Roulette, true probabilities")
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

new_section("Shuffle deck of cards in place")
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

new_section("Sample from deck, remove from deck after sampling")
hand = random.sample(deck, k=5)  # Only unique values
print(hand)
