class Worker:
    def work(self):
        pass  
class Engineer(Worker):
    def work(self):
        return "Engineering and coding tasks."

class Manager(Worker):
    def work(self):
        return "Managing team and projects."

def print_work_details(worker):
    print(worker.work())

# Create instances of Engineer and Manager
engineer = Engineer()
manager = Manager()


print_work_details(engineer)  
print_work_details(manager)  