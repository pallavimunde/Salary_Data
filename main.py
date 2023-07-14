from flask import Flask ,jsonify,request,render_template
from utils import Salary_Pred
import config

app = Flask(__name__)

@app.route("/")
def home():
    #return jsonify({"Home":"Successful"})
    return render_template("index.html")
    

@app.route("/Salary_Pred", methods = ["GET","POST"])
def salary_pred():    

    if request.method == "POST":
        data = request.form
        print("Data :",data)
        #return jsonify({"RR":"OO"})
        Age = eval(data['Age'])
        Gender = data['Gender']
        Education_Level  = data["Education_Level"]
        Experience = eval(data["Experience"])
        #return jsonify({"RR":"OO"})
        #return jsonify({"RR":"OO"})

        Obj = Salary_Pred(Age,Gender,Education_Level,Experience)
        sal = Obj.pred_salary()
        if sal <= 25000:
            sal=25000

        #return jsonify({"Predicted Salary - ":sal})
        return render_template("index.html", prediction = sal)
        return print(sal)

    elif request.method == "GET":
    
        data = request.args.get
        print("Data - ",data)

        Age = data('Age')
        Gender = data('Gender')
        Education_Level  = data("Education_Level")
        Experience = data("Experience")

        Obj = Salary_Pred(Age,Gender,Education_Level,Experience)
        pred_sal = Obj.pred_salary()
        if pred_sal<=25000:
            pred_sal=25000
        

        return render_template("index.html", prediction = pred_sal)
        return jsonify({"Predicted Salary - ":pred_sal})
        #return jsonify({"Home":"Success"}) #jsonify({"Salary":f"{int(pred_sal)}"}) 

    return jsonify({"Re":"Check 'GET' or 'POST' "})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= config.PORT_NO, debug=False)



    