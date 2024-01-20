@echo off
echo now building distributions, please wait...
cd ..\renpy-8.1.3-sdk\
.\renpy.exe launcher distribute "..\EllenVague"
echo done
pause