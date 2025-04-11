
This is the standard folder structure for the Java Employee Scheduler application and details the steps required to compile and run the code from the command line.

1. Folder Structure:

The recommended folder structure adheres to common Java project conventions, facilitating organization and compatibility with build tools.

EmployeeScheduler/          [Root project directory]
├── src/                      [Source code directory]
│   └── main/                 [Main application source code]
│       └── java/             [Java source files]
│           └── com/          [Top-level package directory]
│               └── example/  [Sub-package directory]
│                   └── employeescheduler/ [Application-specific package]
│                       ├── Employee.java        [Class definition for employees]
│                       └── EmployeeScheduler.java [Main class with scheduling logic]

EmployeeScheduler/: The top-level directory containing all project files.
src/main/java/: This path houses the main Java source code files, organized by their package structure.
com.example.employeescheduler/: This series of subdirectories reflects the package name declared within the .java files. Using a structured package name helps prevent naming conflicts and logically organizes the codebase.
Employee.java: Contains the definition of the Employee class, likely including attributes for name, preferences, and methods for availability and shift assignment.
EmployeeScheduler.java: Contains the main method, which is the entry point of the application, along with the core logic for collecting employee data, generating the schedule, and printing the output.

2. Running the Code:

To execute the Employee Scheduler application from the command line, follow these steps:

Open your terminal or command prompt.

Navigate to the directory containing the src folder (the root of the EmployeeScheduler project).

Compile the Java source files:
Use the Java compiler (javac) to translate the .java files into bytecode (.class files). You need to specify the correct path to the source files based on the package structure:

Bash

javac java/src/main/java/com/example/employeescheduler/Employee.java java/src/main/java/com/example/employeescheduler/EmployeeScheduler.java
Upon successful compilation, .class files will be created in the same directory as their corresponding .java files (src/main/java/com/example/employeescheduler/).

Run the compiled application:
Use the Java Virtual Machine (java) to execute the main method in the EmployeeScheduler class. You need to provide the fully qualified name of the main class (including the package) and ensure your terminal is positioned such that the JVM can find the root of the package structure (the directory containing the com folder, which is src/main/java/). Therefore, navigate to the java/src/main/java directory and execute:

Bash

java com.example.employeescheduler.EmployeeScheduler
Alternatively, if you are in the root of the EmployeeScheduler project, you might need to specify the classpath:

Bash

java -cp src/main/java com.example.employeescheduler.EmployeeScheduler
The -cp or --class-path option tells the JVM where to look for the compiled class files.

Upon successful execution, the application will proceed to collect employee data (currently hardcoded), generate the weekly schedule, and print the schedule to the console.


Ready to use commands:
Step1: cd EmployeeSchedular
Step2: javac java/src/main/java/com/example/employeescheduler/Employee.java java/src/main/java/com/example/employeescheduler/EmployeeScheduler.java ----> to create class files
Step3: cd java/src/main/java
Step4: java com.example.employeescheduler.EmployeeScheduler  ----> run the application
