# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['GUI_of_ToolKit.py'],
             pathex=['button1.py', 'button2.py', 'button3.py', 'C:\\Users\\Administrator\\Desktop\\Tool_Kit'],
             binaries=[],
             datas=[],
             hiddenimports=['button1', 'button2', 'button3'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='GUI_of_ToolKit',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='GUI_of_ToolKit')
