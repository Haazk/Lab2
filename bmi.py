def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/(height*height)
    print("bmi is"+str(bmi))
    if bmi<18.5:
        return -1
    elif bmi>=18.5 and bmi<=25.0:
        return 0
    elif bmi>25.0:
        return 1
bmiresults=calculate_bmi(weight=57, height=1.73)
    
if bmiresults==-1:
    print("underweight")
elif bmiresults==0:
    print("normal weight")
elif bmiresults==1:
    print("overweight")