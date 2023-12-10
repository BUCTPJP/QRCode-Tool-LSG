# QRCode-Tool-LSG
We have integrated and updated the original code for generating and parsing QR codes, deleted the old warehouse, and moved it here uniformly
***
## Language：
+ Chinese Simplified|[zh](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/README/README_zh.md)
+ English|[en](https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/README/README_en.md)
## Function：
### 1.Generate QR code
+ Directly generate regular style QR codes  

  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/common-mod1.png" width="200" height="200"  alt="common_mod1"/>
  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/common-mod2.png" width="200" height="200"  alt="common_mod2"/><br/>

+ Generate QR code with logo  

  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/logo-mod1.png" width="200" height="200"  alt="logo_mod1"/>
  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/logo-mod2.png" width="200" height="200"  alt="logo_mod2"/></br>

+ Generate QR codes with background images  

  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/bg-mod1.png" width="200" height="200"  alt="bg_mod1"/>
  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/bg-mod2.png" width="200" height="200"  alt="bg_mod2"/></br>

### 2.Parsing QR codes
### 3.Generate WIFI QR code, scan the code to connect to WIFI  

  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/wifi-code.png" width="200" height="200"  alt="wifi-code"/>
  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/wifi-effect.png" width="200" height="400"  alt="wifi-effect"/></br>

### 4.Generate a business card QR code, scan the code to display your personal business card  

  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/Business-card-code.png" width="200" height="200"  alt="Business card_code"/>
  <img src="https://github.com/BUCTPJP/QRCode-Tool-LSG/blob/master/img-Example/Business-card-effect.png" width="200" height="400"  alt="Business card_effect"/></br>

***
## Instructions for use：
+ 1.When generating QR codes with background images, ``try not to choose images with overly complex backgrounds``
+ 2.When generating a QR code with a background image, try to have a ``significant difference`` between the color of the QR code and the main color of the background as much as possible
+ 3.QR codes with background images may not be recognized by this software in some cases, but applications such as WeChat can
+ 4.If you still cannot recognize the QR code with a background image, you can use advanced settings (input boxes in the software that prompt careless use)<br>
This option defaults to 8, which can be increased appropriately to obtain a more easily recognizable QR code. It is recommended to gradually increase the value. If the value is too large, it will cause the generation time to be too long and the GUI will get stuck
+ 5.Choose a ``square`` as much as possible for the ``background image`` or ``logo image``, otherwise there may be incomplete or distorted image display
+ 6.Please refer to`` WIKI ``for specific usage instructions