def palindrome(sentence):
    #replace all punctuation character into "" 
    for i in (",.'?/}{[]'"):
        sentence=sentence.replace(i,"")
    #declare a list to store the data temporarily
    palindrome=[]
    #
    word=sentence.split(' ')
    for i in word:
        i=i.lower()
        if i==i[::-1]:
            palindrome.append(i)
    return palindrome

sentence=input("Enter a sentence: ")
print(palindrome(sentence))






