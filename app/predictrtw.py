def predictrtw(df):
    import pickle
    import pandas as pd
    from sklearn.tree import DecisionTreeRegressor
    # Load model from file
    with open('dt_model.pkl', 'rb') as file:
        model = pickle.load(file)
    pred_sample = df

    df_test = pred_sample.drop(['gender', 'mstatus', 'inj_premise', 'inj_off_hrs', 'age_group'], axis=1)
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    column = ['age_injury', 'avgwage', 'scenai_rtw', 'total_spends', 'scenai_medspends']
    for col in column:
        df_test[[col]] = scaler.fit_transform(df_test[[col]])
    df = df_test.drop(["claimno", 'rtw'], axis=1)

    from sklearn import preprocessing
    df_categorical_1 = df.select_dtypes(include=['object'])
    le = preprocessing.LabelEncoder()
    df_categorical_1 = df_categorical_1.apply(le.fit_transform)
    df = df.drop(df_categorical_1.columns, axis=1)
    df = pd.concat([df, df_categorical_1], axis=1)
    pred_rtw = model.predict(df)
    df_pred_rtw = pd.DataFrame(data=pred_rtw, columns=["rtw_pred"])
    pred_sample.reset_index(drop=True, inplace=True)
    df_pred_rtw.reset_index(drop=True, inplace=True)
    result = pd.concat([pred_sample, df_pred_rtw], axis=1)
    return result.to_dict('records')