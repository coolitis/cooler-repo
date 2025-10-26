import xbmcplugin, xbmcgui, sys

url = "https://www.popcornflix.com/"

li = xbmcgui.ListItem("Open Popcornflix Movies")
xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
