import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
X = df[marks_columns]
y = df['placement']
imputer = SimpleImputer(strategy='mean')
X = pd.DataFrame(imputer.fit_transform(X), columns=marks_columns)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
print("\nEnter the marks of the new student out of 100:")
try:
    dsa = float(input("DSA: "))
    daa = float(input("DAA: "))
    os = float(input("Operating System: "))
    dbms = float(input("DBMS: "))
    compiledesign = float(input("Compile Design: "))
    java = float(input("Java: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()
new_student = pd.DataFrame([[dsa, daa, os, dbms, compiledesign, java]], columns=marks_columns)
new_student_imputed = pd.DataFrame(imputer.transform(new_student), columns=marks_columns)
pred = model.predict(new_student_imputed)[0]
average = new_student.mean(axis=1).values[0]
min_mark = new_student.min(axis=1).values[0]
rule_based_placement = 1 if average >= 75 and min_mark >= 45 else 0
def get_companies_and_packages(avg, placed):
    if placed == 0 or avg < 75:
        return [], "None"
    companies = assign_companies(avg)
    temp_row = pd.Series({'average': avg, 'company': companies, 'placement': 1})
    packages = assign_packages(temp_row)
    return companies, packages
eligible_companies, eligible_packages = get_companies_and_packages(average, rule_based_placement)
print(f"\nModel Prediction: {'Yes' if pred == 1 else 'No'}")
print(f"Final Placement Decision (Rule-Based): {'Yes' if rule_based_placement else 'No'}")
print(f"Average Marks: {average:.2f}")
print(f"Eligible Companies: {', '.join(eligible_companies) if eligible_companies else 'None'}")
print(f"Package Offers: {eligible_packages}")
