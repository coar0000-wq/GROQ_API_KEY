@echo off
REM ?¤– JARVIS Gemini API Key ?ë™ ?±ë¡
REM GitHub CLI ?¬ìš©

setlocal enabledelayedexpansion

echo.
echo ================================================
echo  ?¤– JARVIS ?ë™???œìŠ¤??echo  ?“ Gemini API Key ?ë™ ?±ë¡
echo ================================================
echo.

REM GitHub CLI ?•ì¸
echo [1/5] GitHub CLI ?•ì¸ ì¤?..
gh --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ??GitHub CLIê°€ ?¤ì¹˜?˜ì? ?Šì•˜?µë‹ˆ??
    echo.
    echo ?’¡ ?¤ì¹˜ ë°©ë²•:
    echo    1. https://cli.github.com/ ë°©ë¬¸
    echo    2. ?¤ì¹˜ ?Œì¼ ?¤ìš´ë¡œë“œ ë°??¤í–‰
    echo    3. ?ëŠ” PowerShell?ì„œ: choco install gh
    echo.
    pause
    exit /b 1
)
echo ??GitHub CLI ?¤ì¹˜??echo.

REM GitHub ?¸ì¦ ?•ì¸
echo [2/5] GitHub ?¸ì¦ ?•ì¸ ì¤?..
gh auth status >nul 2>&1
if errorlevel 1 (
    echo.
    echo ??GitHub ?¸ì¦???„ìš”?©ë‹ˆ??
    echo.
    echo ëª…ë ¹?´ë? ?¤í–‰?˜ì„¸??
    echo    gh auth login
    echo.
    pause
    exit /b 1
)
echo ??GitHub ?¸ì¦ ?„ë£Œ
echo.

REM API ???¤ì •
echo [3/5] Gemini API Key ?¤ì • ì¤?..
set API_KEY=[YOUR_GEMINI_API_KEY]
set REPO=coar0000/kms
echo ??API Key: %API_KEY:~0,20%...
echo ??Repository: %REPO%
echo.

REM Secrets ?±ë¡
echo [4/5] GitHub Secrets ?±ë¡ ì¤?..
echo !API_KEY! | gh secret set GEMINI_API_KEY -R %REPO%
if errorlevel 1 (
    echo.
    echo ??Secrets ?±ë¡ ?¤íŒ¨
    echo.
    echo ?˜ë™ ?±ë¡:
    echo https://github.com/%REPO%/settings/secrets/actions
    echo.
    pause
    exit /b 1
)
echo ??GEMINI_API_KEY ?±ë¡ ?„ë£Œ
echo.

REM ?±ë¡ ?•ì¸
echo [5/5] ?±ë¡ ?•ì¸ ì¤?..
timeout /t 2 /nobreak >nul
gh secret list -R %REPO% | find "GEMINI_API_KEY" >nul
if errorlevel 1 (
    echo ? ï¸  ?•ì¸ ?€ê¸?ì¤?..
) else (
    echo ???±ë¡ ê²€ì¦??„ë£Œ
)
echo.

REM ?„ë£Œ
echo ================================================
echo ??ëª¨ë“  ?‘ì—… ?„ë£Œ!
echo ================================================
echo.
echo ?“‹ ?¤ìŒ ?¨ê³„:
echo   1. ??1-2ë¶???GitHub Actions ?ë™ ?¤í–‰
echo   2. ë§?10ë¶„ë§ˆ???ë™ ë°˜ë³µ
echo   3. cumulative_products.json ?…ë°?´íŠ¸ ?•ì¸
echo.
echo ?”— GitHub Actions ëª¨ë‹ˆ?°ë§:
echo   https://github.com/%REPO%/actions
echo.
echo ?”— ?¤ì • ?•ì¸:
echo   https://github.com/%REPO%/settings/secrets/actions
echo.
pause
