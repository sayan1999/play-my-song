# Play My Song
A wrapper on linux based music player Rhythmbox, that avails colsest search mechanism on your music library.

![Preview](src/examples/preview1.png?raw=true "Entering song name by user")
![Preview](src/examples/preview1.png?raw=true "Approximate search result")


## Dependencies
Rhythmbox, Python3 and import modules

```
sudo apt install python3.8 python3-pip
pip3 install <modulename>
```

## Configuration
1. Navigate into playmysong/src/. Run 

```
chmod +x playmysong
./playmysong
```
## If app doesn't start your rhythmbox db file location is different. (Follow these instructions to fix it)
2. Find out your rhythmbox xml db filepath (usually <~/.local/share/rhythmbox/rhythmdb.xml>); open play-my-song/src/env.py file in editing mode and edit the 2nd line as RHYTHMBOXXMLPATH=<Rhythmbox_xml_db_filepath_string_within_quotes>.
4. Run PLay My Song and do as the console says. Resolve the modulenotfound error by running

```
pip3 install <modulename>
```
5. (Optional) add <path to play-my-song/src> to your PATH variable and use this command from any directory. You can also write a desktop file (as given in the examples folder, first add src directory to your path)and put it in your home/applications folder to have a full fledged application use.  