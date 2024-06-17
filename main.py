'''
Description: This main file contains an infinite loop that only exits when the users press 0.
'''

def main():

    toDo = []

    print("*** Welcome to your to-do list ***")
    menuSelection()

    userInput = getInput(">> ")

    while True:
        if userInput == 0:
            displayList(toDo)
        elif userInput == 1:
            addTask(toDo)
        elif userInput == 2:
            if len(toDo) > 0:
                removeTask(toDo)
            else:
                print("Your list is empty. Please add tasks first.")
        elif userInput == 999:
            print("Goodbye!")
            break
        else:
            print("This is not a valid option")
        
        menuSelection()
        userInput = getInput(">> ")


def getInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def menuSelection():

    print("\nSelect a button to continue or press 999 to exit:")
    print("--------------------------------------------------")
    print("[0] - Look at your to-do list")
    print("[1] - Add a task to your list")
    print("[2] - Remove a task from your list")


def addTask(toDo):
    task = str(input("What would you like to add to your list: "))
    toDo.append(task)


def removeTask(toDo):
    displayList(toDo)
    taskNumber = getInput("What task would you like to remove? ")
    if taskNumber > 0 and taskNumber <= len(toDo):
        toDo.remove(toDo[taskNumber - 1])
        displayList(toDo)
    else:
        print("Invalid task number. Please try again.")

def displayList(toDo):
    print("\n              To Do List")
    print("---------------------------------------------")
    for n, v in enumerate(toDo):
        print("|{}|    {}".format(n + 1, v))
    print("---------------------------------------------")

main()