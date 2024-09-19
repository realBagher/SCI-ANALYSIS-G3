import pandas as pd  
import matplotlib.pyplot as plt  
data_dir = '../Data/'
R_files = ['R98', 'R99', 'R1400', 'R1401']
U_files = ['U98', 'U99', 'U1400', 'U1401']
results = {}  
all_total_values = {}  
def trend(files_name)  :
    

    for file_name  in files_name:
          
        try: 
             
            df = pd.read_excel(f'../Data/{file_name}.xlsx', sheet_name=(file_name + 'P3S11'))  
        
            filtered_data = df[(df['code'] >= 111111) & (df['code'] <= 112016)]  
        
            filtered_data['total_value'] = filtered_data['purchased'] * filtered_data['value']  
        
            household_expenses = filtered_data.groupby('Address')['total_value'].sum().reset_index()  
        
            results[file_name] = household_expenses  
        
            all_total_values[file_name] = household_expenses['total_value']  

        except Exception as e:  
            print(f"An error occurred while processing {file_name}: {e}")  

    plt.figure(figsize=(10, 6))  

    num_bins = 50  

    for file_name, total_values in all_total_values.items():  
       plt.hist(total_values, bins=num_bins, alpha=0.5, label=file_name, edgecolor='black')  

    plt.title('Distribution of Household Expenses', fontsize=16)  
    plt.xlabel('Total Expenses (in your currency)', fontsize=14)  
    plt.ylabel('Number of Households', fontsize=14)  

    plt.yscale('log')   
    plt.grid(axis='y', alpha=0.75)  
    plt.legend(title='Files')  

    plt.tight_layout()  
    plt.show() 
trend(R_files)
trend(U_files)


