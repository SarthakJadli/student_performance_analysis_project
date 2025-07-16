import pandas as pd
df = pd.read_csv("student_performance1.csv")
print("Original Dataset:\n", df.head())
df.fillna(0, inplace=True)
marks_columns = ["DSA Marks", "DAA Marks", "Operating System", "DBMS Marks", "Compile Design Marks", "Java Marks"]
df[marks_columns] = df[marks_columns].apply(pd.to_numeric, errors='coerce')
df['average'] = df[marks_columns].mean(axis=1)
def check_placement(row):
    if row['average'] >= 75 and all(row[col] >= 45 for col in marks_columns):
        return 'Yes'
    else:
        return 'No'
df['placement'] = df.apply(check_placement, axis=1)
def assign_companies(avg):
    if avg > 90:
        return ["Amazon", "Microsoft", "Google", "Adobe", "Wipro", "TCS", "Infosys"]
    elif avg > 85:
        return ["Adobe", "Wipro", "TCS", "Infosys"]
    elif avg > 80:
        return ["Wipro", "TCS", "Infosys"]
    elif avg >= 75:
        return ["TCS", "Infosys"]
    else:
        return []
df['company'] = df['average'].apply(assign_companies)
def assign_packages(row):
    avg = row['average']
    companies = row['company']
    if row['placement'] == 'No' or not companies:
        return "None"
    packages = []
    for company in companies:
        if company in ["Amazon", "Microsoft", "Google"]:
            if avg > 95:
                packages.append(f"{company}: ₹4800000")
            elif avg > 90:
                packages.append(f"{company}: ₹4300000")
        elif company in ["Adobe", "Wipro"]:
            if avg > 95:
                packages.append(f"{company}: ₹2500000")
            elif avg > 90:
                packages.append(f"{company}: ₹2300000")
            elif avg > 85:
                packages.append(f"{company}: ₹1600000")
            elif avg > 80 and company == "Wipro":
                packages.append(f"{company}: ₹1300000")
        elif company in ["TCS", "Infosys"]:
            if avg > 95:
                packages.append(f"{company}: ₹1200000")
            elif avg > 90:
                packages.append(f"{company}: ₹1000000")
            elif avg > 85:
                packages.append(f"{company}: ₹850000")
            elif avg > 80:
                packages.append(f"{company}: ₹600000")
            elif avg >= 75:
                packages.append(f"{company}: ₹450000")
    return ", ".join(packages) if packages else "None"
df['package'] = df.apply(assign_packages, axis=1)
df['company'] = df['company'].apply(lambda x: ", ".join(x) if x else "None")
df.to_csv("student_performance_updated3.csv", index=False)
print("\nProcessed Dataset:\n", df.head())
