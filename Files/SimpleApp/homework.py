import pickle

names = ["Dio", "Erina", "Poko", "Jonathan", "Speedvagen"]
print(names)
pickle.dump(names, open("names.dat", "wb"))

names.remove("Jonathan")
print(names)

names = pickle.load(open("names.dat", "rb"))
print(names)
