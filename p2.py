inputs = [1,2,5.1,2.1]

weights1 = [0.2,0.8,-0.5,1.0]
weights2 = [0.5,-0.91,0.26,-0.5] 
weights3 = [-0.26,-0.27,0.17,0.87]


bias1 = 2
bias2 = 3 
bias3 = 0.5

output = []

sum = 0
for i in range(4):
        sum = weights1[i]*inputs[i] + sum
sum = sum + bias1
output.append(sum)

sum = 0
for i in range(4):
        sum = weights2[i]*inputs[i] + sum
sum = sum + bias2
output.append(sum)

sum = 0
for i in range(4):
        sum = weights3[i]*inputs[i] + sum
sum = sum + bias3
output.append(sum)

print(output)