from MouseTraker import MouseTracker

from skimage import color
import cv2
import os
import re
import numpy as np
import math
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter, QColor, QKeyEvent
from PyQt5.QtCore import QDateTime, Qt, QTimer, QPoint, QEvent
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,  QPlainTextEdit, QScrollArea, QFileDialog, QMainWindow)

global colorDetailsList
colorDetailsList = [['RGB'], ['HSV'], ['LAB']]

class WidgetSetup(QDialog):
    def __init__(self, parent=None):
        super(WidgetSetup, self).__init__(parent)
        QtWidgets.qApp.installEventFilter(self)

        #self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLabel')

        self.originalPalette = QApplication.palette()

        # Top Layout
        openDirectory = QPushButton('Open Directory')
        openDirectory.clicked.connect(self.openDirectory)

        saveImage = QPushButton('Save Image')
        saveImage.clicked.connect(self.save_image)

        topLayout = QHBoxLayout()
        topLayout.addWidget(openDirectory)
        topLayout.addWidget(saveImage)

        #Image Viewer Layout
        self.img = QImage('D:\\Cloud\\Github\\Qt-image-processor\\sdfsd.png')
        self.pixmap = QPixmap(QPixmap.fromImage(self.img))
        global imageLabel
        imageLabel = QLabel()
        imageLabel.setPixmap(self.pixmap)
        imageLabel.mousePressEvent = self.getPixel

        tracker = MouseTracker(imageLabel)
        tracker.positionChanged.connect(self.on_positionChanged)

        self.label_position = QLabel(
            imageLabel, alignment=Qt.AlignCenter
        )
        self.label_position.setStyleSheet('background-color: white; border: 1px solid black')

        self.resize(800, 600)

        imageLayout = QGridLayout()
        imageLayout.addWidget(imageLabel,0,0)

        #Bottom Layout
        self.colorValuesGroup()
        self.colorThreshold1()
        self.colorThreshold2()
        lineEditRGB.setStyleSheet("color: black;  background-color: red")
        lineEditRGB.setAlignment(Qt.AlignCenter)

        lineEditHSV.setStyleSheet("color: black;  background-color: red")
        lineEditHSV.setAlignment(Qt.AlignCenter)

        lineEditLAB.setStyleSheet("color: black;  background-color: red")
        lineEditLAB.setAlignment(Qt.AlignCenter)

        saveColorValue.clicked.connect(self.save_csv_file)

        # Main Layout
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0)
        mainLayout.addLayout(imageLayout, 1, 1, Qt.AlignCenter)
        mainLayout.addWidget(self.colorValuesGroup, 2, 0)
        mainLayout.addWidget(self.colorThreshold1, 2, 1)
        mainLayout.addWidget(self.colorThreshold2, 2, 2)

        self.setLayout(mainLayout)


    def colorValuesGroup(self):
        self.colorValuesGroup = QGroupBox('Color Values')

        labelRGB = QLabel('RGB')
        global lineEditRGB
        lineEditRGB = QLineEdit()
        lineEditRGB.setReadOnly(True)

        labelHSV = QLabel('HSV')
        global lineEditHSV

        lineEditHSV = QLineEdit()
        lineEditHSV.setReadOnly(True)

        labelLAB = QLabel('LAB')
        global lineEditLAB
        lineEditLAB = QLineEdit()
        lineEditLAB.setReadOnly(True)

        global colorDetails
        colorDetails = QPlainTextEdit()
        colorDetails.setReadOnly(True)
        colorDetails.setPlaceholderText('Nr. RGB HSV LAB')
        colorDetails.setPlainText("Nr  RGB  HSV  LAB")


        global saveColorValue
        saveColorValue = QPushButton('Save Color Values')

        layout = QGridLayout()
        layout.addWidget(labelRGB, 0,0)
        layout.addWidget(lineEditRGB, 0, 1)
        layout.addWidget(labelHSV, 1, 0)
        layout.addWidget(lineEditHSV, 1, 1)
        layout.addWidget(labelLAB, 2, 0)
        layout.addWidget(lineEditLAB, 2, 1)
        layout.addWidget(colorDetails, 0,2, 3, 4)
        layout.addWidget(saveColorValue, 3,2, 2, 2)

        self.colorValuesGroup.setLayout(layout)

    def colorThreshold1(self):
        self.colorThreshold1 = QGroupBox('Color Threshold 1')

        labelRGBMin = QLabel('RGB(min)')
        lineEditRGBMin = QLineEdit()
        lineEditRGBMin.setReadOnly(True)

        labelRGBMax = QLabel('RGB(max)')
        lineEditRGBMax = QLineEdit()
        lineEditRGBMax.setReadOnly(True)

        labelHSVMin = QLabel('HSV(min)')
        lineEditHSVMin = QLineEdit()
        lineEditHSVMin.setReadOnly(True)

        labelHSVMax = QLabel('HSV(max)')
        lineEditHSVMax = QLineEdit()
        lineEditHSVMax.setReadOnly(True)

        labelLABMin = QLabel('LAB(min)')
        lineEditLABMin = QLineEdit()
        lineEditLABMin.setReadOnly(True)

        labelLABMax = QLabel('LAB(max)')
        lineEditLABMax = QLineEdit()
        lineEditLABMax.setReadOnly(True)

        applyThreshold1 = QPushButton('Apply Threshold 1')

        layout = QGridLayout()
        layout.addWidget(labelRGBMin, 0, 0)
        layout.addWidget(lineEditRGBMin, 0, 1)
        layout.addWidget(labelRGBMax, 0, 2)
        layout.addWidget(lineEditRGBMax, 0, 3)

        layout.addWidget(labelHSVMin, 1, 0)
        layout.addWidget(lineEditHSVMin, 1, 1)
        layout.addWidget(labelHSVMax, 1, 2)
        layout.addWidget(lineEditHSVMax, 1, 3)

        layout.addWidget(labelLABMin, 2, 0)
        layout.addWidget(lineEditLABMin, 2, 1)
        layout.addWidget(labelLABMax, 2, 2)
        layout.addWidget(lineEditLABMax, 2, 3)
        layout.addWidget(applyThreshold1, 3, 2,1,1)

        self.colorThreshold1.setLayout(layout)

    def colorThreshold2(self):
        self.colorThreshold2 = QGroupBox('Color Threshold 2')

        labelRGBMin = QLabel('RGB(min)')
        lineEditRGBMin = QLineEdit()
        lineEditRGBMin.setReadOnly(True)

        labelRGBMax = QLabel('RGB(max)')
        lineEditRGBMax = QLineEdit()
        lineEditRGBMax.setReadOnly(True)

        labelHSVMin = QLabel('HSV(min)')
        lineEditHSVMin = QLineEdit()
        lineEditHSVMin.setReadOnly(True)

        labelHSVMax = QLabel('HSV(max)')
        lineEditHSVMax = QLineEdit()
        lineEditHSVMax.setReadOnly(True)

        labelLABMin = QLabel('LAB(min)')
        lineEditLABMin = QLineEdit()
        lineEditLABMin.setReadOnly(True)

        labelLABMax = QLabel('LAB(max)')
        lineEditLABMax = QLineEdit()
        lineEditLABMax.setReadOnly(True)

        applyThreshold2 = QPushButton('Apply Threshold 2')

        layout = QGridLayout()
        layout.addWidget(labelRGBMin, 0, 0)
        layout.addWidget(lineEditRGBMin, 0, 1)
        layout.addWidget(labelRGBMax, 0, 2)
        layout.addWidget(lineEditRGBMax, 0, 3)

        layout.addWidget(labelHSVMin, 1, 0)
        layout.addWidget(lineEditHSVMin, 1, 1)
        layout.addWidget(labelHSVMax, 1, 2)
        layout.addWidget(lineEditHSVMax, 1, 3)

        layout.addWidget(labelLABMin, 2, 0)
        layout.addWidget(lineEditLABMin, 2, 1)
        layout.addWidget(labelLABMax, 2, 2)
        layout.addWidget(lineEditLABMax, 2, 3)
        layout.addWidget(applyThreshold2, 3, 2,1,1)

        self.colorThreshold2.setLayout(layout)

    def openDirectory(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '', 'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)

        #print(fileName[0])
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

        global imgName, imgDir
        splitimage = fileName.split('/')

        imgName = "\\".join(splitimage)
        imgDir = "\\".join(splitimage[:-1])

        #print(imgDir)
        self.set_image(imgName)

    def getPixel(self, event):
        x = event.pos().x()
        y = event.pos().y()
        #print(x,y)
        c = self.img.pixel(x, y)  # color code (integer): 3235912
        # depending on what kind of value you like (arbitary examples)
        c_qobj = QColor(c)  # color object
        c_rgb = QColor(c).getRgb()  # 8bit RGBA: (255, 23, 0, 255)
        r = c_qobj.red()
        g = c_qobj.green()
        b = c_qobj.blue()
        colrgb = np.uint8([[[r,g,b]]])

        HSV = cv2.cvtColor(colrgb, cv2.COLOR_RGB2HSV)
        H = (HSV[0,0,0] * 2)
        S = (HSV[0,0,1]  / 255.0)
        V = (HSV[0,0,2] / 255.0)

        LAB = cv2.cvtColor(colrgb, cv2.COLOR_RGB2Lab)
        L = (LAB[0][0][0] * 100//255.0)
        A = (LAB[0][0][1] - 128)
        B = (LAB[0][0][2] - 128)

        rgbText = "%d, %d, %d" % (r,g,b)
        hsvText = "%d, %d, %d" % (H,S,V)
        labText = "%d, %d, %d" % (L,A,B)

        lineEditRGB.setText(rgbText)
        lineEditHSV.setText(hsvText)
        lineEditLAB.setText(labText)

        #colText = colorDetails.toPlainText()
        colorDetailsList[0].append(rgbText)
        colorDetailsList[1].append(hsvText)
        colorDetailsList[2].append(labText)
        text = rgbText+'    '+hsvText+'    '+labText
        colorDetails.appendPlainText(text)
        #print(text)

    #@QtCore.pyqtSlot(QPoint)
    def on_positionChanged(self, pos):
        delta = QPoint(-25, 30)
        self.label_position.show()
        self.label_position.move(pos + delta)

        c = self.img.pixel(pos.x(), pos.y())  # color code (integer): 3235912
        # depending on what kind of value you like (arbitary examples)
        c_qobj = QColor(c)  # color object
        c_rgb = QColor(c).getRgb()
        r = c_qobj.red()
        g = c_qobj.green()
        b = c_qobj.blue()
        #self.label_position.setText("(%d, %d)" % (pos.x(), pos.y()))
        self.label_position.setText("(%d, %d, %d)" % (r,g,b))
        self.label_position.adjustSize()

    def save_csv_file(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()', '',
                                                  'File (*.csv)', options=options)
        with open(fileName, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(colorDetailsList)
        f.close()
        colorDetailsList.clear()
        #print(colorDetailsList)

    def save_image(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        pixmap_r.save(fileName)
        #QFileDialog.saveFileContent( fileContent)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Right:
                self.get_next_image()
            elif key == Qt.Key_Left:
                self.get_previous_image()
            return True
        return super(WidgetSetup, self).eventFilter(source, event)

    def get_next_image(self):
        print('Next Image')

        images = self.load_images_from_folder(imgDir)
        print(images)
        print(imgName)
        if imgName in images:
            i = images.index(imgName)+1
            self.set_image(images[i])


    def get_previous_image(self):
        print('Previous Image')

    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = os.path.join(folder, filename)
            if img is not None:
                images.append(img)

        r = re.compile(".*\.(jpg|png|jpeg|bmp|gif)")
        imagelist = list(filter(r.match, images))
        return imagelist

    def set_image(self, filename):
        pixmap = QPixmap(filename)
        pixmap_r = pixmap.scaled(800, 600, Qt.KeepAspectRatio)
        imageLabel.setPixmap(QPixmap(pixmap_r))
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    gallery = WidgetSetup()
    gallery.show()
    sys.exit(app.exec_())