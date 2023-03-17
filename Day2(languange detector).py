from langdetect import detect
dict={'en':"english",'fi':'filipino'}

text=detect(str(input("Enter a text:" )))
print(dict[text])