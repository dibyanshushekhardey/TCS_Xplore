age=15
status='minor' if age < 18 else 'adult'
sunny=False
print("Let's go to the", 'beach' if sunny else 'room')
humidity=76.8
setting = 25 if humidity > 75 else 28

# nesting the conditional expressions
# assigns Prim
wt=55
msg='Obese' if wt > 85 else 'Hefty' if wt > 60 else 'Prim'
print(msg)