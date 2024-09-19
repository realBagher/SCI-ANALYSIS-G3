import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  

R_files = ['R98', 'R99', 'R1400', 'R1401']  
U_files = ['U98', 'U99', 'U1400', 'U1401']  
data_dir = '../Data/'

def matrix_correlation(files_name):   
    for file_name in files_name:  
        file_path = f'../Data/{file_name}.xlsx'
        
        sheet_names = [f"{file_name}P3S03", f"{file_name}P3S01", f"{file_name}P3S04", f"{file_name}P3S06"]  
        
        dfs = []   
        
        for sheet in sheet_names:  
            df = pd.read_excel(file_path, sheet_name=sheet)  
            df.columns = [f"{col}_{sheet}" if col != 'Address' else 'Address' for col in df.columns]   
            dfs.append(df)  

        merged_df = dfs[0]  
        for df in dfs[1:]:  
            merged_df = pd.merge(merged_df, df, on='Address', how='outer')    

        print(f"\nDataFrame for {file_name} merged columns:")  
        print(merged_df.columns.tolist())  

        for col in merged_df.columns:  
            if col != 'Address':    
                merged_df[col] = pd.to_numeric(merged_df[col], errors='coerce')  

        numeric_features = merged_df.select_dtypes(include='number')  

        correlation_matrix = numeric_features.corr()  
        print(f"\nCorrelation Matrix for {file_name}:")  
        print(correlation_matrix)  

        plt.figure(figsize=(10, 6))  
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True, linewidths=0.5)  
        plt.title(f'Correlation Matrix Heatmap - {file_name}', fontsize=16)  
        plt.xlabel('Features', fontsize=12)  
        plt.ylabel('Features', fontsize=12)  
        plt.tight_layout()  
        plt.show()  

matrix_correlation(R_files)
matrix_correlation(U_files)