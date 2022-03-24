(
    air_df
    .rolling('7D')
    .mean()
    .nlargest(1, 'aqi')
)