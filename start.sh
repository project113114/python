clear
a = ""
echo "$a"
while [ "$a" == "" ];
do
  clear
  nano rangeevent_randome_percentage.py
  python rangeevent_randome_percentage.py
  read -p "enter" a
done
