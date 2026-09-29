def give_suggestion(final_BMI):

    if final_BMI<18.5:
         suggestion= "Eat nutrient-dense foods and do strength training to build muscels."

    elif final_BMI>=18.5 and final_BMI<=24.9:
         suggestion= "Keep up a balanced diet and regular weekly exercise."

    elif final_BMI>=25 and final_BMI<=29.9:
         suggestion= " Practice portion control and increase daily movement to drop weight."

    elif final_BMI>=30:
         suggestion= "Work with a doctor on a safe,sustainable health plan."

    return suggestion
        
    


    
