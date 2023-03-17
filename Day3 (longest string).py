def longest_string(lst):
    longest_string=" "
    for i in lst:
        if len(i)>len(longest_string):
            longest_string=i
    return longest_string

print(longest_string(["apple",'daniel','volcanic']))