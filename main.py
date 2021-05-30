# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from graph import Graph



class Ui_mainClass(object):
    
    def setupUi(self, mainClass):
        mainClass.setObjectName("mainClass")
        self.mainGraph= None
        mainClass.resize(1311, 611)
        self.centralwidget = QtWidgets.QWidget(mainClass)
        self.centralwidget.setObjectName("centralwidget")
        self.sizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.sizeLabel.setEnabled(True)
        self.sizeLabel.setGeometry(QtCore.QRect(60, 80, 91, 31))
        self.sizeLabel.setObjectName("sizeLabel")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 130, 471, 311))
        self.tableView.setObjectName("tableView")
        self.sizeInput = QtWidgets.QSpinBox(self.centralwidget)
        self.sizeInput.setGeometry(QtCore.QRect(160, 80, 111, 31))
        self.sizeInput.setMinimum(2)
        self.sizeInput.setMaximum(10)
        self.sizeInput.setObjectName("sizeInput")
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(290, 80, 111, 31))
        self.genButton.setObjectName("genButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 20, 321, 31))
        self.label.setObjectName("label")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(180, 500, 89, 25))
        self.calculateButton.setObjectName("calculateButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 460, 201, 21))
        self.label_2.setObjectName("label_2")
        self.pathInput = QtWidgets.QLineEdit(self.centralwidget)
        self.pathInput.setGeometry(QtCore.QRect(250, 460, 241, 25))
        self.pathInput.setObjectName("pathInput")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 80, 121, 31))
        self.label_3.setObjectName("label_3")
        self.degreeNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.degreeNumber.setGeometry(QtCore.QRect(680, 80, 71, 31))
        self.degreeNumber.setObjectName("degreeNumber")
        self.sumNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.sumNumber.setGeometry(QtCore.QRect(890, 80, 71, 31))
        self.sumNumber.setObjectName("sumNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 80, 121, 31))
        self.label_4.setObjectName("label_4")
        self.degreeMinNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.degreeMinNumber.setGeometry(QtCore.QRect(1090, 80, 71, 31))
        self.degreeMinNumber.setObjectName("degreeMinNumber")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(980, 80, 121, 31))
        self.label_5.setObjectName("label_5")
        self.graphImage = QtWidgets.QLabel(self.centralwidget)
        self.graphImage.setGeometry(QtCore.QRect(550, 190, 351, 321))
        self.graphImage.setScaledContents(True)
        self.graphImage.setObjectName("graphImage")
        self.pathImage = QtWidgets.QLabel(self.centralwidget)
        self.pathImage.setGeometry(QtCore.QRect(910, 190, 351, 321))
        self.pathImage.setScaledContents(True)
        self.pathImage.setObjectName("pathImage")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 160, 141, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1010, 160, 141, 17))
        self.label_7.setObjectName("label_7")
        mainClass.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainClass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1311, 22))
        self.menubar.setObjectName("menubar")
        self.menuProyecto = QtWidgets.QMenu(self.menubar)
        self.menuProyecto.setObjectName("menuProyecto")
        mainClass.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainClass)
        self.statusbar.setObjectName("statusbar")
        mainClass.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuProyecto.menuAction())

        self.retranslateUi(mainClass)
        QtCore.QMetaObject.connectSlotsByName(mainClass)
        self.calculateButton.clicked.connect(self.show_graph)
        self.genButton.clicked.connect(self.genTable)

    def retranslateUi(self, mainClass):
        _translate = QtCore.QCoreApplication.translate
        mainClass.setWindowTitle(_translate("mainClass", "mainClass"))
        self.sizeLabel.setText(_translate("mainClass", "Tamaño"))
        self.genButton.setText(_translate("mainClass", "Generar Tabla"))
        self.label.setText(_translate("mainClass", "Proyecto Grafos - Teoría de la Computación"))
        self.calculateButton.setText(_translate("mainClass", "Calcular"))
        self.label_2.setText(_translate("mainClass", "Ingrese un camino a calcular"))
        self.label_3.setText(_translate("mainClass", "Grado del Grafo"))
        self.label_4.setText(_translate("mainClass", "Suma del Grafo"))
        self.label_5.setText(_translate("mainClass", "Grado Menor"))
        self.graphImage.setText(_translate("mainClass", ""))
        self.pathImage.setText(_translate("mainClass", ""))
        self.label_6.setText(_translate("mainClass", "Grafo"))
        self.label_7.setText(_translate("mainClass", "Camino"))
        self.menuProyecto.setTitle(_translate("mainClass", "Proyecto"))

    def genTable(self):
        size = int(self.sizeInput.text())
        table_headers=[str(i) for i in range(1,size)]
        adjMatrix = []
        for i in range(size):
            adjMatrix.append([0 for i in range(size)])

        self.mainGraph = Graph(adjMatrix,size)
        self.mainGraph.printAdjMatrix()
        self.tableView.setHorizontalHeaderLabels(table_headers)
        self.tableView.setVerticalHeaderLabels(table_headers)
        self.tableView.setRowCount(size)
        self.tableView.setColumnCount(size)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row in range(0, size):
            for column in range(0, size):
                relationInput = QtWidgets.QSpinBox()
                relationInput.setMinimum(0)
                relationInput.setMaximum(1)
                relationInput.setObjectName(""+str(row)+"-"+str(column))
                relationInput.setValue(self.mainGraph.getAdjMatrix()[row][column])
                self.tableView.setCellWidget(row,column,relationInput)


    def show_graph(self):
        self.graphImage.setPixmap(QtGui.QPixmap("graph.png"))
        self.pathImage.setPixmap(QtGui.QPixmap("graphPath.png"))

       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainClass = QtWidgets.QMainWindow()
    ui = Ui_mainClass()
    ui.setupUi(mainClass)
    mainClass.show()
    sys.exit(app.exec_())



