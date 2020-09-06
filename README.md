# Sideshow Wallpaper Generator
## What for
This python script generates a xml file ready to use as background.
## How to use
### Dependency
The script works Pyhton2 and 3.
### Generating XML
```bash
git clone https://github.com/imbodensamuel/ubuntu-sideshow-wallpaper.git
cd ubuntu-sideshow-wallpaper
python3 ss-gen.py -t TRANSISTION -d DURATION FILES... > yourfile.xml
```
### Applying XML
```bash
gsettings set org.gnome.desktop.background picture-uri 'file:///path/to/file/yourfile.xml'
```
## More informations
I found this method from this [post](http://ubuntuhandbook.org/index.php/2020/09/desktop-wallpaper-slideshow-ubuntu-20-04/)
