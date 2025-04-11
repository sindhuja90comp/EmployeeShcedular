package com.example.employeescheduler;

import java.util.*;

public class EmployeeScheduler {
    private final String[] DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
    private final String[] SHIFTS = {"Morning", "Afternoon", "Evening"};
    private final Map<String, Employee> employees = new HashMap<>();
    private final Map<String, Map<String, List<String>>> schedule = new LinkedHashMap<>();

    public static void main(String[] args) {
        EmployeeScheduler scheduler = new EmployeeScheduler();
        scheduler.collectEmployeeData();
        scheduler.generateSchedule();
        scheduler.printSchedule();
    }

    // 1. Input and Storage
    private void collectEmployeeData() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Enter employee name (or 'done' to finish): ");
            String name = scanner.nextLine().trim();
            if (name.equalsIgnoreCase("done")) {
                break;
            }
            String[] preferences = new String[DAYS.length];
            System.out.println("Enter preferred shifts for " + name + " (1. Morning, 2. Afternoon, 3. Evening) for each day:");
            for (int i = 0; i < DAYS.length; i++) {
                while (true) {
                    System.out.println(DAYS[i] + ":");
                    System.out.println("1. Morning");
                    System.out.println("2. Afternoon");
                    System.out.println("3. Evening");
                    System.out.print("Enter your choice (1-3): ");
                    String choice = scanner.nextLine().trim();
                    if (choice.equals("1")) {
                        preferences[i] = "Morning";
                        break;
                    } else if (choice.equals("2")) {
                        preferences[i] = "Afternoon";
                        break;
                    } else if (choice.equals("3")) {
                        preferences[i] = "Evening";
                        break;
                    } else {
                        System.out.println("Invalid choice. Please enter a number between 1 and 3.");
                    }
                }
            }
            employees.put(name, new Employee(name, preferences));
        }
        scanner.close();
    }

    // 2. Scheduling Logic and 3. Shift Conflicts
    private void generateSchedule() {
        // Initialize schedule
        for (String day : DAYS) {
            schedule.put(day, new LinkedHashMap<>());
            for (String shift : SHIFTS) {
                schedule.get(day).put(shift, new ArrayList<>());
            }
        }

        // First pass: Assign preferred shifts
        for (String day : DAYS) {
            for (String shift : SHIFTS) {
                List<Employee> preferred = getPreferredEmployees(day, shift);
                Collections.shuffle(preferred);
                int assignedCount = 0;
                for (Employee employee : preferred) {
                    if (employee.isAvailable(day) && schedule.get(day).get(shift).size() < 2) {
                        schedule.get(day).get(shift).add(employee.getName());
                        employee.assignShift(day, shift);
                        assignedCount++;
                    }
                    if (assignedCount >= 2) break;
                }
            }
        }

        // Second pass: Fill remaining slots and resolve conflicts (basic)
        for (String day : DAYS) {
            for (String shift : SHIFTS) {
                while (schedule.get(day).get(shift).size() < 2) {
                    Employee bestCandidate = findBestAvailableEmployee(day, shift);
                    if (bestCandidate != null) {
                        schedule.get(day).get(shift).add(bestCandidate.getName());
                        bestCandidate.assignShift(day, shift);
                    } else {
                        break; // No more available employees
                    }
                }
            }
        }
    }

    private List<Employee> getPreferredEmployees(String day, String shift) {
        List<Employee> preferred = new ArrayList<>();
        for (Employee employee : employees.values()) {
            if (employee.canWork(day, shift)) {
                preferred.add(employee);
            }
        }
        return preferred;
    }

    private Employee findBestAvailableEmployee(String day, String shift) {
        List<Employee> available = new ArrayList<>();
        for (Employee employee : employees.values()) {
            if (employee.isAvailable(day) && !schedule.get(day).get(shift).contains(employee.getName())) {
                available.add(employee);
            }
        }
        if (available.isEmpty()) return null;

        // Simple conflict resolution: Prioritize employees who haven't worked yet or fewest days
        available.sort(Comparator.comparingInt(Employee::getWorkDays));
        return available.get(0);
    }

    // 4. Output
    private void printSchedule() {
        System.out.println("\n=== Weekly Employee Schedule ===\n");
        for (String day : schedule.keySet()) {
            System.out.println(day + ":");
            for (String shift : schedule.get(day).keySet()) {
                String assigned = String.join(", ", schedule.get(day).get(shift));
                System.out.printf("  %-10s: %s%n", shift, assigned.isEmpty() ? "No employees assigned" : assigned);
            }
            System.out.println();
        }
    }
}