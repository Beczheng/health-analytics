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
        result = "RBCs are smaller than normal for " + Name, MCV
    elif MCV >= 80 and MCV <= 100:
        result = "RBCs are smaller than normal for " + Name, MCV
    else:
        result = "RBCs are smaller than normal for " + Name, MCV
    return result 

Patient_MCV_result = MCV_result("Harry Potter", 86)
print(Patient_MCV_result)

Patient_MCV_result = MCV_result("Ron Weasley", 70)
print(Patient_MCV_result)

Patient_MCV_result = MCV_result("Hermione Granger", 103)
print(Patient_MCV_result)

# This is a list of the urine color results

def Urine_color_result(Name, Color):
    if Color == "Yellow":
        result = "The urine color is normal for " + Name, Color
    else:
        result = "The urine color is not normal for " + Name, Color
    return result

Patient_urine_color_result = Urine_color_result("Harry Potter", "Yellow")
print(Patient_urine_color_result)

Patient_urine_color_result = Urine_color_result("Ron Weasley", "Black")
print(Patient_urine_color_result)

Patient_urine_color_result = Urine_color_result("Hermione Granger", "Yellow")
print(Patient_urine_color_result)