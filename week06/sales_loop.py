# --- Reflection 1 ---
# The accumulator pattern starts to give you a place to sort variables that you are going to adding items (accumulating) whose numbers may increase or decrease based on your code.
# The first step is to initialize the item or variable to whatever your starting total is. We used the number 0 for the exercises in this lesson.
# The second step is to loop through the data. This will act like a conveyor belt and take your data through the loop.
# The third step is to update your accumulator. You do something with the accumulator (update counts) and it will get a new result.
# --- Reflection 2 ---
# The while loop took extra lines of code to do the same thing. The for loop was easier to follow and track what was going to happen.
# --- Reflection 3 ---
# The only data sets that I could look at would be my watch counts and view times on YouTube. I could use the information to see how subscribers are reacting to the content I produce.
# The data could be printed out by video to see which ones got the most watches and how much time was spent watching (was it engaging?).
# --- Exercise 1 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
count = 0
current_max = sales[0]
big_sales_count = 0
big_sales_total = 0
for sale in sales:
    total += sale   # update
    count += 1
    if sale > current_max:
        current_max = sale
    if sale > 100:
        big_sales_total += sale
        big_sales_count += 1
print(f"Total: ${total}")
# --- Exercise 2 ---
average = total / count
print(f"Count: {count}")
print(f"Average: ${average:.2f}")
# --- Exercise 3 ---
print(f"Largest Sale: ${current_max}")
# --- Exercise 4 ---
print(f"Sales over $100: {big_sales_count}")
print(f"Total of those sales: ${big_sales_total}")
# --- Exercise 5 ---
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")
# --- Exercise 6 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0            
while i < len(sales):   # The code is cleaner using for as the loop mechanism. It make it easier to read and has less chance of accidently going in to an infinite loop.
    total += sales[i]  
    i += 1             
print(f"Total: ${total}")
# --- Exercise 7 ---
for sale in sales:
    if sale >= 200:
        discount_rate = 0.10
        discount_text = "10%"
    elif sale >= 100:
        discount_rate = 0.05
        discount_text = "5%"
    else:
        discount_rate = 0.00
        discount_text = "0%"
    discounted_price = sale * (1 - discount_rate)
    print(f"${sale:<3} → {discount_text} discount → ${discounted_price:.2f}")