import requests
import re
import subprocess
from lxml import html

class WorkshopHelper:

    def __init__(self) -> None:
        pass

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

        #using link
        if len(args) == 1:
            game_id = self.getGameId(args[0])
            item_id = self.getItemId(args[0])
        
        #using id's
        else:
            game_id = args[0]
            item_id = args[1]
        
        script = f"""
        login anonymous
        workshop_download_item {game_id} {item_id}
        quit
        """

        with open("steamcmd\script.txt", 'w') as file:
            file.write(script)

        steamcmd = 'steamcmd\steamcmd.exe'
        args = ['+runscript', "script.txt"]

        command = [steamcmd] + args

        subprocess.run(command, check=True)
