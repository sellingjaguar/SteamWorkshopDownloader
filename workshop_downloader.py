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

link = ""
if len(sys.argv) > 1:
    link = sys.argv[1]
else:
    link = input("Workshop page url: ")

#run steam cmd
WorkshopHelper().downloadItem(link)
