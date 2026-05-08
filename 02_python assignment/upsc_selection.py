# 01. UPSC Selection Process

age=int(input("Enter your age :- "))

if(21<=age<=32):
    grad=int(input("Are you graduate 1- yes 2- no"))
    if(grad==1):
        nat=int(input("Are you indian 1-yes 2-no"))
        if(nat==1):
            print("you are elegible to prelims")
            pre=int(input("Enter your prelims score"))
            if(pre>=90):
                print("you are eligible for mains")
                main=int(input("Enter your mains score"))
                if(main>=1200):
                    print("you are invited for interview")
                    interview=int(input("Enter interview score"))
                    if(interview>=1800):
                        print("congratuation!you have cleared upsc")
                    else:
                        print("you havn't cleared interview")
                else:
                    print("sorry you have cleared mains")
            else:
                print("you havn't cleared the cutoff")
        else:
            print("you are not elegible")
    else:
        print("you are not elegible")
else:
     print("Are you not elegible")