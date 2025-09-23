#tip calculator
print("welcome to tip calculator")
total_bill=float(input("Enter the total amount: "))
service_rate=input("Did you like the service(Yes/No) :")
if service_rate=="yes":
    tip_percentage=float(input("Enter the tip % (10,15,20): "))
    tip_amount=(total_bill*tip_percentage)/100
else:
    print("Since you didn't like the service there will be no tip added.")
    tip_amount=0
final_amount=total_bill+tip_amount
total_members=int(input("Enter number of people u would like to split the bill with: "))
print(f"Amount per person : {final_amount/total_members:}")