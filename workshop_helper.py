import requests
import re
import subprocess
from lxml import html
import configparser
import shutil

class WorkshopHelper:

    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.read("config.ini")

        self.steamcmd_dir = config['SETTINGS']['steamcmd_dir']
        self.output_dir = config['SETTINGS']['output_dir']

    def getGameId(self, url):
        r = requests.get(url)
        tree = html.fromstring(r.content)
        elem = tree.xpath('//*[@id="ig_bottom"]/div[3]/a[1]')
        elem_txt = elem[0].get('href')
        #Get the numbers present in the href link for the game page
        game_id = re.search(r'\d+$', elem_txt).group()

        return game_id
    
    def getItemId(self, url):
        #Match numbers between "id=" and either the string end or a & (in case of the GET variable for search)
        item_id = re.search(r'(?!id=)\d+($|(?=&))', url).group()

        return item_id
    
    def downloadItem(self, *args):

        #Using link
        if len(args) == 1:
            game_id = self.getGameId(args[0])
            item_id = self.getItemId(args[0])
        
        #Using id's
        else:
            game_id = args[0]
            item_id = args[1]
        
        #Create download script
        script = f"""
        login anonymous
        workshop_download_item {game_id} {item_id}
        quit
        """

        #Make it be a file to be sent as arguments
        with open(self.steamcmd_dir + '\script.txt', 'w') as file:
            file.write(script)

        steamcmd = self.steamcmd_dir + '\steamcmd.exe'
        args = ['+runscript', 'script.txt']

        command = [steamcmd] + args

        subprocess.run(command)

        #Move downloaded file to output folder
        shutil.move(f'{self.steamcmd_dir}\steamapps\workshop\content\{game_id}', self.output_dir)

