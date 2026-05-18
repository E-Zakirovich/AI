from src.data import Loader

loader = Loader()


images, labels = loader.train_data()

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
	
	

for r in range(40):
	current = images[r * 134]
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
		