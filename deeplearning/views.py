from django.shortcuts import render, redirect
from django.contrib import messages
import numpy as np
import pandas as pd
from matplotlib import image
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def ANNSigmoiod(request):
    context = {}
    context["deeplearningPage"] = True
    template_name = "Deep Learning/Sub-Categories/Artificial NN(Sigmoid).html"
    if request.method == 'POST':
        csv_file = request.FILES['data_file']
        input_csv_file = request.FILES['input_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'data file is not a valid CSV file')
            return redirect('ann')
        if not input_csv_file.name.endswith('.csv'):
            messages.error(request, 'input file is not a valid CSV file')
            return redirect('ann')
        dataset = pd.read_csv(csv_file)
        lst = pd.read_csv(input_csv_file)
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values
        l = len(X[1, :])
        p = (l+1)/2
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        imputer.fit(X[:, :])
        X[:, :] = imputer.transform(X[:, :])
        lst = pd.read_csv(input_csv_file)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0)
        sc = StandardScaler()
        X_train, X_test = sc.fit_transform(X_train), sc.transform(X_test)
        ann = tf.keras.models.Sequential()
        ann.add(tf.keras.layers.Dense(units=p, activation='relu'))
        ann.add(tf.keras.layers.Dense(units=p, activation='relu'))
        ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
        ann.compile(optimizer='adam', loss='binary_crossentropy',
                    metrics=['accuracy'])
        ann.fit(X_train, y_train, batch_size=32, epochs=100)
        result = ann.predict_classes(sc.transform(lst))
    return render(request, template_name, context)


def ANNSoftmax(request):
    context = {}
    context["deeplearningPage"] = True
    template_name = "Deep Learning/Sub-Categories/Artificial NN(Sigmoid).html"
    if request.method == 'POST':
        csv_file = request.FILES['data_file']
        input_csv_file = request.FILES['input_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'data file is not a valid CSV file')
            return redirect('ann-softmax')
        if not input_csv_file.name.endswith('.csv'):
            messages.error(request, 'input file is not a valid CSV file')
            return redirect('ann-softmax')
        dataset = pd.read_csv(csv_file)
        lst = pd.read_csv(input_csv_file)
        X, y = dataset.iloc[:, :-1].values, dataset.iloc[:, -1].values
        l, p = len(X[1, :]), (l+1)/2
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        imputer.fit(X[:, :])
        X[:, :] = imputer.transform(X[:, :])
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=0)
        sc = StandardScaler()
        X_train, X_test = sc.fit_transform(X_train), sc.transform(X_test)
        ann = tf.keras.models.Sequential()
        ann.add(tf.keras.layers.Dense(units=p, activation='relu'))
        ann.add(tf.keras.layers.Dense(units=p, activation='relu'))
        ann.add(tf.keras.layers.Dense(units=1, activation='softmax'))
        ann.compile(optimizer='adam', loss='categorical_crossentropy',
                    metrics=['accuracy'])
        ann.fit(X_train, y_train, batch_size=32, epochs=100)
        result = ann.predict_classes(sc.transform(lst))
    return render(request, template_name, context)
