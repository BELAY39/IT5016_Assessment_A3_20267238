#Assessment 3,programming principles and concepts
#author:Belay Gebressilassie
#IT5016-Assessment 3,(Student ID:20267238)
#Class:Software Development

#Global counter used to generate a unique requisition Id
#Task 1:collect Staff information
requisition_counter=10000
def staff_info():
    #Use the global counter so the requisition ID increases each time
    global requisition_counter

   #Collect staff information from the user
    date=input("Enter Date:")
    staff_id=input("Enter Staff ID:")
    staff_name=input("Enter Staff Name:")

   #Increase the counter to create a new requisition ID
    requisition_counter+=1
    requisition_id=requisition_counter

    #Return all staff information for use by other functions
    return date,staff_id,staff_name,requisition_id

