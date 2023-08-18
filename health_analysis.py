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
    "Blood test" : ["RBC", "WBC", "PLT", "MCV"],
    "Urine test" : ["Color", "Odor", "Turbidity"],
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
    "Blood test" : ["RBC", "WBC", "PLT", "MCV"],
    "Urine test" : ["Color", "Odor", "Turbidity"],
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
    "Blood test" : ["RBC", "WBC", "PLT", "MCV"],
    "Urine test" : ["Color", "Odor", "Turbidity"],
}

# This is the MCV result for Harry Potter

MCV_result = 86

if MCV_result < 80:
    print("RBCs are smaller than normal:", MCV_result)
elif MCV_result >= 80 and MCV_result <= 100:
    print("RBCs are normal in size:", MCV_result)
else: 
    print("RBCs are bigger than normal:", MCV_result)

# This is the urine color result for Harry Potter

Urine_color_result = "yellow"

if Urine_color_result == "yellow":
    print("Urine color is normal:", Urine_color_result)
else:
    print("Urine color is not normal:", Urine_color_result)

