import xbmcplugin, xbmcgui, sys

url = "https://tubitv.com/movies"

li = xbmcgui.ListItem("Open Tubi Movies")
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
