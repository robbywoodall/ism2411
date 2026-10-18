# --- Self-Assessment 1 ---
# Python will check the first if and recognize it as false and move to the next elif line. It will recognize it as true and apply the correct discount.
# --- Self-Assessment 2 ---
# The first code is flattened and it will check for them at the same time. The second is a nested if that has to check one line at a time. If the values are not put in the correct order, it could lead to a mess.
# --- Self-Assessment 3 ---
# I think when applying for college, a system like that could have been used to differentiate for students that qualify for USF based scholarships with qualifiers such as GPA and test scores. I like how Python can make these tasks quicker as long as the coding is done correctly.
# --- Exercise 1 ---
total = float(input("Enter Cart Total Here: $"))
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final Price: ${final:.2f}")
# --- Exercise 2 ---
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")
# --- Exercise 3 ---
region = str(input("Enter your region: "))
if region == "South":
    region_bonus = 0.02
    print("Region bonus applied: additional 2% off")
else:
    region_bonus = 0
final_discount = float(discount) + float(region_bonus)
final_price = total * (1 - final_discount)
print(f"Final Discount: {final_discount*100:.0f}%")
print(f"Final Price: ${final_price:.2f}")
# --- Exercise 4 ---
if total > 100:
    customer_type = "wholesale"
if region == "South" and total > 100 and customer_type == "wholesale":    # flat statements are easier to read since we are not tracking code across multiple lines. Having multiple nested if/elif/else can make problem solving more difficult than it needs to be.
    extra_discount = 0.03
# --- Exercise 5 ---
if total >= 10000:
    print("LARGE - REVIEW REQUIRED")
elif total <= 10000 and total >= 1:
    print("Normal")
elif total <= 0:
    print("SUSPICOUS")
# --- Exercise 6 ---
total_this_year = 3500
total_orders_placed = 19
has_outstanding_balance = False
if total_this_year > 2000 or total_orders_placed > 10 and not has_outstanding_balance:
    vip_status = "VIP Upgrade Eligible"
else:
    vip_status = "Standard Account"
