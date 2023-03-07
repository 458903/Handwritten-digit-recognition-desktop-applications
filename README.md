# Handwritten-digit-recognition-desktop-applications
# 手写数字识别桌面小程序：使用方法,源码解析

## 目录

-   [一、食用方法：](#一食用方法)
    -   [PS：如果运行失败👇🏽](#PS如果运行失败)
-   [二、源码：](#二源码)

![](image/image_Yfuj4j7tpz.png)

2022/12/23 10:57:33  大作业题目四：手写体数字的识别👆

> 🏞️**目录**
>
> -   **一.使用方法:→如果运行失败，那没办法了，直接跳到第2部分看源码解析吧**
>     -   1.代码仓库:→不看源码的话跳过这步
>     -   2.直接运行GUI应用:
>         -   功能一
>         -   功能二
> -   **二.源码解析：**
>     -   1.数字识别算法部分
>     -   2.GUI图形界面部分

***

***

## 一、食用方法：

-   ***1.1如要查看代码，我的项目源码仓库地址*** 👇🏼

    [https://gitee.com/sailsailone/digital-recognition](https://gitee.com/sailsailone/digital-recognition "https://gitee.com/sailsailone/digital-recognition")

    ![](image/image_DSWOwiWA5v.png)

    &#x20;    🦕\~\~\*\*\*如要运行源码（不推荐，环境很难配置）: \*\*\*\~\~
    1.  解压zip文件后用PyCharm打开，配置好解释器
    2.  环境中用到的packages如下：低于这些版本跑不起来；高版本的请注意package之间的版本冲突：
        | Python          | 3.6.5  |
        | --------------- | ------ |
        | PyQt5           | 5.15.4 |
        | Tensorflow（CPU） | 1.13.1 |
        | keras           | 2.2.4  |
        | h5py            | 2.7.1  |
        | matplotlib      | 2.0.2  |
        | numpy           | 1.19.5 |
    3.  程序入口文件是：CallWindow\.py；运行CallWindows.py即可唤出如下GUI界面，程序运行时间较长。

        ![](image/image_3iITU1FAYm.png)
    4.  成功弹出GUI界面之后，点击保存并识别后需要等待较长一段时间，中间会有Tensorflow的爆红警告，如果是FutureWarrning类型就不必理会；
    5.  如果是别的error并闪退，就是python环境没配置好，运行失败了。
-   ***1.2 or直接运行桌面应用→项目源码打包成的可执行程序：***
    -   **1.2.0** 解压缩执行文件夹test1，可以看到文件夹目录结构如下（不可更改，否则程序运行失败）：

        ‼️即使在同一台电脑上，这个exe文件有时能跑,有时不行，主要看电脑的python环境和运气。i5以下的也跑不动。若双击后闪退，或者过了一分钟还没跳出图形界面，就是环境不兼容，运行失败了，建议放弃。

        ![](image/image_nGemIA67eY.png)
    -   **1.2.1功能1：识别本地图片**

        ‼️要写对图片路径（注意看图片后缀名是.jpg还是.png），路径不对的话，它找不到文件就会闪退：

        ![](image/image_cZdti-Cob_.png)
    -   **1.2.2功能2：手写数字识别**

        ![](image/image_uES8wW9t6s.png)

        &#x20;  🦥等待约一分钟后弹出识别结果：

        ![](image/image_HK4b3HS1gp.png)

### PS：如果运行失败👇🏽

⚡这个程序稳健性很差，可能在以上任何一步出现闪退，此时可以直接放弃。~~不嫌麻烦的话~~也可以：

-   下载源码后，*自行打包*，生成exe可执行文件（不建议，因为要先装Anaconda环境，环境不对或者Packages版本冲突就会失败），打包命令：
-   pyinstaller -F -w [CallWindows.py](http://CallWindows.py "CallWindows.py") --hidden-import [Sketchpad.py](http://Sketchpad.py "Sketchpad.py") --hidden-import [PaintBoard.py](http://PaintBoard.py "PaintBoard.py") --hidden-import [model.py](http://model.py "model.py") --hidden-import my\_mnist\_model.h5 --hidden-import PyQt5 --hidden-import sys --hidden-import cv2 --hidden-import numpy --hidden-import matplotlib --hidden-import keras --hidden-import os
-   打包方法：先把python环境配置好。进入源码文件夹，在源码文件夹所在路径打开cmd输入打包命令，或在Anaconda Prompt激活装有上述packages的env后输入以上打包命令。

***

***

## 二、源码：

-   ***2.1识别算法部分：***
    -   🦜用的是这位大佬的代码  —>  [https://gitcode.net/mirrors/Wangzg123/HandwrittenDigitRecognition?utm\_source=csdn\_github\_accelerator](https://gitcode.net/mirrors/Wangzg123/HandwrittenDigitRecognition?utm_source=csdn_github_accelerator "https://gitcode.net/mirrors/Wangzg123/HandwrittenDigitRecognition?utm_source=csdn_github_accelerator")
    -   🌵源码解析看里面的README.md和他的csdn博客；直接跑他的代码会报错，因为已经是三年前的代码了，里面一些API已经被弃用或升级了
    -   🌲和GUI部分整合后，main.py内的代码移到了`PaintBoard.py`中

        **API解析：**

        1.图像预处理

        `def accessPiexl(img):` 反相灰度图，将黑白阈值颠倒
        ```python
        def accessPiexl(img):
            height = img.shape[0]# img.shape[0]→图像的垂直尺寸（高度）;
            width = img.shape[1] # img.shape[1]→图像的水平尺寸（宽度）;
            # 在矩阵中，[0]就表示行数，[1]则表示列数。
            for i in range(height):
               for j in range(width):
                   img[i][j] = 255 - img[i][j]# 反相
            return img
        ```
        `def accessBinary(img, threshold=128):` 反相二值化图像&#x20;
        ```python
        def accessBinary(img, threshold=128):# 阈值threshold设置为128
            img = accessPiexl(img)#调用accessPiexl()颠倒黑白阈值
            # 边缘膨胀
            kernel = np.ones((3, 3), np.uint8)
            # kernel – 进行操作的内核，默认为3×3的矩阵;iterations – 腐蚀次数，默认为1
            img = cv2.dilate(img, kernel, iterations=1)
            # cv2.threshold()把img分成二值图像
            _, img = cv2.threshold(img, threshold, 0, cv2.THRESH_TOZERO)
            return img

        ```
        `cv2.dilate()`是opencv中形态学操作的膨胀函数，一般用于处理二值化图像。膨胀的作用是连通边界（白色部分的边界），可以连接在不在一起的物体。

        `cv2.threshold()`把整幅图像分成了非黑即白的二值图像了,把阈值设置成了128，只需要规定一个阈值值，整个图像都和这个阈值比较。当图像中的灰度值大于128的重置像素值为255

        2.分割数字
        -   `def findBorderContours(path, maxArea=50):`寻找边缘，返回边框的左上角和右下角（利用cv2.findContours）

            `contours, hierarchy = cv2.findContours(image,mode,method)`：轮廓检测函数；该函数接受的参数为二值图，即黑白的（不是灰度图），所以读取的图像要先转成灰度的，再转成二值图

            `mode`：轮廓的模式。cv2.RETR\_EXTERNAL只检测外轮廓；
            `method：`轮廓的近似方法。cv2.CHAIN\_APPROX\_NOME存储所有的轮廓点，相邻的两个点的像素位置差不超过1；
            `contours：`返回的轮廓
            ```python
            def findBorderContours(path, maxArea=50):
            # 图像读取方法中使用cv2.IMREAD_GRAYSCALE读取灰度图
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                img = accessBinary(img)# 转成黑白二值图 
                contours, _ = cv2.findContours(img, 
                                                  cv2.RETR_EXTERNAL, 
                                                  cv2.CHAIN_APPROX_NONE)
                borders = []
                for contour in contours:
                    # 将边缘拟合成一个边框
                    x, y, w, h = cv2.boundingRect(contour)
                    if w*h > maxArea:# if矩形边框的宽*高>50
                        border = [(x, y), (x+w, y+h)]# 画出边框
                        borders.append(border)
                return borders

            ```
            `cv2.boundingRect(img)`这个函数可以获得一个图像的最小矩形边框一些信息，参数img是一个[二值图像](https://so.csdn.net/so/search?q=二值图像\&spm=1001.2101.3001.7020 "二值图像")，它可以返回四个参数，左上角坐标x,y，矩形的宽高w,h
        -   `def convert_path(path: str) `：转换输入路径，把windows系统文件路径的‘/’转换成cv2可以识别的‘\\\’；
        -   `def showResults(path, borders, results=None):`
            -   ` cv2.putText(img,str(results[i]),border[0], cv2.FONT_HERSHEY_COMPLEX,2.8，(102, 102, 255),  1)`参数列表如下：

                （图片，要添加的文字（即识别出来的数字results\[i]），文字添加到图片上的位置：右上角，字体的类型，字体大小：2.8，字体颜色RGB：红色，字体粗细：1）
            ```python
            def showResults(path, borders, results=None):
                img = cv2.imread(path)

                print(img.shape)
                for i, border in enumerate(borders):
                    # 绘制矩形边框
                    cv2.rectangle(img, border[0], border[1], (0, 0, 255))
                    if results:
                        cv2.putText(img,
                                    str(results[i]),
                                    border[0], 
                                    cv2.FONT_HERSHEY_COMPLEX,
                                    2.8,
                                    (102, 102, 255), 
                                     1)
                cv2.imshow('test', img)# 显示识别的结果
                cv2.waitKey(0)
            ```
        -   `def transMNIST(path, borders, size=(28, 28)):`根据边框转换为MNIST格式

            `np.zeros`返回来一个给定形状和类型的用0填充的数组；zeros([shape](https://so.csdn.net/so/search?q=shape\&spm=1001.2101.3001.7020 "shape"), dtype=float)shape:(len(borders), size\[0], size\[0], 1)形状；dtype:数据类型uint8
            ```python
            def transMNIST(path, borders, size=(28, 28)):
                imgData = np.zeros((len(borders), size[0], size[0], 1), dtype='uint8')
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                img = accessBinary(img)
                for i, border in enumerate(borders):
                    borderImg = img[border[0][1]:border[1][1], border[0][0]:border[1][0]]
                    # 根据最大边缘拓展像素
                    extendPiexl = (max(borderImg.shape) - min(borderImg.shape)) // 2
                    targetImg = cv2.copyMakeBorder(borderImg, 7, 7,
                     extendPiexl + 7, extendPiexl + 7, cv2.BORDER_CONSTANT)
                    targetImg = cv2.resize(targetImg, size)
                    targetImg = np.expand_dims(targetImg, axis=-1)
                    imgData[i] = targetImg
                return imgData
            ```
        -   `def predict(modelpath, imgData):`使用刚才训练好的模型‘my\_mnist\_model.h5’预测手写数字
            ```python
            def predict(modelpath, imgData):
                from keras import models
               #返回模型实例 my_mnist_model
                my_mnist_model = models.load_model(modelpath)
                print(my_mnist_model.summary())
                img = imgData.astype('float32') / 255 # 归一化
                results = my_mnist_model.predict(img)
                result_number = []
                for result in results:
                    result_number.append(np.argmax(result))
                return result_number
            ```
        -
-   ***2.2 GUI部分：***
    -   🐋Sketchpad.py：手写画板程序
    -   🐳PaintBoard.py：Ui\_MainWindow类API→

        &#x20;`def on_btn_Save_Clicked(self)`：将手写板内容保存为图片
        ```python
         def on_btn_Save_Clicked(self):
                savePath = QFileDialog.getSaveFileName(self,
                                                       'Save Your Paint', '.\\imgs', '*.png')
                print(savePath)
                if savePath[0] == "": # 若文件名输入为空
                    print("Save cancel")
                    return
                image = self.__paintBoard.GetContentAsQImage()
                image.save(savePath[0])
                model = 'my_mnist_model.h5'
                borders = findBorderContours(savePath[0])
                imgData = transMNIST(savePath[0], borders)
                results = predict(model, imgData)
                showResults(savePath[0], borders, results)
        ```
        ` def setupUi(self, MainWindow)`：初始化MainWindow的data和view

        &#x20;`def Quit(self):`退出MainWindows

        ![](image/image_KlRgxSvuLZ.png)
    -   🐟CallWindows.py:启动程序入口
        ![](image/image_JSCmssIEvb.png)
