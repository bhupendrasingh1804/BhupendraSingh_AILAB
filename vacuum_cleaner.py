def vacuum_world():
    # initializing goal_state (0 indicates Clean and 1 indicates Dirty)
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # Simulate user input
    location_input = 'A'  # Replace with 'A' or 'B'
    status_input = '1'  # Replace with '0' or '1' (0=Clean, 1=Dirty)
    status_input_complement = '1'  # Replace with '0' or '1' (0=Clean, 1=Dirty)

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        # Vacuum is in Location A
        print("Vacuum is placed in Location A")

        if status_input == '1':
            # Location A is Dirty
            print("Location A is Dirty.")
            # Suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # Cost for cleaning
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                # If Location B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # Cost for moving right
                print("COST for moving RIGHT: " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1  # Cost for cleaning
                print("COST for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("No action needed. Location B is already clean.")
        else:
            print("Location A is already clean.")

            if status_input_complement == '1':
                # If Location B is Dirty
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # Cost for moving right
                print("COST for moving RIGHT: " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['B'] = '0'
                cost += 1  # Cost for cleaning
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("No action needed. Location B is already clean.")

    else:
        # Vacuum is in Location B
        print("Vacuum is placed in Location B")

        if status_input == '1':
            # Location B is Dirty
            print("Location B is Dirty.")
            # Suck the dirt and mark it as clean
            goal_state['B'] = '0'
            cost += 1  # Cost for cleaning
            print("COST for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                # If Location A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1  # Cost for moving left
                print("COST for moving LEFT: " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # Cost for cleaning
                print("COST for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("No action needed. Location A is already clean.")
        else:
            print("Location B is already clean.")

            if status_input_complement == '1':
                # If Location A is Dirty
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1  # Cost for moving left
                print("COST for moving LEFT: " + str(cost))
                # Suck the dirt and mark it as clean
                goal_state['A'] = '0'
                cost += 1  # Cost for cleaning
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("No action needed. Location A is already clean.")

    # Done cleaning
    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement: " + str(cost))

vacuum_world()
