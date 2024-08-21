# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui.py'],
    pathex=['D:/Projects/CurrencyRecognizationApp'],
    binaries=[],
    datas=[('models/indian.h5','models'),('models/nepali.h5','models'),('camera.py','.'),('convert.py','.'),('predict.py','.')],
    hiddenimports=['wheel','numpy','opencv_python','Pillow','tensorflow'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=1,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CurrencyRecognizationApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
