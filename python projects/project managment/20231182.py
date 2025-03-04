#defining the lists
ongoing_projects=[]
client=[]
start=[]
end=[]
workersassigned=[]
stats=[]
completed_projects=[]
client2=[]
start2=[]
end2=[]
workersassigned2=[]
stats2=[]
actualend2=[]
onhold_projects=[]
onholdclient=[]
onholdstart=[]
onholdend=[]
onholdstats=[]
onholdworkersassigned=[]
workerstot=int(input('before the program should start running enter the total number of workers the company has'))
available_workers=workerstot
main_menu_input=0
taken_workers=0
#creat a while loop for the whole program to run until the user exsists
while(main_menu_input!=6):
    print('XYZ Company-main menu')
    main_menu=['1. Add a new project to existing projects.','2. Remove a completed project from existing projects.','3. Add new workers to available workers group.','4. Update details on ongoing projects',
'5. Project Statistics','6. Exit']
    for i in range (len(main_menu)):
        print(main_menu[i])
    main_menu_input=int(input('enter your choice'))
    #putting main menue option in if elife else condition to choose depending on user inputs
    if(main_menu_input==1):
        print('XYZ Company')
        print('Add a new project.')
        print('** Enter ‘0’ to Project Code to exit.')
        add_project_menu=['Project Code-','Clients Name -','Start date -','Expected end date -','Number of workers -','Project status -','Do you want to save the project (Yes/No)?']
        project_code=int(input(add_project_menu[0]))
        if(project_code!=0):#diving condition to rerun the program if input is zero
            client_name=str(input(add_project_menu[1])) #taking inputs for the main menue                
            start_date=str(input(add_project_menu[2]))
            expected_date=str(input(add_project_menu[3]))
            workers_no=int(input(add_project_menu[4]))
            project_status=str(input(add_project_menu[5]))
            save_project=str(input(add_project_menu[6]))
            if(save_project=='yes'):#giving condition to exit if user inputs no
                    if(workers_no<=available_workers):#checking if the number of workers are available,if workers are avilable the data will be added to ongoing list
                        ongoing_projects.append(project_code)
                        client.append(client_name)
                        start.append(start_date)
                        end.append(expected_date)
                        stats.append(project_status)
                        workersassigned.append(workers_no)
                        taken_workers=workers_no
                        available_workers=available_workers-taken_workers
                    else:
                        print('!!!')#display that workers are not available then add data into hold list
                        print('the needed amount of workers are not avaiable to carry out this project there for the project will be added to the onhold_list')
                        onhold_projects.append(project_code)
                        onholdclient.append(client_name)
                        onholdstart.append(start_date)
                        onholdend.append(expected_date)
                        onholdstats.append(project_status)
                        onholdworkersassigned.append(workers_no)
    elif(main_menu_input==2):
        print('XYZ Company')#display menu 2
        print('Remove Completed Project')
        remove_menu=['project code-','Do you want to remove the project(yes/no)?']
        delete_project_code=int(input(remove_menu[0]))#taking inputs for menu 2
        command=str(input(remove_menu[1]))
        if(command=='yes'):#giving condition to exit if user inputs no
            trackno=ongoing_projects.index(delete_project_code)#giving a variable for the index no of the specifc project code
            completed_projects.append(ongoing_projects[trackno])#using that variable index to find the element in and add to the completed list
            client2.append(client[trackno])
            start2.append(start[trackno])
            end2.append(end[trackno])
            workersassigned2.append(workersassigned[trackno])
            available_workers=available_workers+workersassigned[trackno]
            del(ongoing_projects[trackno])#using the variable with the valu of the index to delete the elements with that index in ongoing project list
            del(client[trackno])
            del(start[trackno])
            del(end[trackno])
            del(stats[trackno])
        else:
            print(' program will run again')
    elif(main_menu_input==3):
        print('XYZ Company')#printing the third menue
        print('Add new workers')
        workersadd=int(input('Number workers to add -'))#taking inputs in the third menu
        command2=str(input('Do you want to add (Yes/No)?'))
        if(command2=='yes'):#giving condition to exit if user inputs no
            workerstot=workerstot+workersadd#adding the new workers to the total and the available list
            available_workers=available_workers+workersadd
        else:
            print('the program will run again')
    elif(main_menu_input==4):
        print('XYZ Company')#printing menu 4
        print('Update Project Details')
        editproject=int(input('Project Code - '))#taking inputs and assigning them to variables
        edittrackno=ongoing_projects.index(editproject)
        client3=str(input('Clients Name -'))
        start3=str(input('Start date -'))
        end3=str(input('Expected end date -'))
        workersassigned3=int(input('Number of workers -'))
        stats3=str(input('Project status(ongoing/completed) -'))
        command3=str(input('Do you want to update the project details (Yes/No)?'))
        if(command3=='yes'):
            client[edittrackno]=client3#updating the changes the user make
            start[edittrackno]=start3
            end[edittrackno]=end3
            x=workersassigned[edittrackno]
            workersassigned[edittrackno]=workersassigned3
            if (stats3=='completed'):
                completed_projects.append(ongoing_projects[edittrackno])#if the user change the status changing the inteams from ongoing list to complete list
                client2.append(client[edittrackno])
                start2.append(start[edittrackno])
                end2.append(end[edittrackno])
                workersassigned2.append(workersassigned[edittrackno])
                available_workers=available_workers-x+workersassigned3
                del(ongoing_projects[edittrackno])
                del(client[edittrackno])
                del(start[edittrackno])
                del(end[edittrackno])
                del(stats[edittrackno])
    elif(main_menu_input==5):
        print('XYZ Company')
        print('Project Statistics')#displaying the fifth menu
        #counting the elemnts of each list through a for loop
        countp=0
        for p in range(len(ongoing_projects)):
            countp=countp+1
        print('Number of ongoing projects -',countp)#dispaying the count
        countq=0
        for q in range(len(completed_projects)):
            countq=countq+1
        print('Number of completed projects -',countq)
        countr=0
        for r in range(len(onhold_projects)):
            countr=countr+1
        print('Number of on hold projects -',countr)
        print('Number of available workers to assign -',available_workers)
        command4=str(input('Do you want to add the project (Yes/No)? __'))
        if(command4=='yes'):
            print(' add new project from main menu')

    
                 

    
    
    
        
                 
    
   
        
