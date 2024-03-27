## Name Generator

import random

print("Welcome to name generator")

def generator_name():
    first_name = ["enes","umut","deniz","ersel","albert","isaac","marie","jhonny"]
    last_name = ["black","white","star","faraday","newton","hawking"]
    return "{} {}".format(random.choice(first_name), random.choice(last_name))


print(generator_name())