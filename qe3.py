#Write a program that can parse an integer array and verify that is of social security number format.
#SSN number format is [3 digits – 2 digits – 4 digits] Ex: 123-45-5678
import re
ssn="123-45-5678"
print(re.match(r"\d{3}-\d{2}-\d{4}$",ssn))
