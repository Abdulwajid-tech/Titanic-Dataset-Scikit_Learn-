import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.cluster import KMeans
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier


dataset = pd.read_csv("Titanic Disaster Dataset.csv")           #Read Data Set...

dataset = dataset.fillna(method='ffill')                                                       #So we fill NaN value using builtin method...

                                                  #Convert Categorical Data into integer and float...

dataset.Gender.replace({'male' : 0, 'female' : 1 },inplace = True)
dataset.Embarked.replace({'S' : 0, 'C' : 1 ,'Q': 2},inplace = True)

X = dataset.loc[:, ['PassengerId','PClass', 'Gender','Sibling', 'Embarked']]                #X variable contains all the attributes/features...

Y = dataset['Survived'].values                                                              #Y variables contains labels...

X_train , X_test , Y_train, Y_test = train_test_split(X, Y ,test_size = 0.2 ,random_state = 0)          #80% of data into training set and 20% of data into test set...

                                                          #Now we train our models...

linearRegression = LinearRegression()                                           #Linear Regression...
linearRegression.fit(X_train,Y_train)

decisionTreeClassifier = DecisionTreeClassifier()                               #Decision Tree Classifier...
decisionTreeClassifier.fit(X_train,Y_train)

gaussianNB = GaussianNB()                                                       #GaussianNB...
gaussianNB.fit(X_train,Y_train)

kmeans = KMeans()                                                               #KMeans...
kmeans.fit(X_train,Y_train)

rfc = RandomForestClassifier()                                                  #RandomForestClassifier
rfc.fit(X_train,Y_train)

svr = SVR()                                                                     #SVR
svr.fit(X_train,Y_train)

logisticRegression = LogisticRegression()                                       #LogisticRegression
logisticRegression.fit(X_train,Y_train)

multinomialNB = MultinomialNB()                                                 #MultinomialNB
multinomialNB.fit(X_train,Y_train)

bernoulliNB = BernoulliNB()                                                     #BernoulliNB
bernoulliNB.fit(X_train,Y_train)

gradientBoostingClassifier = GradientBoostingClassifier()                       #GradientBoostingClassifier
gradientBoostingClassifier.fit(X_train,Y_train)

                                                            #Now we predict on Test data...

y1_predict = linearRegression.predict(X_test)              #Predict Survival value for X_test data set...


print(y1_predict)                       #In point  -0.9 to 0.9



def givePrediction(passengerID , pClass , gender , sibling , embarked , algo):
    predict = 0
    if(algo=="LinearRegression"):

        predict = LinearRegression.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "DecisionTreeClassifier"):

        predict = DecisionTreeClassifier.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "GaussianNB"):

        predict = GaussianNB.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "KMeans"):

        predict = KMeans.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])                #Give value from 0 to 10

        if( predict < 5 ):
            predict = 0
        elif( predict >= 5):
            predict = 1

    elif (algo == "SVR"):

        predict = SVR.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])               #0.0 TO 0.1

        if(predict <0.05):
            predict = 0
        elif(predict >=0.05 ):
            predict = 1

    elif (algo == "RandomForestClassifier"):

        predict = RandomForestClassifier.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "LogisticRegression"):

        predict = LogisticRegression.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "MultinomialNB"):

        predict = MultinomialNB.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "BernoulliNB"):

        predict = BernoulliNB.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    elif (algo == "GradientBoostingClassifier"):

        predict = GradientBoostingClassifier.predict([passengerID,pClass,getGenderValue(gender),sibling,getEmbarkedValue(embarked)])

    return predict

def getGenderValue(gender):
    if(gender=="Male"):
        return 0
    elif(gender == "Female"):
        return 1

def getEmbarkedValue(embarked):
    if(embarked == "S"):
        return 0
    elif(embarked == "C"):
        return 1
    elif(embarked == "Q"):
        return 2
