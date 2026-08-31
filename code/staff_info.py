#Task 1
#Part:A,Python code file
#author:Belay Gebressilassie
#IT5016-Assessment2-part:A,(Student ID:20267238)
#Class:Software Development

#task 1:Staff information
requisition_counter=10000
def staff_info():
    global requisition_counter

    date=input("Enter Date:")
    staff_id=input("Enter Staff ID:")
    staff_name=input("Enter Staff Name:")

    requisition_counter+=1
    requisition_id=requisition_counter
    return date,staff_id,staff_name,requisition_id

# call the function
date,staff_id,staff_name,requisition_id=staff_info()

print("\nPrinting Requisions:")
print("Date:",date)
print("Staff ID:",staff_id)
print("Staff Name",staff_name)
print("Requisition ID:",requisition_id)


