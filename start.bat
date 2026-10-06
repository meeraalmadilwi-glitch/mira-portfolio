@echo off
chcp 65001 >nul
echo =====================================================
echo   مساعد ميرة الذكي - Mira AI Assistant
echo =====================================================
echo.

REM Check for API key argument
if not "%~1"=="" (
    set GEMINI_API_KEY=%~1
    echo   API key provided via argument.
    goto start
)

REM Check if .env exists
if exist "%~dp0.env" (
    echo   Found .env file, reading key...
    for /f "tokens=1,2 delims==" %%a in (%~dp0.env) do (
        if "%%a"=="GEMINI_API_KEY" set GEMINI_API_KEY=%%b
    )
    goto start
)

REM Optional key prompt
echo   (Optional) Enter your Gemini API key from aistudio.google.com/apikey
echo   Or press ENTER directly to use the built-in Smart Engine:
echo.
set /p GEMINI_API_KEY=  Paste your GEMINI_API_KEY (or press Enter): 

:start
echo.
echo   [1/2] Starting AI server on port 5001...
if "%GEMINI_API_KEY%"=="" (
    start "Mira AI Server" /min python "%~dp0local-ai-server.py"
) else (
    start "Mira AI Server" /min python "%~dp0local-ai-server.py" %GEMINI_API_KEY%
)

timeout /t 2 >nul
echo   [2/2] Opening browser at http://localhost:3000 ...
start "" http://localhost:3000
echo   Starting web server on port 3000...
python -m http.server 3000
