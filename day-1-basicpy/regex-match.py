import re

word = "Bank My Official Account Number is 1234567890"
# Check if the word "Bank" is present in the string
pattern = r"Bank"
match = re.match(pattern, word)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")

# Output: Match found: Bank which means the regular expression pattern "Bank" is found at the beginning of the string, and the match object contains the matched substring "Bank". and match() only checks for a match at the beginning of the string. If the pattern is found at the beginning, it returns a match object; otherwise, it returns None. In this case, since "Bank" is at the beginning of the string, a match is found and printed.

