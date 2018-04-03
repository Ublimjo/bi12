#!/data/data/com.termux/files/usr/bin/sh

cp bi12 $PREFIX/bin
chmod +x $PREFIX/bin/bi12
cp bible.py $PREFIX/bin
cp part.py $PREFIX/bin
cp edit_distance.py $PREFIX/bin
unzip FloatingBible.zip -d $PREFIX/share/bi12/
pip install -r requirement.txt
