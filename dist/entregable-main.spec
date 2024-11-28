# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['entregable-main.py'],
    pathex=[],
    binaries=[],
    datas=[('dataset/*', 'dataset'), ('models/*', 'models'), ('scripts/*', 'scripts'), ('output/*', 'output'), ('preprocess.py', '.'), ('real_time_reco.py', '.'), ('train_model.py', '.'), ('utils.py', '.'), ('word_filter.py', '.'), ('proyecto/*', 'proyecto'), ('1/*', '1')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='entregable-main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
