# employee_scheduler/src/input_handler.py
def get_employee_preferences():
    """Collects employee names and their preferred shifts using numbered options."""
    employee_preferences = {}
    all_employees = []
    while True:
        employee_name = input("Enter employee name (or 'done' to finish): ").strip()
        if employee_name == "done":
            break
        if employee_name in employee_preferences:
            print(f"Preferences for {employee_name} already entered.")
            continue

        all_employees.append(employee_name)
        employee_preferences[employee_name] = {}

        print(f"Enter preferred shifts for {employee_name}:")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        shift_options = {"1": "morning", "2": "afternoon", "3": "evening"}

        for day in days:
            while True:
                print(f"{day}:")
                print("1. Morning")
                print("2. Afternoon")
                print("3. Evening")
                preference_choice = input("Enter your choice (1-3): ").strip()
                if preference_choice in shift_options:
                    employee_preferences[employee_name][day] = shift_options[preference_choice]
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
    return employee_preferences