import re

def no_dups(s):
    # Your code here

    d = {}

    # create an array of words
    words = re.findall(r"\w+(?:'\w+)?", s)

    # loop through each word
    for word in words:
        # if word lowercased is not in dictinary
        if word.lower() not in d:
            # add the word as a key and string value to dictionary
            d[word.lower()] = f'{word.lower()}'
    # combine all items in dictionary into a string
    return ' '.join(d)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))