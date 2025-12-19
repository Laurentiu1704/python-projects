import math

print("""==================
Area Calculator 📐
==================\nChoose one of the shapes to calculate the area!\n""")

shape_choice = int(input("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n"))
print(f"Chosen shape: {shape_choice}")

if shape_choice == 1:
    base = int(input("Fill here your base value: "))
    height = int(input("Fill here your height value: "))
    area_triangle = (height * base) / 2
    print(f"Your triangle area radius in cm is: {area_triangle}")
    
elif shape_choice == 2:
    lenght = int(input("Fill here your length value: "))
    width = int(input("Fill here your width value: "))
    area_rectangle = lenght * width
    print(f"Your rectangle area radius in cm is: {area_rectangle}")  

elif shape_choice == 3:
    side = int(input("Fill here your side value: "))
    area_square = side ** 2
    print(f"Your square area radius in cm is: {area_square}")
    
elif shape_choice == 4:
    radius = int(input("Fill here your side value: "))
    area_circle = math.pi * radius ** 2
    print(f"Your circle area radius in cm is: {area_circle}")  
    
elif shape_choice == 5:
    print(f"Bye bye")

else:
    print("\nInvalid choice, try again!")