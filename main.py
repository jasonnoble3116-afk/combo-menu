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
        if choice == "no":
            print("proceed to checkout")
    else:
        print(f"Final total: ${Total_cost:.2f}")