import csv
from validation import only_letters, only_digits, open_file


def generator():
    for n in range(100):
        yield n


class Worker:
    id = generator()

    def __init__(self, name="", surname="", department="", salary=0):
        self.set_id(next(self.id))
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

    def get_id(self):
        return self.__ID

    def set_id(self, new_id):
        self.__ID = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_department(self):
        return self.department

    def set_department(self, new_department):
        self.department = new_department

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def display(self):
        print(
            f"\nID: {self.get_id()}\nName: {self.name}\nSurname: {self.surname}\nDepartment: {self.department}\nSalary: {self.salary}\n"
        )

    def input(self):
        self.name = input("Name: ")
        while not only_letters(self.name):
            self.name = input("Name: ")
        self.surname = input("Surname: ")
        while not only_letters(self.surname):
            self.surname = input("Surname: ")
        self.department = input("Department: ")
        self.salary = input("Salary: ")
        while not only_digits(self.salary):
            self.salary = input("Salary: ")


def dec_search(func):
    def wrapper(*args, **kwargs):
        instance, field, data = args
        print(f"Result where {field} is {data}")
        func(*args, **kwargs)

    return wrapper


def dec_sort(func):
    def wrapper(*args, **kwargs):
        instance, field = args
        print(f"Sorted by {field}")
        func(*args, **kwargs)

    return wrapper


class Collection:
    def __init__(self):
        self.workers = []

    def add_worker(self):
        worker = Worker()
        worker.input()
        self.workers.append(worker)

    def display_all_workers(self):
        for worker in self.workers:
            worker.display()

    def worker_db(self, filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=",")
            for row in reader:
                name, surname, department, salary = (
                    row["name"],
                    row["surname"],
                    row["department"],
                    row["salary"],
                )
                if only_letters(name) and only_letters(surname) and only_digits(salary):
                    worker = Worker(name, surname, department, salary)
                    self.workers.append(worker)

    def write_with_file(self, filename):
        with open(filename, "w", newline="") as file:
            header = ["id", "name", "surname", "department", "salary"]
            writer = csv.DictWriter(file, fieldnames=header, delimiter=",")
            writer.writeheader()
            for worker in self.workers:
                writer.writerow(
                    {
                        "id": worker.get_id(),
                        "name": worker.get_name(),
                        "surname": worker.get_surname(),
                        "department": worker.get_department(),
                        "salary": worker.get_salary(),
                    }
                )

    def delete_worker(self, id):
        for worker in self.workers:
            if worker.get_id() == id:
                self.workers.remove(worker)

    def edit_worker(self, id):
        for worker in self.workers:
            if worker.get_id() == id:
                while True:
                    data = input(
                        "Enter the data for changes (name, surname, department, salary)(Press 0 to return to the menu): "
                    )
                    if data == "name":
                        new_name = input("Enter name: ")
                        while not only_letters(new_name):
                            new_name = input("Enter name: ")
                        worker.set_name(new_name)
                    elif data == "surname":
                        new_surname = input("Enter surname: ")
                        while not only_letters(new_surname):
                            new_surname = input("Enter surname: ")
                        worker.set_surname(new_surname)
                    elif data == "department":
                        new_department = input("Enter department: ")
                        worker.set_department(new_department)
                    elif data == "salary":
                        new_salary = input("Enter salary: ")
                        while not only_digits(new_salary):
                            new_salary = input("Enter salary: ")
                        worker.set_salary(new_salary)
                    elif data == "0":
                        break
                    else:
                        print("Invalid option! Try again: ")

    @dec_search
    def search_workers(self, field, data):
        getters = {
            "id": lambda w: w.id,
            "name": lambda w: w.name,
            "surname": lambda w: w.surname,
            "department": lambda w: w.department,
            "salary": lambda w: w.salary,
        }
        getter = getters.get(field)
        if getter is not None:
            for worker in self.workers:
                if getter(worker) == data:
                    worker.display()
            return

        else:
            print("Field doesn`t exist")

    @dec_sort
    def sort_workers(self, field):
        getters = {
            "id": lambda w: w.id,
            "name": lambda w: w.name,
            "surname": lambda w: w.surname,
            "department": lambda w: w.department,
            "salary": lambda w: w.salary,
        }

        getter = getters.get(field)

        if getter is not None:
            self.workers.sort(key=getter)
        return

        print("Field doesn't exist")


def main():
    collection = Collection()
    filename = input("Enter filename: ")
    while not open_file(filename):
        filename = input("Enter filename: ")
    collection.worker_db(filename)
    while True:
        print("\nChoose option: ")
        print("1.Add worker")
        print("2.Show all")
        print("3.Delete worker")
        print("4.Write to file")
        print("5.Edit worker")
        print("6.Search worker")
        print("7.Sort")
        print("0.Exit")
        choice = input(">> ")

        if choice == "1":
            collection.add_worker()
            collection.write_with_file("result.csv")
            print("The data is saved to a file!")

        elif choice == "2":
            collection.display_all_workers()

        elif choice == "3":
            id = int(input("Enter the ID: "))
            collection.delete_worker(id)
            collection.write_with_file("result.csv")
            print("The data is saved to a file!")

        elif choice == "4":
            collection.write_with_file("result.csv")
            print("The data is saved to a file!")

        elif choice == "5":
            id = int(input("Enter id: "))
            collection.edit_worker(id)
            collection.write_with_file("result.csv")
            print("The data is saved to a file!")

        elif choice == "6":
            field = input("Enter field name: ")
            data = input("Enter the data: ")
            collection.search_workers(field, data)

        elif choice == "7":
            field = input("Enter sorting field: ")
            collection.sort_workers(field)
            collection.write_with_file("result.csv")

        elif choice == "0":
            break

        else:
            print("Try again!")


if __name__ == "__main__":
    main()
