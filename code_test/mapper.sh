date +"%T"
head -10000 ../train/train.txt > train.txt
time cat train.txt | python mapper.py  > mapper.txt

date +"%T"

