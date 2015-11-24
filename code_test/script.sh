date +"%T"
<<<<<<< Updated upstream
head -10000 ../train/train.txt > train.txt
=======
head -5000 ../train/train.txt > train.txt
>>>>>>> Stashed changes
cat train.txt | python mapper.py | python reducer.py > centers.txt
python evaluate.py centers.txt train.txt
date +"%T"

