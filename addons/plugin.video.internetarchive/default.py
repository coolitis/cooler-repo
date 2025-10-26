import xbmcplugin, xbmcgui, sys

url = "https://archive.org/details/movies"

li = xbmcgui.ListItem("Open Internet Archive Movies")
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
