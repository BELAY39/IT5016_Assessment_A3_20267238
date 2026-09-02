
#Assessment 3,programming principles and concepts
#author:Belay Gebressilassie
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



#Task 3:Requisition Approval
def requisition_approval(staff_id,requisition_id,total):
    #set the default status to pending
    status="pending"

    #Start with an empty approval reference number
    approval_reference_number="N/A"

    #Approve the requisition if the total is less than $500
    if  total<500:
        status="Approved"

        #Creat the approval reference number
        approval_reference_number=staff_id+str(requisition_id)[-3:]

        #Display the total and approval information
    else:
        approval_reference_number="N/A"
    print("Total:$",total)
    print("Status:",status)
    print("Approval Reference Number:",approval_reference_number)

#Task 4:The function displays all the requisition information.
def display_requisitions(date,staff_id,staff_name,requisition_id,total,status,approval_reference_number):

    #display the heading
    print("\nPrinting Requisions:")
    #Display the requisition date
    print("Date:",date)
    #Display the requisition ID
    print("Requisition ID:",requisition_id)
    #Display the staff information
    print("Staff ID:",staff_id)
    #Display the staff name
    print("Staff Name:",staff_name)
    #Display the total cost 
    print("Total:$",total)
    #Display the approval status
    print("Status:",status)
    #Display the approval reference number
    print("Approval Reference Number:",approval_reference_number)
    


