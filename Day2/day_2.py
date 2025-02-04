#Day 2. Creating tip calculator with taking percentage of bill
print("Welcome to the Tip Calculator")
bill = float(input("How much is the total bill? "))
tip = int(input("What percentage tip whould you like to give? "))
people = int(input("How many people split the bill? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: {final_amount}")
