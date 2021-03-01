Dim Arg, var1
Set Arg = WScript.Arguments
var1 = Arg(0)

Set WshShell = CreateObject("WScript.Shell")
Dim val
For val = 1 to var1
	WshShell.SendKeys(chr(&hAE))
Next