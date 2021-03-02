@echo off
title Downloading Files...
cd "C:\Users\Administrator\Desktop\pixelgame_installer\pixelgame_installer"
if exist "..\pixelgame" (rmdir "..\pixelgame" /s /q)
if exist "pixelgame" (rmdir "pixelgame" /s /q)
git clone --depth 3 https://github.com/Tobdu399/pixelgame.git
title Finishing Installation...
pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/Administrator/Desktop/pixelgame_installer/pixelgame/lib/pictures/display/icon.ico" --add-data "C:/Users/Administrator/Desktop/pixelgame_installer/pixelgame/lib;lib/"  "C:/Users/Administrator/Desktop/pixelgame_installer/pixelgame/__main__.pyw"
if exist "pixelgame\__pycache__" (rmdir "pixelgame\__pycache__" /s /q)
ren "pixelgame" "source"
mkdir pixelgame
move source pixelgame
ren "dist\__main__.exe", "PixelGame.exe"
move "dist\PixelGame.exe" pixelgame
move pixelgame ../
if exist "build" (rmdir "build" /s /q)
if exist "dist" (rmdir "dist" /s /q)
if exist "__main__.spec" (del /f /q "__main__.spec")
title Installation Completed
echo **********************************
echo PixelGame installed in:
echo C:\Users\Administrator\Desktop\pixelgame
echo **********************************
pause
