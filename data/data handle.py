import json
import pandas as pd


def parse_idomaar_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) >= 4:
                entity_type = parts[0]
                entity_id = int(parts[1])
                timestamp = int(parts[2])
                try:
                    attributes = json.loads(parts[3])
                    data.append((entity_type, entity_id, timestamp, attributes))
                except json.JSONDecodeError:
                    # 忽略JSON解析错误的行
                    continue
    return data

file_path = 'users.idomaar'
data = parse_idomaar_file(file_path)


df = pd.DataFrame(data, columns=['entity_type', 'entity_id', 'timestamp', 'attributes'])


sample_size = 1000
sample_df = df.sample(n=sample_size, random_state=42)


def extract_user_info(attributes):
    return (attributes.get('lastfm_username'), attributes.get('gender'), attributes.get('age'),
            attributes.get('country'), attributes.get('playcount'), attributes.get('playlists'),
            attributes.get('subscribertype'))

sample_df['lastfm_username'], sample_df['gender'], sample_df['age'], sample_df['country'], sample_df['playcount'], sample_df['playlists'], sample_df['subscribertype'] = zip(*sample_df['attributes'].map(extract_user_info))

# 保存数据到CSV文件
sample_df.to_csv('sample_users.csv', index=False)

# 展示前几行数据
print(sample_df.head())
