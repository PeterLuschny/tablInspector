@echo off
REM Start the Python Flask server for tablInspector
cd /D "%~dp0src"

REM Start the server in the background
start /B ..\.venv\Scripts\python.exe _tablserver.py

REM Wait for server to be ready
cd ..
echo Waiting for server to be ready...
:wait
REM Wait 1 second
timeout /T 1 /NOBREAK >nul
curl -s -o nul http://localhost:3000/triangle && goto ready
goto wait

:ready
echo.
echo Server is running at http://localhost:3000
REM Open the TableExplorer in the browser (adjust filename if needed)
start http://localhost:3000/TableExplorer.html
pause
