import pandas as pd


def ingestion_run():

    ### This function will call the dataset and return a dataframe to proced with further steps
    ### It will call a CSV file using the pandas read_csv function as below

    dataset_var = pd.read_csv('./datasets/customer_churn.csv')

    ### 'dropna' is a function that is used to delete Nan values

    #df = dataset.dropna(how='any')

    ### This var will select the columns to proced with the process

    df_var = dataset_var[['Call Failure', 'Subscription Length', 'Charge Amount', 'Seconds of Use', 'Frequency of use',\
                            'Frequency of SMS', 'Distinct Called Numbers', 'Age Group', 'Age', 'Customer Value', 'Churn']]

    return df_var
