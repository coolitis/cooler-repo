import xbmcaddon, xbmcgui, xbmcplugin, sys

addon = xbmcaddon.Addon()
handle = int(sys.argv[1])

def list_channels():
    channels = [
        ("BBC News", "https://example.com/bbcnews.m3u8"),
        ("CNN", "https://example.com/cnn.m3u8"),
        ("Sky Sports", "https://example.com/skysports.m3u8")
    ]
    for name, url in channels:
        li = xbmcgui.ListItem(label=name)
        li.setInfo('video', {'title': name})
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle, url, li, False)
    xbmcplugin.endOfDirectory(handle)

if __name__ == "__main__":
    list_channels()
