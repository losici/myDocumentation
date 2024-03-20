# Useful commands
1. Search for a string pattern within all files regardless of their extension
```
Get-ChildItem -Recurse | Select-String -Pattern "textToLookFor"
```