import xbmcaddon
import xbmcgui
import xbmcplugin
import sys

# Get the Kodi handle for this plugin instance
handle = int(sys.argv[1])

# Get the Addon instance (to access settings, info, etc.)
addon = xbmcaddon.Addon()

# Read the IPTV URL entered in Settings (from resources/settings.xml)
iptv_url = addon.getSetting("iptv_url")

def list_channels():
    """
    Displays a list of channels in Kodi's UI.
    The first channel uses the M3U URL the user entered in the settings.
    """
    # Optional: show a small popup to confirm the URL being used
    dialog = xbmcgui.Dialog()
    dialog.notification("IPTV Addon", f"Using playlist: {iptv_url}", xbmcgui.NOTIFICATION_INFO, 5000)

    # Example list of channels
    channels = [
        ("BBC News", iptv_url if iptv_url else "https://example.com/bbcnews.m3u8"),
        ("CNN", "https://example.com/cnn.m3u8"),
        ("Sky Sports", "https://example.com/skysports.m3u8")
    ]

    for name, url in channels:
        li = xbmcgui.ListItem(label=name)
        li.setInfo('video', {'title': name})
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle, url, li, False)

    # Finalize the directory
    xbmcplugin.endOfDirectory(handle)


if __name__ == "__main__":
    list_channels()
