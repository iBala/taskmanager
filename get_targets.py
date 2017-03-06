#Get Daily targets from user

from  datetime import datetime
import MySQLdb
import os
import time
import pprint

db = MySQLdb.connect(host = "127.0.0.1",user="root",passwd="iBala$123",db="goals")
cursor = db.cursor()
db.autocommit(True)

DB_TASK = 'task_list'

#Logic to get current user will go here
def get_curr_user():
	return 1

#Deprecated
def create_goal(goal,uid = get_curr_user()):
	cursor.execute('INSERT INTO goal_list (goal, uid) VALUES (\''+str(goal)+'\',\''+str(uid)+'\');')
	print ('INSERT INTO goal_list (goal, uid) VALUES (\''+str(goal)+'\',\''+str(uid)+'\');')

#Create tasks in the DB once it is done
def create_tasks(task,uid = get_curr_user()):
	cursor.execute('INSERT INTO task_list (task, uid) VALUES (\''+str(task)+'\',\''+str(uid)+'\');')
	print "Task Created: "+task

#Deprecated
def create_no_list(no_list, uid = get_curr_user()):
	for i in no_list:
		cursor.execute('INSERT INTO no_list (task, uid) VALUES (\''+str(task)+'\',\''+str(uid)+'\');')

#Fetch all tasks from DB
def get_tasks(filter):
	if (filter == 'all'):
		cursor.execute('SELECT * from '+DB_TASK+' ORDER BY id DESC;')
	if (filter == 'incomplete'):
		cursor.execute('SELECT * from '+DB_TASK+' WHERE completed=0 ORDER BY id DESC;')
	if (filter == 'complete'):
		cursor.execute('SELECT * from '+DB_TASK+' WHERE completed=1 ORDER BY id DESC;')
	output = cursor.fetchall()
	task_list = []
	for i in output:
		task_list.append(i[1])
	return task_list

#Delete task from DB
def delete_task(task_id):
	cursor.execute('DELETE FROM '+DB_TASK+' WHERE id = '+str(task_id)+';')

#Mark a task as completed
def mark_complete_task(task_id):
	cursor.execute('UPDATE '+DB_TASK+' SET completed = 1 WHERE id = '+task_id+';')
	
#Get user input
def get_task_name():
	task = raw_input("Enter the name of the task to be created:\n")
	return task

#Get one goal for the day
#goal = raw_input("Enter the one thing you will complete today.\n")
#create_goal(goal)
#print "I'll follow up tomorrow morning whether you have completed this: \"" + goal + "\""
#print "##############################################################################"

##Things that you will not do today
#print "It's very important to know what you will not do today. Go ahead. Tell me\n"

#no_list = []
#var = 0
#while (1):
#	var = var + 1
#	no_list.append(raw_input("Enter task no "+str(var)+". Enter 'c' to end\n"))
#	if no_list[len(no_list)-1] == 'c':
#		break
#
#create_no_list(no_list[:-1])

def menu():
	os.system('clear')
	print "Welcome to the Task Manager. Please choose an option below:"
	print "1. Create new tasks"
	print "2. Fetch pending tasks"
	print '3. Fetch all tasks'
	print '4. Exit'
	user_input = raw_input('Enter an option:')
	if user_input == '1':
		create_tasks(get_task_name())
		raw_input("Press enter to continue")
	elif user_input == '2':
		pprint.pprint(get_tasks('incomplete'))
		raw_input("Press enter to continue")
	elif user_input == '3':
		pprint.pprint(get_tasks('all'))
		raw_input("Press enter to continue")
	elif user_input == '4':
		print "Goodbye!"
		exit()
	else:
		print "Please enter a valid input."

	menu()

if __name__ == "__main__":
	menu()
