import pandas as pd 
import matplotlib.pyplot as plt  
data_dir = '../Data/'
R_files = ['R98', 'R99', 'R1400', 'R1401']
U_files = ['U98', 'U99', 'U1400', 'U1401']
def total_expense(files_name):
    all_data = pd.DataFrame()  

    for file_name in files_name:
                data = pd.read_excel(f'../Data/{file_name}.xlsx', sheet_name=(file_name + 'P4S01'))  
                data = pd.DataFrame(data)
                data = data[['year','income_w_m','netincome_w_m']]
                for column in data.columns:
                             data[column] = pd.to_numeric(data[column], errors='coerce')
                             data[column].fillna(data[column].mean(), inplace=True)
                data = data.groupby('year').agg({  
                            'income_w_m': 'sum',   
                            'netincome_w_m': 'sum'     
                                            }).reset_index() 
                data.rename(columns={'year' : 'year_data'},inplace = True)
                             
                              
                p1 = pd.read_excel(f'../Data/{file_name}.xlsx', sheet_name=(file_name + 'P4S02')) 
                p1 = pd.DataFrame(p1) 
                p1 = p1[['year','sale','income_s_y']]
                p1.rename(columns = {'year' : 'year_p'}, inplace = True)
                for column in p1.columns:
                            p1[column] = pd.to_numeric(p1[column], errors='coerce')
                            p1[column].fillna(p1[column].mean(), inplace=True)
                p1 = p1.groupby('year_p').agg({
                    'sale' : 'sum' ,
                    'income_s_y' :'sum'
                }) 
                merged_df = pd.merge(data,p1,left_on='year_data',right_on='year_p') 
                merged_df = pd.DataFrame(merged_df)
                merged_df['before_inflection'] = merged_df['sale'] + merged_df['income_w_m']
                merged_df['before_inflection'] = pd.to_numeric(merged_df['before_inflection'], errors='coerce')
                merged_df['after_inflection'] = merged_df['netincome_w_m'] + merged_df['income_s_y']
                merged_df['after_inflection'] = pd.to_numeric(merged_df['after_inflection'], errors='coerce')

                merged_df = merged_df.drop(columns=['sale','income_w_m','netincome_w_m','income_s_y'])
                all_data = pd.concat([all_data, merged_df], ignore_index=True)    

    plt.figure(figsize=(10, 6))  
    plt.plot(all_data['year_data'], all_data['before_inflection'], label='Before Inflection', marker='o')  
    plt.plot(all_data['year_data'], all_data['after_inflection'], label='After Inflection', marker='x')  
    
    plt.xlabel('Year')  
    plt.ylabel('Value')  
    plt.title('Inflection Points for All R Files')  
    plt.xticks(all_data['year_data'], rotation=45)    
    plt.legend()  
    plt.grid()  
    plt.tight_layout()    
    
    plt.show()  

        
                
total_expense(R_files)          
total_expense(U_files)          
 

                
 
  
  



