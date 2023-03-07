
import os
import sys
import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QFileDialog, QSplitter

from Sketchpad import Sketchpad

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']


class Ui_MainWindow(QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 612)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color:rgb(27, 47, 117)\n"
                                 "    border-bottom-left-radius: 50px;\n"
                                 "    border-top-left-radius: 10px;\n"
                                 "    border-bottom-right-radius:20px;\n"
                                 "    border-top-right-radius:50px;\n"
                                 "    \n"
                                 "}\n"
                                 "")
        MainWindow.setIconSize(QtCore.QSize(60, 24))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
                                         "    background-color:rgb(2, 21, 85)\n"
                                         "    border-bottom-left-radius: 50px;\n"
                                         "    border-top-left-radius: 10px;\n"
                                         "    border-bottom-right-radius:20px;\n"
                                         "    border-top-right-radius:50px;\n"
                                         "    \n"
                                         "}\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")

        # 获取颜色列表(字符串类型)（*）
        self.__colorList = QColor.colorNames()

        # 画板区域（*）
        self.__paintBoard = Sketchpad(self)
        # 设定画板区域位置（30，110）（*）
        self.__paintBoard.setGeometry(QtCore.QRect(30, 110, 611, 461))

        # 上传图片按钮（-）
        self.uploadbutten = QtWidgets.QPushButton(self.centralwidget)
        self.uploadbutten.setGeometry(QtCore.QRect(680, 30, 171, 41))
        self.uploadbutten.setStyleSheet("QPushButton {\n"
                                        "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                        "    stop:0 rgb(231, 255, 246), stop:1 rgb(255, 250, 235));\n"
                                        "    color:rgb(57, 91, 3);\n"
                                        "border-bottom-left-radius:20px;\n"
                                        "    border-top-left-radius:20px;\n"
                                        "    border-bottom-right-radius:20px;\n"
                                        "    border-top-right-radius:20px;\n"
                                        "    font-size: 16px;\n"
                                        "    \n"
                                        "}\n"
                                        " \n"
                                        "QPushButton:hover {\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                        "    stop:0 rgb(247, 233, 255), stop:1 rgb(237, 255, 245));\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color: rgb(228, 255, 237);\n"
                                        "    color:white;\n"
                                        "}")
        self.uploadbutten.setObjectName("uploadbutten")

        # 清空画板区域按钮（*）
        self.clearbutton = QtWidgets.QPushButton(self.centralwidget)
        self.clearbutton.setGeometry(QtCore.QRect(680, 110, 171, 41))
        self.clearbutton.setStyleSheet("QPushButton {\n"
                                       "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                       "    stop:0 #cbffe8, stop:1 #faff98);\n"
                                       "    color:rgb(57, 91, 3);\n"
                                       "    padding: 4px;\n"
                                       "    min-width: 65px;\n"
                                       "    min-height: 12px;\n"
                                       "    border-bottom-left-radius:20px;\n"
                                       "    border-top-left-radius:20px;\n"
                                       "    border-bottom-right-radius:20px;\n"
                                       "    border-top-right-radius:20px;\n"
                                       "    font-size: 16px;\n"
                                       "}\n"
                                       " \n"
                                       "QPushButton:hover {\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                       "    stop:0 #FF6465, stop:1 #9198FF);\n"
                                       "    color:white;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    background-color: rgb(65, 65, 65);\n"
                                       "    color:white;\n"
                                       "}")
        self.clearbutton.setObjectName("clearbutton")
        self.savebutton = QtWidgets.QPushButton(self.centralwidget)
        # 将按键按下信号与画板清空函数相关联（*）
        self.clearbutton.clicked.connect(self.__paintBoard.Clear)

        # 保存画板内容作为图片按钮（*）
        self.savebutton.setGeometry(QtCore.QRect(680, 170, 171, 41))
        self.savebutton.setStyleSheet("QPushButton {\n"
                                      "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                      "    stop:0 rgb(199, 246, 255), stop:1 rgb(255, 152, 233));\n"
                                      "    color:rgb(57, 91, 3);\n"
                                      "    padding: 4px;\n"
                                      "    min-width: 65px;\n"
                                      "    min-height: 12px;\n"
                                      "    border-bottom-left-radius:20px;\n"
                                      "    border-top-left-radius:20px;\n"
                                      "    border-bottom-right-radius:20px;\n"
                                      "    border-top-right-radius:20px;\n"
                                      "    font-size: 16px;\n"
                                      "}\n"
                                      " \n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                      "    stop:0 #FF6465, stop:1 #9198FF);\n"
                                      "    color:white;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgb(65, 65, 65);\n"
                                      "    color:white;\n"
                                      "}")
        self.savebutton.setObjectName("savebutton")
        self.savebutton.clicked.connect(self.on_btn_Save_Clicked)

        # 退出按钮（*）
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setGeometry(QtCore.QRect(700, 500, 121, 71))
        self.exitbutton.setStyleSheet("QPushButton {\n"
                                      "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                      "    stop:0 #e66465, stop:1 #9198e5);\n"
                                      "    color:rgb(227, 227, 227);\n"
                                      "    padding: 4px;\n"
                                      "    min-width: 65px;\n"
                                      "    min-height: 12px;\n"
                                      "    border-bottom-left-radius:30px;\n"
                                      "    border-top-left-radius:30px;\n"
                                      "    border-bottom-right-radius:30px;\n"
                                      "    border-top-right-radius:30px;\n"
                                      "    font-size: 16px;\n"
                                      "}\n"
                                      " \n"
                                      "QPushButton:hover {\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
                                      "    stop:0 #FF6465, stop:1 #9198FF);\n"
                                      "    color:white;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: rgb(65, 65, 65);\n"
                                      "    color:white;\n"
                                      "}")
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.clicked.connect(self.Quit)

        self.splitter = QSplitter(self)  # 占位符
        # sub_layout.addWidget(splitter)
        self.splitter.setObjectName("splitter")

        # 橡皮擦选择（*）
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(710, 290, 121, 41))
        self.checkBox.setStyleSheet("QCheckBox {\n"
                                    "  \n"
                                    "    color:rgb(57, 91, 3);\n"
                                    "    padding: 4px;\n"
                                    "    min-width: 65px;\n"
                                    "    min-height: 12px;\n"
                                    "    border-bottom-left-radius:3px;\n"
                                    "    border-top-left-radius:3px;\n"
                                    "    border-bottom-right-radius:3px;\n"
                                    "    border-top-right-radius:3px;\n"
                                    "    font-size: 16px;\n"
                                    "}\n"
                                    " \n"
                                    "")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.clicked.connect(self.on_cbtn_Eraser_clicked)

        # 图片输入框完整路径
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 30, 631, 31))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit{\n"
                                         "border-bottom-left-radius:20px;\n"
                                         "    border-top-left-radius:20px;\n"
                                         "    border-bottom-right-radius:20px;\n"
                                         "    border-top-right-radius:20px;\n"
                                         "    font-size: 20px;\n"
                                         "}")
        self.plainTextEdit.setPlaceholderText("请输入图片完整的文件路径,如F:\picture.png,不带中文和空格")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 85, 871, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.uploadbutten.clicked.connect(MainWindow.push_button_click)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.uploadbutten.setText(_translate("MainWindow", "上传图片"))
        self.clearbutton.setText(_translate("MainWindow", "清空手写板"))
        self.savebutton.setText(_translate("MainWindow", "保存并识别"))
        self.exitbutton.setText(_translate("MainWindow", "退出程序"))
        self.checkBox.setText(_translate("MainWindow", "使用橡皮擦"))

    def Quit(self):
        self.close()

    # 保存图片函数
    def on_btn_Save_Clicked(self):
        savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\imgs', '*.png')
        print(savePath)
        if savePath[0] == "":
            print("Save cancel")
            return
        image = self.__paintBoard.GetContentAsQImage()
        image.save(savePath[0])
        print("保存成功")

        model = 'my_mnist_model.h5'
        borders = findBorderContours(savePath[0])
        imgData = transMNIST(savePath[0], borders)
        results = predict(model, imgData)
        showResults(savePath[0], borders, results)

    # 橡皮擦函数
    def on_cbtn_Eraser_clicked(self):
        if self.checkBox.isChecked():
            self.__paintBoard.EraserMode = True
        else:
            self.__paintBoard.EraserMode = False

    def push_button_click(self):
        texts = self.plainTextEdit.toPlainText()
        onr = convert_path(texts)
        model = 'my_mnist_model.h5'
        borders = findBorderContours(onr)
        imgData = transMNIST(onr, borders)
        results = predict(model, imgData)
        showResults(onr, borders, results)


def accessPiexl(img):
    height = img.shape[0]
    width = img.shape[1]
    for i in range(height):
        for j in range(width):
            img[i][j] = 255 - img[i][j]
    return img


def accessBinary(img, threshold=128):
    img = accessPiexl(img)
    # 边缘膨胀，不加也可以
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    _, img = cv2.threshold(img, threshold, 0, cv2.THRESH_TOZERO)
    return img


def extractPeek(array_vals, min_vals=10, min_rect=20):
    extrackPoints = []
    startPoint = None
    endPoint = None
    for i, point in enumerate(array_vals):
        if point > min_vals and startPoint == None:
            startPoint = i
        elif point < min_vals and startPoint != None:
            endPoint = i

        if startPoint != None and endPoint != None:
            extrackPoints.append((startPoint, endPoint))
            startPoint = None
            endPoint = None

        # 剔除一些噪点
    for point in extrackPoints:
        if point[1] - point[0] < min_rect:
            extrackPoints.remove(point)
    return extrackPoints

    # 寻找边缘，返回边框的左上角和右下角（利用直方图寻找边缘算法（需行对齐））


def findBorderHistogram(path):
    borders = []
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = accessBinary(img)
    # 行扫描
    hori_vals = np.sum(img, axis=1)
    hori_points = extractPeek(hori_vals)
    # 根据每一行来扫描列
    for hori_point in hori_points:
        extractImg = img[hori_point[0]:hori_point[1], :]
        vec_vals = np.sum(extractImg, axis=0)
        vec_points = extractPeek(vec_vals, min_rect=0)
        for vect_point in vec_points:
            border = [(vect_point[0], hori_point[0]), (vect_point[1], hori_point[1])]
            borders.append(border)
    return borders

    # 寻找边缘，返回边框的左上角和右下角（利用cv2.findContours）


def findBorderContours(path, maxArea=50):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = accessBinary(img)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    borders = []
    for contour in contours:
        # 将边缘拟合成一个边框
        x, y, w, h = cv2.boundingRect(contour)
        if w * h > maxArea:
            border = [(x, y), (x + w, y + h)]
            borders.append(border)
    return borders


def showResults(path, borders, results=None):
    img = cv2.imread(path)
    # 绘制
    print(img.shape)
    for i, border in enumerate(borders):
        cv2.rectangle(img, border[0], border[1], (0, 0, 255))
        if results:
            cv2.putText(img, str(results[i]), border[0], cv2.FONT_HERSHEY_COMPLEX, 2.8, (102, 102, 255), 1)
        # cv2.circle(img, border[0], 1, (0, 255, 0), 0)
    cv2.imshow('test', img)
    cv2.waitKey(0)


# 根据边框转换为MNIST格式
def transMNIST(path, borders, size=(28, 28)):
    imgData = np.zeros((len(borders), size[0], size[0], 1), dtype='uint8')
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = accessBinary(img)
    for i, border in enumerate(borders):
        borderImg = img[border[0][1]:border[1][1], border[0][0]:border[1][0]]
        # 根据最大边缘拓展像素
        extendPiexl = (max(borderImg.shape) - min(borderImg.shape)) // 2
        targetImg = cv2.copyMakeBorder(borderImg, 7, 7, extendPiexl + 7, extendPiexl + 7, cv2.BORDER_CONSTANT)
        targetImg = cv2.resize(targetImg, size)
        targetImg = np.expand_dims(targetImg, axis=-1)
        imgData[i] = targetImg
    return imgData

    # 预测手写数字


def predict(modelpath, imgData):
    from keras import models
    my_mnist_model = models.load_model(modelpath)
    print(my_mnist_model.summary())
    img = imgData.astype('float32') / 255
    results = my_mnist_model.predict(img)
    result_number = []
    for result in results:
        result_number.append(np.argmax(result))
    return result_number


def convert_path(path: str) -> str:
    return path.replace('\\', '/')
