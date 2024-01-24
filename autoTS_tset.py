# import pandas as pd
# from autots import  AutoTS
# url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
# df = pd.read_csv(url,header = 0,index_col =  0,parse_dates = True).squeeze("columns")
# model = AutoTS(
#     forecast_length = 365,#预测时间
#     frequency = 'D',#每日
#     prediction_interval = 0.9,#置信水平
#     ensemble = 'superensemble',
#     max_generations = 5,#迭代次数
#     num_validations = 2,
#     validation_method = 'backwards',
#     model_list = ['ARIMA','Prophet'],
#     transformer_list = ['differencing','scaling'],
# )
# preds = model.predict(df)
import pandas as pd
from autots import AutoTS
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
df = pd.read_csv(url, header=0, index_col=0, parse_dates=True)
df.squeeze("columns")
model = AutoTS(
    forecast_length=365,
    frequency='D',
    prediction_interval=0.9,
    ensemble='superensemble',
    max_generations=5,
    num_validations=2,
    validation_method='backwards',
    model_list="superfast",
    transformer_list=['differencing','scaling'],
)

model.fit(df)
preds = model.predict()
