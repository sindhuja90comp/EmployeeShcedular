def output_schedule(schedule):
    """Outputs the final schedule for the week."""
    print("\n----- Employee Schedule for the Week -----")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    shifts = ["morning", "afternoon", "evening"]
    for day in days:
        print(f"\n--- {day} ---")
        for shift in shifts:
            employees = schedule[day][shift]
            print(f"{shift.capitalize()}: {', '.join(employees) if employees else 'No employees assigned'}")