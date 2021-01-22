import gzip
from rich.progress import  track

input_file = gzip.open("MNIST  Dataset/train-images-idx3-ubyte.gz", 'rb')
input_labels = gzip.open("MNIST  Dataset/train-labels-idx1-ubyte.gz", "rb")
out_file = open("MNIST  Dataset/train_data.csv",'w')
	
for i in track(range(60000)):
	out_file.write(", ".join(map(str,input_file.read(785))))
	out_file.write(", ".join(map(str,input_labels.read(1))))
	out_file.write("\n")

out_file.close()
input_file.close()