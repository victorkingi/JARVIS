@echo off
set arg1=%1
cd D:\intelliJ\proj\spider-upload-lite && mvn clean compile package && cd target && spider-upload-lite.exe %arg1% || cmd /k