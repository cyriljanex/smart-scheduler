from datetime import datetime

exams = []
exam_id_counter = 1

def is_conflict(date, time):
    for exam in exams:
        if exam["date"] == date and exam["time"] == time:
            return True
    return False

def add_exam():
    global exam_id_counter
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter exam room: ")
    if is_conflict(date, time):
        print("Conflict detected: Another exam is already scheduled at that date and time.\n")
        return
    exam = {
        "id": exam_id_counter,
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }
    exams.append(exam)
    exam_id_counter += 1
    print("Exam added successfully.\n")

def view_exams():
    if not exams:
        print("No exams scheduled.\n")
        return
    print("\nScheduled Exams:")
    for exam in exams:
        print(f"ID: {exam['id']} | {exam['name']} | {exam['date']} {exam['time']} | Room: {exam['room']}")
    print()

def edit_exam():
    exam_id = int(input("Enter the ID of the exam to edit: "))
    for exam in exams:
        if exam["id"] == exam_id:
            name = input("Enter new exam name: ")
            date = input("Enter new exam date (YYYY-MM-DD): ")
            time = input("Enter new exam time (HH:MM): ")
            room = input("Enter new exam room: ")
            if is_conflict(date, time) and (exam["date"] != date or exam["time"] != time):
                print("Conflict detected: Another exam is already scheduled at that date and time.\n")
                return
            exam["name"] = name
            exam["date"] = date
            exam["time"] = time
            exam["room"] = room
            print("Exam updated successfully.\n")
            return
    print("Exam not found.\n")

def delete_exam():
    exam_id = int(input("Enter the ID of the exam to delete: "))
    for exam in exams:
        if exam["id"] == exam_id:
            exams.remove(exam)
            print("Exam deleted successfully.\n")
            return
    print("Exam not found.\n")

def menu():
    while True:
        print("Smart Scheduler Menu:")
        print("1. Add Exam")
        print("2. View Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
        choice = input("Select an option (1-5): ")
        print()
        if choice == "1":
            add_exam()
        elif choice == "2":
            view_exams()
        elif choice == "3":
            edit_exam()
        elif choice == "4":
            delete_exam()
        elif choice == "5":
            print("Exiting Smart Scheduler. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    menu()
