def long_length(a):
    long=0
    for word in a.split(' '):
        if len(word)>long:
            long=len(word)
            longest_word=word
    print("",word)


a=input("Enter the sentence")
long_length(a)
