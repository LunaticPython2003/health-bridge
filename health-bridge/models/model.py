import pickle
import pandas as pd

diagonosis_model = pickle.load(open('./telemedicine_model', 'rb'))
   
decoded_final = {15: "Fungal Infection",4:"Allergy",16:"GERD",9:"Chronic cholestasis",14:'Drug Reaction'
,33:'Peptic ulcer diseae'
,1:'AIDS'
,12:'Diabetes' 
,17:'Gastroenteritis'
,6:'Bronchial Asthma'
,23:'Hypertension' 
,30:'Migraine'
,7:'Cervical spondylosis'
,32:'Paralysis (brain hemorrhage)'
,28:'Jaundice'
,29:'Malaria'
,8:'Chicken pox'
,11:'Dengue'
,37:'Typhoid'
,40:'hepatitis A'
,19:'Hepatitis B'
,20:'Hepatitis C'
,21:'Hepatitis D'
,22:'Hepatitis E'
,3:'Alcoholic hepatitis'
,36:'Tuberculosis'
,10:'Common Cold'
,34:'Pneumonia'
,13:'Dimorphic hemmorhoids(piles)'
,18:'Heart attack'
,39:'Varicose veins'
,26:'Hypothyroidism'
,24:'Hyperthyroidism'
,25:'Hypoglycemia'
,31:'Osteoarthristis'
,5:'Arthritis'
,0:'(vertigo) Paroymsal  Positional Vertigo'
,2:'Acne'
,38:'Urinary tract infection',35:'Psoriasis',27:'Impetigo'
}

csv_file = "predict.csv"

df = pd.read_csv(csv_file)
predictions = diagonosis_model.predict(csv_file)
print(decoded_final[predictions[0]])