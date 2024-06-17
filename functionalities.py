'''

Description: This file contains the functionalities for the to-do list.
'''

class Functionalities:

    def Functionalities(self, tasks):
        self.tasks = tasks

    def addTask(self, task):
        self.tasks.append(task)


    def removeTask(self, task):
        self.tasks.remove(task)