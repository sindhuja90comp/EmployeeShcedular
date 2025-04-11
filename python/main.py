# Importing the JSON module to handle reading and writing JSON data
import json
# Importing the os module for interacting with the operating system
import os
from src.input_handler import get_employee_preferences
from src.schedular import assign_shifts, resolve_conflicts, schedule
from output.display import output_schedule

# Define the filename for storing employee data and a flag for schedule generation status
DATA_FILE = "employee_data.json"
schedule_generated = False

def load_employee_data():
    """Loads employee preferences from the data file if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error decoding employee data file. Starting with empty data.")
                return {}
    return {}

def save_employee_data(employee_data):
    """Saves employee preferences to the data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(employee_data, f, indent=4)

if __name__ == "__main__":
    # Load existing employee data at the start of the application
    employee_preferences = load_employee_data()

    # Handle the case where no existing data is found, prompting for new input
    if not employee_preferences:
        employee_preferences = get_employee_preferences()
        save_employee_data(employee_preferences)
        schedule_generated = True
    # If data is loaded, provide options to the user
    else:
        print("Loaded existing employee preferences.")
        while True:
            action = input("Do you want to (a)dd new employees, (v)iew existing preferences, or (s)how schedule? (a/v/s): ").lower()
            # Block for handling user actions after loading data
            if action == 'a':
                new_preferences = get_employee_preferences()
                employee_preferences.update(new_preferences)
                save_employee_data(employee_preferences)
                schedule_generated = False # Schedule needs regeneration
            elif action == 'v':
                for emp, prefs in employee_preferences.items():
                    print(f"\n{emp}:")
                    for day, pref in prefs.items():
                        print(f"  {day}: {pref}")
            elif action == 's':
                break
            else:
                print("Invalid action.")

    # Generate and output the schedule if employee data is available
    if employee_preferences:
        if not schedule_generated:
            assign_shifts(employee_preferences)
            resolve_conflicts(schedule, employee_preferences)
        output_schedule(schedule)
        
    else:
        print("No employee data available. Schedule cannot be generated.")