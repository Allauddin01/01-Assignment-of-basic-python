word=input('Enter the word = ') #abcd
# for i in range(len(word)-1,-1,-1):
    # print(word[i],end=" ")
rev=""
for i in word: #i=a,i=b
    rev=i+rev #rev=a,rev=b+a=ba
print(rev)
