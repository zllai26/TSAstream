'''
Code is made by zllai26
This is licensed with GNU GPL 3.0
'''



import matplotlib
import matplotlib.pyplot as plt
import numpy as np

comx = []
comy = []
perx = []
pery = []
classxmyp = ["Acacia", "Aster", "Begonia", "Castanea", "Juniper", "MYP Intensive"]
classymyp = [0] * len(classxmyp)
classxhs = ["Aspen", "Hickory", "Salix"]
classyhs = [0] * len(classxhs)

def classes():
    while True:
        try:
            classes_input = input("Are you from MYP or HS? ").strip().upper()
            if classes_input == "MYP":
                print(classxmyp)
                classesmyp = input("What class do you want to modify? ").strip()
                if classesmyp in classxmyp:
                    numbers = int(input("Enter how many person in it: "))
                    idx = classxmyp.index(classesmyp)
                    classymyp[idx] = numbers
                    plt.figure()
                    plt.bar(classxmyp, classymyp)
                    plt.savefig("tsastream-classes.png")
                    plt.show()
                    print("result can be seen in tsastream-classes.png")
                    break
            elif classes_input == "HS":
                print(classxhs)
                classeshs = input("What class do you want to modify? ").strip()
                if classeshs in classxhs:
                    numbers = int(input("Enter how many person in it: "))
                    idx = classxhs.index(classeshs)
                    classyhs[idx] = numbers
                    plt.figure()
                    plt.bar(classxhs, classyhs)
                    plt.savefig("tsastream-classes.png")
                    plt.show()
                    print("result can be seen in tsastream-classes.png")
                    break
            break
        except ValueError:
            print("Only numbers boi. \n")
            continue


def comparestudents():
    while True:
        try:
            math = float(input("Give me your math marks: "))
            if math > 100 or math < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            chem = float(input("Give me your chemistry marks: "))
            if chem > 100 or chem < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            phys = float(input("Give me your physics marks: "))
            if phys > 100 or phys < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            biol = float(input("Give me your biology marks: "))
            if biol > 100 or biol < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            geog = float(input("Give me your geography marks: "))
            if geog > 100 or geog < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            hist = float(input("Give me your history marks: "))
            if hist > 100 or hist < 0:
                print("Must be in range of 0 to 100 boi")
                continue

            stream = ((math*0.55)+(chem*0.125)+(phys*0.125)+(biol*0.1)+(geog*0.05)+(hist*0.05))
            print(f"Your calculated streaming score is: {stream}")

            person = input("Give a person's name: ")

            perx.append(person)
            pery.append(stream)

            plt.figure()
            plt.bar(perx, pery)
            plt.savefig("tsastream-comparestudents.png")
            plt.show()
            print("result can be seen in tsastream-comparestudents.png")
            
            break

        except ValueError:
            print("Only numbers boi.\n")
            continue


def comparemarks():
    while True:
        try:
            math = float(input("Give me your math marks: "))
            if math > 100 or math < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            chem = float(input("Give me your chemistry marks: "))
            if chem > 100 or chem < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            phys = float(input("Give me your physics marks: "))
            if phys > 100 or phys < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            biol = float(input("Give me your biology marks: "))
            if biol > 100 or biol < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            geog = float(input("Give me your geography marks: "))
            if geog > 100 or geog < 0:
                print("Must be in range of 0 to 100 boi")
                continue
                
            hist = float(input("Give me your history marks: "))
            if hist > 100 or hist < 0:
                print("Must be in range of 0 to 100 boi")
                continue

            stream = ((math*0.55)+(chem*0.125)+(phys*0.125)+(biol*0.1)+(geog*0.05)+(hist*0.05))
            print(f"Your calculated streaming score is: {stream}")

            year = int(input("What year: "))

            comx.append(year)
            comy.append(stream)

            plt.figure()
            plt.scatter(comx, comy, marker="o")
            plt.savefig("tsastream-comparemarks.png")
            plt.show()

            print("result can be seen in tsastream-comparemarks.png")
            
            break

        except ValueError:
            print("Only numbers boi.\n")
            continue


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
