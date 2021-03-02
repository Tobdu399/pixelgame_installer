# PixelGame Installer

# NOTE
# This script will create a pixelgame installation file. to install
# pixelgame, execute this script and run the pixelgame.bat file which
# will appear in the same directory as this script.

# INSTALLATION 
# The PixelGame will be installed in the same parent directory as
# this folder. For example, if the 'pixelgame_installer/' folder is
# located in 'C:\Users\<user>\Desktop\pixelgame_installer\', the
# PixelGame will be installed In 'C:\Users\<user>\Desktop\pixelgame\'


from lib import setup

# INSTALLER PREPARATION -----
setup.setup()

# CREATE THE INSTALLER ------
from lib import installer_setup
installer_setup.installer()
