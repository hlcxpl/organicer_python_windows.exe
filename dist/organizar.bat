@echo off
setlocal enabledelayedexpansion

:: Obtener el directorio actual donde se está ejecutando el bat
set "directorio_actual=%CD%"
echo Directorio actual: !directorio_actual!

:: Ejecutar organice.exe con el directorio actual como argumento
@"%~dp0organice.exe" "!directorio_actual!"

endlocal