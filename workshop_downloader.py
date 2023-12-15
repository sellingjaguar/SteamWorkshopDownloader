import sys
from workshop_helper import WorkshopHelper
import configparser
import PySimpleGUI as gui

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

    #Download area part
    mod_download = [
        [
            gui.Text('Mod link'),
            gui.In(key='-MOD LINK-', do_not_clear=False),
            gui.Button('Download', key='-DOWNLOAD-')
        ],
        [
            gui.Text('Waiting download...', key='-STATUS-')
        ]
    ]

    settings = [
        [
            gui.Text('Settings')
        ],
        [
            gui.Text('SteamCMD:'),
            gui.Text(config["SETTINGS"]["steamcmd_dir"]),
            gui.Button('Change', key='-CHANGE STEAMCMD-')
        ],
        [
            gui.Text('Output:'),
            gui.Text(config["SETTINGS"]["output_dir"]),
            gui.Button('Change', key='-CHANGE OUTPUT-')
        ]
    ]

    layout = [
        [mod_download],
        [gui.HSeparator()],
        [settings]
    ]

    window = gui.Window('Workshop downloader',layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == gui.WIN_CLOSED:
            break

        #Download events
        if event == '-DOWNLOAD-':
            try:
                WorkshopHelper().downloadItem(values['-MOD LINK-'])
                window['-STATUS-'].update('Download successful.')
            except:
                window['-STATUS-'].update('Download failed, check your mod link again.')

        #Settings events
        elif event == '-CHANGE STEAMCMD-':
            pass
        elif event == '-CHANGE OUTPUT-':
            pass
