import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def ChefCook(ingredientList, number_of_days):
    ingredientsDaywise_dict = {}
    day = 1

    for ingredient in ingredientList:
        cat_list = []
        for c in ingredient:
            if c.isupper():
                cat_list.append(c)
        
        ingredientsDaywise_dict[day] = ''.join(cat_list[:-1])
        day += 1


    dishType_dict = {}
    ingredientType_dict = {}

    dishType_dict['X'] = [] 
    ingredientType_dict["FAT"] = 0
    ingredientType_dict["FIBER"] = 0
    ingredientType_dict["CARB"] = 0


    responseArr = []
    responseArr2 = []

    for k, v in ingredientsDaywise_dict.items():
        ingredientType_dict[v] += 1

        if (ingredientType_dict["CARB"] == 2 and ingredientType_dict["FIBER"] == 2):
            print("Y")
            responseArr.insert(k-1, "Y")
            responseArr2.append("Y")

            ingredientType_dict["CARB"] -= 2
            ingredientType_dict["FIBER"] -= 2

        elif (ingredientType_dict["CARB"] == 3 and ingredientType_dict["FIBER"] == 1):
            print("Y")
            responseArr.insert(k-1, "Y")
            responseArr2.append("Y")
            ingredientType_dict["CARB"] -= 3
            ingredientType_dict["FIBER"] -= 1

        elif (ingredientType_dict["CARB"] == 1 and ingredientType_dict["FIBER"] == 3) :
            print("Y")
            responseArr.insert(k-1, "Y")
            responseArr2.append("Y")
            ingredientType_dict["CARB"] -= 1
            ingredientType_dict["FIBER"] -= 3
        


        elif (ingredientType_dict["FAT"] == 3 and ingredientType_dict["FIBER"] == 1):
            print("X")
            responseArr.insert(k-1, "X")
            responseArr2.append("X")
            ingredientType_dict["FAT"] -= 3
            ingredientType_dict["FIBER"] -= 1

        elif (ingredientType_dict["FAT"] == 2 and ingredientType_dict["FIBER"] == 2):
            print("X")
            responseArr.insert(k-1, "X")
            responseArr2.append("X")

            ingredientType_dict["FAT"] -= 2
            ingredientType_dict["FIBER"] -= 2

        elif (ingredientType_dict["FAT"] == 4) :
            print("X")
            responseArr.insert(k-1, "Y")
            responseArr2.append("X")

            ingredientType_dict["FAT"] -= 4
        

        else:
            responseArr.insert(k-1, "-")
            responseArr2.append("-")

    
    print("".join(responseArr))


    



if __name__ == "__main__":

    """
    9
    FATOil FIBERSpinach CARBRice FATCheese FIBERBeans FATOlive CARBPotato FIBERBroccoli FIBERBanana
    """
    number_of_days = int(input())
    ingredientList = input().split()
    ChefCook(ingredientList, number_of_days)

