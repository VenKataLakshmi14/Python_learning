age = int(input("Enter your age: "))
experience = int(input("Enter your years of work experience: "))

if age >= 18 and experience >= 2:
    print("You are eligible for the job based on age and experience.")
elif age >= 25 or experience > 5:
    print("You are eligible for the job based on age or experience.")
else:
    print("You are not eligible for the job.") 
