import sys
from workshop_helper import WorkshopHelper
import configparser

#Prepare configs in case there isn't a config file
config = configparser.ConfigParser()

if config.read("config.ini") == []:
    print("No config file, let's create one...")
    config.add_section('SETTINGS')
    config.set('SETTINGS', 'steamcmd_dir', input("SteamCMD folder directory: "))
    config.set('SETTINGS', 'output_dir', input("Output directory: "))

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

#Being ran via command, supports both links or ID's
if len(sys.argv) > 1:
    if len(sys.argv) > 3: 
        raise("Invalid arguments, must be either a link or the game ID followed by the item ID.")
    WorkshopHelper().downloadItem(sys.argv[1:])
#Use GUI
else:
    link = input("Workshop page url: ")
    WorkshopHelper().downloadItem(link)
