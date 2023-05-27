import sys
from workshop_helper import WorkshopHelper

link = ""
if len(sys.argv) > 1:
    link = sys.argv[1]
else:
    link = input("Workshop page url: ")

#get game ID
helper = WorkshopHelper()

game_id = helper.getGameId(link)

#get item ID
item_id = helper.getItemId(link)

#run steam cmd
helper.downloadItem(game_id, item_id)
