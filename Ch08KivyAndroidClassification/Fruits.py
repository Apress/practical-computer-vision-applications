import numpy
import PIL.Image

def sigmoid(inpt):
    return 1.0/(1.0+numpy.exp(-1*inpt))
    
def relu(inpt):
    result = inpt
    result[inpt<0] = 0
    return result

def predict_output(weights_mat_path, data_inputs, activation="relu"):
    weights_mat = numpy.load(weights_mat_path)
    r1 = data_inputs
    for curr_weights in weights_mat:
        r1 = numpy.matmul(a=r1, b=curr_weights)
        if activation == "relu":
            r1 = relu(r1)
        elif activation == "sigmoid":
            r1 = sigmoid(r1)
    r1 = r1[0, :]
    predicted_label = numpy.where(r1 == numpy.max(r1))[0][0]
    class_labels = ["Apple", "Raspberry", "Mango", "Lemon"]
    predicted_class = class_labels[predicted_label]
    return predicted_class

def extract_features(img_path):
    im = PIL.Image.open(img_path).convert("HSV")
    fruit_data_hsv = numpy.asarray(im, dtype=numpy.uint8)

    indices = numpy.load(file="indices.npy")
    
    hist = numpy.histogram(a=fruit_data_hsv[:, :, 0], bins=360)
    im_features = hist[0][indices]
    img_features = numpy.zeros(shape=(1, im_features.size))
    img_features[0, :] = im_features[:im_features.size]
    return img_features

