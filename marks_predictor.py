import joblib

print("welcome to AI..")

hrs = input("Enter ur hrs : ")

model = joblib.load("mymarksmodel")


print ( model.predict([[ int(hrs) ]] ) )
