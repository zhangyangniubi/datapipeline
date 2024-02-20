import pandas as pd
df = pd.read_csv('./utils/rawimus.csv')
gps_week = df['Week']
gps_second = df['Seconds']/1000
df['gps_epoch_second'] = 315964800 + gps_week * 7 * 24 * 60 * 60 + gps_second - 18
gps_epoch_second = df['gps_epoch_second']
df = df.drop('gps_epoch_second',axis=1)
df.insert(1,'gps_epoch_second',gps_epoch_second)
df.to_csv('rawimus.csv')


def GetGPSEpochSecond(gps_week,gps_second):
    gps_epoch_s = 315964800 + gps_week * 7 * 24 * 60 * 60 + gps_second - 18
    return gps_epoch_s

#########some modified
