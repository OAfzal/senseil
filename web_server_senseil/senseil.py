from sklearn import datasets, svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import csv
import numpy
import random
from twilio.rest import Client as twi

# loading train dataset using csv


# Determining accuracy on test data
# print(clf.predict(test_x[0:]))
# print('------------------------------')
# print("Accuracy of algorithm: "+ str(round(accuracy_score(clf.predict(test_x[0:]), test_y[0:])*100, 1)) + " %")


# from twilio.rest import Client as twi   #importing this to allow us to create a Twilio Client object capable of sending messages between phone numbers

# acc_sid="AC581386961962cc5d454db9cba850e705"

# auth_token="ca4be4ff7462d5658b40bacfe821c891"

# client=twi(acc_sid,auth_token)      #Client object called client created here

# if(clf.predict(soil1[0:]) == '0'):
#     print(clf.predict(soil1[0:]))
#     print("Erodable")

# else:
#     print(clf.predict(soil1[0:]))
#     print("Good to go")

# erod =["Decrement pH value by adding more nitrogenous content", "Need to establish greater cover of vegetation", "Increase amount of biomass added to the soil", "Decrease amount of calcium by cutting down on calcium carbonate fertilizer", "Increase percentage of phosphorus by increasing phosphorus fertilizer dosage"]
# erod1 = ["Ideal soil for growing wheat", "Ideal conditions for grwoing perennial crops", "Advisable to grow grains and cereals on this soil"]

# if(clf.predict(soil1[0:]) == '0'):

#     message=client.messages.create(to = "+923361127068",
#                               from_= "+12017191570",
#                               body = random.choice(erod))
# else:

#     message=client.messages.create(to = "+923361127068",
#                               from_= "+12017191570",
#                               body = random.choice(erod1))

# print(message.sid)

def runModel(ca, p, ph, soc, sand):


    textToSend = ""

    
    erod =["Decrement pH value by adding more nitrogenous content", "Need to establish greater cover of vegetation", "Increase amount of biomass added to the soil", "Decrease amount of calcium by cutting down on calcium carbonate fertilizer", "Increase percentage of phosphorus by increasing phosphorus fertilizer dosage"]
    erod1 = ["Ideal soil for growing wheat", "Ideal conditions for grwoing perennial crops", "Advisable to grow grains and cereals on this soil"]

    acc_sid = "ACcba3b4dcde78726c9d27e3978433de5c"

    auth_token = "9fa7576ca8518eccc5ba337d2e1da088"

    client = twi(acc_sid, auth_token)  # Client object called client created here

    filename = 'training.csv'
    raw_data = open(filename, 'rt')
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)

    filename1 = 'train_y.csv'
    raw_data1 = open(filename1, 'rt')
    reader1 = csv.reader(raw_data1, delimiter=',', quoting=csv.QUOTE_NONE)

    scaler = StandardScaler()
    train_x = (scaler.fit_transform(list(reader)[1:]))

    train_y = list(reader1)[1:]

    print("Training....")

    x, y = train_x, train_y

    clf = svm.SVC(C=7120.0, cache_size=200, class_weight=None, coef0=0.0,
                decision_function_shape='ovr', degree=3, gamma=6.191, kernel='rbf',
                max_iter=-1, probability=False, random_state=None, shrinking=True,
                tol=0.001, verbose=False)

    clf.fit(x, y)

    print("Training Completed!")

    filename2 = 'sorted_test.csv'
    raw_data2 = open(filename, 'rt')
    reader2 = csv.reader(raw_data2, delimiter=',', quoting=csv.QUOTE_NONE)

    filename3 = 'test_y.csv'
    raw_data3 = open(filename1, 'rt')
    reader3 = csv.reader(raw_data3, delimiter=',', quoting=csv.QUOTE_NONE)

    test_x = list(reader2)[1:]
    test_y = list(reader3)[1:]
    soil = []
    soil1 = []
    soil.append(ca)
    soil.append(p)
    soil.append(ph)
    soil.append(soc)
    soil.append(sand)
    soil1.append(soil)

    if(clf.predict(soil1[0:]) == '0'):
            print(clf.predict(soil1[0:]))
            textToSend += "Erodable\n"
            textToSend += random.choice(erod)

    else:
        print(clf.predict(soil1[0:]))
        textToSend +="Good To go\n"
        textToSend +=random.choice(erod1)

    if(clf.predict(soil1[0:]) == '0'):
        

        message=client.messages.create(to = "+923213898699",
                                  from_= "+12028755822",
                                  body = "ERODABLE\n" + random.choice(erod))
    else:
        
        message=client.messages.create(to = "+923213898699",
                                  from_= "+12028755822",
                                  body = "GOOD TO GO\n" + random.choice(erod1))

    return textToSend;

    print(message.sid)
