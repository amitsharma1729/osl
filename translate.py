from textblob import TextBlob
from PyDictionary import PyDictionary

dictionary=PyDictionary()
choice=0
print("Welcome to Translator")

while(choice!=7):

    print("---------------------------------------------")
    print("Select from the following options:")
    print("1.Translate a word, sentence or a paragraph")
    print("2.Detect the language")
    print("3.Spelling check")
    print("4.Synonyms")
    print("5.Antonyms")
    print("6.Dictionary meaning")
    print("7.Exit")

    choice=int(input())
    if(choice==1):
        def translate():
            print("You chose : Translate a word, sentence or a paragraph")
            print("Enter text:")
            sent=input()
            print("Choose language:")
            print("1.French")
            print("2.Spanish")
            print("3.German")
            print("4.Italian")
            choice1=int(input())
            blob = TextBlob(sent)
            if(choice1==1):
                print(blob.translate(to='fr'))
            elif(choice1==2):
                print(blob.translate(to='es'))
            elif(choice1==3):
                print(blob.translate(to='de'))
            elif(choice1==4):
                print(blob.translate(to='it'))
            else:
                print("Please choose from the given options")
        translate()
    elif(choice==2):
        def detect():
            print("You chose : Detect the language")
            print("Enter text:")
            sent=input()
            blob=TextBlob(sent)
            print("The language is %s"%(blob.detect_language()))
        detect()
    elif(choice==3):
        def spell():
            print("You chose : Spell check")
            print("Enter text:")
            sent=input()
            blob=TextBlob(sent)
            if(sent!=blob.correct()):
                print("The correct sentence is :%s"%(blob.correct()))
            else:
                print("The sentence is already correct")
        spell()
    elif(choice==4):
        def synonym():
            try:
                print("You chose : Synonyms")
                print("Enter text:")
                sent=input()
                print("Synonym is:%s"%(dictionary.synonym(sent)))
            except:
                print();
        synonym()
    elif(choice==5):
        def antonym():
            print("You chose : Antonyms")
            print("Enter text:")
            sent=input()
            print("Antonym is:%s"%(dictionary.antonym(sent)))
        antonym()
    elif(choice==6):
        def meaning():
            print("You chose : Dictionary meaning")
            print("Enter text:")
            sent=input()
            print("Dictionary Meaning is:%s"%(dictionary.meaning(sent)))
        meaning()
