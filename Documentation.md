1. Steam Web API: https://developer.valvesoftware.com/wiki/Steam_Web_API

2. Get Steam App List: http://api.steampowered.com/ISteamApps/GetAppList/v1/
    - v2 lacks some games like: AC Rogue

3. Game names with ':' like 'The Witcher 3: Wild Hunt' will only keep its name before ':': 'The Witcher 3', the same way it is named in the Documents folder.

4. KeyError will be raised if the game is not listed, e.g. the beta version of a game is not available anymore. I just ignore these cases and leave the screenshots in the 'Z-Unorganized' folder.