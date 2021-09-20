# this project create by Soheil Nikroo for advance programming class WD

# import dependencies
import arabic_reshaper
import yaml
from bidi.algorithm import get_display
import keyboard
from os import system
from termcolor import colored

# global variable for storage the dictionary
dic={}
client_words=[]
practice_word=''


#lower case the dictionery storage name
def word_list_lower_case(word_list):
    word_list_lower_case={}
    for k in word_list:
        word_list_lower_case[k.lower()] =word_list[k]
    return word_list_lower_case


# find function dictionery
def dictionery():
    
    # clear the terminal
    clear = lambda: system('cls')
    clear()
    
    # get the word
    word=input('What word do you looking for?!! (s:continue / e:exit):')
    words=word.split(' ')
    
    # get the all of the word that in the dictionery
    with open(r'./dictionery_storage.yaml',encoding="utf-8") as file:
        word_list=yaml.load(file, Loader=yaml.FullLoader)
        word_list_lowercase=word_list_lower_case(word_list)
        
    # looking for the word in dictionery_storage
    for word in words:
        if word.lower() in word_list_lowercase.keys():
            
            # add the wor that client is looking for
            client_words.append(word.lower() +" ") 
            
            # print the definition of word in persian
            reshaped_text_persian = arabic_reshaper.reshape(word_list_lowercase[word.lower()])
            persian_text = get_display(reshaped_text_persian)
            print("\n"+word+": "+persian_text)
        
        else:
            
            # call the intelligent function
            intelligent_word(word.lower())
            
            # notify the client that word is not in the dictionery
            print(colored(f'The word {repr(word)}  is not in the dictionery.\n','red'))
            dictionery_add(word)
            
    startgame()
    
# add function dictionery
def dictionery_add(word_not_found):
    
    # check for adding that word to dictioner or not
    check_statement=input(colored('Do you want to add that word to the dictionary?!! (yes / no)',"yellow"))
    if check_statement.lower() =='yes': 
        
        # question for defenition of that word
        mean_word_not_found=input('What is the mean of that word?!!')
        
        # open the dictionery
        with open(r'./dictionery_storage.yaml',encoding="utf-8") as file:
            word_list=yaml.load(file, Loader=yaml.FullLoader)
            word_list=word_list_lower_case(word_list)
        # add that word to dictionery
        dic=word_list
        dic[word_not_found]=mean_word_not_found
        with open(r'./dictionery_storage.yaml','w') as file:
            word_list=yaml.safe_dump(dic,file)

        # call dictionery function again
        dictionery()
    else:
        dictionery();
        

    
#farewell to the user
client_name=input(colored('What is your Fullname?',"magenta"))

# clear the terminal
clear = lambda: system('cls')
clear()

# say the tips
print(colored('Welcome to English to persian dictionary '+client_name,"blue"))
print(colored("\nTIP:\n1-If you want to continue in the program press s key, and if you want to exit the program enter the e\n2-If there is the word that it is not in the dictionery you can help us to add that word.\n3-The dictionery is not case sensetive.\n","yellow"))

# start the game
print(colored("When you are ready just press the s key.","green"))

def startgame():
    key_press=""
    key_press=keyboard.read_key()
    if(key_press=='s'): 
        dictionery()
    elif(key_press=='e'):    
        # clear the terminal
        clear = lambda: system('cls')
        clear()
        
        # thank to the client
        
        # remove the duplicate values from the list
        client_word=list(dict.fromkeys(client_words))
        practice_word=', '
        practice_word= practice_word.join(client_word)
        
        # print the words that client looking for
        print(colored("Thank you "+client_name+":)\n","cyan"))
        print(colored("practice "+practice_word+", I wish you learn it when you come back later :)","green"))

    else:
            if (key_press=='E' or key_press=='S'):
                # clear the terminal
                clear = lambda: system('cls')
                clear()

                # warn the client
                print(colored("Please turn off the CAPS LOCK and then press the key (s:continue / e:exit)","yellow"))
                startgame()
            else:
                startgame()
                
# intelligent word tip
def intelligent_word(word):
    
    # variables
    letters=''
    words_related=[]
    
    # get the all of the word that in the dictionery
    with open(r'./dictionery_storage.yaml',encoding="utf-8") as file:
        word_list=yaml.load(file, Loader=yaml.FullLoader)
        word_list_lowercase=word_list_lower_case(word_list)
        
    # itrate in word
    for letter in word:
        letters+=letter
        for word in word_list_lowercase.keys():
            if letters in word:
                words_related.append(word)
    print(colored("\nserach related: " +str((list(dict.fromkeys(words_related[len(words_related)-5:])))+(list(dict.fromkeys(words_related[0:5]))))+"\n","green"))
    
startgame()
