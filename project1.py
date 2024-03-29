# -*- coding: utf-8 -*-
"""Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lhK5rqCFaUfYEhZ47jlo8bTt--IeXXlS
"""

import csv
import os
from tabulate import tabulate

def mark_attendance(student_id):
    filename = "attendance.csv"
    mode = 'a' if os.path.exists(filename) else 'w'

    with open(filename, mode, newline='') as file:
        writer = csv.writer(file)
        if mode == 'w':
            writer.writerow(["Student ID", "Status"])
        writer.writerow([student_id, "Present"])
    print("Attendance marked successfully.")

def view_attendance():
    filename = "attendance.csv"
    if not os.path.exists(filename):
        print("Attendance data not found.")
        return

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) > 1:
            print(tabulate(data, headers="firstrow", tablefmt="grid"))
        else:
            print("No attendance records found.")

def delete_attendance():
    filename = "attendance.csv"
    if not os.path.exists(filename):
        print("Attendance data not found.")
        return

    os.remove(filename)
    print("Attendance data deleted successfully.")

def main():
    print("Welcome to the Attendance Management System")
    while True:
        print("\nMENU:")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Delete Attendance Data")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            mark_attendance(student_id)
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            delete_attendance()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()