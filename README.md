# Volatility Forecasting of CSI 1000 Index using GARCH(1,1) coding by DeepSeek-R1

This project uses Python and the GARCH(1,1) model to forecast the volatility of the CSI 1000 Index based on historical data. It includes data acquisition, preprocessing, model fitting, volatility prediction, and visualization of the results.

## Project Description
This project aims to analyze the historical price data of the CSI 1000 Index and predict its future volatility using the GARCH(1,1) model. The GARCH(1,1) model is widely used in financial time series analysis to model and forecast volatility. This project serves as an example of how to apply this model to real-world financial data.

## Features
- Fetch historical price data of the CSI 1000 Index using the `akshare` library.
- Calculate daily returns and log returns from the historical price data.
- Fit a GARCH(1,1) model to the log returns to model volatility.
- Forecast future volatility for the next 5 days.
- Visualize daily returns and conditional volatility using `matplotlib`.

## Requirements
- Python 3.8+
- `akshare` (for fetching financial data)
- `pandas` (for data manipulation)
- `numpy` (for numerical computations)
- `arch` (for GARCH model fitting)
- `matplotlib` (for data visualization)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/STVZTS/GARCH-made-by-DeepSeek.git
2. Navigate to the project directory:
   ```bash
   cd GARCH-made-by-DeepSeek
3. Install the required dependencies:
   ```bash
   pip install akshare pandas numpy arch matplotlib
   
## Usage
1. Run the script to fetch data, calculate returns, fit the GARCH model, and visualize the results:
   python CSI1000GARCH.py
2. The script will:
   Fetch historical data from October 17, 2004 to March 7, 2025.
   Save the data to an Excel file named csi1000_data.xlsx.
   Calculate daily and log returns.
   Fit a GARCH(1,1) model to the log returns.
   Forecast volatility for the next 5 days.
   Display a plot of daily returns and conditional volatility.
   
## Example Output
The script will generate the following outputs:
Data File: csi1000_data.xlsx containing the historical price data.
Model Summary: A summary of the fitted GARCH(1,1) model.
Volatility Forecast: Predicted volatility for the next 5 days.
Visualization: A plot showing daily returns and conditional volatility.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, please contact langhuafeiyang@outlook.com.

## Chinese Edition 中文版
## 中证1000指数波动率预测（基于GARCH(1,1)模型） 使用DeepSeek-R1自动编程
本项目使用 Python 和 GARCH(1,1) 模型对中证1000指数的历史数据进行波动率预测。项目包括数据获取、数据预处理、模型拟合、波动率预测以及可视化结果。
项目描述
本项目旨在分析中证1000指数的历史价格数据，并使用 GARCH(1,1) 模型预测其未来的波动率。GARCH(1,1) 模型广泛应用于金融时间序列分析中，用于建模和预测波动率。本项目展示了如何将该模型应用于实际金融数据。
## 功能特点
使用 akshare 库获取中证1000指数的历史价格数据。
计算日收益率和对数收益率。
使用对数收益率拟合 GARCH(1,1) 模型以建模波动率。
预测未来5天的波动率。
使用 matplotlib 可视化日收益率和条件波动率。
## 依赖项
Python 3.8+
akshare（用于获取金融数据）
pandas（用于数据处理）
numpy（用于数值计算）
arch（用于 GARCH 模型拟合）
matplotlib（用于数据可视化）
## 安装
克隆仓库：
bash
git clone https://github.com/STVZTS/GARCH-made-by-DeepSeek.git
进入项目目录：
bash
cd GARCH-made-by-DeepSeek
安装依赖项：
bash
pip install akshare pandas numpy arch matplotlib
## 使用方法
运行脚本以获取数据、计算收益率、拟合 GARCH 模型并可视化结果：
bash
python CSI1000GARCH.py
脚本将执行以下操作：
获取 2004 年 10 月 17 日至 2025 年 3 月 7 日的历史数据。
将数据保存到名为 csi1000_data.xlsx 的 Excel 文件中。
计算日收益率和对数收益率。
使用对数收益率拟合 GARCH(1,1) 模型。
预测未来 5 天的波动率。
显示日收益率和条件波动率的图表。
## 示例输出
脚本将生成以下输出：
数据文件：csi1000_data.xlsx，包含历史价格数据。
模型摘要：拟合的 GARCH(1,1) 模型摘要。
波动率预测：未来 5 天的波动率预测。
可视化图表：显示日收益率和条件波动率的图表。
## 许可证
本项目采用 MIT 许可证。
## 联系方式
如有任何问题或反馈，请联系 langhuafeiyang@outlook.com。
