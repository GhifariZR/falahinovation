import datetime
def login(hours):
	result = str(datetime.timedelta(minutes=hours))
	return result
def register(hours):
	result = str(datetime.timedelta(minutes=hours))
	return result
def user(hours):
	result = str(datetime.timedelta(minutes=hours))
	return result
def employee(hours):
	result = str(datetime.timedelta(minutes=hours))
	return result
def timesheet(hours):
	result = str(datetime.timedelta(minutes=hours))
	return result

name = input("enter your name : ")
num = int(input("enter number of task you want to do :"))
task_list =[]
hours_list =[]
time_list =[]
result = 0
for i in range(num):
	print("Please choose your task: ")
	exist = False
	while exist == False:
		task =input("choose a task")
		if task == "LG":
			task_list.append("Login")
			hours = float(input("Enter your working hour for login (in float):"))
			hours_list.append(login(hours))
			time_list.append(hours)
			result+= hours
			exist= True
		elif task == "RG":
			task_list.append("register")
			hours = float(input("Enter your working hour for register (in float):"))
			hours_list.append(register(hours))
			time_list.append(hours)
			result+= hours
			exist = True
		elif task == "US":
			task_list.append("user")
			hours = float(input("Enter your working hour for user (in float):"))
			hours_list.append(user(hours))
			time_list.append(hours)
			result+= hours
			exist = True
		elif task == "EMP":
			task_list.append("employee")
			hours = float(input("Enter your working hour for employee (in float):"))
			hours_list.append(employee(hours))
			time_list.append(hours)
			exist = True
		elif task == "TS":
			task_list.append("timesheet")
			hours = float(input("Enter your working hour timesheet (in float):"))
			hours_list.append(timesheet(hours))
			time_list.append(hours)
			exist = True
		else:
			print("input invalid Please try again")
print("summary of task for "+ name)			
for i in range(len(task_list)):
	print("Task: " + task_list[i]+" working hours:  "+str(time_list[i]) + " ( "+ hours_list[i]+" )" )


		







