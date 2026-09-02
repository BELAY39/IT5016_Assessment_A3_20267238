#Task 2, Requisition Total
#Assessment 3,programming principles and concepts
#a#uthor:Belay Gebressilassie
#IT5016-Assessment 3,(Student ID:20267238)
#Class:Software Development

#Task 1:collect Staff information
requisition_counter=10000
def staff_info():
    global requisition_counter

   #ask the user to enter staff details
    date=input("Enter Date:")
    staff_id=input("Enter Staff ID:")
    staff_name=input("Enter Staff Name:")

   #Generate a unique requisition ID  
    requisition_counter+=1
    requisition_id=requisition_counter

    #return the staff information and requisition ID
    return date,staff_id,staff_name,requisition_id

#Task 2:Calculate the total cost of requisition items
def requisitions_total():

   #Get staff information from task1
   date,staff_id,staff_name,requisition_id=staff_info()

   #start with total at zero
   total=0

   #Enter the first itm and its price
   item_name=input("Enter item name:")
   price=float(input("Enter price:$"))
   total=total+price

    #Enter the second item and  its price
   item_name=input("Enter item name:")
   price=float(input("Enter price:$"))
   total=total+price

    #Enter the third item and  its price
   item_name=input("Enter item name:")
   price=float(input("Enter price:$"))
   total=total+price

   #return the staff details and calculated total
   return date,staff_id,staff_name,requisition_id,total

