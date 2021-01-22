import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("MNIST  Dataset/train_data.csv", header = None)
print("Import Complete")

x = np.array(data.iloc[:,:-1])
y = np.array(data.iloc[:,-1])

im = x[2].reshape(28,28)
plt.imshow(im)
plt.show()
