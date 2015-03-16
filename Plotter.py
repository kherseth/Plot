# -*- coding: utf-8 -*-
"""
Created on Sun Mar 08 12:57:41 2015

@author: kim
"""

import sys
import numpy
from PyQt4 import QtGui, QtCore, uic, Qt
import matplotlib.pyplot as plt
import PyQt4.Qwt5 as Qwt
import serial
from threading import Thread
import time, datetime
 
 
#global connected
#global win

class TestApp(QtGui.QMainWindow):
       # DataTimer = QtCore.QTimer()
        ser = serial.Serial("COM4", 38400)
        ser.setTimeout(0.2)
        DataTimer = QtCore.QTimer()
        first = True
        plotList = []
        
        data = ""
        
        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.ui = uic.loadUi('plot.ui')        
            self.ui.show()                 
            self.connect(self.ui.okButton, QtCore.SIGNAL("clicked()"), self.buttonFn)
            self.connect(self.ui.OpenCom, QtCore.SIGNAL("clicked()"), OpenComClicked)
            self.connect(self.ui.CloseCom, QtCore.SIGNAL("clicked()"), CloseComClicked)            
            self.connect(self.DataTimer, QtCore.SIGNAL("timeout()"), self.updatePlot)
            self.connect(self.ui.measurandList, QtCore.SIGNAL("itemClicked(QListWidgetItem *)"), self.listClick )          
            self.DataTimer.start(2)
            self.ui.qwtPlot.setAutoReplot(True)
            #self.ui.measurandList.addItem("test")
#            self.ui.measurandList.checkable(True)
            self.setupPlot()
#            self.ui.dataView.
        
        def listClick(self):
            Item = self.ui.measurandList.currentRow()
            
            if self.plotList[Item].curve.isVisible():          
                self.plotList[Item].curve.hide()
                self.ui.measurandList.item(Item).setCheckState(QtCore.Qt.Unchecked)
            else:
                self.plotList[Item].curve.show()
                self.ui.measurandList.item(Item).setCheckState(QtCore.Qt.Checked)
        
        def setupPlot(self):
            temp = self.ser.readline() # 
            
            tempsplit = temp.split(';')
            measurands = len(tempsplit)
            self.ui.label_4.setText(str(len(tempsplit)))

            if self.first: # This runs only once to initialize curveitems
                for i in range(measurands):
                    self.ui.measurandList.addItem('Data %s' % (i+1))
                
                for i in (range(measurands)):
                    self.plotList.append(plotItem(i))
                    print self.plotList
                    self.plotList[i].curve.attach(self.ui.qwtPlot)
                    #self.plotList[i].curve.show()
                self.first = False
            
            for i in range(self.ui.measurandList.count()):
                self.ui.measurandList.item(i).setFlags(self.ui.measurandList.item(i).flags() | QtCore.Qt.ItemIsUserCheckable)
                self.ui.measurandList.item(i).setCheckState(QtCore.Qt.Checked)
        
        def updatePlot(self):
            
            #self.data = self.ser.readline()
            temp = self.ser.readline() # 
            
            tempsplit = temp.split(';')
            measurands = len(tempsplit)
            self.ui.label_4.setText(str(len(tempsplit)))            
            
            for i in (range(measurands)): # Update all measurands with the current values
                self.plotList[i].update(tempsplit[i])
                
        def retrieveData(self):
            
            print self.data
        def buttonFn():
            print("button clicked")
            

class plotItem():
    
        
    
    def __init__(self, ID):
        self.numPoints=1000
        self.xs=numpy.arange(self.numPoints)
        self.ys=numpy.sin(3.14159*self.xs*10/self.numPoints)
        self.identity = 0
        self.curve = Qwt.QwtPlotCurve()
        self.identity = ID
        print("Init of plot %s" % ID)
    
    def update(self, newData):
        self.ys=numpy.roll(self.ys,-1)
        self.ys[0] = newData
        #print self.identi
        self.curve.setData(self.xs, self.ys)
    
    def clear():
        for i in self.ys:
            self.ys[i] = 0



class WorkThread(QtCore.QThread):
 def __init__(self):
  QtCore.QThread.__init__(self)

 def __del__(self):
  self.wait()
   
def OpenComClicked():
    ser.open()
    print("button clicked")

    
def CloseComClicked():
    print("button clicked")
    
def main():
    global app
    global win
    app = QtGui.QApplication(sys.argv)
    win = TestApp()
    sys.exit(app.exec_())
    print("Exited")
    
if __name__ == "__main__":
        
    main()
    
    
 