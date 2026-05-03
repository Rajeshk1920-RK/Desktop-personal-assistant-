@echo off
title J.A.R.V.I.S - Online
color 0B
echo.
echo  Starting J.A.R.V.I.S...
echo.
python jarvis.py
if errorlevel 1 (
    echo.
    echo  Error starting JARVIS. Run INSTALL.bat first.
    pause
)
