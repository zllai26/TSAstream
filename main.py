'''
Code is made by zllai26
This is licensed with GNU GPL 3.0
'''
 
import matplotlib.pyplot as plt
 
comx = []
comy = []
perx = []
pery = []
classxmyp = ["Acacia", "Aster", "Begonia", "Castanea", "Juniper", "MYP Intensive"]
classymyp = [0] * len(classxmyp)
classxhs = ["Aspen", "Hickory", "Salix"]
classyhs = [0] * len(classxhs)
 
 
def marks(subject):
    while True:
        try:
            value = float(input(f"Enter your {subject} marks: "))
        except ValueError:
            print("You can only key in numbers and decimals. ")
            continue
 
        if 0 <= value <= 100:
            return value
        print("You can only give your marks in a range of 0 to 100 (0 <= value <= 100). ")
 
 
def classes():
    while True:
        try:
            classes_input = input("Are you from MYP or HS? ").strip().upper()
            if classes_input == "MYP":
                print(classxmyp)
                classesmyp = input("What class do you want to modify? ").strip()
                if classesmyp not in classxmyp:
                    print("That class doesn't exist. \n")
                    continue
                numbers = int(input("Enter how many person in it: "))
                if numbers < 0:
                    print("It can't be negative. \n")
                    continue
                idx = classxmyp.index(classesmyp)
                classymyp[idx] = numbers
                plt.figure()
                plt.bar(classxmyp, classymyp)
                plt.title("MYP class sizes")
                plt.xlabel("Class")
                plt.ylabel("Number of students")
                plt.savefig("tsastream-classes-myp.png")
                plt.show()
                print("result can be seen in tsastream-classes-myp.png")
                break
            elif classes_input == "HS":
                print(classxhs)
                classeshs = input("What class do you want to modify? ").strip()
                if classeshs not in classxhs:
                    print("That class doesn't exist. \n")
                    continue
                numbers = int(input("Enter how many person in it: "))
                if numbers < 0:
                    print("It can't be negative. \n")
                    continue
                idx = classxhs.index(classeshs)
                classyhs[idx] = numbers
                plt.figure()
                plt.bar(classxhs, classyhs)
                plt.title("HS class sizes")
                plt.xlabel("Class")
                plt.ylabel("Number of students")
                plt.savefig("tsastream-classes-hs.png")
                plt.show()
                print("result can be seen in tsastream-classes-hs.png")
                break
            else:
                print("Please type MYP or HS. \n")
                continue
        except ValueError:
            print("Only numbers boi. \n")
            continue
 
 
def comparestudents():
    perx.clear()
    pery.clear()
 
    print("You have to give 2 person's marks")
    print("This is the first one. ")
    math = marks("math")
    chem = marks("chemistry")
    phys = marks("physics")
    biol = marks("biology")
    geog = marks("geography")
    hist = marks("history")
 
    stream = ((math*0.55)+(chem*0.125)+(phys*0.125)+(biol*0.1)+(geog*0.05)+(hist*0.05))
    print(f"Your calculated streaming score is: {stream}")
 
    person = input("Give a person's name: ")
 
    perx.append(person)
    pery.append(stream)
 
    print("Now you have to give another person's marks")
 
    math = marks("math")
    chem = marks("chemistry")
    phys = marks("physics")
    biol = marks("biology")
    geog = marks("geography")
    hist = marks("history")
 
    stream = ((math*0.55)+(chem*0.125)+(phys*0.125)+(biol*0.1)+(geog*0.05)+(hist*0.05))
    print(f"Your calculated streaming score is: {stream}")
 
    person = input("Give a person's name: ")
 
    perx.append(person)
    pery.append(stream)
 
    plt.figure()
    plt.bar(perx, pery)
    plt.title("Streaming comparison")
    plt.xlabel("Student")
    plt.ylabel("Stream")
    plt.savefig("tsastream-comparestudents.png")
    plt.show()
    print("result can be seen in tsastream-comparestudents.png")
 
 
def comparemarks():
    comx.clear()
    comy.clear()
 
    print("You have to give your previous and your current marks")
    print("This is the first one. ")
    math = marks("math")
    chem = marks("chemistry")
    phys = marks("physics")
    biol = marks("biology")
    geog = marks("geography")
    hist = marks("history")
 
    stream = ((math*0.55)+(chem*0.125)+(phys*0.125)+(biol*0.1)+(geog*0.05)+(hist*0.05))
    print(f"Your calculated streaming score is: {stream}")
 
    year = input("Your year for the value: ")
 
    comx.append(year)
    comy.append(stream)
 
    print("This is the second one. ")
 
    math = marks("math")
    chem = marks("chemistry")
    phys = marks("physics")
    biol = marks("biology")
    geog = marks("geography")
    hist = marks("history")
 
    stream = ((math*0.55)+(chem*0.125)+(phys*0.125)+(biol*0.1)+(geog*0.05)+(hist*0.05))
    print(f"Your calculated streaming score is: {stream}")
 
    year = input("Your year for the value: ")
 
    comx.append(year)
    comy.append(stream)
 
    plt.figure()
    plt.bar(comx, comy)
    plt.title("Streaming by term/year")
    plt.xlabel("Year")
    plt.ylabel("Streaming")
    plt.savefig("tsastream-comparemarks.png")
    plt.show()
    print("result can be seen in tsastream-comparemarks.png")
 
 
while True:
    print("Welcome to TSAstream Official.")
    print("Now enter your marks")
    print("You have 4 Choices: ")
    print("1. Compare marks from term to term")
    print("2. Compare other person marks")
    print("3. Insert how many people went into each class")
    print("4. Exit")
 
    user = input("What do you want to choose? 1, 2, 3 or 4: ")
    match user:
        case "1":
            comparemarks()
        case "2":
            comparestudents()
        case "3":
            classes()
        case "4":
            break
        case _:
            print("Try again")
