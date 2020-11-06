# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['..\\Sprider_pic_tx.py'],
             pathex=['S:\\Desktop\\py文件\\PytoExe打包\\Sprider_pic_tx'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Sprider_pic_tx',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='S:\\Desktop\\py文件\\Tkinter 图型界面\\5f4226701e4e0.128px.ico')
