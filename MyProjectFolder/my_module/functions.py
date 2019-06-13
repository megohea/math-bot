"""A collection of functions for doing my project."""

import string
import random
import nltk
import time


def is_question(input_string):
    
    """Checks if an input string is a question.
    
    Source: COGS 18 A3 Chatbot Assignment
    
    Parameters
    ----------
    input_string: string
        String that is being checked for question marks.
    
    Returns
    -------
    output: boolean
        Boolean that returns true if the string is a question, false otherwise.
    """
    
    
    
    output=None
    if "?" in input_string:
        output=True
    else:
        output=False
    return output

def remove_punctuation(input_string):
    
    """Removes the punctuation from a string.
    Source: COGS18 A3 Chatbot Assignment
    
    Parameters
    ----------
    input_string: string
        String that is examined and prepared for removing punctuation.
        
    Returns
    -------
    out_string: string
        String containing the content of input string without punctuation.
    """
    
    
    
    out_string=''
    for c in input_string:
        if c not in string.punctuation:
           out_string += c
    return out_string

def prepare_text(input_string):
    
    """Prepares a string for processing by removing punctuation and converting to lowercase.
    Source: COGS18 A3 Chatbot Assignment
    Parameters
    ----------
    input_string: string
        String to be processed and prepared for reading.
        
    Returns
    -------
    out_list: list
        A list formed from the string that has now been changed.
    """
    
    
    
    temp_string=input_string.lower()
    temp_string=remove_punctuation(temp_string)
    
    out_list=temp_string.split()
    
    return out_list

def selector(input_list,check_list,return_list):
    """Helps select a random option for output messages out of a pool of inputs.
    Source: COGS18 A3 Chatbot Assignment
    
    Parameters
    ----------
    input_list: list
        List of strings that is based on the user's input
    check_list: list
        List of string to compare with the input_list
    return_list: list
        List of string that has several possible messages.
        
    Returns
    -------
    output: string, or None
        String that has a random message from return_list, or is None
    
    """
    
    
    output=None
    
    for element in input_list:
        #check if items in input list shares common items with check list to choose a random message
        if element in check_list:
                output=random.choice(return_list)
                break
                
    return output

def list_to_string(input_list,separator):
    """Converts a list into a string.
    Source: COGS18 A3 Chatbot Assignment
    
    Parameters
    ----------
    input_list: list 
        List of string from input to be converted.
    separator: string
        String that will separate each element of the input list.
    
    Returns
    -------
    output: string
        String that is the result of the concatenation of the list items.
    """
    
    
    
    output=input_list[0]
    
    for element in input_list[1:]:
        output=string_concatenator(output,element,separator)
        
    return output
        
def end_chat(input_list):
    """Returns a true or false, depending of input indicating if user wants to 'quit' or not.
    Source: COGS18 A3 Chatbot Assignment
    
    Parameters
    ----------
    input_list: list
        List that checked for the word 'quit'
        
    Returns
    -------
    output: boolean
        Returns a boolean, True if 'quit' is found, False otherwise.
    """
    
    
    
    if 'quit' in input_list:
        return True
    else:
        return False
    
def is_in_list(list_one, list_two):
    """Checks if elements in one list are in another
    
    Source: COGS18 A3 Chatbot Assignment
    
    Parameters
    ----------
    list_one: list
        List that is to be compared with list_two for similarity
    list_two: list
        List that is compared with list one for similarity
        
    Returns
    -------
    boolean
        True is there are common elements, False otherwise
    
    """
    
    
    
    for element in list_one:
        #If elements in list_one are found in list_two, True is returned
        if element in list_two:
            return True
        
    return False
             
def assistance(input_list):
    """Returns True or False depending on if 'help' is in input
    
    Parameters
    ----------
    input_list: list
        List of string that is being checked for 'help'
        
    Returns
    -------
    boolean
        Returns True if 'help' is found, False otherwise.
    """
    
    
    
    if 'help' in input_list:
        return True
    else:
        return False
    
def is_add(input_list):
    """Returns True or False depending on if 'add' is in input
    
    Parameters
    ----------
    input_list: list
        List of string that is being checked for 'add'
        
    Returns
    -------
    boolean
        Returns True if 'add' is found, False otherwise.
    """
    
    
    
    output=None
    
    if 'add' in input_list:
        output=True
    else:
        output=False
        
    return output

def is_sub(input_list):
    """Returns True or False depending on if 'subtract' is in input
    
    Parameters
    ----------
    input_list: list
        List of string that is being checked for 'subtract'
        
    Returns
    -------
    boolean
        Returns True if 'subtract' is found, False otherwise.
    """
    
    
    
    output=None
    
    if 'subtract' in input_list:
        output=True
    else:
        output=False
        
    return output

def is_divide(input_list):
    """Returns True or False depending on if 'divide' is in input
    
    Parameters
    ----------
    input_list: list
        List of string that is being checked for 'divide'
        
    Returns
    -------
    boolean
        Returns True if 'divide' is found, False otherwise.
    """
    
    
    output=None
    
    if 'divide' in input_list:
        output=True
    else:
        output=False
        
    return output

def is_multiply(input_list):
    """Returns True or False depending on if 'multiply' is in input
    
    Parameters
    ----------
    input_list: list
        List of string that is being checked for 'multiply'
        
    Returns
    -------
    boolean
        Returns True if 'multiply' is found, False otherwise.
    """
    
    
    output=None
    
    if 'multiply' in input_list:
        output=True
    else:
        output=False
        
    return output

def input_number():
    """Takes a string input from user, rejecting it if it contains characters other than numbers.
       Converts a valid input into an integer.
    
    
    Returns
    -------
    value: integer
        Integer that has been derived from the user's valid string input.
    """
    
    
    
    value=input("USER: ")
    #list of digits being used to filter non-number characters
    digits=['1','2','3','4','5','6','7','8','9','0']
    num=False
    
    while num==False:
        #Reiterating over every character to find non-numeric items
        for chr in value:
            
            if chr not in digits:
                
                num=False
                print("MATHBOT: INVALID INPUT—— please enter a single number!")
                
                value=input("USER: ")
                #breaks out of for loop immediately if non-number is found, after taking a new input for value,
                break
                
            else:
                num=True  
                
    #value is converted into an integer for mathematical purposes            
    value=int(value)
    
    return value

def addition():
    """Adds together two inputs and returns the equation of the operation as a string
    
    
    Returns
    -------
    result: string
        String that displays which numbers were added and their solution
    """
    
    
    
    print("MATHBOT: Please type the first number you want to add!\n")
    #user is prompted to enter an input that is checked as a valid numeric answer
    num1=input_number()
    
    print("MATHBOT: Now, type the second number you want to add!\n")
    num2=input_number()
    
    answer=num1+num2
    
    #makes both inputs into strings to phrase into an answer
    problem=str(num1)+ ' + ' + str(num2) + ' = '
    result=problem +str(answer)
    
    return result

def subtract():
    """Subtract one input from another and returns the equation of the operation as a string
    
    
    Returns
    -------
    result: string
        String that displays which numbers were subtracted and their solution
    """
    
    
    
    print("SUBBOT: Please type the first number you want to subtract.\n")
    num1=input_number()
    
    print("MATHBOT: Now, type the second number you want to subtract from!\n")
    num2=input_number()
    
    answer=num1-num2
    
    problem=str(num1)+ ' - ' + str(num2) + ' = '
    result=problem +str(answer)
    
    return result

def divide():
    """Divides one input by another and returns the equation of the operation as a string
    
    
    Returns
    -------
    result: string
        String that displays which numbers were divided and their solution
    """
    
    
    
    print("MATHBOT: Please type the dividend.\n")
    num1=input_number()
    
    print("MATHBOT: Now, type the divisor!\n")
    num2=input_number()
    
    #float is used to account for uneven division
    answer=float(num1)/float(num2)
    
    problem=str(num1)+ '/' + str(num2) + ' = '
    result=problem +str(answer)
    
    return result

def multiply():
    """Multiplies one input by another and returns the equation of the operation as a string
    
    
    Returns
    -------
    result: string
        String that displays which numbers were multiplied and their solution
    """
    
    
    
    print("MATHBOT: Please type the first number to multiply.\n")
    num1=input_number()
    
    print("MATHBOT: Now, type the second multiplier!\n")
    num2=input_number()
    
    answer=num1*num2
    
    problem=str(num1)+ '*' + str(num2) + ' = '
    result=problem +str(answer)
    
    return result

#collection of inputs and outputs chatbot will read and respond to
#heavily modified from A3 Chatbot assignment

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hi, I'm Mathbot!",\
                 "What's up dude I'm Mathbot.",\
                 "Hey! Got any math questions?"]
    
DOGS_IN = ['dog', 'pitbull', 'shiba', 'pets',]
DOGS_OUT = ["I love pitbulls, did you know that?",\
               "Did you know pitbulls are the most caregiving dogs?",\
               "You should get a pitbull as a pet!"]

CALC_IN = ['derivative', 'integral', 'calculus', 'matrix', ]
CALC_OUT = ["Whoa! I can't handle that.", \
                "What are you even saying?", \
                "Yeah, I can't do calculus.", \
                "I failed calculus in mathbot school."]

UNKNOWN = ['So... when are you gonna do some math?', "Interesting.", "Strange.", "Alright."]

def math_chat():
    """Runs a chatbot that can undertake mathematical operations of addition, subtraction, division
       and multiplication.
       
       Heavily modified from source: A3 Chatbot assignment
    """
    
    
    
    print("MATHBOT: Hello! Please ask me a question about math")
    print('MATHBOT: Type "help" for a list of what I am capable of! ٩(◕‿◕｡)۶\n')
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('USER :\t')
        out_msg = None
        
        #string that will be used to help separate line of texts in the chatbox
        next_msg="\n *********************\nMathbot: What else would you like me to solve?"
        
        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg, closing the chat if found
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
        
        # Checks if user asks for help, displaying available commands
        if assistance(msg):
            out_msg = "Type 'ADD', 'SUBTRACT', 'MULTIPLY', or 'DIVIDE' to get started.\n Integers only please, I'm not good with decimals :("
        
        #checks if the message input from the user is a certain operation, and then performing it.
        if is_sub(msg):
            out_msg= subtract() + next_msg
        
        if is_add(msg):
            out_msg= addition() + next_msg
            
        if is_divide(msg):
            out_msg= divide() + next_msg
            
        if is_multiply(msg):
            out_msg= multiply() + next_msg
        
        
        # Check for a selection of topics that we have defined to respond to
        if not out_msg:

            # Initializing a list to hold possible outputs
            outs = []

            # Checks for greeting type inputs, responding with greetings as well
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
            
            # Checks for mentioning of dogs, responding with relevant messages
            outs.append(selector(msg, DOGS_IN, DOGS_OUT))
            
            # Checks for mentioning of calculus, responding with messages of incompetence
            outs.append(selector(msg,CALC_IN,CALC_OUT))
       
            # Removes any possible "None" outputs, and chooses a random option from the possible outputs.
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)
                
        # Message to display if no other input rules applied
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('MATHBOT:', out_msg)
        
               