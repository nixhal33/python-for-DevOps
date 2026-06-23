# 1. Replace
import re

word = "Roman Reigns is the G.O.A.T of Current WWE Generations. He's not the AURA Farmer But The Epitome of AURA."
print("Original Word:", word)
print("--------------------")
pattern = r"Farmer"
replace = "king of kings"
replace_word = re.sub(pattern, replace, word)
print("Modified Word:", replace_word)  

# 2. Findall
pattern = r"AURA"
findall = re.findall(pattern, word)
if findall:
    print("Findall found:", findall)
else:
    print("No findall found.")

# 3. Split 
pattern = r"AURA"
split_word = re.split(pattern, word)
if split_word:
    print("Split found:", split_word[0])
else:
    print("No split found.")

