import nltk
def toknize_text(text):
    return nltk.word_tokenize(text)
def toknize_sentences(text):
    return nltk.sent_tokenize(text)
def main():
    user_input=input('enter the text')
    print("Choose an option:")
    print("1. Print tokenized words")
    print("2. Print tokenized sentences")
    print("3. Print output using split function")

    print('enter the number')
    choice=int(input('enter the number 1/2/3: '))
    if choice==1:
        tokenized_words = toknize_text(user_input)
        print("Tokenized wordqs:", tokenized_words)
    elif choice==2:
        toknize_sentence=toknize_sentences(user_input)
        print(toknize_sentence)
    elif choice ==3:
        split_words=user_input.split()
        print(split_words)
    
if __name__ =='__main__':
    main()