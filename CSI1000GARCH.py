import akshare as ak
import pandas as pd
import numpy as np
from arch import arch_model
import matplotlib.pyplot as plt

# 获取中证1000历史数据
csi1000 = ak.index_zh_a_hist(symbol="000852", start_date="20041017", end_date="20250307")

# 查看数据条数
print("数据条数：", csi1000.shape[0])
csi1000.to_excel('csi1000_data.xlsx', index=False)
print("数据已成功保存到 'csi1000_data.xlsx' 文件中")

#将 "日期" 列转换为 Pandas 的 datetime 类型，方便后续的时间序列操作。
#将 "日期" 列设置为 DataFrame 的索引，方便按日期进行数据操作。
csi1000['日期'] = pd.to_datetime(csi1000['日期'])
csi1000.set_index('日期', inplace=True)
print("数据的起始日期：", csi1000.index.min())
print("数据的结束日期：", csi1000.index.max())

# 计算百分比收益率
returns = 100*csi1000['收盘'].pct_change().dropna()

# 计算对数收益率
log_returns = 100*np.log(csi1000['收盘'] / csi1000['收盘'].shift(1)).dropna()

# 建立GARCH(1,1)模型
garch = arch_model(log_returns, vol='Garch', p=1, q=1, dist='normal')
model = garch.fit(update_freq=5)

# 输出模型摘要
print(model.summary())

# 预测未来5天波动率
forecast = model.forecast(horizon=5, reindex=False)
print("\n未来5天波动率预测：")
print(forecast.variance.iloc[-1].apply(lambda x: x**0.5))

# 可视化结果
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者使用 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False  # 用于正常显示负号
plt.figure(figsize=(12,6))
plt.plot(returns, label='日收益率')
plt.plot(model.conditional_volatility, label='条件波动率')
plt.title('中证1000指数波动率预测')
plt.legend()
plt.show()

