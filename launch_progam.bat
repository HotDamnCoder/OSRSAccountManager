@echo off
chcp 65001
cls
set PROGRAM_DIRECTORY=C:\Users\Marcus\OneDrive - Tallinna Tehnikaülikool\Projects\OSRSAccountManager
"%PROGRAM_DIRECTORY%\.venv\Scripts\python.exe" "%PROGRAM_DIRECTORY%\main.py"
if %ERRORLEVEL% == -1 (
    pause
)
if %ERRORLEVEL% == 0 (
    echo Launching bots...
    "%PROGRAM_DIRECTORY%\launch_bots.bat"
)
