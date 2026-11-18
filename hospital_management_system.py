"""
Hospital Management System (PS No. 64)
--------------------------------------
A menu-driven Python 3 console application that performs CRUD
(Create, Read, Update, Delete) operations on patient records.

Storage : in-memory dictionary (data is lost when the program exits)
Patient IDs : auto-generated, starting from P101
Fields  : Name, Age (0-120), Disease, Doctor
"""

patients = {}      # {"P101": {"name": ..., "age": ..., "disease": ..., "doctor": ...}}
next_id = 101      # counter used to generate patient IDs


# ---------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------
def generate_id():
    """Return a new unique patient ID such as P101, P102, ..."""
    global next_id
    pid = f"P{next_id}"
    next_id += 1
    return pid


def read_text(prompt):
    """Keep asking until the user enters a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Please try again.")


def read_age(prompt):
    """Keep asking until the user enters a whole number from 0 to 120."""
    while True:
        value = input(prompt).strip()
        try:
            age = int(value)
        except ValueError:
            print("  Age must be a whole number. Please try again.")
            continue
        if 0 <= age <= 120:
            return age
        print("  Age must be between 0 and 120. Please try again.")


def print_patient(pid, record):
    """Print a single patient record."""
    print(f"  ID      : {pid}")
    print(f"  Name    : {record['name']}")
    print(f"  Age     : {record['age']}")
    print(f"  Disease : {record['disease']}")
    print(f"  Doctor  : {record['doctor']}")


def ask_patient_id():
    """Ask for a patient ID and return it in upper case."""
    return input("Enter Patient ID (e.g. P101): ").strip().upper()


# ---------------------------------------------------------------
# CRUD operations
# ---------------------------------------------------------------
def add_patient():
    """CREATE: add a new patient record."""
    print("\n--- Add New Patient ---")
    name = read_text("Name    : ")
    age = read_age("Age     : ")
    disease = read_text("Disease : ")
    doctor = read_text("Doctor  : ")

    pid = generate_id()
    patients[pid] = {"name": name, "age": age, "disease": disease, "doctor": doctor}
    print(f"\nPatient added successfully. Patient ID: {pid}")


def view_patients():
    """READ: display all patient records."""
    print("\n--- All Patients ---")
    if not patients:
        print("No patient records found.")
        return
    for pid, record in patients.items():
        print_patient(pid, record)
        print("  " + "-" * 30)
    print(f"Total patients: {len(patients)}")


def search_patient():
    """READ: search for one patient by ID."""
    print("\n--- Search Patient ---")
    pid = ask_patient_id()
    if pid in patients:
        print()
        print_patient(pid, patients[pid])
    else:
        print(f"No patient found with ID {pid}.")


def update_patient():
    """UPDATE: change details of an existing patient (blank = keep old value)."""
    print("\n--- Update Patient ---")
    pid = ask_patient_id()
    if pid not in patients:
        print(f"No patient found with ID {pid}.")
        return

    record = patients[pid]
    print("\nCurrent details:")
    print_patient(pid, record)
    print("\nPress Enter to keep the current value.")

    new_name = input(f"Name    [{record['name']}]: ").strip()
    if new_name:
        record["name"] = new_name

    while True:
        new_age = input(f"Age     [{record['age']}]: ").strip()
        if not new_age:
            break
        try:
            age = int(new_age)
        except ValueError:
            print("  Age must be a whole number. Please try again.")
            continue
        if 0 <= age <= 120:
            record["age"] = age
            break
        print("  Age must be between 0 and 120. Please try again.")

    new_disease = input(f"Disease [{record['disease']}]: ").strip()
    if new_disease:
        record["disease"] = new_disease

    new_doctor = input(f"Doctor  [{record['doctor']}]: ").strip()
    if new_doctor:
        record["doctor"] = new_doctor

    print("\nPatient record updated successfully.")


def delete_patient():
    """DELETE: remove a patient record after confirmation."""
    print("\n--- Delete Patient ---")
    pid = ask_patient_id()
    if pid not in patients:
        print(f"No patient found with ID {pid}.")
        return

    print()
    print_patient(pid, patients[pid])
    confirm = input("Are you sure you want to delete this record? (y/n): ").strip().lower()
    if confirm == "y":
        del patients[pid]
        print("Patient record deleted successfully.")
    else:
        print("Deletion cancelled.")


# ---------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------
def show_menu():
    print("\n" + "=" * 40)
    print("      HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")
    print("=" * 40)


def main():
    actions = {
        "1": add_patient,
        "2": view_patients,
        "3": search_patient,
        "4": update_patient,
        "5": delete_patient,
    }

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "6":
            print("\nThank you for using the Hospital Management System. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
