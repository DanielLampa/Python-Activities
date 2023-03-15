def count_characters(str):
    count={} #declare a dictionary to hold the count of each characters in the strings
    for i in str:
        if i in count: #if the character is already seen it will increment to 1
            count[i]+=1
        else:
            count[i]=1
    print(count)

word=input("Input a string: ") # get from the user input
print(count_characters(word))