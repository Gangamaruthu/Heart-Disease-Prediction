from flask import Flask,redirect,url_for,render_template,request
import pymysql

app =Flask(__name__)
@app.route('/prediction', methods=['GET','POST'])

def prediction():
    msg=''
    output=""
    if request.method=='POST':
        age=int(request.form['age'])
        sex=int(request.form['sex'])
        cp=int(request.form['cp'])
        trestbps=int(request.form['trestbps'])
        chol=int(request.form['chol'])
        fbs=int(request.form['fbs'])
        restecg=int(request.form['restecg'])
        thalach=int(request.form['thalach'])
        exang=int(request.form['exang'])
        oldpeak=int(request.form['oldspeak'])
        slope=int(request.form['slope'])
        ca=int(request.form['ca'])
        thal=int(request.form['thal'])
        target =int(request.form['target'])
        test_data=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target]
        print("Testdata",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn import tree

        from sklearn.metrics import accuracy_score

        data = pd.read_csv("heart.csv")
        data.head()

        data.tail()

        data.describe()

        data.info()

        X= data.drop('target', axis=1)
        Y= data['target']

        X.shape

        Y.shape

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        X_train.shape
        
        X_test.shape

        #model = KNeighborsClassifier(n_neighbors=5)
        model = LogisticRegression(random_state=0)
        #model = tree.DecisionTreeClassifier()

        X_test.shape

        model.fit(X_train, Y_train)

        predicted_output = model.predict(X_test)
        print(predicted_output)
        print(Y_test)



        accuracy = accuracy_score(Y_test, predicted_output)
        accuracy

        #X_test=[54,1,0,122,286,0,0,116,1,3.2,1,2,2]
        Predictions = model.predict([test_data])
        print(Predictions)

        #age=int(input("Enter Age: "))
        #sex=int(input("Enter Gender: "))
        #cp=int(input("Enter Chest Pain: "))
        #trestbps=int(input("Enter Blood Pressure: "))
        #chol=int(input("Enter Cholestrol: "))
        #fbs=int(input("Fasting Blood Sugar: "))
        #restecg=int(input("Enter Restecg: "))
        #thalach=int(input("Enter Thalach: "))
        #Exang=int(input("Enter Exang: "))
        #Oldpeak=float(input("Enter Oldpeak: "))
        #slope=int(input("Enter Slope: "))
        #ca=int(input("Enter Ca: "))
        #Thal=int(input("Enter Thal: "))

        #list=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, Exang, Oldpeak, slope, ca, Thal]
        #print(list)
        Predictions = model.predict([test_data])
        print(Predictions)

        if(Predictions[0]==0):
            print("No Heart Disease")
            output="No Heart Disease"
        else:
            print("Heart Disease")
            output="Heart Disease"
    return render_template('heart.html',output=output ,Title="heart.html")
@app.route('/')
def home():
    return render_template('heart.html' , output="output",Title="heart.html")

if __name__=="__main__":
    app.run(port=5000 ,debug=True)

        
        
        