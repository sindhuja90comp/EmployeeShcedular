def get_employee_preferences():
    """Collects employee names and their preferred shifts using numbered options."""
    employee_preferences = {}  
    all_employees = []  

    while True:
        # Prompt user to enter an employee name or 'done' to finish
        employee_name = input("Enter employee name (or 'done' to finish): ").strip()
        if employee_name == "done":  # Exit loop if user enters 'done'
            break
        if employee_name in employee_preferences:  # Check if preferences for this employee already exist
            print(f"Preferences for {employee_name} already entered.")
            continue

        # Add employee name to the list and initialize their preferences in the dictionary
        all_employees.append(employee_name)
        employee_preferences[employee_name] = {}

        print(f"Enter preferred shifts for {employee_name}:")
        # List of days for which preferences will be collected
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # Mapping of numbered options to shift names
        shift_options = {"1": "morning", "2": "afternoon", "3": "evening"}

        for day in days:
            while True:
                # Display shift options for the current day
                print(f"{day}:")
                print("1. Morning")
                print("2. Afternoon")
                print("3. Evening")
                # Prompt user to select a shift for the current day
                preference_choice = input("Enter your choice (1-3): ").strip()
                if preference_choice in shift_options:  # Validate input
                    # Store the selected shift for the current day
                    employee_preferences[employee_name][day] = shift_options[preference_choice]
                    break
                else:
                    # Inform user of invalid input and prompt again
                    print("Invalid choice. Please enter a number between 1 and 3.")
    return employee_preferences  # Return the dictionary containing all employee preferences