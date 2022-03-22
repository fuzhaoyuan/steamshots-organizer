# Steam截图整理器 Steamshots-Organizer
## 效果图 Example

![](.\Example.png)

## 整理Steam截图  

### 使用方法:  
将dist文件夹下的.exe文件复制到存放Steam截图的目录，然后运行。  
需要网络连接。

### 效果：
在该目录下，截图会进入对应游戏名的新建文件夹。  
如果这个游戏在Steam商店不存在了(比如某些限时Beta），则会进入名叫“Z-Unorganized”的文件夹（一般在最后一个）。

### 注意：
受到Windows文件夹命名的限制，游戏名中带有冒号‘:’的游戏只会创建其前半段名字的文件夹。其他受限制的字符暂未支持，需要支持请提交反馈。  
例如：“The Witcher 3: Wild Hunt”的截图会进入名叫“The Witcher 3”的文件夹。 

### 反馈：
欢迎在Issues区提交bug或申请新功能！

#### 更新日志：
v0.1: 提供最基础的功能  
v0.1.1: 修复了尝试对非截图进行处理的bug

---
## Organize screenshots taken in Steam  

### Guide:
Copy the .exe file in the 'dist' folder to the same directory where screenshots are saved and execute.  
Requires Internet connection.

### Effect:
In this directory, screenshots will be organized into newly created folders that match their game names.  
If this game is no longer available in the Steam store (like some Beta), its screenshots will enter the folder called "Z-Unorganized" (usually at last).

### Note:
Under the Windows folder naming restrictions, game name with ':' will only has their first half name as their folder name. Other restricted symbols are yet to be supported. If you want, create an issue.  
E.g., the screenshots of "The Witcher 3: Wild Hunt" will enter the folder called "The Witcher 3".

### Feedback:
Welcome to report bugs or apply for new features in the Issues section!

#### UpdateLog:
v0.1: Provides basic functions.  
v0.1.1: Fixed bug trying to handle non-screenshots.