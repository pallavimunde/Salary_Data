import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings("ignore")

class Salary_Pred():
    
    def __init__(self,Age,Gender,Education_Level,Experience):
        self.Age = Age
        self.Gender = Gender
        self.Education_Level = Education_Level
        self.Experience = Experience
        
    def load_data(self):
        with open("Model.pkl","rb") as k:
            self.model = pickle.load(k)
        
        with open("pro_data.json","r") as l:
            self.json_data = json.load(l)

        
    def pred_salary(self):
        self.load_data()
        
        test_array = np.zeros([1,len(self.json_data["Col"])])
        
        test_array[0][0] = self.Age
        test_array[0][1] = self.json_data["Gender"][self.Gender]
        test_array[0][2] = self.json_data["Education_Level"][self.Education_Level]
        test_array[0][3] = self.Experience
        print("Test Array -",test_array)
        
        pred_sal = self.model.predict(test_array)
        print("Salary Predicted By Model is :", pred_sal[0].round(2),"-Rs")
        return pred_sal[0].round()
    

