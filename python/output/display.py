def output_schedule(schedule):
    """Outputs the final schedule for the week."""
    print("\n----- Employee Schedule for the Week -----")

    # Define the order of days for consistent output
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Define the order of shifts for consistent output
    shifts = ["morning", "afternoon", "evening"]

    # Iterate through each day of the week
    for day in days:
        print(f"\n--- {day} ---")
        for shift in shifts:
            employees = schedule[day][shift]
            print(f"{shift.capitalize()}: {', '.join(employees) if employees else 'No employees assigned'}")