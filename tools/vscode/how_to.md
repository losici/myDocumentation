# Vs Code Introduction

By default, VS Code is installed under C:\Users\{Username}\AppData\Local\Programs\Microsoft VS Code.

**Contents**
[TOC]

## Useful extensions
1. To show all the extensions and save them in a file .list
    ```sh
    code --list-extensions > extensions.list
    ```
1. To install the extension on a different machine
    ```sh
     cat extensions.list |% { code --install-extension $_}
    ```

### Editor
```
bierner.markdown-preview-github-styles
dzhavat.bracket-pair-toggler
hbrok.markdown-preview-bitbucket
oderwat.indent-rainbow
streetsidesoftware.code-spell-checker
usernamehw.errorlens
```
### Git
```
donjayamanne.githistory
eamodio.gitlens
mhutchie.git-graph
```
### C/Cpp
```
ms-vscode.cpptools
ms-vscode.cpptools-extension-pack
ms-vscode.cpptools-themes
```
### Cmake
```
ms-vscode.cmake-tools
```
ms-vscode.cmake-tools

### Embedded
```
dseight.disasexpl
mcu-debug.debug-tracker-vscode
mcu-debug.memory-view
mcu-debug.peripheral-viewer
mcu-debug.rtos-views
```

### Python
```
ms-python.python
ms-python.vscode-pylance
```

## Useful Commands
`Ctrl+Shift+P`: open the configurations