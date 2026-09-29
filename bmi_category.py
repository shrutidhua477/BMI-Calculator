def find_category(final_BMI):
    
   if final_BMI<18.5:
            category= "UNDERWEIGHT"
            

   elif final_BMI>=18.5 and final_BMI<=24.9:
             category= "HEALTHY WEIGHT"
             

   elif final_BMI>=25 and final_BMI<=29.9:
             category= " OVERWEIGHT"
            

   elif final_BMI>=30:
             category= "OBESE"

   return category
             
