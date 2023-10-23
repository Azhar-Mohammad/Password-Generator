import random
import string

if __name__ == "__main__":
    strUpper = string.ascii_uppercase    #Gives alphabets in uppercase     

    strLower = string.ascii_lowercase    #Gives alphabets in lowercase

    digit = string.digits                #Gives numbers

    punctuations = string.punctuation    #Gives special characters 

    # User inputs the length of the password
    passLen = int(input("Enter length of your password : "))

    empList = []

    empList.extend(list(strUpper))
    empList.extend(list(strLower))
    empList.extend(list(digit))
    empList.extend(list(punctuations))

    random.shuffle(empList)

    print("".join(empList[0 : passLen]))


    
