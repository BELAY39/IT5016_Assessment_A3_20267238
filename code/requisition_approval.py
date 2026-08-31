#Task 3, Requisition Approval
#Part:A,Python code file
#author:Belay Gebressilassie
#IT5016-Assessment2-part:A,(Student ID:20267238)
#Class:Software Development

#Task 1:Staff information
requisition_counter=10000
def staff_info():
    global requisition_counter

    date=input("Enter Date:")
    staff_id=input("Enter Staff ID:")
    staff_name=input("Enter Staff Name:")

    requisition_counter+=1
    requisition_id=requisition_counter
    return date,staff_id,staff_name,requisition_id

#Task 2:Calculate Requisition Total
def requisitions_total():
   date,staff_id,staff_name,requisition_id=staff_info()
   total=0
   item_name=input("Enter item name:")
   price=float(input("Enter price:$"))
   total=total+price
   item_name=input("Enter item name:")
   price=float(input("Enter price:$"))
   total=total+price
   item_name=input("Enter item name:")
   price=float(input("Enter price:$"))
   total=total+price
   return total,staff_id,requisition_id

#Task 3:Requisition Approval
def requisition_approval():
    total,staff_id,requisition_id=requisitions_total()
    
    status="pending"
    approval_reference="N/A"
    if  total<500:
        status="Approved"
        approval_reference=staff_id+str(requisition_id)[-3:]
    else:
        approval_reference="N/A"
    print("Total:$",total)
    print("Status:",status)
    print("Approval Reference Number:",approval_reference )


requisition_approval()
