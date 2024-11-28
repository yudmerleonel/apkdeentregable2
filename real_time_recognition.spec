# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['scripts\\real_time_recognition.py'],
    pathex=[],
    binaries=[],
    datas=[('dataset/*', 'dataset'), ('models/*', 'models'), ('scripts/*', 'scripts'), ('output/*', 'output'), ('scripts/preprocess.py', '.'), ('scripts/real_time_recognition.py', '.'), ('scripts/train_model.py', '.'), ('scripts/utils.py', '.'), ('scripts/word_filter.py', '.')],
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
    name='real_time_recognition',
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
