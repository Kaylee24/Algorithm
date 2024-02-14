import re

password = input()

for vowel in ['a', 'e', 'i', 'o', 'u']:
    if vowel not in password:
        result = no_acceptable

jaeums = re.split('a|e|i|o|u', password)
print(jaeums)

for jaeum in jaeums:
    if len(jaeum) >= 3:
        result = no_acceptable