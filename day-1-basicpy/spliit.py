nix = "This is my first python script. I am learning python for DevOps. I am loving it/ splitting things is fun"

print(nix.split(".")[2])

# Output: I am loving it/ splitting things is fun which means the string has been split into a list of substrings using the period as a delimiter, and the third substring (index 2) has been printed.

arn = "arn:aws:iam::123456789012:user/JohnDoe"
print(arn.split(":")[4])
# Output: 123456789012 which means the string has been split into a list of substrings using the colon as a delimiter, and the fifth substring (index 4) has been printed.