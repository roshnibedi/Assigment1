#Single Output Vertex:
a = [1.0, 3.5]
c = [3.8, 1.5]
d = -1.7
z = []
result = 0
sum = 0

def linear(w,x,b):
    global result
    for i in range(len(x)):
        z = x[i]*w[i]
        result = result + z

    sum = result + b

    return sum

output = linear(a,c,d)
print(output)

#Output Layer:
x = [1, 3.5]
w = [[3.8, 1.5], [-1.2, 1.1]]
b = [-1.7, 2.5]
result = []

def linear_layer(x, w, b):
    for i in range(len(b)):
        product = 0
        for j in range(len(x)):
            product = product + w[i][j]*x[j]
        result.append(round(product + b[i], 2))
    return result 

result = linear_layer(x,w,b)
print(result)


#Inner Layers:
x1 = [1,0]
w1 = [[2.1,-3.1], [-0.7, 4.1]]
b1 = [-1.1, 4.2]

def inner_layer(x1,w1,b1):
    for i in range(len(b1)):
        product = 0
        for j in range(len(x1)):
            product = product + w1[i][j]*x1[j]
        result.append(round(product + b1[i], 2))
    return result

result = inner_layer(x1,w1,b1)
print(result)

#Full Inference: 

#reading Weights: 
def read_weights(file_name):
    l = []
    f = open(file_name, "r")
    for x in f:
        m = [] 
        if x == "#\n":
            continue 
        else:
            x = x.split(",")
        temp = []
        for i in x: 
            i = float(i)
            temp.append(i)
            print(temp)
            m.append(temp)
            l.append(m)
        return l

result = read_weights('weights.txt')
print(result)

#PART 2: 
#Flip a pixel:

def flip_pixel(x):
    if x == 0: 
        x = 1
    else: 
        x = 0
    return x

flip = flip_pixel(0)
print(flip)

#Modify a list:

def modified_list(i, x):
    x[i] = flip_pixel(x[i])
    return x 

x = [1, 0, 1, 1, 0, 0, 0]
i = 2
flip_list = modified_list(i, x)
print(flip_list)

#Quality Computation: 

def compute_difference(x1, x2):
    count = 0 
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            count += 1 
    return count 

x1 = [1, 0, 1, 1, 0, 0, 0]
x2 = [1, 1, 1, 0, 0, 0, 1]

compute = compute_difference(x1, x2)
print(compute)

#Select a pixel

#def select_pixel(x, w, b):
    
#x = read_image(‘image.txt’)
#w = read_weights(‘weights.txt’)
#b = read_biases(‘biases.txt’)
#pixel = select_pixel(x, w, b)

