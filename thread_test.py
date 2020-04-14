from PyQt5 import QtCore

class Worker(QtCore.QRunnable):
    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        print('Running Worker')

class Tasks(QtCore.QObject):
    def __init__(self):
        super(Tasks, self).__init__()
        self.pool = QtCore.QThreadPool.globalInstance()
        self.pool.setMaxThreadCount(2)

    def start(self):
        for task in range(3):
            worker = Worker()
            self.pool.start(worker)
        self.pool.waitForDone()

if __name__ == '__main__':
    tasks = Tasks()
    tasks.start()