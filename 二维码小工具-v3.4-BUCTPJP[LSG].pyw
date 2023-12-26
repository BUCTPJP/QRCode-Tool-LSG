#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二维码小工具-v3.4-BUCTPJP[LSG].pyw
@Time    :   2023/12/10 12:20:41
@Author  :   BUCTPJP 
@Version :   3.4
@Contact :   pjp1095765918@gmail.com
@License :   Copyright (C) 2023 , Inc. All Rights Reserved 
@Desc    :   None
'''

# here put the import lib
import qrcode,logging,time,sys,pyzbar,tempfile,os,webbrowser,UI.UI_rc,win32ui
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer,GappedSquareModuleDrawer,CircleModuleDrawer,SquareModuleDrawer,VerticalBarsDrawer,HorizontalBarsDrawer
from qrcode.image.styledpil import StyledPilImage
from PIL.ImageFilter import SHARPEN
from PIL import Image,ImageEnhance
import pyzbar.pyzbar as pyzbar
from segno import helpers
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QSize,QMetaObject
from PyQt5.QtWidgets import *
from UI.Ui_主窗口 import Ui_MainWindow
from UI.Ui_WIFI import Ui_WIFI
from UI.Ui_名片 import Ui_identify

#TODO:日志输出
logger = logging.getLogger('log')
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(funcName)s - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='./log.log',
                    filemode='a',
                    encoding = 'utf-8')

#TODO:方法
def seek_color():       #FIXME:颜色选择
    global col_select
    col_select = QColorDialog.getColor()
    myWindow.text3.setText(str(col_select.name())) 

def produce():          #FIXME:正常二维码
    global runtime,img_s
    start = time.time()
    if myWindow.mod.checkedId() == 1:
        logger.info('用户选择 模式一')                  #TODO:info运行信息输出
        string= myWindow.text1.toPlainText()           
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
                )
        qr.add_data(string)
        qr.make(fit=True)                                           #使用make方法生成                                
        img_s = qr.make_image(back_color='#FFF',image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
        end = time.time()
        runtime = "生成用时：{:.2f}s".format(end - start)
        p_vew(img_s)    
    elif myWindow.mod.checkedId() == -1:
        QMessageBox.critical(myWindow, "错误", "未选择生成模式")
        logger.error("用户未选择生成模式")                      #TODO:error错误信息输出
    else:
        logger.info('用户选择 模式二')                  #TODO:info运行信息输出
        string = myWindow.text1.toPlainText()       
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)                                           #使用make方法生成                                
        img_s = qr.make_image(fill_color=str(col_select.name()), back_color='#FFF')
        end = time.time()
        runtime = "生成用时：{:.2f}s".format(end - start)
        p_vew(img_s)   

def logo():             #FIXME:带logo二维码
    global runtime,img_s
    start = time.time()  
    if myWindow.mod.checkedId() == 1:
        logger.info('用户选择 模式一')                       # TODO:info运行信息输出
        string = myWindow.text1.toPlainText()               # 获取用户输入内容 
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)    
        end = time.time()  
        lpszFilter = "Image Files (*.jpg *.gif *.png *.jpeg)|*.jpg;*.gif;*.png;*.jpeg|" \
                    "Files (*.*)|*.*|| "                                                    # 文件类型过滤
        dlg = win32ui.CreateFileDialog(True, "png", None, 0x04 | 0x02, lpszFilter)          # True表示打开文件对话框
        #dlg.SetOFNInitialDir(os.path.dirname(__file__))                                     # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()                                                                       # 等待获取用户选择的文件
        image = dlg.GetPathName()  
        if image == (''):
            logger.warning('用户未选择图片退出')            #TODO:warning警告输出
            pass
        else:
            img = qr.make_image(back_color='#FFF',image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),embeded_image_path=image)
            img_s = img.convert('RGB')
            runtime = "生成用时：{:.2f}s".format(end - start)
            p_vew(img_s)   
    elif myWindow.mod.checkedId() == -1:
        QMessageBox.critical(myWindow, "错误", "未选择生成模式")
        logger.error("用户未选择生成模式")                          #TODO:error错误信息输出
    else:
        logger.info('用户选择 模式二')                               #TODO:info运行信息输出
        string= myWindow.text1.toPlainText()
        qr = qrcode.QRCode(
                version=5,                                          # 二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
                error_correction=qrcode.constants.ERROR_CORRECT_H,  # ERROR_CORRECT_L/M/Q/H  7%/15%/25%/30%的容错率
                box_size=8,                                         # 控制二维码中每个小格子包含的像素数
                border=1,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)  
        img = qr.make_image(fill_color=str(col_select.name()), back_color='#FFF')  
        end1 = time.time()                          
        lpszFilter = "Image Files (*.jpg *.gif *.png *.jpeg)|*.jpg;*.gif;*.png;*.jpeg|" \
                    "Files (*.*)|*.*|| "                                                    # 文件类型过滤
        dlg = win32ui.CreateFileDialog(True, "png", None, 0x04 | 0x02, lpszFilter)          # True表示打开文件对话框
        #dlg.SetOFNInitialDir(os.path.dirname(__file__))                                     # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()                                                                       # 等待获取用户选择的文件
        image = dlg.GetPathName()
        if image == (''):
            logger.warning('用户未选择图片退出')            #TODO:warning警告输出
            pass
        else:
            start1 = time.time()
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
            img_s = img.convert('RGB')
            end = time.time()
            runtime = "生成用时：{:.2f}s".format((end1 - start)+(end - start1))    
            p_vew(img_s)   

def bg():               #FIXME:带背景二维码
    global runtime,img_s
    start = time.time()                                         #开始计时
    if myWindow.mod.checkedId() == 1:
        logger.info('用户选择 模式一')                          #TODO:info运行信息输出
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
        end1 = time.time() 
        lpszFilter = "Image Files (*.jpg *.gif *.png *.jpeg)|*.jpg;*.gif;*.png;*.jpeg|" \
                    "Files (*.*)|*.*|| "                                                    # 文件类型过滤
        dlg = win32ui.CreateFileDialog(True, "png", None, 0x04 | 0x02, lpszFilter)          # True表示打开文件对话框
        #dlg.SetOFNInitialDir(os.path.dirname(__file__))                                     # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()                                                                       # 等待获取用户选择的文件
        image = dlg.GetPathName()
        if image == (''):
            logger.warning('用户未选择图片退出')            #TODO:warning警告输出
            pass
        else:
            start1 = time.time()
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
            img_s = bg_.convert('RGB')
            end = time.time()  
            runtime = "生成用时：{:.2f}s".format((end1 - start)+(end - start1))                 
            p_vew(img_s)
    elif myWindow.mod.checkedId() == -1:
        QMessageBox.critical(myWindow, "错误", "未选择生成模式")
        logger.error("用户未选择生成模式")                          #TODO:error错误信息输出
    else:
        logger.info('用户选择 模式二')                          #TODO:info运行信息输出
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
                border=4,                                           # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
        )
        qr.add_data(string)
        qr.make(fit=True)
        img = qr.make_image(fill_color=str(col_select.name()), back_color='#FFF').convert('RGBA')                            
        end1 = time.time() 
        lpszFilter = "Image Files (*.jpg *.gif *.png *.jpeg)|*.jpg;*.gif;*.png;*.jpeg|" \
                    "Files (*.*)|*.*|| "                                                    # 文件类型过滤
        dlg = win32ui.CreateFileDialog(True, "png", None, 0x04 | 0x02, lpszFilter)          # True表示打开文件对话框
        #dlg.SetOFNInitialDir(os.path.dirname(__file__))                                     # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()                                                                       # 等待获取用户选择的文件
        image = dlg.GetPathName()
        if image == (''):
            logger.warning('用户未选择图片退出')            #TODO:warning警告输出
            pass
        else:
            start1 = time.time()                 
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
            img_s = bg_.convert('RGB')
            end = time.time()  
            runtime = "生成用时：{:.2f}s".format((end1 - start)+(end - start1))                 
            p_vew(img_s)   

def parse():            #FIXME:解析二维码
    lpszFilter = "Image Files (*.jpg *.gif *.png *.jpeg)|*.jpg;*.gif;*.png;*.jpeg|" \
                    "Files (*.*)|*.*|| "                                                    # 文件类型过滤
    dlg = win32ui.CreateFileDialog(True, "png", None, 0x04 | 0x02, lpszFilter)          # True表示打开文件对话框
    dlg.SetOFNInitialDir(os.path.dirname(__file__))                                     # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()                                                                       # 等待获取用户选择的文件
    image = dlg.GetPathName()
    if image == (''):
        logger.warning('用户未选择图片退出')            #TODO:warning警告输出
        pass
    else:
        start = time.time()
        img = Image.open(image)
        #处理图片
        img = ImageEnhance.Brightness(img).enhance(1.0)             #调整亮度        0~1~无穷
        img = ImageEnhance.Sharpness(img).enhance(1.0)              #锐利化          0~1~2
        img = ImageEnhance.Contrast(img).enhance(1.0)               #调整对比度      0~1~无穷
        img = ImageEnhance.Color(img).enhance(1.0)                  #调整色彩平衡    0~1~无穷
        p_vew(img)  
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
        runtime = "用时:{:.2f}s".format(end - start)             #解析内容格式化
        myWindow.text5.setText(runtime)
        logger.info(texts)                                     #TODO:info运行信息输出

def clean():            #FIXME:清空解析区显示
    myWindow.text5.clear()
    myWindow.text6.clear()

def save(img):          #FIXME:保存二维码图像
    lpszFilter ="PNG Files (*.png)|*.png|" \
                "JPG Files (*.jpg)|*.jp|" \
                "JPEG Files (*.jpeg)|*.jpeg|" \
                "GIF Files (*.gif)|*.gif|" \
                "Files (*.*)|*.*|| "                                                    # 文件类型过滤
    dlg = win32ui.CreateFileDialog(False, "png", None, 0x04 | 0x02, lpszFilter)         # True表示打开文件对话框
    #dlg.SetOFNInitialDir(os.path.dirname(__file__))                                    # 设置打开文件对话框中的初始显示目录,不设置记忆上次路径
    dlg.DoModal()                                                                       # 等待获取用户选择的文件
    file_path = dlg.GetPathName()
    if file_path == (''):
        logger.warning('用户未选择路径退出')            #TODO:warning警告输出
        pass
    else:
        img.save(file_path,quality=100)               
        logger.info(file_path + '保存完成-'+ runtime)   #TODO:info运行信息输出
        myWindow.text4.clear()
        myWindow.text4.setText(file_path+ '保存完成' + '\n' + runtime)

def save_1(img):        #FIXME:保存wifi码/名片码图像
    lpszFilter ="PNG Files (*.png)|*.png|" \
                "JPG Files (*.jpg)|*.jp|" \
                "JPEG Files (*.jpeg)|*.jpeg|" \
                "GIF Files (*.gif)|*.gif|" \
                "Files (*.*)|*.*|| "                                                    # 文件类型过滤
    dlg = win32ui.CreateFileDialog(False, "png", None, 0x04 | 0x02, lpszFilter)         # True表示打开文件对话框
    #dlg.SetOFNInitialDir(os.path.dirname(__file__))                                    # 设置打开文件对话框中的初始显示目录,不设置记忆上次路径
    dlg.DoModal()                                                                       # 等待获取用户选择的文件
    file_path = dlg.GetPathName()
    if file_path == (''):
        logger.warning('用户未选择路径退出')            #TODO:warning警告输出
        pass
    else:
        file_path = file_path+type[5:9]
        if file_path:
            img.save(file_path,scale = 10)               
        logger.info(file_path + '保存完成-')   #TODO:info运行信息输出
        QMessageBox.information(wifi_window, "提示", "保存完成",QMessageBox.Yes)

def p_vew(img):         #FIXME:预览二维码图像
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    logger.info('++创建临时文件夹++')                   #TODO:info运行信息输出
    img.resize((350, 350),Image.Resampling.LANCZOS).save(temp_file.name)
    logger.info('++将图片保存为临时文件++')             #TODO:info运行信息输出
    pixmap = QPixmap(temp_file.name)
    myWindow.privew.setPixmap(pixmap)
    temp_file.close()
    logger.info('++清除临时文件夹++')                   #TODO:info运行信息输出

def p_vew_1(img):       #FIXME:预览wifi码图像
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    logger.info('++创建临时文件夹++')                   #TODO:info运行信息输出
    img.save(temp_file.name)
    logger.info('++将图片保存为临时文件++')             #TODO:info运行信息输出
    pixmap = QPixmap(temp_file.name)
    pixmap = pixmap.scaled(350, 350)
    wifi_window.privew.setPixmap(pixmap)
    temp_file.close()
    logger.info('++清除临时文件夹++')                   #TODO:info运行信息输出

def p_vew_2(img):       #FIXME:预览名片码图像
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    logger.info('++创建临时文件夹++')                   #TODO:info运行信息输出
    img.save(temp_file.name)
    logger.info('++将图片保存为临时文件++')             #TODO:info运行信息输出
    pixmap = QPixmap(temp_file.name)
    pixmap = pixmap.scaled(350, 350)
    identify_window.privew.setPixmap(pixmap)
    temp_file.close()
    logger.info('++清除临时文件夹++')                   #TODO:info运行信息输出

def description():      #FIXME:使用说明
    os.system(r'v3.3使用说明.txt')

def git_open():         #FIXME:打开github
    webbrowser.open('https://github.com/BUCTPJP/QRCode-Tool-LSG/issues')

def lsg_open():         #FIXME:打开lsg帖子
    webbrowser.open('https://www.52pojie.cn/forum.php?mod=viewthread&tid=1865282&page=1#pid48817438')

def getwifi():          #FIXME:获取电脑中的WiFi信息
    message = os.popen('netsh wlan show profiles').readlines()
    wifi_name = {}
    number = 0
    QMessageBox.information(wifi_window, "提示", "正在查找，请耐心等待",QMessageBox.Yes)
    logger.info('开始查找本机连接过WIFI信息')                                       #TODO:info运行信息输出
    for i in message:
        # 读取WiFi名称
        if '所有用户配置文件' in i:
            wifi = i.split(':')[1].replace('\n', '')
            wifi = wifi.replace(' ', '')
            # 根据WiFi名称查找密码
            command = "netsh wlan show profiles name=" + wifi + " key=clear"
            per_wifi = os.popen(command).readlines()
            for k in per_wifi:
                if '关键内容' in k:
                    passwd = k.split(':')[1].replace('\n', '').replace(' ', '')
                    wifi_name.update({wifi: passwd})
                    number+=1
    QMessageBox.information(wifi_window, "提示", "查找完成",QMessageBox.Yes)
    logger.info('获取到{}条WIFI信息'.format(number))                                #TODO:info运行信息输出
    wifi_window.form.setRowCount(number)
    k=0
    for i in wifi_name.keys():
        wifi= QTableWidgetItem(str(i))
        wifi_window.form.setItem(k, 0, wifi)
        k+=1
    k=0 
    for j in wifi_name.values():
        passwd = QTableWidgetItem(str(j))
        wifi_window.form.setItem(k, 1, passwd)
        k+=1

def make_wificode():    #FIXME:生成wifi连接码
    global wfcode
    wfcode = helpers.make_wifi(ssid=wifi_window.lineEdit.text(),password=wifi_window.lineEdit_2.text(),security='WPA2',hidden=False)
    p_vew_1(wfcode)

def make_identifycode():#FIXME:生成名片码
    global itcode
    itcode = helpers.make_mecard(name=identify_window.lineEdit.text(),
                                 email=identify_window.lineEdit_3.text(),
                                 phone=identify_window.lineEdit_4.text(),
                                 city=identify_window.lineEdit_2.text())
    p_vew_2(itcode)

#TODO:初始化GUI
class MyWindow(QMainWindow,Ui_MainWindow):              #FIXME:主窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button4.clicked.connect(seek_color)
        self.button1.clicked.connect(produce)
        self.button2.clicked.connect(logo)
        self.button3.clicked.connect(bg)
        self.button5.clicked.connect(parse)
        self.button6.clicked.connect(clean)
        self.button7.clicked.connect(lambda:save(img_s)) 
    def open_child_window(self):                        #打开关于子窗口
        child_window.show()
    def open_wifi_window(self):                         #打开WIFI码子窗口
        wifi_window.show()
    def open_identify_window(self):                     #打开名片码子窗口
        identify_window.show()
      
class WIFI(QWidget,Ui_WIFI):                            #FIXME:WIFI码子窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.form.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.bt3.clicked.connect(getwifi)
        self.bt1.clicked.connect(make_wificode)
        self.bt2.clicked.connect(lambda:save_1(wfcode))

class identify(QWidget,Ui_identify):                    #FIXME:名片码子窗口
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.bt1.clicked.connect(make_identifycode)
        self.bt2.clicked.connect(lambda:save_1(itcode))

class Child(QWidget):                                   #FIXME:关于子窗口
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关于")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/关于.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.resize(600, 350)
        self.setMinimumSize(QSize(600, 350))
        self.setMaximumSize(QSize(600, 350))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(0, 55))
        self.label.setMaximumSize(QtCore.QSize(100, 55))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_3)
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(300, 0))
        self.label_3.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(300, 0))
        self.label_4.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.label.setText("版本：\n""V3.2")
        self.label_2.setText("Email:")
        self.label_3.setText("pjp1095765918@gmail.com")
        self.label_4.setText("pjp1095765918@163.com")
        self.label_5.setText("软件发布页")
        self.label_6.setText("<a href = 'https://github.com/BUCTPJP/QRCode-Tool-LSG'>Github</a>")
        self.label_7.setText("<a href = 'https://www.52pojie.cn/forum.php?mod=viewthread&tid=1865282&page=1#pid48817438'>LSG</a>")
        self.label_6,self.label_7.setStyleSheet('QLabel {color: blue; text-decoration: underline}')
        self.label_6,self.label_7.setOpenExternalLinks(True)

app = QApplication(sys.argv)
myWindow = MyWindow()                                   #TODO:实例化
wifi_window = WIFI()
identify_window = identify()  
child_window = Child()           

myWindow.show()

logger.info('---日志模块加载完成---')
logger.info('---GUI加载成功，程序启动---正在加载必要功能---')                #TODO:info运行信息输出
myWindow.explain.triggered.connect(description)
logger.info('---帮助模块加载完成---')                                       #TODO:info运行信息输出
myWindow.github.triggered.connect(git_open)
myWindow.lsg.triggered.connect(lsg_open)
logger.info('---反馈模块加载完成---')                                       #TODO:info运行信息输出
myWindow.about.triggered.connect(myWindow.open_child_window)
myWindow.wifi_code.triggered.connect(myWindow.open_wifi_window)
logger.info('---WIFI码模块加载完成---')                                     #TODO:info运行信息输出
myWindow.identify_code.triggered.connect(myWindow.open_identify_window)
logger.info('---名片码模块加载完成---')                                     #TODO:info运行信息输出

app.exec_()
myWindow.close()