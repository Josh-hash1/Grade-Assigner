def Hash(score):
    if score < 0:
        print("Invalid score! Please enter a value between 0 and 100.")
         
    elif score <= 60:
        print("Grade: F!")        
    elif score <= 69:
        print("Grade: D!")        
    elif score <= 79:
        print("Grade: C!")        
    elif score <= 89:
        print("Grade: B!")        
    elif score <= 100:
        print("Grade: A!")
    else: 
        print("Failed.")
       
print("Grade Assigner")

while True:
    try:
        josh = input("State you Grade: ")
        Hash(int(josh))        
    except ValueError:
        print("Invalid score! Please enter a value between 0 and 100!")
        break
