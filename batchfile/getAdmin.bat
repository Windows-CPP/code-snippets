:: Gets admin privilages- Important step for a lot of scripts!

:: --------------------------------------------
:: BatchGetAdmin
if not "%1"=="am_admin" (
	powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
	exit /b
)
:: --------------------------------------------
