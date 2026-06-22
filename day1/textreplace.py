name = "This is nix"
surname = "williams"

new_name = name.replace("nix", "raymond") + " " + surname
print("Modified New Name:", new_name)

# Output: Modified New Name: This is raymond williams which means the replace() method has been used to replace the substring "nix" with "raymond" in the original string, and then the modified string has been concatenated with the surname to create the new name.