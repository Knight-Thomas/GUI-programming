#import required modules
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

#Eacvh window will need its own class
class Ui(QtWidgets.QMainWindow):
    '''constructor'''
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('/Users/tomknight/GUI-programming/GUI-programming/login-copy.ui', self) #loads ui we just created for this class
  
        #add button functionality
        
    
        #display the ui
        self.show()

#write main applicatiion which creates class instance

def mainApplication():
    '''main app which instantiates the classes'''
    app=QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
mainApplication()