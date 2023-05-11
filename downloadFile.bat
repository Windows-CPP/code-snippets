SET FILELINK="YOURLINKHERE"
:: filelocname has the file name you save it as *plus* the path to where you want to save it
SET FILELOCNAME="YOURFILENAMEHERE"

:: download the file specefied
BITSADMIN /transfer /download %FILELINK% %FILELOCNAME%> nul

:: (optional if) zip files
:: unzip & cleanup
:: powershell -Command "Expand-Archive FILE_NAME_HERE.ZIP"
:: del "FILE_NAME_HERE.ZIP" /Q