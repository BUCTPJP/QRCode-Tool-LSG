# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['二维码小工具-v3.3-BUCTPJP[LSG].pyw'],
    pathex=['D:\\学习\\理科类\\编程设计\\python\\二维码小工具'],
    binaries=[('D:/学习/理科类/编程设计/python/二维码小工具/UI_rc.py','.'),
        ('D:/学习/理科类/编程设计/python/二维码小工具/Ui_UI.py','.'),
        ('D:/学习/理科类/编程设计/python/二维码小工具/ico.ico','.'),],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='二维码小工具-v3.3-BUCTPJP[LSG]',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='二维码小工具-v3.3-BUCTPJP[LSG]',
)
