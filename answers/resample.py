(
    air_df
    .resample('W-Mon')
    .mean()
    .sort_values(by='aqi', ascending=False)
)