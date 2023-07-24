char=input('Enter the Alphabet = ')
char=char.lower() #Important
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print(f'This is Vowel = {char}')
else:
    print(f'This {char} is not a Vowel')