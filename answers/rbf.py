X_gsf = air_df[['time_point']].copy()

days = X_gsf.index.dayofyear

for month in month_peaks.index:
    peak = month_peaks.at[month]
    X_gsf[month] = gsf_feature_maker(peak, days)

X_gsf_train = X_gsf.loc[:'2014']
X_gsf_test = X_gsf.loc['2015':]

lm_rbf = LinearRegression()

lm_rbf.fit(X_gsf_train, y_train)

air_df['linear_rbf'] = lm_rbf.predict(X_gsf)

air_df[['aqi','linear_rbf']].loc[:'2014'].plot(color=['#499DE6','red']);
