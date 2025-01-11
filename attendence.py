class AttendanceTracker:
    def __init__(self):
        # A dictionary to store attendance data
        # Format: {student_name: {date: 'present'/'absent'}}
        self.attendance_data = {}

    def add_student(self, student_name):
        """ Adds a student to the attendance system """
        if student_name not in self.attendance_data:
            self.attendance_data[student_name] = {}
            print(f"Student {student_name} added.")
        else:
            print(f"Student {student_name} already exists.")

    def mark_attendance(self, student_name, date, status):
        """ Marks attendance for a student on a specific date """
        if student_name not in self.attendance_data:
            print(f"Student {student_name} not found.")
            return
        
        if status.lower() not in ['present', 'absent']:
            print("Invalid status! Use 'present' or 'absent'.")
            return
        
        # Update the attendance record
        self.attendance_data[student_name][date] = status.lower()
        print(f"Attendance for {student_name} on {date} marked as {status}.")

    def view_attendance(self, student_name):
        """ View the attendance records of a specific student """
        if student_name not in self.attendance_data:
            print(f"Student {student_name} not found.")
            return
        
        print(f"Attendance record for {student_name}:")
        for date, status in self.attendance_data[student_name].items():
            print(f"{date}: {status}")

    def view_all_attendance(self):
        """ View the attendance records for all students """
        if not self.attendance_data:
            print("No attendance records available.")
            return
        
        print("All attendance records:")
        for student_name, attendance in self.attendance_data.items():
            print(f"\n{student_name}:")
            for date, status in attendance.items():
                print(f"{date}: {status}")
                
    def remove_student(self, student_name):
        """ Removes a student from the system """
        if student_name in self.attendance_data:
            del self.attendance_data[student_name]
            print(f"Student {student_name} removed from system.")
        else:
            print(f"Student {student_name} not found.")

# Example usage
tracker = AttendanceTracker()

# Add students
tracker.add_student("John Doe")
tracker.add_student("Jane Smith")

# Mark attendance
tracker.mark_attendance("John Doe", "2025-01-10", "Present")
tracker.mark_attendance("Jane Smith", "2025-01-10", "Absent")

# View specific student's attendance
tracker.view_attendance("John Doe")

# View all students' attendance
tracker.view_all_attendance()

# Remove a student
tracker.remove_student("John Doe")

# View all students' attendance after removal
tracker.view_all_attendance()

