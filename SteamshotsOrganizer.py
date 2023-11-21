import os
import pathlib
import requests
import shutil

# cache app list json from Steam API
get_app_list = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v1/', verify = False)
app_list = get_app_list.json()['applist']['apps']['app']

# organize app list into a map
appid_to_name = {}
for app in app_list:
    appid_to_name[app['appid']] = app['name'].replace(':', '-')

# put screenshots into (newly created) folders
pics = os.listdir()
for pic in pics:
    if pathlib.Path(pic).suffix == '.png':
        try:
            appid = int(pic.split('_')[0])
            folder_path = os.getcwd() + '\\' + appid_to_name.get(appid, 'Z-Unorganized')
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            src_path = os.getcwd() + '\\' + pic
            shutil.move(src_path, folder_path)
        except ValueError:
            continue