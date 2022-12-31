# use of and operator in python using 
# a marksheet question here

english_score = int(input("English score? "))
science_score = int(input("Science score? "))
maths_score = int(input("Maths score? "))

if english_score > 9 and science_score > 90 and maths_score > 90:
    print("Well Done !!!")
else:
    print("You can do well")