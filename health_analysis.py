import pandas as pd
import numpy as np

# This is a list of all the patients

PatientA = {
    "Firstname" : "Harry",
    "Lastname" : "Potter",
    "Age" : "16",
    "Sex" : "M",
    "Disease" : {
        "Chronic" : "None",
        "Acute" : "None",
    },
    "Tests" : {
        "Blood test" : ["RBC", "WBC", "PLT", "MCV"],
        "Urine test" : ["Color", "Odor", "Turbidity"],
    }
}

PatientB = {
    "Firstname" : "Ron",
    "Lastname" : "Weasley",
    "Age" : "16",
    "Sex" : "M",
    "Disease" : {
        "Chronic" : "None",
        "Acute" : "None",
    },
    "Tests" : {
        "Blood test" : ["RBC", "WBC", "PLT", "MCV"],
        "Urine test" : ["Color", "Odor", "Turbidity"],
    }
}

PatientC = {
    "Firstname" : "Hermione",
    "Lastname" : "Granger",
    "Age" : "16",
    "Sex" : "F",
    "Disease" : {
        "Chronic" : "None",
        "Acute" : "None",
    },
    "Tests" : {
        "Blood test" : ["RBC", "WBC", "PLT", "MCV"],
        "Urine test" : ["Color", "Odor", "Turbidity"],
    }
}

# This is a list of the MCV results 

def MCV_result(Name, MCV):
    if MCV < 80:
        result = Name + ": RBCs are smaller than normal"
    elif MCV >= 80 and MCV <= 100:
        result = Name + ": RBCs are normal in size"
    else:
        result = Name + ": RBCs are bigger than normal" 
    return result

Patient_result = MCV_result("Harry Potter", 86)
print(Patient_result)

Patient_result = MCV_result("Ron Weasley", 70)
print(Patient_result)

Patient_result = MCV_result("Hermione Granger", 103)
print(Patient_result)

# This is a list of the urine color results

def Urine_color_result(Name, Color):
    if Color == "Yellow":
        result = Name + ": the urine color is normal"
    else:
        result = Name + ": the urine color is not normal"
    return result

Patient_result = Urine_color_result("Harry Potter", "Yellow")
print(Patient_result)

Patient_result = Urine_color_result("Ron Weasley", "Black")
print(Patient_result)

Patient_result = Urine_color_result("Hermione Granger", "Yellow")
print(Patient_result)