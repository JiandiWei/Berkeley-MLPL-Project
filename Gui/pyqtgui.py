#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:47:28 2017

@author: jiandiwei
"""
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
qtCreatorFile = "test.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        ## some variable and initialization 
        self.Input_text.insertPlainText('type your patent description here')
        
        ## Logo
        # 
       # myScaledPixmap = myPixmap.scaled(self.label.size(), Qt.KeepAspectRatio)
        #self.label_logo.setPixmap(myScaledPixmap)
        self.label_logo.setPixmap(QPixmap("avatar-small.PNG")) 
        self.label_logo.show() 
            
        ## button 
        self.pushButton_open.clicked.connect(self.open_file)
        self.pushButton_refresh.clicked.connect(self.refresh)
        self.pushButton_retrieve.clicked.connect(self.retrieve)
        
        ## Menu action 
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave_Input.triggered.connect(self.save_input_file)
        self.actionSave_Output.triggered.connect(self.save_output_file)
        self.actionContact_Us.triggered.connect(self.contact_us)
        
        
    
    def open_file(self):
       # Open the file from directory 
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")		
        if dlg.exec_():
            file_adress = dlg.selectedFiles()
            f = open(file_adress[0], 'r')
            with f:                
                self.Input_text.insertPlainText(f.read())
        
    def refresh(self):
        FILE_UPLOADED=False
        MODEL_INPUT=None
        self.Input_text.clear()
        self.Output_text.clear()
    
    def retrieve(self):
        self.Output_text.clear()
        k="""       
            8521642
            8352357
            8635150
            7930237
            8108492
            8346894
            8037158
            5987500
            8394406
            8206740

                    """
        
        
        self.Output_text.insertPlainText(k)
        #if not self.Input_text.toPlainText():
            #self.Output_text.insertPlainText("Please type description first")
       # elif len(self.Input_text.toPlainText())< 25 :
            #self.Output_text.insertPlainText("Please give more information for a better result")
            
        #self.Output_text.insertPlainText()
            
        
    def save_input_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')+".txt"
        file = open(name,'w')
        text = self.Input_text.toPlainText()
        file.write(text)
        file.close()

    
        
    def save_output_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')+".txt"
        file = open(name,'w')
        text = self.Output_text.toPlainText()
        file.write(text)
        file.close()
         
    def contact_us(self):
        self.Input_text.clear()
        self.Output_text.clear()
        text="""       
            Lakshay Seth <lakshayseth@berkeley.edu>
            Tu Ni <nitu@berkeley.edu>
            Ethan Wells <ethan_wells@berkeley.edu>
            Titouan Jehl <titouan.jehl@berkeley.edu>
            Jiandi Wei <jiandi.wei@berkeley.edu
                    """
        self.Output_text.insertPlainText(text)
       
    
    
    
    
    
    
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())