import datetime
import json

ID = 0

class task:
  def __init__( self, description ):
    self.id = ID
    self.description = description
    self.status = "todo"
    self.createdAt = datetime.datetime.now()
    self.updatedAt = datetime.datetime.now()


def addTask(description):
  newTask = task(description)
  with open('tasks.json', 'w') as json_file:
    json.dump(newTask.__dict__, json_file, indent=4)
  print(f'Task added successfully (id: {newTask.id})')
  ID = ID + 1

def updateTask(id, description):
  pass

def deleteTask(id):
  pass

def listTasks(status):
  with open('tasks.json', 'r') as json_file:
    data = json.load(json_file)
    if status == '':
      print(data)
    else:
      for task in data:
        if (status == '' or task['status'] == status):
          print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

def markTask(id, status):
  with open('tasks.json', 'w') as json_file:
    data = json.load(json_file)
    for task in data:
      if (task['id'] == id):
        task['status'] = status
        task['updatedAt'] = datetime.datetime.now()
    json.dump(data, json_file, indent=4)


while(True):
  print('Welcome to the task manager!')
  userinput = input('What would you like to do? (add, list, update, delete, exit) ')
  inputs = userinput.split(' ')
  if inputs[0] == 'add':
    if (len(inputs) < 2):
      print('Please provide a description for the task.')
    addTask(inputs[1])
  elif inputs[0] == 'list':
    if (len(inputs) < 2):
      listTasks('')
    else:
      match inputs[1]:
        case 'todo':
          listTasks('todo')
        case 'done':
          listTasks('done')
        case 'in-progress':
          listTasks('in-progress')
        case _:
          print('Invalid input, please try again.')
  elif inputs[0] == 'update':
    if (len(inputs) < 3):
      print('Please provide an id and a description for the task.')
    updateTask(inputs[1], inputs[2])
  elif inputs[0] == 'delete':
    if (len(inputs) < 2):
      print('Please provide an id for the task.')
    deleteTask(inputs[1])
  elif inputs[0] == 'mark-in-progress':
    if (len(inputs) < 2):
      print('Please provide an id for the task.')
    markTask(inputs[1], 'in-progress')
  elif inputs[0] == 'mark-done':
    if (len(inputs) < 2):
      print('Please provide an id for the task.')
    markTask(inputs[1], 'done')
  elif inputs[0] == 'exit':
    break
  else:
    print('Invalid input, please try again.')