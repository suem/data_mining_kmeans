date +"%T"
head -20 ../train/train.txt > train.txt
time cat train.txt | python mapper.py  > mapper.txt

date +"%T"

