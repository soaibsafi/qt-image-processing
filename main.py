from PyQt5 import QtGui
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget,  QPlainTextEdit, QScrollArea, QFileDialog)

class WidgetSetup(QDialog):
    def __init__(self, parent=None):
        super(WidgetSetup, self).__init__(parent)

        #self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLabel')

        self.originalPalette = QApplication.palette()

        # Top Layout
        openDirectory = QPushButton('Open Directory')
        openDirectory.clicked.connect(self.openDirectory)
        saveImage = QPushButton('Save Image')
        topLayout = QHBoxLayout()
        topLayout.addWidget(openDirectory)
        topLayout.addWidget(saveImage)

        #Image Viewer Layout
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap("sample.jpg"))

        #self.resize(800, 600)

        imageLayout = QGridLayout()
        imageLayout.addWidget(imageLabel,0,0)

        #Bottom Layout
        self.colorValuesGroup()
        self.colorThreshold1()
        self.colorThreshold2()

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
        lineEditRGB = QLineEdit()
        lineEditRGB.setReadOnly(True)

        labelHSV = QLabel('HSV')
        lineEditHSV = QLineEdit()
        lineEditHSV.setReadOnly(True)

        labelLAB = QLabel('LAB')
        lineEditLAB = QLineEdit()
        lineEditLAB.setReadOnly(True)

        colorDetails = QPlainTextEdit()
        colorDetails.setReadOnly(True)

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
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        print(fileName)
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer", "Cannot load %s." % fileName)
                return

            print(image)
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetSetup()
    gallery.show()
    sys.exit(app.exec_())