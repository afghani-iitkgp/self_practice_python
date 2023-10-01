# class Employee:
#     raise_amount=1.05
#     emp_count=0
#     def __init__(self,first_name,last_name, amount):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.amount=amount
#         self.email_id="{0}.{1}@{1}.com" .format(first_name,last_name)
#         Employee.emp_count +=1

#     def fullname(self):
#         print ("%s %s"%(self.first_name,self.last_name))

#     def print1(self):
#         print (self.email)
#         print ("Total no of Employee are :%d" %(Employee.emp_count))


#     def raise_amount(self):
#         self.amount *=self.raise_amount
#         return self.amount


# class Developer(Employee):
#     raise_amount = 1.10
#     def __init__(self,f,l,a,prog):
#         super.__init__(f,l,a)
#         self.programming=prog

# class Manager(Employee):
#     def __init__(self,f,l,a,emp=None):
#         super.__init__(f,l,a)
#         if emp is None:
#             self.my_employee=[]
#         else:
#             self.my_employee=emp



#     def add_employee(self,emp):
#         if emp in self.my_employee:
#             print("employee is already exist")
#         else:
#             self.my_employee.append(emp)

#     def remove_employee(self,emp):
#         if emp in self.my_employee:
#             self.my_employee.remove(emp)

#     def print_employee(self):
#         for emp in self.my_employee:
#             print (emp.fullnamme())



# dev1=Developer("subhendu","panda",500000,"Python")
# dev1.raise_amount()
# dev2=Developer('Aditya','bishoyi',5688989,'java')
# dev2.fullname()
# dev1.fullname()
# emp1=Employee("tonu","trip",30000)
# emp1.raise_amount()
# emp1.fullname()
# mgr1=Manager("Biplab","choudhury",5000000)
# mgr1.fullname()
# mgr1.add_employee(dev1)
# mgr1.add_employee(emp1)
# mgr1.add_employee(dev2)
# mgr1.print_employee()
# mgr1.remove_employee(dev1)
# mgr1.print_employee()