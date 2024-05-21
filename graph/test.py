from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col
import json

# 初始化SparkSession
spark = SparkSession.builder.appName("CFRecommendation").getOrCreate()

# 加载数据
def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['playlists']

data_files = ["path_to_mpd.slice.0-999.json", "path_to_mpd.slice.1000-1999.json"] # 示例数据文件路径
data = []
for file in data_files:
    data.extend(load_data(file))

# 构建DataFrame
rows = []
for playlist in data:
    for track in playlist['tracks']:
        rows.append((playlist['pid'], track['track_uri'], 1))

columns = ['user_id', 'item_id', 'interaction_value']
df = spark.createDataFrame(rows, columns)

# 划分训练集和测试集
(train, test) = df.randomSplit([0.8, 0.2], seed=42)

# ALS模型训练
als = ALS(maxIter=10, regParam=0.1, userCol="user_id", itemCol="item_id", ratingCol="interaction_value", coldStartStrategy="drop")
model = als.fit(train)

# 生成推荐
userRecs = model.recommendForAllUsers(10)
itemRecs = model.recommendForAllItems(10)

# 模型评估
predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="interaction_value", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print(f"Root-mean-square error = {rmse}")
