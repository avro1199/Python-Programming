# -*- coding: utf-8 -*-
'''

The functions and classes defined in this module will be called by a marker script. 
You should complete the functions and classes according to their specified interfaces.

No partial marks will be awarded for functions that do not meet the specifications
of the interfaces.

Last modified 2024-05-07 by Anthony Vanderkop.
Hopefully without introducing new bugs.
'''


### LIBRARY IMPORTS HERE ###
import os
import numpy as np
import keras.applications as ka  # type: ignore
import keras


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)

    '''
    # raise NotImplementedError
    return [(2020338038, 'Rj', 'Avro')]

def load_model():
    '''
    Load in a model using the tf.keras.applications model and return it.
    Insert a more detailed description here
    '''
    # raise NotImplementedError-

    model = ka.MobileNetV2(
        input_shape=None,
        alpha=1.0,
        include_top=True,
        weights='imagenet',
        input_tensor=None,
        pooling=None,
        classes=1000,
        classifier_activation='softmax'
    )

    return model

def load_data(path):
    '''
    Load in the dataset from its home path. Path should be a string of the path
    to the home directory the dataset is found in. Should return a numpy array
    with paired images and class labels.

    Insert a more detailed description here.
    '''

    # raise NotImplementedError

    data = []
    labels = []
    class_names = sorted(os.listdir(path))
    class_to_idx = {class_name: idx for idx,
                    class_name in enumerate(class_names)}

    for class_name in class_names:
        class_dir = os.path.join(path, class_name)
        for img_name in os.listdir(class_dir):
            img_path = os.path.join(class_dir, img_name)
            img = keras.preprocessing.image.load_img(
                img_path, target_size=(224, 224))
            img = keras.preprocessing.image.img_to_array(img) / 255.0
            data.append(img)
            labels.append(class_to_idx[class_name])

    data = np.array(data)
    labels = np.array(labels)
    return data, labels, class_names

def split_data(X, Y, train_fraction, randomize=False, eval_set=True):
    """
    Split the data into training and testing sets. If eval_set is True, also create
    an evaluation dataset. There should be two outputs if eval_set there should
    be three outputs (train, test, eval), otherwise two outputs (train, test).

    To see what type train, test, and eval should be, refer to the inputs of 
    transfer_learning().

    Insert a more detailed description here.
    """
    # raise NotImplementedError

    if randomize:
        indices = np.random.permutation(len(X))
    else:
        indices = np.arange(len(X))

    train_size = int(len(X) * train_fraction)
    eval_test_size = len(X) - train_size

    train_indices = indices[:train_size]
    eval_test_indices = indices[train_size:]

    train_X, eval_test_X = X[train_indices], X[eval_test_indices]
    train_Y, eval_test_Y = Y[train_indices], Y[eval_test_indices]

    if eval_set:
        eval_X = eval_test_X[:(len(eval_test_X)//2)]
        eval_Y = eval_test_Y[:(len(eval_test_Y)//2)]
        test_X = eval_test_X[(len(eval_test_X)//2):]
        test_Y = eval_test_Y[(len(eval_test_Y)//2):]

        return train_X, train_Y, eval_X, eval_Y, test_X, test_Y
    else:
        return train_X, train_Y, eval_test_X, eval_test_Y
    

def confusion_matrix(predictions, ground_truth, plot=False, all_classes=None):
    '''
    Given a set of classifier predictions and the ground truth, calculate and
    return the confusion matrix of the classifier's performance.

    Inputs:
        - predictions: np.ndarray of length n where n is the number of data
                       points in the dataset being classified and each value
                       is the class predicted by the classifier
        - ground_truth: np.ndarray of length n where each value is the correct
                        value of the class predicted by the classifier
        - plot: boolean. If true, create a plot of the confusion matrix with
                either matplotlib or with sklearn.
        - classes: a set of all unique classes that are expected in the dataset.
                   If None is provided we assume all relevant classes are in 
                   the ground_truth instead.
    Outputs:
        - cm: type np.ndarray of shape (c,c) where c is the number of unique  
              classes in the ground_truth

              Each row corresponds to a unique class in the ground truth and
              each column to a prediction of a unique class by a classifier
    '''
    # raise NotImplementedError
    
    if all_classes is None:
        all_classes = np.unique(ground_truth)
    
    cm = np.zeros((len(all_classes), len(all_classes)), dtype=int)
    
    class_to_index = {cls: idx for idx, cls in enumerate(all_classes)}
    
    for true, pred in zip(ground_truth, predictions):
        cm[class_to_index[true], class_to_index[pred]] += 1
    
    if plot:
        try:
            import matplotlib.pyplot as plt
            import seaborn as sns
            
            plt.figure(figsize=(10, 7))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=all_classes, yticklabels=all_classes)
            plt.ylabel('True Class')
            plt.xlabel('Predicted Class')
            plt.title('Confusion Matrix')
            plt.show()
        except ImportError:
            print("Plotting is disabled. Install matplotlib and seaborn to enable plotting.")
    
    return cm


def precision(predictions, ground_truth):
    '''
    Similar to the confusion matrix, now calculate the classifier's precision

    Inputs: see confusion_matrix above
    Outputs:
        - precision: type np.ndarray of length c,
                     values are the precision for each class
    '''
    raise NotImplementedError
    return precision


def recall(predictions, ground_truth):
    '''
    Similar to the confusion matrix, now calculate the classifier's recall

    Inputs: see confusion_matrix above
    Outputs:
        - recall: type np.ndarray of length c,
                     values are the recall for each class
    '''
    raise NotImplementedError
    return recall


def f1(predictions, ground_truth):
    '''
    Similar to the confusion matrix, now calculate the classifier's f1 score
    Inputs:
        - see confusion_matrix above for predictions, ground_truth
    Outputs:
        - f1: type nd.ndarry of length c where c is the number of classes
    '''

    raise NotImplementedError
    return f1


def k_fold_validation(features, ground_truth, classifier, k=2):
    '''
    Inputs:
        - features: np.ndarray of features in the dataset
        - ground_truth: np.ndarray of class values associated with the features
        - fit_func: f
        - classifier: class object with both fit() and predict() methods which
        can be applied to subsets of the features and ground_truth inputs.
        - predict_func: function, calling predict_func(features) should return
        a numpy array of class predictions which can in turn be input to the 
        functions in this script to calculate performance metrics.
        - k: int, number of sub-sets to partition the data into. default is k=2
    Outputs:
        - avg_metrics: np.ndarray of shape (3, c) where c is the number of classes.
        The first row is the average precision for each class over the k
        validation steps. Second row is recall and third row is f1 score.
        - sigma_metrics: np.ndarray, each value is the standard deviation of 
        the performance metrics [precision, recall, f1_score]
    '''

    # split data
    ### YOUR CODE HERE ###

    # go through each partition and use it as a test set.
    for partition_no in range(k):
        # determine test and train sets
        ### YOUR CODE HERE###

        # fit model to training data and perform predictions on the test set
        classifier.fit(train_features, train_classes)
        predictions = classifier.predict(test_features)

        # calculate performance metrics
        ### YOUR CODE HERE###

    # perform statistical analyses on metrics
    ### YOUR CODE HERE###

    raise NotImplementedError
    return avg_metrics, sigma_metrics


##################### MAIN ASSIGNMENT CODE FROM HERE ######################

# def transfer_learning(train_set, eval_set, test_set, model, parameters):
def transfer_learning():
    '''
    Implement and perform standard transfer learning here.

    Inputs:
        - train_set: list or tuple of the training images and labels in the
            form (images, labels) for training the classifier
        - eval_set: list or tuple of the images and labels used in evaluating
            the model during training, in the form (images, labels)
        - test_set: list or tuple of the training images and labels in the
            form (images, labels) for testing the classifier after training
        - model: an instance of tf.keras.applications.MobileNetV2
        - parameters: list or tuple of parameters to use during training:
            (learning_rate, momentum, nesterov)


    Outputs:
        - model : an instance of tf.keras.applications.MobileNetV2
        - metrics : list of classwise recall, precision, and f1 scores of the 
            model on the test_set (list of np.ndarray)

    '''
    input_shape = (224, 224, 3)
    num_classes = 5
    base_model = ka.MobileNetV2(
        weights='imagenet', include_top=False, input_shape=input_shape)
    base_model.trainable = False

    inputs = keras.Input(shape=input_shape)
    x = base_model(inputs, training=False)
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Dense(1024, activation='relu')(x)
    outputs = keras.layers.Dense(num_classes, activation='softmax')(x)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer='adam', loss=keras.losses.SparseCategoricalCrossentropy(
        from_logits=False), metrics=['accuracy'])
    return model
    # raise NotImplementedError
    return model, metrics


def accelerated_learning(train_set, eval_set, test_set, model, parameters):
    '''
    Implement and perform accelerated transfer learning here.

    Inputs:
        - train_set: list or tuple of the training images and labels in the
            form (images, labels) for training the classifier
        - eval_set: list or tuple of the images and labels used in evaluating
            the model during training, in the form (images, labels)
        - test_set: list or tuple of the training images and labels in the
            form (images, labels) for testing the classifier after training
        - model: an instance of tf.keras.applications.MobileNetV2
        - parameters: list or tuple of parameters to use during training:
            (learning_rate, momentum, nesterov)


    Outputs:
        - model : an instance of tf.keras.applications.MobileNetV2
        - metrics : list of classwise recall, precision, and f1 scores of the 
            model on the test_set (list of np.ndarray)

    '''
    raise NotImplementedError
    return model, metrics


if __name__ == "__main__":

    # model = load_model()
    model = transfer_learning()
    # model.summary()  # new added
    # dataset = load_data('small_flower_dataset')
    im, id, cl = load_data('small_flower_dataset')

    model.fit(im, id, epochs=1) ############### training part ###############

    # #test-01
    output = model.predict(im)
    # # print(out)
    # i = 0
    # for out in output:
    #     print(i, out.argmax(), out.max(), cl[out.argmax()], sep='=>')
    #     i += 1

    #test-02
    # out = model.predict(im[no][np.newaxis, ...])
    # no = 300
    # print(im[no], id[no], cl[id[no]], sep=' => ')
    # print(im[0].shape)
    # import matplotlib.pyplot as plt
    # plt.imshow(im[no])
    # plt.title(cl[id[no]])
    # plt.show()

    # img_path = 'goose.jpeg'
    # img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    # img = keras.preprocessing.image.img_to_array(img) / 255.0

    # op = model.predict(img[np.newaxis, ...])
    # print(op.argmax(), op.max(), sep='=>')
    # plt.imshow(img)
    # plt.show()

##################int code##################
    # train_eval_test = split_data()

    # model, metrics = transfer_learning()

    # model, metrics = accelerated_learning()

    ##### split data test
    # x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # y = x * 100

    # o = split_data(x, y, .6, randomize=True, eval_set=True)
    # print(o[0], o[1],sep='=>')
    # print(o[2], o[3],sep='=>')
    # print(o[4], o[5],sep='=>')

    predictions = np.array(list(out.argmax() for out in output))
    ground_truth = id

    # print(predictions)
    # print(ground_truth)

    # Calculate confusion matrix without plotting
    cm = confusion_matrix(predictions, ground_truth)
    print("Confusion Matrix (without plot):\n", cm)

    # Calculate and plot confusion matrix
    cm_plot = confusion_matrix(predictions, ground_truth, plot=True)

#########################  CODE GRAVEYARD  #############################
