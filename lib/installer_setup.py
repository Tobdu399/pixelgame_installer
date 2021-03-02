import pathlib
from os.path import basename


def installer():
    path = pathlib.Path(__file__).resolve().parent.parent
    parent_folder = basename(path)
    formatted_path = str(path).replace("\\", "/")

    lines = [
        "@echo off",
        "title Downloading Files...",
        'cd "' + str(path) + '\\pixelgame_installer"',
        'if exist "..\pixelgame" (rmdir "..\pixelgame" /s /q)',
        'if exist "pixelgame" (rmdir "pixelgame" /s /q)',
        "git clone --depth 3 https://github.com/Tobdu399/pixelgame.git",
        "title Finishing Installation...",
        'pyinstaller --noconfirm --onefile --windowed --icon "' + formatted_path + '/pixelgame/lib/pictures/display/icon.ico" --add-data "' + formatted_path + '/pixelgame/lib;lib/"  "' + formatted_path + '/pixelgame/__main__.pyw"',
        'if exist "pixelgame\__pycache__" (rmdir "pixelgame\__pycache__" /s /q)',
        'ren "pixelgame" "source"',
        "mkdir pixelgame",
        "move source pixelgame",
        'ren "dist\__main__.exe", "PixelGame.exe"',
        'move "dist\PixelGame.exe" pixelgame',
        "move pixelgame ../",
        'if exist "build" (rmdir "build" /s /q)',
        'if exist "dist" (rmdir "dist" /s /q)',
        'if exist "__main__.spec" (del /f /q "__main__.spec")',
        "title Installation Completed",
        "echo **********************************",
        "echo PixelGame installed in:",
        "echo " + str(path.parent) + "\\pixelgame",
        "echo **********************************",
        "pause",
    ]

    file = open(f"{str(path)}/pixelgame.bat", "w")

    for line in lines:
        line = line + "\n"
        file.write(line)

    file.close()
