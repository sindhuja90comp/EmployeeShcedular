# EmployeeShcedular
a small application for managing employee schedules at a company.

Implementation:

Report on Control Structures, Syntax, and Control Flow in the Employee Scheduler Application
The Employee Scheduler application demonstrates the implementation of conditionals, loops, and branching across multiple Python files to manage employee scheduling. It also showcases fundamental Python syntax and control flow mechanisms.

Conditionals (if/elif/else): Conditionals are used extensively throughout the application to make decisions based on various criteria.

In src/input_handler.py, an if statement checks if the entered employee name is "done" to terminate input. 
Another if/else structure validates the entered shift preference against the allowed options.
Within src/scheduler.py, numerous if conditions control the shift assignment logic. 
For instance, checks are made to ensure an employee hasn't worked 5 days (if employee_workdays[emp] < 5), if their preferred shift matches the current shift being assigned (if employee_preferences.get(emp, {}).get(day) == shift), and if an employee is not already assigned to a shift on that day (if emp not in assigned_today). 
The min() function implicitly acts as a conditional to limit the number of employees assigned to a shift.
The conflict resolution logic in src/scheduler.py uses if statements to detect conflicts (duplicate assignments) and secondary conflicts (preferred shift full).
In main.py, if/else statements handle the loading of existing employee data and provide different user options based on whether data was loaded or not.
Loops (for/while): Loops are crucial for iterating over data structures and performing repetitive tasks.

src/input_handler.py uses a while True loop to continuously collect employee input until the user enters "done." 
A for loop iterates through the days of the week to gather shift preferences for each day. 
Another while True loop ensures valid shift preferences are entered for each day.
src/scheduler.py employs nested for loops to iterate through days and shifts in the schedule dictionary during the assignment and conflict resolution phases. while loops are used to ensure the minimum staffing requirement of 2 employees per shift is met and to attempt conflict resolution by reassigning employees.
output/display.py uses for loops to iterate through the days and shifts in the final schedule to generate the formatted output.
Branching: Branching is achieved through the use of if, elif, else, break, and continue statements, which alter the normal sequential flow of execution.

As mentioned in conditionals and loops, if/elif/else structures direct the program's path based on conditions.
The break statement is used in src/input_handler.py to exit the input loop when "done" is entered and in src/scheduler.py to stop assigning preferred shifts to an employee once they reach their 5-day limit or when no more eligible employees are available for a shift.
The continue statement in src/input_handler.py skips the current iteration if preferences for an employee have already been entered.
Syntax and Control Flow: The code adheres to Python's syntax rules, including indentation to define code blocks within control structures. 
The control flow is clearly defined by the sequential execution of statements within functions and the branching and looping mechanisms that alter this flow based on conditions and iterations. 
The application demonstrates a structured approach to problem-solving by breaking down the task into smaller functions, each with a specific responsibility, contributing to a clear and manageable control flow.