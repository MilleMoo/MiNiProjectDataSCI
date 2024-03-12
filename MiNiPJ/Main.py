userinput1 = int(input("Do you use iPad or Tablet \n"
                        "1.)iPad \n"
                        "2.)Tablet \n3.)Not Have\nplease input number : "));
# Do you use iPad or Tablet
if userinput1 == 1: 
    userinput1 = int(input("\nDo you change phone often \n"
                        "1.)often \n"
                        "2.) not \nplease input number : "));
    # Do you change phone often
    if userinput1 == 2 : 
        userinput1 = int(input("\nDo you prefer installments or paying cash \n"
                        "1.)pay off \n"
                        "2.) cash \nplease input number : "));
        # Do you prefer installments or paying cash
        if userinput1 == 1 : 
            userinput1 = int(input("\nDo you like zoom camera \n"
                        "1.)like \n"
                        "2.) not \nplease input number : "));
            # Do you like zoom camera
            if userinput1 == 1 : print("\nYou use Android\n")
            elif userinput1 == 2 : 
                userinput1 = int(input("\nDo you like to use brandname or not \n"
                        "1.)like \n"
                        "2.) not \nplease input number : "));
                # Do you like to use brandname or not
                if userinput1 == 2 : print("\nYou use Android\n")
                elif userinput1 == 1: print("\nYou use IOS\n") 
                else : print("error")
        elif userinput1 == 2: 
            print("\nYou use IOS\n") 
    # Do you change phone often
    elif userinput1 == 1: 
        userinput1 = int(input("\nDo you like zoom camera \n"
                        "1.)like \n"
                        "2.) not \nplease input number : "));
        if userinput1 == 1: 
            print("\nYou use IOS\n") 
        elif userinput1 == 2:
            print("\nYou use Android\n")
        else: print("error")
    else : print("error")
# Do you use iPad or Tablet
elif userinput1 == 2 : print("\nYou use Android\n") 
# Do you use iPad or Tablet
elif userinput1 == 3 : 
    userinput1 = int(input("\nDo you change phone often \n"
                        "1.)often \n"
                        "2.) not \nplease input number : "));
    # Do you change phone often
    if userinput1 == 2 : 
        print("\nYou use Android\n")
    elif userinput1 == 1:
        print("\nYou use IOS\n")
    else : print("error")
# Do you use iPad or Tablet
else: print("ERROR")


