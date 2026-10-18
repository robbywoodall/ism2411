# --- Reflection 1 ---
# The first bug I found was the missing colon on line 10. I did run the program first, but noticed it missing prior to running it. I think it just means I know what to look for in certain formats, but I still need work with other operators.
# --- Reflection 2 ---
# It will calculate the price of an item based on its price and what discount tier, if any, are applied. I think a colleague would be able to figure it out based on the names used.
# --- Reflection 3 ---
# AI was used to help understand what some of the error codes were given, but I feel that overall it is more of a shortcut with the size of the code we are dealing with. Most of the code written is pretty small and having AI look at larger blocks of code could be beneficial where they could easily be overlooked by the human eye.
# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")
# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    return price * (1-discount)
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")
# --- Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + tax:.2f}")
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')
# --- Exercise 4 --
orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")
# --- Exercise 6 ---
x = 100 # global variable
def double_it():
    x = 999 # local variable - different from global x!
    return x * 2
print(x)            #It should return 100 since it is outside the function.
print(double_it())  #This should return 1998 since it is using the local variable in the function.
print(x)            #I believe that if it asks for x now, it will be 1998 since x has now changed due to the function.
                    #I was correct, except for the last one. The global variable should remain constant unless changed globally.