@echo off
cd D:\intelliJ\proj\backup-free && mvn clean compile package && cd target && spider-upload.exe || cmd /k