@echo off
set arg1=%1
cd D:\intelliJ\proj\spider-upload-lite && mvn clean compile package && cd target && java -jar spider-upload-lite-1.0-SNAPSHOT.jar %arg1% || cmd /k