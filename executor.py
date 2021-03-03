import spoonacular as sp
import json
from alrgorithms import my_capitalize
from plotting import plot_progress
import os
from DailyCalories import calculate_DCI, GetActivenessLevel, GetSuitableDCI

api = sp.API("b258f243a1ad4970a85446eaf0af6d87")
DIETS = ["Gluten Free", "Ketogenic", "Vegetarian", "Lacto-Vegetarian", "Ovo-Vegetarian", "Vegan", "Pescetarian", "Paleo", "Primal", "Whole30"]
REJECTED = ["No", "Nope", "None", "No, I don't", "no", "nope", "none"]

def login():
    usernameTC = input("Username:  ")   # username To Check
    passwordTC = input("Password:  ")   # password To Check
    with open('DB.json', 'r') as fp:
        Users = json.load(fp)
    for i in range(0, len(Users)):
        if Users[i]["username"] == usernameTC:
                if Users[i]["password"] == passwordTC:
                    print("Welcome Back, " + Users[i]["name"].capitalize() + "!")  # Now we need to access users username, password, and name by his index in the Users list
                    current_user_byIND = Users[i]
                    user = User(current_user_byIND["username"],
                                current_user_byIND["password"],
                                current_user_byIND["name"],
                                i)
                    return user

                else:
                    print("Incorrect password. Try again")
                    passwordTC_next = input("Enter password for username: " + Users[i]["username"] + ":  ")
                    while passwordTC_next != Users[i]["password"]:
                        passwordTC_next = input("Try again:  ")
                    print("Welcome Back, " + Users[i]["name"].capitalize() + "!")
                    current_user_byIND = Users[i]
                    user = User(current_user_byIND["username"],
                                current_user_byIND["password"],
                                current_user_byIND["name"],
                                i)
                    return user
    # We reach this line only if user did not succeed logging in
    print("There is no such user with this username, try again or log in first.")


def register():   # This func will add a new user to the network, it will gather his/her data to fill out the needed attributes of User class
    if os.stat("DB.json").st_size != 0:
        with open('DB.json', 'r') as fp:
            Users = json.load(fp)
    else:
        Users = []
    print("Hello, let's sign you up as our user. Fill out following lines.")
    username = input("Enter your preferred username: ")
    password = input("Enter your preferred password: ")
    name = input("What is your actual name:  ")
    IND = len(Users)   # !!! Here we check the length of the list Users, and

    print("Welcome, " + name.capitalize() + "!")
    print("Now, let me know about you a bit more, so that you will get personalized offers only!")
    current_height = int(input("What is your current height (in centimeters):  "))
    current_weight = int(input("What is your current mass (in kgs):  "))
    current_age = int(input("How old are you:  "))
    gender = input("Your Biological Gender:  ")
    if gender.capitalize() == "Male" or gender.capitalize() == "M":
        gender = "male"
    if gender.capitalize() == "Female" or gender.capitalize() == "F":
        gender = "female"
    current_BMI = current_weight / (current_height**2) * 10000
    current_BMI = round(current_BMI, 2)
    excludes = input("What food products do you NOT eat in general (due to allergies, or religious purposes): ").split(", ")
    activenessLevel = GetActivenessLevel()
    CN = calculate_DCI(mass=current_weight, height=current_height, age=current_age, gender=gender, activeness=activenessLevel)
    user = dict(username=username, password=password, name=name,
                weights=[current_weight], heights=[current_height], age=current_age, gender=gender,
                BMI_history=[current_BMI], excludes=excludes,
                search_history=[], CalorieNeeds=CN)
    Users.append(user)
    with open("DB.json", "w") as fp:
        json.dump(Users, fp, indent=2)
    new_user = User(username, password, name, IND)
    print("Welcome, " + name.capitalize() + "!")
    return new_user


class User:
    def __init__(self, username, password, name, userIND):
        self.username = username
        self.password = password
        self.name = name.capitalize()
        self.userIndex = userIND
        with open('DB.json', 'r') as fp:
            Users = json.load(fp)
        user = Users[self.userIndex]
        self.weights = user["weights"]  # Will be filled later
        self.heights = user["heights"]  # Will be filled later
        self.age = user["age"]
        self.gender = user["gender"]
        self.BMI_history = user["BMI_history"]  # Will be filled later
        self.excludes = user["excludes"]  # Will be filled later
        self.search_history = user["search_history"]  # Will be filled later
        self.DCI = user["CalorieNeeds"]

    def change_password(self):  # WORKS
        last_password = input("Enter your current password:  ")
        new_password = input("Enter new password:  ")
        if last_password != self.password:
            print("It seems like your previous password does not match with an actual one. Try again later.")
        else:
            self.password = last_password
            with open("DB.json", "r") as fp:
                Users = json.load(fp)
            current_user = Users[self.userIndex]
            current_user["password"] = new_password   # make a change in datafile as well
            with open("DB.json", "w") as fp:
                json.dump(Users, fp, indent=2)
            print("Password changed successfully!")
    # works 10/10

    def check_up(self):  # WORKS
        current_weight = float(input("Please, enter your current weight:  "))  # This will check up on current weight of the user. It saves the weight, and can project the trajectory of change in user's body
        ind = self.userIndex
        Last_Height = len(self.heights) - 1
        self.weights.append(current_weight)
        current_BMI = round((current_weight / self.heights[Last_Height]**2 * 10000), 2)
        self.BMI_history.append(current_BMI)
        with open("DB.json", "r") as fp:
            Users = json.load(fp)
        current_user = Users[self.userIndex]
        current_user["weights"] = self.weights  # Updating data
        current_user["BMI_history"] = self.BMI_history   # Updating data
        with open("DB.json", "w") as fp:
            json.dump(Users, fp, indent=2)
        print("Changes applied successfully!")
    # works 10/10

    def build_weekly_mealPlan(self):  # diet, exclude, targetCalories, timeframe
        diets = input("Do you have any diets you commit to:  ").split(", ")
        for diet in diets:
            if diet.capitalize() not in DIETS:
                diet = None
        goal = int(input(" Type 1 if you want to maintain your current weight \n Type 2 if you want to lose weight \n Type 3 if you want to lose weight fast \n Type 4 if you want to gain more weight (to gain muscle and not fat you will need to exercise more) \n Your response:  "))
        targetCalories = GetSuitableDCI(goal, self.DCI)
        timeFrame = input('Type "day" if you want to have DAILY meal plan \nType "week" if you want to have WEEKLY meal plan\n').lower()
        response = api.generate_meal_plan(diet=diets, exclude=self.excludes, targetCalories=targetCalories,
                                          timeFrame=timeFrame)
        data = response.json()

        meal_names = []
        meal_ids = []
        meals = [meal_names, meal_ids]
        if timeFrame == "day":
            for meal in data['meals']:
                meal_names.append(meal['title'])
                meal_ids.append(meal['id'])
            print("Here is your daily meal plan: \n  * BREAKFAST:  " + meal_names[0] + "  <Meal Code: 1> \n  * LUNCH:  " + meal_names[1] + "  <Meal Code: 2> \n  * DINNER:  " + meal_names[2] + "  <Meal Code: 3>")
            search_by_code = int(input("If you are not familiar with any meal in your plan, type its code, and I will give you its stats & recipe:  "))
            search_index = search_by_code - 1
            search_id = meal_ids[search_index]
            self.calculate_calories(includeRecipe=True, id_known=search_id, rank=True)

        if timeFrame == "week":
            day_counter = 0
            days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
            for i in range(0, len(data["items"])):
                current_meal = data["items"][i]["value"]
                parsedCurrent_meal = json.loads(current_meal)
                meal_names.append(parsedCurrent_meal["title"])
                meal_ids.append(parsedCurrent_meal["id"])

            print("Here is your personal weekly plan!")

            for i in range(0, 7):
                current_day = days[i]
                current_meal_index = i * 3
                current_meal_code = (i + 1) * 10
                print("Meal Plan for " + current_day + ":")
                print(" * BREAKFAST:  " + meal_names[current_meal_index] + " <Meal code: " + str(
                    current_meal_code + 1) + ">")
                print(" * LUNCH:  " + meal_names[current_meal_index + 1] + " <Meal code: " + str(
                    current_meal_code + 2) + ">")
                print(" * DINNER:  " + meal_names[current_meal_index + 2] + " <Meal code: " + str(
                    current_meal_code + 3) + ">")
            search_by_code = int(input("If you are not familiar with any meal in your plan, type its code, and I will give you its stats & recipe:  "))
            search_index = ((search_by_code // 10 - 1) * 3 + search_by_code % 10) - 1
            search_id = meal_ids[search_index]
            self.calculate_calories(includeRecipe=True, id_known=search_id, rank=True)
    # works works 8/10  add functionality to daily plan

    def calculate_calories(self, includeRecipe=True, id_known=0, rank=False):  # WORKS
        if id_known == 0:
            recipe = input(
                "Hello, I will calculate the amount of calories and nutrients in your meal! \n Type your meal: ")
            response = api.autocomplete_recipe_search(recipe)  # response is a list of all possible options that start with "recipe" string variable
            data = response.json()  # This translates data from web to txt, I guess
            names = []
            ids = []
            all_recipes = [names, ids]
            if len(data) == 0:
                print("I do not recognize this meal, was the spelling correct? ")
                data_2 = []
                while len(data_2) == 0:
                    recipe_2 = input("Type your meal again:  ")
                    response = api.autocomplete_recipe_search(recipe_2)  # response is a list of all possible options that start with "recipe" string variable
                    data_2 = response.json()  # This translates data from web to txt, I guess
                    names = []
                    ids = []
                data = data_2


            for part in data:
                all_recipes[0].append(part['title'])  # here we add all the meals' names so that we will be able to access them with their id
                all_recipes[1].append(part['id'])  # id's of all the options, we can access both name and id of the meal by the same id

            for i in range(0, len(all_recipes[0])):
                print("Type " + str(i + 1) + " if you want to have this meal: " + my_capitalize(
                    str(all_recipes[0][i])))
            option = input("Enter your chosen meal number: ")
            first_ans = data[int(option) - 1]  # Here we take the first value of the response, which is the closest recipe to the searched one
            firstAns_id = first_ans['id']  # Here we get the id number of the meal, so that we could use it to access info about this meal

        else:
            firstAns_id = id_known  # variable that stores the id that will be used to search any meal later is being filled with the known_id (in case that there is one)
        recipe_info = api.get_recipe_information(firstAns_id, includeNutrition=True)
        recipe_info = recipe_info.json()  # Translating the response of the API again

        nutrients = recipe_info["nutrition"]["nutrients"]
        recipe_name = recipe_info["title"]

        print("\nStats for " + recipe_name + ":")
        for section in nutrients:
            if section['name'] == "Calories":
                calories = section['amount']
                calories_unit = section['unit']

            if section['name'] == "Fat":
                fats = section['amount']
                fats_unit = section['unit']

            if section['name'] == "Protein":
                proteins = section['amount']
                proteins_unit = section['unit']

            if section['name'] == "Carbohydrates":
                carbs = section['amount']
                carbs_unit = section['unit']

        print("  * Total calories in this meal:  " + str(calories) + " (" + calories_unit + ")")
        print("  * Nutrients: \n            Proteins:  " + str(proteins) + " (" + proteins_unit + ") \n            Carbs:  " + str(carbs) + " (" + carbs_unit + ") \n            Fats:  " + str(fats) + " (" + fats_unit + ")")
        if not includeRecipe:
            txt_in = input("Do you want to also check out the step-by-step recipe of this meal:  ")
            if txt_in not in REJECTED:
                includeRecipe = True


        if includeRecipe:  # and len(recipe_info["analyzedInstructions"]) == 1:
            print("======================================================================================================================================================================================================================================================")
            if len(recipe_info["analyzedInstructions"]) != 0 and recipe_info["instructions"] is not None:
                print('Recipe for  "' + recipe_name + '" :')
                steps = recipe_info["analyzedInstructions"][0]["steps"]  # This list consists of all the steps that will guide. Each step is a dictionary, that has values "number", and "step": (NEEDED INFO) itself
                for step in steps:
                    print("Step #" + str(step["number"]) + " : " + step["step"])
            else:
                print("Unfortunately, here is no recipe for this meal yet. Stay tuned! : )")

        if rank:
            ranking = input("Where would you place this meal on a scale of 100:  ")
            if ranking.isdigit():
               ranking = int(ranking)
            else:
                ranking_2 = ''
                while not ranking_2.isdigit():
                    ranking_2 = input("Just type a number in range between 0 and 100:")
                ranking_2 = int(ranking_2)
                ranking = ranking_2

                # This is the part where we save the search info to search_history
                         # \|/
            with open("DB.json", "r") as fp:
                Users = json.load(fp)
            current_user = Users[self.userIndex]
            search_historyLen = len(current_user["search_history"])
            meal_searched = dict(item=search_historyLen + 1, value=recipe_name,
                                 id=firstAns_id, ranking=ranking)
            current_user["search_history"].append(meal_searched)

            with open("DB.json", "w") as fp:
                json.dump(Users, fp, indent=2)
            print("Changes applied successfully!")
    # works 10/10

    def refresh_data(self):
        with open("DB.json", "r") as fp:
            Users = json.load(fp)
        key = self.userIndex
        user_TS = Users[key]   # User to save
        self.username = user_TS["username"]
        self.password = user_TS["password"]
        self.name = user_TS["name"]
        self.weights = user_TS["weights"]
        self.heights = user_TS["heights"]
        self.BMI_history = user_TS["BMI_history"]
        self.excludes = user_TS["excludes"]
        self.search_history = user_TS["search_history"]  # Works
    # works 10/10

    def display_BMI_progress(self):
        
        token = 1
        token = self.userIndex
        plot_progress(token)
    # works 7/10

    def suggest_recipe(self):
        TOKEN = self.userIndex
        with open("DB.json", "r") as fp:
            data = json.load(fp)
        requests = data[TOKEN]["search_history"]
        highest_ranking = 0
        suggestId = 0
        suggestIndex = 0
        for i in range(len(requests)):
            if requests[i]["ranking"] > highest_ranking:
                highest_ranking = requests[i]["ranking"]
                suggestId = requests[i]["id"]
                suggestIndex = i
        response = api.get_similar_recipes(suggestId)
        meals = response.json()
        firstOption = meals[0]
        id = firstOption["id"]
        title = firstOption["title"]
        timeFrame = firstOption["readyInMinutes"]
        meal_chosen = data[TOKEN]["search_history"][suggestIndex]
        rankingTL = meal_chosen["ranking"]
        rankingTL -= 4
        with open("DB.json", "w") as fp:
            json.dump(data, fp, indent=2)
        print("Alright, so for today you will have:  " + title)
        print("It takes " + str(timeFrame) + " minutes to cook.")
        self.calculate_calories(id_known=id, rank=True, includeRecipe=True)


# This is the execution part


SessionOn = True
INSTRUCTIONS = 'Hello, there! Here are some instructions on how to call commands:  \n  - Type "search" to get stats about a meal.  \n  - Type "mealplan" to receive a personalized mealplan \n  - Type "checkup" if it is time for you to check up on your weight and let me know your progress  \n  - Type "displaybmi" to see your progress so far \n  - Type "suggest" and I will suggest you a meal based on your own taste! \n  - Type "exit" if you want to exit the program'
txt_in = input("Do you have an account:  ")
if txt_in in REJECTED:
    user = register()
else:
    user = login()

print(INSTRUCTIONS)
while SessionOn:
    command = input("Type command:  ")
    if command == "search":
        user.calculate_calories(rank=True)
    if command == "mealplan":
        user.build_weekly_mealPlan()
    if command == "checkup":
        user.check_up()
    if command == "displaybmi":
        user.display_BMI_progress()
    if command == "suggest":
        user.suggest_recipe()


    if command == "exit":
        user.refresh_data()
        SessionOn = False