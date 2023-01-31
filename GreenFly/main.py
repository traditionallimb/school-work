def main_menu():
    loopCtrl = 1
    print("\n\n==========GREENFLY SIMULATION==========")
    print("\n\t1. Set the Generation 0 values\n\t2. Display the Generation 0 values\n\t3. Run the model\n\t4. Export data\n\t5. Quit")

    while loopCtrl == 1:
        loopCtrl = 2
        userChoice = int(input("\nEnter a number > "))

        errorCheck = [userChoice >= 1,
                      userChoice <= 5,
                      type(userChoice) == int
                      ]

        if all(errorCheck): loopCtrl = 3
        else:
            print("That isn't a valid input, please try again.")
            loopCtrl = 1
    return userChoice


def set_values():
    def validation(prompt, validator):
        if validator == int:
            while True:
                try:
                    return validator(input(prompt))
                except ValueError:
                    print("\tInvalid value, please try again")
        if validator == float:
            while True:
                try:
                    val = validator(input(prompt))
                except ValueError:
                    print("\tInvalid value, please try again")
                finally:
                    if "birthrate" not in prompt:
                        if val > 1 or val < 0:
                            print("\tInvalid value, please try again")
                        elif 1 >= val >= 0:
                            return val
                    elif "birthrate" in prompt: return val

    juvenilePopulation = validation("Enter the population of the juvenile greenfly (1000s) > ", int)
    juvenileSurvivalRate = validation("Enter the survival rate of juvenile greenfly (decimal, 0-1) > ", float)
    adultPopulation = validation("Enter the population of the adult greenfly (1000s) > ", int)
    adultSurvivalRate = validation("Enter the survival rate of adult greenfly (decimal, 0-1) > ", float)
    senilePopulation = validation("Enter the population of the senile greenfly (1000s) > ", int)
    senileSurvivalRate = validation("Enter the survival rate of senile greenfly (decimal, 0-1) > ", float)
    birthRate = validation("Enter the birthrate of the greenfly > ", float)

    newGens = int(input("Enter the number of new generations to model (5-25) > "))

    with open("set_values.txt", "w") as f:
        f.write(f"{juvenilePopulation}\n{juvenileSurvivalRate}\n{adultPopulation}\n{adultSurvivalRate}\n{senilePopulation}\n{senileSurvivalRate}\n{birthRate}\n{newGens}")

    return juvenilePopulation, juvenileSurvivalRate, adultPopulation, adultSurvivalRate, senilePopulation, senileSurvivalRate, birthRate, newGens


def display_values():
    with open("set_values.txt", "r") as f:
        for i, line in enumerate(f):
            if i == 0: print(f"Juvenile Population: {line}")
            elif i == 1: print(f"Juvenile Survival Rate: {line}")
            elif i == 2: print(f"Adult Population: {line}")
            elif i == 3: print(f"Adult Survival Rate: {line}")
            elif i == 4: print(f"Senile Population: {line}")
            elif i == 5: print(f"Senile Survival Rate: {line}")
            elif i == 6: print(f"Birth rate: {line}")
            elif i == 7: print(f"New Generations: {line}")


def run_model():
    workingValues = []
    with open("set_values.txt", "r") as f:
      workingValues = [line.strip("\n") for line in f]
    print(workingValues)
    currentGen = 0
    while currentGen != workingValues[7]:
        print(f"Generation {currentGen}:\n")
        print(f"Juvenile Population: {workingValues[0]}")
        print(f"Adult Population: {workingValues[2]}")
        print(f"Senile Population: {workingValues[4]}\n\n")
        workingValues.pop(0)
        workingValues.insert(0, (workingValues))
        workingValues[1] = workingValues[]
        adultPopulation = juvenilePopulation * juvenileSurvivalRate
        senilePopulation = (senilePopulation * senileSurvivalRate) + (adultPopulation * adultSurvivalRate)
        currentGen += 1



loopCtrl = 1
while loopCtrl == 1:
    loopCtrl = 2
    menuChoice = main_menu()
    if menuChoice == 1:
        jupop, jusur, adpop, adsur, senpop, sensur, brate, newGens = set_values()
        loopCtrl = 1
    elif menuChoice == 2:
        display_values()
        loopCtrl = 1
    elif menuChoice == 3:
        run_model() #! "jupop is not defined"? check celebrity dogs program
        loopCtrl = 1
