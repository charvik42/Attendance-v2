# List of all users in encodings.pkl
import pickle
with open('encodings.pkl', 'rb') as f:
    encodeListKnown, classNames = pickle.load(f)

print("Stored Users in encodings.pkl:")
for i, name in enumerate(classNames):
    print(f"{i + 1}. {name}")

# Delete encodings.pkl if needed
# import os
# if os.path.exists('encodings.pkl'):
#     os.remove('encodings.pkl')
#     print("encodings.pkl has been deleted.")
# else:
#     print("encodings.pkl not found.")