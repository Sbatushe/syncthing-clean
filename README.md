# syncthing-clean
Python cli tool to fix Syncthing conflicts

## Description
`syncthing_check.py` is made to detect (recursively) for conflicts in the shared drive. `syncthing_clean` is made to fix those conflicts. This software is mainly made for Linux, it won't work on Windows, MacOS, Android.

### Features:
- detect conflicts
- fix conflicts

### Requirements:
- Meld (or any text diff tool. Just edit the source code)
- Nemo (or any file manager. Just edit source again)
- Dialog (to show messages)
- Syncthing
- A terminal

## Install
```
chmod +x syncthing_clean
cp syncthing_clean /usr/bin/
```
