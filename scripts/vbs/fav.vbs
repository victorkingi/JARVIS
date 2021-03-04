Set WshShell = WScript.CreateObject("WScript.Shell")
CreateObject("WScript.Shell").Run("spotify:playlist:37i9dQZF1DX2Z1pVUBGGZs")
WScript.sleep 8000
WshShell.SendKeys " "
WScript.sleep 100
WshShell.SendKeys "^{RIGHT}"
