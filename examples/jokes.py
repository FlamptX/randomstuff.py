import randomstuff

client = randomstuff.Client(key="api-key")

joke = client.get_joke(type="any") # Available joke types: ('pun', 'spooky', 'dev', 'any')

print("Category: ", joke.category) # The category of the joke.
print("Joke Type: ", joke.type) # The type of joke, Can either be `single` or `twopart`.
print("Joke: ", joke.joke) # Actual joke. , if the joke type is single, This is a string otherwise it is a dictionary with two keys "setup" and "delivery".
print("ID: ", joke.id) # The joke's ID. Every joke has a unique ID.
print("Safe: ", joke.safe) # Determines if the joke is safe or not. If this is `True`, the joke is safe.
print("Language: ", joke.lang) # The language of joke.

print("\n=== Flags ===\n")
print("NSFW: ", jokes.flags.nsfw) # Determines if the joke is NSFW or not. If this is `True`, The joke is NSFW.
print("Religious: ", jokes.flags.religious) # Determines if the joke is religious or not. If this is `True`, The joke is religious.
print("Political: ", jokes.flags.political) # Determines if the joke is political or not. If this is `True`, The joke is political.
print("Racist: ", jokes.flags.racist) # Determines if the joke is racist or not. If this is `True`, The joke is racist.
print("Sexist: ", jokes.flags.sexist) # Determines if the joke is sexist or not. If this is `True`, The joke is sexist. 
print("Explicit: ", jokes.flags.explicit) # Determines if the joke is explicit or not. If this is `True`, The joke is explicit.
