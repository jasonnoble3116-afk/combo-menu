# Iteration 1
Total_cost = 0
choice = input("what kind of taco would you like? chicken $5.25, fish $5.75, steak $6.25").strip().lower()
if choice == "steak":
    print("Steak $6.25")
    Total_cost += 6.25
elif choice == "chicken":
    print("chicken $5.25")
    Total_cost += 5.25
elif choice == "fish":
    print("fish $5.75")
    Total_cost += 5.75
choice=input("what type of shell would you like? hard or soft?").strip()
if choice=="hard":
    print("hard shell")
elif choice=="soft":
    print("soft shell")
choice = input("how many tacos would you like? one, two $0.50, three $1.00, four $1.50, five $2.00, six $2.50").strip()
if choice == "one":
    print("one taco")
elif choice == "two":
    print("two tacos $0.50")
    Total_cost += 0.50
elif choice == "three":
    print("three tacos $1.00")
    Total_cost += 1.00
elif choice == "four":
    print("four tacos $1.50")
    Total_cost += 1.50
elif choice == "five":
    print("five tacos $2.00")
    Total_cost += 2.00
elif choice == "six":
    print("six tacos $2.50")
    Total_cost += 2.50

# Iteration 2
choice = input("would you like a beverage?").strip().lower()
if choice == "yes":
    choice = input("what size beverage would you like?").strip().lower()
    if choice == "medium":
        print("medium $1.75")
        Total_cost += 1.75
    elif choice == "small":
        print("small $1.00")
        Total_cost += 1.00
    elif choice == "large":
        print("large $2.25")
        Total_cost += 2.25
if choice == "no":
    print("no beverage")
choice = input("what type of beverage would you like? sode, sweet tea, or water?")
if choice == "soda":
    print("soda")
elif choice == "sweet tea":
    print("sweet tea")
elif choice == "water":
    print("water")

# Iteration 3
choice = input("would you like a bag of chips?").strip().lower()
if choice == "yes":
    choice = input("what size bag of chips would you like?").strip().lower()
    if choice == "medium":
        print("medium $1.50")
        Total_cost += 1.50
    elif choice == "small":
        print("small $1.00")
        Total_cost += 1.00
    elif choice == "large":
        print("large $2.00")
        Total_cost += 2.00

#Iteration 4
choice = input("would you like any sauces for you tacos?").strip().lower()
if choice == "yes":
    choice = input("what sauce would you like? buffalo sauce packets, salsa $0.25, guacamole $0.25, melted cheese $0.50").strip().lower()
    if choice == "buffalo sauce":
        print("buffalo sauce")
    elif choice == "salsa":
        print("salsa")
        Total_cost += 0.25
    elif choice == "guacamole":
        print("guacamole")
        Total_cost += 0.25
    elif choice == "melted cheese":
        print("melted cheese")
        Total_cost += 0.50
    sauce_packets = int(input("how many sauce packets would you like?").strip())
    Total_cost += sauce_packets * 0.25

# final checkout prompts
choice = input("are you ready for checkout?").strip().lower()
if choice == "yes":
    print("all choices and total amount")
    print(f"Total cost: ${Total_cost:.2f}")
elif choice == "no":
    choice = input("would you like anything else?").strip().lower()
    if choice == "yes":
        choice = input("Would you like to MegaSize your order?").strip().lower()
        if choice == "yes":
            print("large beverage $2.25 and large bag of chips $2.00")
            Total_cost += 2.25 + 2.00
            print(f"Final total: ${Total_cost:.2f}")
        if choice == "no":
            print(f"Final total: ${Total_cost:.2f}")
    else:
        print(f"Final total: ${Total_cost:.2f}")