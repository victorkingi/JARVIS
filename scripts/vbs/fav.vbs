Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Users\victo\AppData\Roaming\Spotify\Spotify.exe"
WScript.sleep 500
CreateObject("WScript.Shell").Run("spotify:playlist:37i9dQZF1DX2Z1pVUBGGZs")
WScript.sleep 10000
WshShell.SendKeys " "
WScript.sleep 100
WshShell.SendKeys "^{RIGHT}"
