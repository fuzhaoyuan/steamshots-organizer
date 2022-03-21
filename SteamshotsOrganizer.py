import os
import pathlib
import requests
import shutil

# get list of screenshots
pics = os.listdir()

# collect app_ids for all games
app_ids = set()
for i in range(0, len(pics)):
    if pathlib.Path(pics[i]).suffix == '.png':
        app_ids.add(int(pics[i].split('_')[0]))

# cache app list json from Steam API
get_app_list = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v1/')
app_list = get_app_list.json()['applist']['apps']['app']

# find names of all app_ids
id2name = {}
for i in range(0, len(app_list)):
    if app_list[i]['appid'] in app_ids:
        id2name[app_list[i]['appid']] = app_list[i]['name']

# put screenshots into (newly created) folders
for i in range(0, len(pics)):
    if pathlib.Path(pics[i]).suffix == '.png':
        app_id = int(pics[i].split('_')[0])
        folder_path = os.getcwd() + '\\' + id2name.get(app_id, 'Z-Unorganized').split(':')[0]
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        src_path = os.getcwd() + '\\' + pics[i]
        shutil.move(src_path, folder_path)