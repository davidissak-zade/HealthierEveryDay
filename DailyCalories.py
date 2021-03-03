def calculate_DCI(mass, height, age, gender, activeness):
    DCI = mass*10 + height * 6.25 - age * 5
    if gender == "female":
        DCI -= 161
    elif gender == "male":
        DCI += 5
    DCI * activeness
    return DCI


ActivenessLevelOptions = "  Type '1' if you are not/minimally physically active.  \n  Type '2' if you have 2-3 moderate workouts per week.  \n  Type '3' if you have 4-5 moderate workouts per week.  \n  Type '4' if you have about 5 intense workouts per week.  \n  Type '5' if you workout daily.  \n  Type '6' if you workout twice a day."


def GetActivenessLevel():
    print("Now, let's calculate your activeness level: ")
    print(ActivenessLevelOptions)
    option = int(input("Your option:  "))
    if option == 1:
        return 1.2
    if option == 2:
        return 1.38
    if option == 3:
        return 1.46
    if option == 4:
        return 1.55
    if option == 5:
        return 1.64
    if option == 6:
        return 1.73


def GetSuitableDCI(GoalToken, DCI):
    maintain = DCI
    lose = DCI * 4/5
    loseFast = DCI * 3/5
    bulk = DCI*6/5
    if GoalToken == 1:
        return maintain
    if GoalToken == 2:
        return lose
    if GoalToken == 3:
        return loseFast
    if GoalToken == 4:
        return bulk