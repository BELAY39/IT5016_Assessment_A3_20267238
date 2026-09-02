#Global counter used to generate a unique requisition ID
#Assessment 3,programming principles and concepts
#author:Belay Gebressilassie
#IT5016-Assessment 3,(Student ID:20267238)
#Class:Software Development

#unique requisition ID starts from 10000
requisition_counter=10000
def staff_info():
    #use the global counter to create a unique requisition ID for each requisition
    global requisition_counter

    #collect staff information from the user
    date=input("Enter Date:")
    staff_id=input("Enter Staff ID:")
    staff_name=input("Enter Staff Name:")

    #Increase the counter by 1 for each new requisition
    requisition_counter+=1
    requisition_id=requisition_counter

    #Return the collected information so other function can use it
    return date,staff_id,staff_name,requisition_id



