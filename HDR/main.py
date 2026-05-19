# from src.data import Loader
from src.data.preprocessor import test_data_loader, train_data_loader


images, labels = train_data_loader()

current = images[35343]
# print(labels[3])

counter=0
line = ""
while counter < 744:
	if current[counter] == 0:
		line+=" "
	elif current[counter] > 0 and current[counter] <128:
		line+="*"
	else:
		line+="#"
	if counter%28==0:
		print(line)
		line=""
	counter+=1