import re

word = "OTC ROMAN REIGNS is the G.O.A.T of Current WWE Generations. He's not the AURA Farmer But The Epitome of AURA."

# Check if the word "AURA" is present in the string
pattern = r"AURA"
search = re.search(pattern, word)
if search:
    print("Search found:", search.group())
else:
    print("No search found.")
