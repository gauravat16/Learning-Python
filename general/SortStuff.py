""" quiz materials for feature scaling clustering """


### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    sorted(arr)
    temp = [0,0,0]

    for i in range(0,len(arr)):
        temp[i] = float(arr[i] - arr[0]) / float(arr[len(arr)-1] - arr[0])
    return temp


# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)

