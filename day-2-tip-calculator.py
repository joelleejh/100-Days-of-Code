total_bill = input("Welcome to the tip calculator.\nWhat was the total bill?")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?")
split_by = input("How many people to split the bill?")

each_bill = "{:.2f}".format((float(total_bill)*(1+float(percentage_tip)/100)/int(split_by)))

print("Each person should pay: $" + str(each_bill))