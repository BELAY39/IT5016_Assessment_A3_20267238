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

