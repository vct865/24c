@echo off
cd /d "%~dp0"
git add .
git commit -m "auto update"
git push
echo.
echo === Done! Wait 1 min then refresh. ===
pause
