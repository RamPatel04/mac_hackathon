import re

text = """
Certainly! If you provide me with the context of these scenarios, I can write descriptive narratives for each scenario that remove any reference to scenes, the movie itself, or specific objects.

In this re-imagined version of Toy Story, the following are three examples of how the narrative has evolved to become longer, more interactive, and organized:

1. Extended Friendship: Andy's bond with his toys has become much stronger and lasts longer. Instead of getting rid of his toys when he grows up, he decides to keep them. Andy treats his toys as friends or extended companions who provide comfort and entertainment throughout his life, dealing with new responsibilities and changing scenarios.

2. Adaptive Toys: The toys are now more interactive and adaptive to respond to Andy and each other in various ways. They can incorporate sensors and respond to interactions uniquely, making their use more entertaining and engaging. This allows for diverse play and engagement compared to traditional toys.

3. Improved Toy Organization: The writers added more detail to how Andy organized his toys. They created an efficient system that not only made it easy for Andy to find his toys when needed but also arranged the toys in a way that allowed them to organize themselves, find each other, and maintain a purposeful arrangement.

Do you require any more clarification or additional text examples to illustrate the new narrative aspects of this re-imagined version of Toy Story?
"""

pattern = r'\d\..*?(?=\n\d\.|\n\n|$)'
matches = re.findall(pattern, text, re.DOTALL)

combined_string = '\n'.join(matches)

print(combined_string)
