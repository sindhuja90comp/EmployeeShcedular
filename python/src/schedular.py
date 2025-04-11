import random

# Data structure to store the final schedule
schedule = {
    "Monday": {"morning": [], "afternoon": [], "evening": []},
    "Tuesday": {"morning": [], "afternoon": [], "evening": []},
    "Wednesday": {"morning": [], "afternoon": [], "evening": []},
    "Thursday": {"morning": [], "afternoon": [], "evening": []},
    "Friday": {"morning": [], "afternoon": [], "evening": []},
    "Saturday": {"morning": [], "afternoon": [], "evening": []},
    "Sunday": {"morning": [], "afternoon": [], "evening": []},
}

# Dictionary to keep track of employee workdays
employee_workdays = {}

def assign_shifts(employee_preferences):
    """Assigns shifts to employees based on preferences and constraints."""
    all_employees = list(employee_preferences.keys())
    for emp in all_employees:
        employee_workdays[emp] = 0

    for day in schedule:
        assigned_today = set()
        for shift in schedule[day]:
            preferred_employees = [
                emp for emp in all_employees
                if employee_preferences.get(emp, {}).get(day) == shift
                and employee_workdays[emp] < 5
                and emp not in assigned_today
            ]
            random.shuffle(preferred_employees)
            num_to_assign = min(2, len(preferred_employees))
            assigned = preferred_employees[:num_to_assign]
            schedule[day][shift].extend(assigned)
            assigned_today.update(assigned)
            for emp in assigned:
                employee_workdays[emp] += 1

    # Fill remaining slots if needed
    for day in schedule:
        for shift in schedule[day]:
            while len(schedule[day][shift]) < 2:
                eligible_employees = [
                    emp for emp in all_employees
                    if employee_workdays[emp] < 5
                    and emp not in schedule[day]["morning"]
                    and emp not in schedule[day]["afternoon"]
                    and emp not in schedule[day]["evening"]
                ]
                if not eligible_employees:
                    break

                random_employee = random.choice(eligible_employees)
                schedule[day][shift].append(random_employee)
                employee_workdays[random_employee] += 1

def resolve_conflicts(schedule, employee_preferences):
    """Detects and resolves shift conflicts."""
    for day in schedule:
        for shift in schedule[day]:
            assigned_employees = schedule[day][shift]
            if len(set(assigned_employees)) < len(assigned_employees):
                print(f"Conflict detected on {day}, {shift}: {assigned_employees}")
                schedule[day][shift] = list(dict.fromkeys(assigned_employees))
                print(f"Conflict resolved on {day}, {shift}: {schedule[day][shift]}")

    # Basic secondary conflict resolution (preferred shift full)
    for employee, preferences in employee_preferences.items():
        for day, preferred_shift in preferences.items():
            if employee in schedule[day][preferred_shift] and schedule[day][preferred_shift].count(employee) > 1:
                print(f"Secondary conflict for {employee} on {day} ({preferred_shift} full).")
                other_shifts = [s for s in schedule[day] if s != preferred_shift]
                for other_shift in other_shifts:
                    if employee not in schedule[day][other_shift] and employee_workdays.get(employee, 0) < 5:
                        schedule[day][other_shift].append(employee)
                        schedule[day][preferred_shift].remove(employee)
                        print(f"{employee} reassigned to {other_shift} on {day}.")
                        break

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