
# 1. Класс Employee
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

# 2. Класс Manager (наследуется от Employee)
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self, project_name):
        return f"{self.name} is managing project: {project_name}"

# 3. Класс Technician (наследуется от Employee)
class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, task):
        return f"{self.name} is performing maintenance: {task}"

# 4. Класс TechManager (наследует как Manager, так и Technician)
class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Technician.__init__(self, name, emp_id, specialization)
        Manager.__init__(self, name, emp_id, department)
        self.team = []

    # 5. Метод для добавления сотрудников
    def add_employee(self, employee):
        self.team.append(employee)

    # 6. Метод для вывода информации о всех подчинённых
    def get_team_info(self):
        for employeers in self.team:
            self.team.append(employeers)
        return "\n".join(self.team)

    def manage_project(self, project_name):
        return f"{self.name} is managing project: {project_name}"

    def perform_maintenance(self, task):
        return f"{self.name} is performing maintenance: {task}"


employee_1 = Employee("Alice", 101)
employee_2 = Manager("Bob", 102, "IT")
employee_3 = Technician("Charlie", 103, "Network Maintenance")
employee_4 = TechManager("Dave", 104, "IT", "Server Maintenance")


employee_4.add_employee(employee_1)
employee_4.add_employee(employee_2)
employee_4.add_employee(employee_3)


print(employee_1.get_info())
print(employee_2.get_info())
print(employee_3.get_info())
print(employee_4.get_info())


print(employee_2.manage_project("New Website Development"))
print(employee_3.perform_maintenance("Router Fix"))


print("\nTeam Info:\n", employee_4.get_team_info())


print(employee_4.manage_project("Server Upgrade"))
print(employee_4.perform_maintenance("System Check"))
