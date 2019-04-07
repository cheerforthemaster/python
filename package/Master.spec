# -*- mode: python -*-

block_cipher = None


a = Analysis(['The\\AppData\\Local\\Programs\\Python\\Python36;C:\\Users\\Master', 'The\\AppData\\Local\\Programs\\Python\\Python36\\tcl;C:\\Users\\Master', 'The\\AppData\\Local\\Programs\\Python\\Python36\\Lib;C:\\Users\\Master', 'The\\AppData\\Local\\Programs\\Python\\Python36\\libs', 'qq_sign_in.py'],
             pathex=['C:\\Users\\Master', 'C:\\Users\\Master The\\PycharmProjects\\package'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Master',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Master')
