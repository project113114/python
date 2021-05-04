clear
a = ""
echo "$a"
while [ "$a" == "" ];
do
  clear
  nano Graph_random.py
  python Graph_random.py
  read -p "enter" a
done
