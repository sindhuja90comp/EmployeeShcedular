package com.example.employeescheduler;

import java.util.*;

public class Employee {
    private final String name;
    private final String[] preferences; // Shift preferences for each day
    private final Set<String> assignedDays = new HashSet<>(); // Tracks days an employee is assigned
    private final Map<String, String> assignedShifts = new HashMap<>(); // Tracks specific shifts assigned
    private int workDays = 0; // Days worked this week

    public Employee(String name, String[] preferences) {
        this.name = name;
        this.preferences = preferences;
    }

    public String getName() {
        return name;
    }

    public String getPreference(String day) {
        int dayIndex = getDayIndex(day);
        if (dayIndex >= 0 && dayIndex < preferences.length) {
            return preferences[dayIndex];
        }
        return null;
    }

    public boolean canWork(String day, String shift) {
        int dayIndex = getDayIndex(day);
        if (dayIndex >= 0 && dayIndex < preferences.length) {
            return preferences[dayIndex].equalsIgnoreCase(shift) && workDays < 5 && !assignedDays.contains(day);
        }
        return false;
    }

    public boolean isAvailable(String day) {
        return workDays < 5 && !assignedDays.contains(day);
    }

    public void assignShift(String day, String shift) {
        if (!assignedDays.contains(day)) {
            assignedDays.add(day);
            assignedShifts.put(day, shift);
            workDays++;
        }
    }

    public boolean hasWorkedOn(String day) {
        return assignedDays.contains(day);
    }

    public String getAssignedShift(String day) {
        return assignedShifts.get(day);
    }

    public int getWorkDays() {
        return workDays;
    }

    private int getDayIndex(String day) {
        switch (day) {
            case "Monday":
                return 0;
            case "Tuesday":
                return 1;
            case "Wednesday":
                return 2;
            case "Thursday":
                return 3;
            case "Friday":
                return 4;
            case "Saturday":
                return 5;
            case "Sunday":
                return 6;
            default:
                return -1;
        }
    }
}