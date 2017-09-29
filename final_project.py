import sentiments as pro

i=1

while i == 1:
    text = input("Enter a comment to check weather it is a positive comment")

    print(pro.sentiment(text))
    i=int(input("Enter 1 to try more comments"))

    
