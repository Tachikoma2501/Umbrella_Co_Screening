# Machine Learning Classifier
# While there are many different Classifiers
# Here we will use a decision tree classifier
# Any classifiers you pick, will still have the same
# type of I/O

#This will import the python time and system features
import time
import sys
#imports the sleep feature to slow down prints by 3 seconds
from time import sleep

#Imports the packages
from sklearn import tree
#defines answers as True
answer = True

print("""

        
       (.@%%%%%%%%%@.@       
     @....@%%%%%%%@....@     
   @......,@%%%%%@.......@.  
@,.........#&%%%&,.........(@
&%%%@&,.....%%%%%.....*@@%%%@
 %%%%%%%&@&..@%&.,&@&%%%%%%& 
 &%%%%%%%%%%%@@@%%%%%%%%%%%& 
 &%%%%%%&&%..@%&..#&&%%%%%%& 
&&&&&&,,,,,,%&&&&,,,,,,%&&&%&
&*,,,,,,,,,(&&&&&/,,,,,,,,,,&
   &,,,,,,,&&&&&&&*,,,,,,&   
     &,,,,&&&&&&&&&,,,,%     
       %,&&&&&&&&&&&,%    

""")

print('Welcome to the Umbrella Corporation subject screening process')
print('Here we will determine a subjects registered tag, whether they are currently infected')
print('and the category of virus they currently contain')
print(' ')
sleep(3)
print('Please note: all subjects, infected or otherwise, will be subject to disposal, quarantine,')
print('or any other forms of biohazard control procedures')
print('This is to prevent any infectious or hazardous material from leaving this facility')
print(' ')
sleep(3)
print('Please log in to start screening procedure')
print(' ')
sleep(3)
user_name = input('Enter Last Name: ')
print('')
print('Welcome Dr.', user_name)
print(' ')
sleep(2)
#While loop to create menu for user
while answer:
    print("""
    1. Review Subject Files
    2. Check Email (1 New Message)
    3. Start Screening Process
    4. Exit
    """)
    #if statement for if the user inputs 1 to list current test subjects
    answer=input('Enter Option: ')
    if answer == '1':
        print(' ')
        Lisa_Trevor = print('Title: Lisa Trevor, Infection Status: Positive, Virus Type: G')
        Tyrant = print('Title: T-002, Infection Status: Positive, Virus Type: T')
        Cerberus = print('Title: Cerberus, Infection Status: Positive, Virus Type: T')
        Alfred_Ashford = print('Title: Alfred Ashford, Infection Status: Negative, Virus Type: N/A')
        Curtis_Miller = print('Title: Curtis Miller, Infection Status: Positive, Virus Type: G')
        Brad_Vickers = print('Title: Brad Vickers, Infection Status: Negative, Virus Type: N/A')

    # if statement for if the user inputs 2 to list current test subjects
    elif answer == '2':
        print(' ')
        print('To Dr.',user_name)
        print(' ')
        print('Please get todays screening done by 5:00pm this afternoon.')
        print('Dr. William Birkin is doing a presentation to the higher ups')
        print('this evening and needs the material for it by then.')
        print('You know how agitated he can get when everything isnt done')
        print('on schedule, especially when it involves his precious G-Virus research.')
        print('But I trust you will get it done long before then.')
        print(' ')
        print('From')
        print(' ')
        print('Dr. Wayne Li')
    # if statement for if the user inputs 3 to list current test subjects
    elif answer == '3':
        print('Please begin the scanning procedure')

        # Syntax for the 3 features
        # Features = Age, Infection Status, and Virus
        features = [[44, 40, 37], [60, 200, 70], [5, 15, 10], [25, 0, 0],[35, 100, 50], [36, 0, 0]]
        # Labeled training data
        labels = ['Lisa Trevor', 'Tyrant', 'Cerberus', 'Alfred Ashford', 'Curtis Miller', 'Brad Vickers']

        # Now lets create our Classifier which is a decision tree
        clf = tree.DecisionTreeClassifier()

        # Do the actual training (Machine Learning) Here
        # first is finding the patterns in the data
        clf = clf.fit(features, labels)

        # Put in unknown data
        # age, Infection Status, Virus Type
        # Prediction will be for Tyrant
        print(clf.predict([[60, 60, 30]]))

        # age, Infection Status, Virus Type
        # I predict this will be Lisa Trevor
        print(clf.predict([[90, 150, 55]]))

        # age, Infection Status, Virus Type
        # I predict this will be Lisa Trevor
        print(clf.predict([[10, 20, 15]]))

        # age, Infection Status, Virus Type
        # I predict this will be Lisa Trevor
        print(clf.predict([[25, 0, 3]]))

        # age, Infection Status, Virus Type
        # I predict this will be Lisa Trevor
        print(clf.predict([[31, 120, 41]]))

        # age, Infection Status, Virus Type
        # I predict this will be Lisa Trevor
        print(clf.predict([[43, 0, 1]]))

    #elif statement to end the program
    elif answer == '4':
        break