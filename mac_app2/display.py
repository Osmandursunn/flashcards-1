import json
import os
class Game:
    def __init__(self, level,language='english'):
        self.level = level
        self.language = language
        self.known_words = 0
        self.total_words = 20
    def begin(self):
        with open('{}.json'.format(self.language), 'r') as f:
            glossary = json.load(f)
            self.glossary1 = glossary['{}'.format(self.level)]
            self.dutch = [i for i in self.glossary1.keys()]        
    def flashcard(self):
        return [self.dutch[0],self.glossary1[self.dutch[0]]]
    def progress(self, choice):
        if choice:
            self.true_button_()
        else: 
            self.false_button_()
        return [self.known_words,self.total_words]  
    def true_button_(self):
        self.known_words+=1
        self.dutch.pop(0)
    def false_button_(self):
        self.total_words+=1
        self.dutch.append(self.dutch[0])
        self.dutch.pop(0)
    

import time
import os
import json
from datetime import datetime, timedelta
class User:
    def __init__(self,username=" ",time=0,progress=0):
        self.login(username,time,progress)
    def login(self,name,time,progress):
        self.start_time()
        names_of_file=[name_.split(".")[0]  for name_ in os.listdir('.') if os.path.isfile(name_)]
        if name in names_of_file:
            with open('{}.json'.format(name),'r') as file:
                data = file.read()
                user_current=json.loads(data)
                os.chdir("..")
                self.username=user_current['username']
                self.time=user_current['time']
                self.progress=user_current['progress']
        else:
            self.username=name
            self.progress=progress
            self.time=time
    def save_progress(self):
        with open('{}.json'.format(self.username),'w') as file:
            json.dump({'username':self.username,'time':self.time,'progress':self.progress}, file)
    def next_levels(self):
        self.progress+=1
    def start_time(self):
        self.time_start=time.perf_counter()
    def stop_time(self):
        self.counter_second = time.perf_counter()-self.time_start
        self.total_time=round(self.counter_second)
        self.time+=self.total_time
    def progress(self):
        return self.progress
    def log_out(self):
        self.stop_time()
        self.save_progress()
    def time_(self):
        sec=timedelta(seconds=self.time)
        d=datetime(1,1,1)+sec
        total_= str("%d day:%d hour:%d min:%d sec" % (d.day-1, d.hour, d.minute, d.second))
        return total_
    def level_up(self):
        self.progress+=1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication,QTimer
class Ui_loginwindow(object):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(400, 400)
        loginwindow.setMinimumSize(QtCore.QSize(400, 400))
        loginwindow.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("12345.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginwindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 102), stop:0.326316 rgba(255, 0, 0, 130), stop:0.339799 rgba(255, 255, 255, 255), stop:0.636842 rgba(255, 255, 255, 135), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 95));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 141, 40))
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.label_2.setObjectName("label_2")
        self.username_edit = QtWidgets.QLineEdit(self.groupBox)
        self.username_edit.setGeometry(QtCore.QRect(180, 180, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.username_edit.setFont(font)
        self.username_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_edit.setText("")
        self.username_edit.setObjectName("username_edit")
        self.login_button = QtWidgets.QPushButton(self.groupBox)
        self.login_button.setGeometry(QtCore.QRect(100, 300, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgba(255, 255, 255,150);")
        self.login_button.setObjectName("login_button")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(95, 60, 212, 40))
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.label_3.setObjectName("label_3")
        self.credentials = QtWidgets.QPushButton(self.groupBox)
        self.credentials.setGeometry(QtCore.QRect(310, 360, 80, 23))
        self.credentials.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.credentials.setObjectName("credentials")
        loginwindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)
    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "PyBoysFlashcards"))
        self.label_2.setText(_translate("loginwindow", "User name:"))
        self.login_button.setText(_translate("loginwindow", "Login"))
        self.label_3.setText(_translate("loginwindow", "PyBoysFlashcards"))
        self.credentials.setText(_translate("loginwindow", "Credentials"))
        self.credentials.clicked.connect(self.credentials_) #used for connecting credentials_ function to go credentials screen.
        self.login_button.clicked.connect(self.menu_screen_)#used for connecting menu_screen_ function to go menu screen and save user.
    def get_username(self):   #hold the inside of Line_edit as a getusername 
        self.get_username=self.username_edit.text()
        return self.get_username

    def menu_screen_(self): #inside the function created a class from user.User. by the way if the user exist we take the knowledge of user, otherwise we create a user with default values. (time=0, progress=0)
        user1.username=self.get_username()
        user2=User(self.get_username)
        user1.time=user2.time
        user1.progress=user2.progress
        QtWidgets.QLineEdit(self.username_edit.text())
        self.ui=Ui_menu_window()
        self.ui.setupUi(window)
    
    def credentials_(self): #credential buttons function to go to credentials screen
        self.ui=Ui_credentialwindow()
        self.ui.setupUi(window)
class Ui_credentialwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.groupBox_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 102), stop:0.326316 rgba(255, 0, 0, 130), stop:0.339799 rgba(255, 255, 255, 255), stop:0.636842 rgba(255, 255, 255, 135), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 95));")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(310, 10, 75, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 70, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,10);\n" "border-color: rgb(255, 255, 255,10);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""border-color: rgb(255, 255, 255,10);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""border-color: rgb(255, 255, 255,10);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""border-color: rgb(255, 255, 255,10);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""border-color: rgb(255, 255, 255,10);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(0, 240, 401, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""border-color: rgb(255, 255, 255,10);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBoysFlashcards"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Creators"))
        self.label_2.setText(_translate("MainWindow", "Halit"))
        self.label_3.setText(_translate("MainWindow", "Samet"))
        self.label_4.setText(_translate("MainWindow", "Osman"))
        self.label_5.setText(_translate("MainWindow", "Mehmet"))
        self.label_6.setText(_translate("MainWindow", "The app is created to help who want to improve Dutch skills."))

        self.pushButton.clicked.connect(self.login_menu_go)#Login page button

    def login_menu_go(self): #Login menu function
        self.ui=Ui_loginwindow()
        self.ui.setupUi(window)


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(570, 550)
        menu_window.setMinimumSize(QtCore.QSize(570, 550))
        menu_window.setMaximumSize(QtCore.QSize(570, 550))
        menu_window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 570, 550))
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 102), stop:0.326316 rgba(255, 0, 0, 130), stop:0.339799 rgba(255, 255, 255, 255), stop:0.636842 rgba(255, 255, 255, 135), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 95));")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.which_user = QtWidgets.QLabel(self.groupBox)
        self.which_user.setGeometry(QtCore.QRect(290, 30, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.which_user.setFont(font)
        self.which_user.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.which_user.setObjectName("which_user")

        
        self.progress_label = QtWidgets.QLabel(self.groupBox)
        self.progress_label.setGeometry(QtCore.QRect(40, 100, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.progress_label.setFont(font)
        self.progress_label.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.progress_label.setObjectName("progress_label")
        self.progress = QtWidgets.QProgressBar(self.groupBox)
        self.progress.setGeometry(QtCore.QRect(190, 100, 341, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progress.setFont(font)
        self.progress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progress.setObjectName("progress")
        self.level_label = QtWidgets.QLabel(self.groupBox)
        self.level_label.setGeometry(QtCore.QRect(40, 190, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.level_label.setFont(font)
        self.level_label.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.level_label.setObjectName("level_label")
        self.progress_label_5 = QtWidgets.QLabel(self.groupBox)
        self.progress_label_5.setGeometry(QtCore.QRect(40, 280, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.progress_label_5.setFont(font)
        self.progress_label_5.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.progress_label_5.setObjectName("progress_label_5")
        self.total_time_show = QtWidgets.QLabel(self.groupBox)
        self.total_time_show.setGeometry(QtCore.QRect(190, 280, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.total_time_show.setFont(font)
        self.total_time_show.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.total_time_show.setObjectName("total_time_show")
        self.play = QtWidgets.QPushButton(self.groupBox)
        self.play.setGeometry(QtCore.QRect(75, 430, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.play.setObjectName("play")
        self.quit_2 = QtWidgets.QPushButton(self.groupBox)
        self.quit_2.setGeometry(QtCore.QRect(235, 430, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.quit_2.setFont(font)
        self.quit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quit_2.setObjectName("quit_2")
        self.which_user_label = QtWidgets.QLabel(self.groupBox)
        self.which_user_label.setGeometry(QtCore.QRect(170, 30, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.which_user_label.setFont(font)
        self.which_user_label.setStyleSheet("background-color: rgba(255, 255, 255, 10);")
        self.which_user_label.setObjectName("which_user_label")
        self.quit = QtWidgets.QPushButton(self.groupBox)
        self.quit.setGeometry(QtCore.QRect(395, 430, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.quit.setFont(font)
        self.quit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quit.setObjectName("quit")
        self.level = QtWidgets.QLabel(self.groupBox)
        self.level.setGeometry(QtCore.QRect(190, 190, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.level.setFont(font)
        self.level.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        
        self.level.setObjectName("level")
        self.words_counter = QtWidgets.QLabel(self.groupBox)
        self.words_counter.setGeometry(QtCore.QRect(360, 190, 61, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.words_counter.setFont(font)
        self.words_counter.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.words_counter.setText("")
        self.words_counter.setObjectName("words_counter")
        self.words_counter_2 = QtWidgets.QLabel(self.groupBox)
        self.words_counter_2.setGeometry(QtCore.QRect(420, 190, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.words_counter_2.setFont(font)
        self.words_counter_2.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.words_counter_2.setText("")
        self.words_counter_2.setObjectName("words_counter_2")
        menu_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)
        
        
        
        self.which_user.setText(user1.username) #to show username from user1 class
        self.total_time_show.setText(user1.time_()) #to show time of user with time_ method
        self.level.setText(str(user1.progress)) #to show progress of user
        self.progress.setProperty("value", (user1.progress/250)*100) #to show percentage of user's progress

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "PyBoysFlashcards"))
        self.progress_label.setText(_translate("menu_window", "Progress:"))
        self.level_label.setText(_translate("menu_window", "Level:"))
        self.progress_label_5.setText(_translate("menu_window", "Total Time:"))
        self.play.setText(_translate("menu_window", "Play"))
        self.quit_2.setText(_translate("menu_window", "Log Out"))
        self.which_user_label.setText(_translate("menu_window", "Welkom"))
        self.quit.setText(_translate("menu_window", "Quit"))



        self.quit_2.clicked.connect(self.login_go_back)#Login page button
        self.quit.clicked.connect(QCoreApplication.instance().quit)
        self.play.clicked.connect(self.game_screen_go)

    def login_go_back(self): #Login menu function
        self.ui=Ui_loginwindow()
        self.ui.setupUi(window)
    def game_screen_go(self):
        self.ui=Ui_gamescreen()
        self.ui.setupUi(window)


class Ui_gamescreen(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 102), stop:0.326316 rgba(255, 0, 0, 130), stop:0.339799 rgba(255, 255, 255, 255), stop:0.636842 rgba(255, 255, 255, 135), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 95));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.true_button = QtWidgets.QPushButton(self.frame)
        self.true_button.setGeometry(QtCore.QRect(500, 450, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.true_button.setFont(font)
        self.true_button.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(79, 158, 0);")
        self.true_button.setObjectName("true_button")
        self.false_button = QtWidgets.QPushButton(self.frame)
        self.false_button.setGeometry(QtCore.QRect(180, 450, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.false_button.setFont(font)
        self.false_button.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(255, 0, 0);")
        self.false_button.setObjectName("false_button")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(510, 30, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.label_3.setObjectName("label_3")

        self.word = QtWidgets.QLabel(self.frame)
        self.word.setGeometry(QtCore.QRect(40, 210, 720, 170))
        font = QtGui.QFont()
        font.setPointSize(52)
        font.setBold(True)
        font.setWeight(75)
        self.word.setFont(font)
        self.word.setAutoFillBackground(False)
        self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 0, 255);")
        self.word.setText("")
        self.word.setAlignment(QtCore.Qt.AlignCenter)
        self.word.setObjectName("word")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(620, 530, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.pushButton.setObjectName("pushButton")
        self.twenty = QtWidgets.QLabel(self.frame)
        self.twenty.setGeometry(QtCore.QRect(640, 30, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.twenty.setFont(font)
        self.twenty.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.twenty.setObjectName("twenty")
        self.twenty.setAlignment(QtCore.Qt.AlignCenter)

        self.time_frame = QtWidgets.QLabel(self.frame)
        self.time_frame.setGeometry(QtCore.QRect(345, 90, 120, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.time_frame.setFont(font)
        self.time_frame.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.time_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.time_frame.setObjectName("time_frame")

        self.known_word = QtWidgets.QLabel(self.frame)
        self.known_word.setGeometry(QtCore.QRect(712, 30, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.known_word.setFont(font)
        self.known_word.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.known_word.setObjectName("known_word")
        self.known_word.setAlignment(QtCore.Qt.AlignCenter)
        self.label_level = QtWidgets.QLabel(self.frame)
        self.label_level.setGeometry(QtCore.QRect(30, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_level.setFont(font)
        self.label_level.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.label_level.setObjectName("known_word")
        self.label_level.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_level1 = QtWidgets.QLabel(self.frame)
        self.label_level1.setGeometry(QtCore.QRect(120, 30, 60, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_level1.setFont(font)
        self.label_level1.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.label_level1.setObjectName("known_word")
        self.label_level1.setAlignment(QtCore.Qt.AlignCenter)

        self.next_level = QtWidgets.QPushButton(self.frame)
        self.next_level.setGeometry(QtCore.QRect(640, 120, 120, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.next_level.setFont(font)
        self.next_level.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(79, 158, 0);")
        self.next_level.setObjectName("next_level")
        self.next_level.setVisible(False)
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(690, 30, 16, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,10);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyBoysFlashcards"))
        self.true_button.setText(_translate("MainWindow", "True"))
        self.false_button.setText(_translate("MainWindow", "False"))
        self.label_3.setText(_translate("MainWindow", "Progress:"))
        self.pushButton.setText(_translate("MainWindow", "End Game"))
        self.label.setText(_translate("MainWindow", "/"))
        self.label_level.setText(_translate("MainWindow", "Level"))
        self.next_level.setText(_translate('MainWindow','Next Level'))
		
        self.pushButton.clicked.connect(self.go_back_main)# to run go_back_main function 
        sels.next_level.clicked.connect(self.level_up)#to play next level

        self.game1=Game(level=(user1.progress+1)) #creating a game class with level
        self.game1.begin()
        self.label_level1.setText(str(user1.progress+1)) # to show level in label_level1

        self.start=True #to start counter
        self.count=30 #counter 30 representing 3 seconds
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        
    def showTime(self):
        if self.start:
            self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 255, 0);") 
            if self.game1.known_words<20:
                self.word.setText(self.game1.flashcard()[0]) #to show dutch words
                self.count -= 1
                if self.count == -1:
                    self.start = False
                    self.true_button.clicked.connect(self.true_button_)
                    self.false_button.clicked.connect(self.false_button_)
                    self.word.setStyleSheet("background-color: rgb(255, 255, 255,10);\n""color: rgb(0, 0,255);")  
                    self.word.setText(self.game1.flashcard()[1]) #to show meaning of dutch words after 3 seconds
            else:
                self.word.setText("Gefeliciteerd") # after finishing level to show gefeliciteerd
                self.next_level.setVisible(True) #next level button activated
        if self.start:
            text = str(self.count/10) + " s"
            self.time_frame.setText(text)
    def go_back_main(self):
        self.start=False
        if self.game1.known_words==20:
            user1.level_up()
        user1.log_out()
        self.ui=Ui_menu_window()
        self.ui.setupUi(window)
    def true_button_(self):
        if self.start == False:
            self.game1.progress(True)
            self.twenty.setText(str(self.game1.known_words))
            self.known_word.setText(str(self.game1.total_words))
            self.time_improve()
    def false_button_(self):
        if self.start == False:
            self.game1.progress(False)
            self.twenty.setText(str(self.game1.known_words))
            self.known_word.setText(str(self.game1.total_words))
            self.time_improve()
    def level_up(self):
        user1.level_up()
        user1.save_progress()
        self.game1=Game(user1.progress+1)
        self.game1.begin()
        self.label_level1.setText(str(user1.progress+1))
        self.twenty.setText(str(self.game1.known_words))
        self.known_word.setText(str(self.game1.total_words))
        self.next_level.setVisible(False)
        self.time_improve()
    def time_improve(self):
        self.start=True
        self.count=30

if __name__ == "__main__":
    import sys
    user1=User()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_loginwindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())