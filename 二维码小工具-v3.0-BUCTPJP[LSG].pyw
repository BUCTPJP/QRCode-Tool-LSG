#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二维码小工具-v3.1-BUCTPJP[LSG].pyw
@Time    :   2023/12/04 20:16:29
@Author  :   BUCTPJP 
@Version :   3.1
@Contact :   pjp1095765918@gmail.com
@License :   Copyright (C) 2023 , Inc. All Rights Reserved 
@Desc    :   None
'''

# here put the import lib
import qrcode,qrcode.image.svg,logging,time,sys,pyzbar
import tkinter as tk,pyzbar.pyzbar as pyzbar
from tkinter import filedialog
from PIL import Image,ImageEnhance
from PIL.ImageFilter import SHARPEN
from Ui_UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer,SquareModuleDrawer,VerticalBarsDrawer,HorizontalBarsDrawer

#日志输出
logger = logging.getLogger('log')
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(funcName)s - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='./log.log',
                    filemode='a',
                    encoding = 'utf-8')

def seek_color():
    Image.open('color.png').show()

def produce():
    start = time.time()  
    if myWindow.mod.checkedId() == 1:
        logger.info('用户选择 模式一')
        string= myWindow.text1.toPlainText()            #获取用户输入内容
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
                )
        qr.add_data(string)
        qr.make(fit=True)                                           #使用make方法生成                                
        img = qr.make_image(back_color='#FFF',image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        end = time.time() 
        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Text Files", "*.png"),("All Files", "*.*")])
        if file_path:
            img.save(file_path,quality=100)
        runtime = "生成用时：{:.2f}s".format(end - start)                      
        logger.info(file_path + '保存完成-'+ runtime)
        myWindow.text4.clear()
        myWindow.text4.setText(file_path+ '保存完成' + '\n' + runtime)
    else:
        logger.info('用户选择 模式二')
        string,color = myWindow.text1.toPlainText(),myWindow.text3.toPlainText()            #获取用户输入内容   
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)                                           #使用make方法生成                                
        img = qr.make_image(fill_color=color, back_color='#FFF')
        end = time.time() 
        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Text Files", "*.png"),("All Files", "*.*")])
        if file_path:
            img.save(file_path,quality=100)
        runtime = "生成用时：{:.2f}s".format(end - start)                      
        logger.info(file_path + '保存完成-'+ runtime)
        myWindow.text4.clear()
        myWindow.text4.setText(file_path+ '保存完成' + '\n' + runtime)

def logo():
    start = time.time()  
    if myWindow.mod.checkedId() == 1:
        logger.info('用户选择 模式一')
        string = myWindow.text1.toPlainText()            #获取用户输入内容 
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)                        
        image = filedialog.askopenfilename()
        img = qr.make_image(back_color='#FFF',image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),embeded_image_path=image)
        img = img.convert('RGB')
        end = time.time() 
        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Text Files", "*.png"),("All Files", "*.*")])
        if file_path:
            img.save(file_path,quality=100)
        runtime = "生成用时：{:.2f}s".format(end - start)                      
        logger.info(file_path + '保存完成-'+ runtime)
        myWindow.text4.clear()
        myWindow.text4.setText(file_path + '保存完成' + '\n' + runtime)
    else:
        logger.info('用户选择 模式二')
        string,color = myWindow.text1.toPlainText(),myWindow.text3.toPlainText() 
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)  
        img = qr.make_image(fill_color=color, back_color='#FFF')                            
        image = filedialog.askopenfilename()                       #选择文件
        icon = Image.open(image).convert('RGBA')                   #转换为RGBA4通道
        img_w, img_h = img.size                                    #获得二维码尺寸
        size_w,size_h = int(img_w / 4),int(img_h / 4)
        icon_w, icon_h = icon.size
        if icon_w > size_w:                                        #调整logo图片大小
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h),Image.Resampling.LANCZOS)
        w,h = int((img_w - icon_w) / 2),int((img_h - icon_h) / 2)
        img.paste(icon, (w, h), icon)                              #将logo图片贴在二维码指定位置
        img = img.convert('RGB')
        end = time.time()    
        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Text Files", "*.png"),("All Files", "*.*")])
        if file_path:
            img.save(file_path,quality=100)
        runtime = "生成用时：{:.2f}s".format(end - start)                      
        logger.info(file_path + '保存完成-'+ runtime)
        myWindow.text4.clear()
        myWindow.text4.setText(file_path + '保存完成' + '\n' + runtime)

def bg():
    start = time.time()                                         #开始计时
    if myWindow.mod.checkedId() == 1:
        logger.info('用户选择 模式一')
        string = myWindow.text1.toPlainText()
        box = 8
        if myWindow.text7.toPlainText() == '':
            pass
        else:
            box = int(myWindow.text7.toPlainText())
        qr = qrcode.QRCode(
            version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
            box_size=box,                                         # 控制二维码中每个小格子包含的像素数
            border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)
        img = qr.make_image(back_color='#FFF',image_factory=StyledPilImage, module_drawer=CircleModuleDrawer()).convert('RGBA')                           
        image = filedialog.askopenfilename()                       #选择文件
        start = time.time()
        bg = Image.open(image).convert('RGBA')
        img_w, img_h = img.size
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] > 220 and item[1] > 220 and item[2] > 220:# 将白色（也可以调整为其他颜色）全部变为透明
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        bg_w,bg_h = bg.size                                     #获得背景图片尺寸
        if bg_w != img_w:                                       #改变背景图片大小与二维码一致
            bg_w = img_w
        if bg_h != img_h:
            bg_h = img_h
        bg_ = bg.resize((bg_w, bg_h),Image.Resampling.LANCZOS)
        bg_.paste(img,(0,0),img)                                 #将二维码贴在背景图片上
        bg_ = bg_.convert('RGB')
        end = time.time()                   
        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Text Files", "*.png"),("All Files", "*.*")])
        if file_path:
            bg_.save(file_path,quality=100)
        runtime = "生成用时：{:.2f}s".format(end - start)
        logger.info(file_path + '保存完成-'+ runtime)
        myWindow.text4.clear()
        myWindow.text4.setText(file_path + '保存完成' + '\n' + runtime)
    else:
        logger.info('用户选择 模式二')
        string,color = myWindow.text1.toPlainText(),myWindow.text3.toPlainText()
        box = 8
        if myWindow.text7.toPlainText() == '':
            pass
        else:
            box = int(myWindow.text7.toPlainText())
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/ERROR_CORRECT_M/ERROR_CORRECT_Q/ERROR_CORRECT_H     7%/15%/25%/30%的容错率
                box_size=box,                                         # 控制二维码中每个小格子包含的像素数
                border=4,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color='#FFF').convert('RGBA')                            
        image = filedialog.askopenfilename()                       #选择文件
        start = time.time()
        bg = Image.open(image).convert('RGBA')
        img_w, img_h = img.size
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] > 220 and item[1] > 220 and item[2] > 220:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        bg_w,bg_h = bg.size                                     #获得背景图片尺寸
        if bg_w != img_w:                                       #改变背景图片大小与二维码一致
            bg_w = img_w
        if bg_h != img_h:
            bg_h = img_h
        bg_ = bg.resize((bg_w, bg_h),Image.Resampling.LANCZOS)
        bg_.paste(img,(0,0),img)                                 #将二维码贴在背景图片上
        bg_ = bg_.convert('RGB')
        end = time.time()                   
        file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("Text Files", "*.png"),("All Files", "*.*")])
        if file_path:
            bg_.save(file_path,quality=100)
        runtime = "生成用时：{:.2f}s".format(end - start)
        logger.info(file_path + '保存完成-'+ runtime)
        myWindow.text4.clear()
        myWindow.text4.setText(file_path + '保存完成' + '\n' + runtime)

def parse():                        
    image = filedialog.askopenfilename()                        #选择文件
    start = time.time()
    img = Image.open(image)
    #处理图片
    img = ImageEnhance.Brightness(img).enhance(1.0)             #调整亮度        0~1~无穷
    img = ImageEnhance.Sharpness(img).enhance(1.0)              #锐利化          0~1~2
    img = ImageEnhance.Contrast(img).enhance(1.0)               #调整对比度      0~1~无穷
    img = ImageEnhance.Color(img).enhance(1.0)                  #调整色彩平衡    0~1~无穷
    #img = img.filter(SHARPEN)                                  #SHARPEN：补偿图像的轮廓，增强图像的边缘及灰度跳变的部分，使图像变得清晰
    img.show()
    texts = pyzbar.decode(img)                                  #解析到信息
    if texts == []:
        result = '此图片不包含二维码,或未解析到信息，请重试或更换'
        myWindow.text6.setText(result)
    else:                                              
        for text in texts:                                      #查找输出结果
            content = text.data.decode("utf-8")                 #data-内容；type-类型；rect-尺寸;polygon-边角定位点；quality-质量；orientation-方向
            result = "二维码中的内容是:\n{}".format(content)   
            myWindow.text6.setText(result)                                      
    end = time.time()
    runtime = "解析用时:{:.2f}s".format(end - start)             #解析内容格式化
    myWindow.text5.setText(runtime)
    logger.info(texts)  

def clean():
    myWindow.text5.clear()
    myWindow.text6.clear()

#GUI
class MyWindow(QMainWindow,Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.button4.clicked.connect(seek_color)
            self.button1.clicked.connect(produce)
            self.button2.clicked.connect(logo)
            self.button3.clicked.connect(bg)
            self.button5.clicked.connect(parse)
            self.button6.clicked.connect(clean)
            self.statusbar.showMessage('BUCTPJP[LCG]-禁止售卖，搬运请说明出处')
app = QApplication(sys.argv)
myWindow = MyWindow()               #实例化
myWindow.show()
explore = tk.Tk()                                          #打开资源管理器窗口
explore.withdraw() 
logger.info('GUI加载成功，程序启动')
app.exec_()
myWindow.close()