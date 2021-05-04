clear
a = ""
echo "$a"
while [ "$a" == "" ];
do
  clear
  nano Xsquargraph.py
  python Xsquargraph.py
  read -p "enter" a
done
