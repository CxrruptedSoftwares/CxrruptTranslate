@echo off
setlocal enabledelayedexpansion

echo Installing CxrruptTranslate...

:: Function to download Python installer
:download_python
echo Downloading Python installer...
powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe' -OutFile 'python_installer.exe'}"
if not exist python_installer.exe (
    echo Failed to download Python installer.
    pause
    exit /b 1
)
goto :eof

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Attempting to install...
    call :download_python
    
    echo Installing Python...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    if errorlevel 1 (
        echo Failed to install Python.
        pause
        exit /b 1
    )
    
    :: Clean up installer
    del python_installer.exe
    
    :: Refresh environment variables
    call refreshenv.cmd
)

:: Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Attempting to install...
    python -m ensurepip --default-pip
    if errorlevel 1 (
        echo Failed to install pip.
        pause
        exit /b 1
    )
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Failed to create virtual environment.
    pause
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate virtual environment.
    pause
    exit /b 1
)

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

:: Install requirements
echo Installing requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install requirements.
    pause
    exit /b 1
)

:: Create desktop shortcut
echo Creating desktop shortcut...
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
echo sLinkFile = oWS.SpecialFolders("Desktop") ^& "\CxrruptTranslate.lnk" >> CreateShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
echo oLink.TargetPath = "%~dp0venv\Scripts\pythonw.exe" >> CreateShortcut.vbs
echo oLink.Arguments = "%~dp0main.py" >> CreateShortcut.vbs
echo oLink.WorkingDirectory = "%~dp0" >> CreateShortcut.vbs
echo oLink.Description = "VRChat Translation Tool" >> CreateShortcut.vbs
echo oLink.IconLocation = "%~dp0venv\Scripts\pythonw.exe, 0" >> CreateShortcut.vbs
echo oLink.Save >> CreateShortcut.vbs
cscript //nologo CreateShortcut.vbs
del CreateShortcut.vbs

:: Create start menu shortcut
echo Creating start menu shortcut...
echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateStartMenuShortcut.vbs
echo sLinkFile = oWS.SpecialFolders("StartMenu") ^& "\Programs\CxrruptTranslate.lnk" >> CreateStartMenuShortcut.vbs
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateStartMenuShortcut.vbs
echo oLink.TargetPath = "%~dp0venv\Scripts\pythonw.exe" >> CreateStartMenuShortcut.vbs
echo oLink.Arguments = "%~dp0main.py" >> CreateStartMenuShortcut.vbs
echo oLink.WorkingDirectory = "%~dp0" >> CreateStartMenuShortcut.vbs
echo oLink.Description = "VRChat Translation Tool" >> CreateStartMenuShortcut.vbs
echo oLink.IconLocation = "%~dp0venv\Scripts\pythonw.exe, 0" >> CreateStartMenuShortcut.vbs
echo oLink.Save >> CreateStartMenuShortcut.vbs
cscript //nologo CreateStartMenuShortcut.vbs
del CreateStartMenuShortcut.vbs

echo Installation complete!
echo To run CxrruptTranslate, double-click the desktop shortcut or run: venv\Scripts\python main.py
pause 