from users_input import user_information
from bmi_calculation import calculating_bmi
from bmi_category import find_category
from category_suggestion import give_suggestion
from display_result import results_display



print("                           BODY MASS INDEX CALCULATOR                            ")

ask= input("\n Do you want to calculate your BMI?:")

while True:  
    

    if ask.lower()=="yes":

      #MODULE 1:Getting the user's information
      NAME,AGE,HEIGHT,WEIGHT=user_information()

      #MODULE 2:Calculate the BMI
      final_BMI=calculating_bmi(WEIGHT,HEIGHT)

      #MODULE 3:Finding the BMI category
      category=find_category(final_BMI)

      #MODULE 4:Giving suggestions according to BMI category
      suggestion=give_suggestion(final_BMI)

      #MODULE 5:Displaying the BMI results
      results_display(NAME,AGE,HEIGHT,WEIGHT,final_BMI,category,suggestion)

      #If you want to calculate another BMI
      ask_again=input("\n Do you want to calculate your BMI?:")
      if ask_again.lower()!="yes":
          print("\n")
          print("THANK YOU. GOODBYE!")
          break 
    

    else:
        print("THANK YOU. GOODBYE!")
        break

