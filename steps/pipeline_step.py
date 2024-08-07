from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def pipeline_run():
    
    ### Pipe function is made on sklearn pipeline structure and basically all the additional data transformation needded will run here
    ### The data is splited in numerical and categorical so it will be possible to provide proper destination as explained bellow
    
    ###-----NUMERICAL-----###

    # Numerical columns to be transformed
    numerical_features = ['Call Failure', 'Subscription Length', 'Charge Amount', 'Seconds of Use', 'Frequency of use',\
                            'Frequency of SMS', 'Distinct Called Numbers', 'Age Group', 'Age', 'Customer Value']

    # Pipeline for numerical data with the steps commented bellow
    # Using method SimpleImputer to fill the empty numerical spaces with the median
    numerical_transform = Pipeline(steps=[\
                                            ('imputer', SimpleImputer(strategy='median')), \
                                            ('scaler', StandardScaler())\
                                            ])

    ###-----CATEGORICAL-----###

    # Categorical columns to be transformed
    categorical_features = []

    # Pipeline for categorical data with the steps commented bellow
    # Use OneHotEncoder to transform categorical data
    categorical_transform = Pipeline(steps=[\
                                            ('one-hot-encoder', OneHotEncoder(handle_unknown='ignore'))\
                                                ])

    ### PREPROCESSOR ###

    #Creating a preprocessor with the pipelines above to be used on training step
    pipeline_preprocessor = ColumnTransformer(transformers=[\
                                                            #('numerical', numerical_transform, numerical_features), \
                                                            #('categorical', categorical_transform, categorical_features) \
                                                            ], remainder='passthrough')

    return pipeline_preprocessor