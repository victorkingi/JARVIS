@echo off
cd D:\intelliJ\proj\backup-free && mvn clean compile package && java -jar target/spider-upload-1.0-SNAPSHOT.jar || cmd /k