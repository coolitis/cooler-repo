import xbmcplugin, xbmcgui, sys

url = "https://www.crackle.com/"

li = xbmcgui.ListItem("Open Crackle Movies")
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
