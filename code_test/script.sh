date +"%T"
head -10000 ../train/train.txt > train.txt
cat train.txt | python mapper.py | python reducer.py > centers.txt
python evaluate.py centers.txt train.txt
date +"%T"

