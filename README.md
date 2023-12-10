# QRCode-Tool-LSG
对原来生成二维码与解析二维码的代码做了整合更新，删除了旧仓库，统一移至此处进行更新维护
***
## 语言：
+ 简体中文|[zh](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/README/README_zh.md)
+ 英语|[en](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/README/README_en.md)
***
## 功能：
### 1.生成二维码
+ 直接生成普通样式二维码
  ![common_mod1](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/common-mod1.png =100x100)
  ![common_mod2](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/common-mod2.png =100x100)</br>
  
+ 生成带logo的二维码
  ![log_mod1](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/common-mod1.png =100x100)
  ![log_mod2](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/logo-mod2.png =100x100)</br>
  ​​
+ 生成带背景图片的二维码
  ![bg_mod1](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/bg-mod1.png =100x100)
  ![bg_mod2](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/bg-mod2.png =100x100)</br>
  
### 2.解析二维码  
### 3.生成WIFI二维码，扫码即可连接WIFI
  ![wifi-code](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/wifi-code.png =100x100)
  ![wifi-effect](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/wifi-effect.png =200x100)</br>
### 4.生成名片二维码，扫码即可显示个人名片
  ![Business card_code](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/Business%20card-code.png =100x100)
  ![Business card_effect](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/Business%20card-effect.png =200x100)</br>
***
## 使用提醒：
+ 1.生成带有背景图片的二维码时，尽量``不要选择背景过于复杂``的图片
+ 2.生成带有背景图片的二维码时，二维码颜色和背景主体``颜色尽量有较大差异``
+ 3.带有背景图片的二维码在某些情况下本软件无法识别，微信等应用可以
+ 4.如果始终无法识别带有背景图片的二维码，可以使用``高级设置``（软件中提示``慎用``的输入框）<br>
    + 此选项默认为8，可以适当提高此数值以获得更易识别的二维码，建议逐步增加，如果数值太大，会导致生成时间过长，GUI卡住的情况
+ 5.``背景``图片或``logo``图片尽量选用``正方形``,否则会出现图像显示不全或变形
+ 6.具体使用说明请参阅``WIKI``
