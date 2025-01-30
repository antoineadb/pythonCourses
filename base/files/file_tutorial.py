
# students_list = ["Paul","Louis", "Mathieu", "Edouard","Laurent", "Maxime"]
#
# with open("student.txt","w+") as file:
#     for student in students_list:
#         file.write(student + "\n")
#     file.close()
import os
import random
import shutil

if os.path.exists("meals.txt"):
    with open("meals.txt", "r+") as file:
        meals_list = file.readlines()
        meal_random_choice =  random.choice(meals_list)
        print("Je vous propose aujourd'hui, le repas " + meal_random_choice)
        file.close()
else:
    print("Le document n'existe pas ! attention!")


source = "logo.ico"
target = "images/logo.ico"
shutil.copy(source,target)
os.remove(source)
