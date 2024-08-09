# Useful commands
1. Search for a string pattern within all files regardless of their extension
```
Get-ChildItem -Recurse | Select-String -Pattern "textToLookFor"
```
1. Rename LRV files into mp4 files
```
Get-ChildItem -Filter *.LRV | Rename-Item -NewName {$_.Name -replace '.LRV','.MP4'}
```