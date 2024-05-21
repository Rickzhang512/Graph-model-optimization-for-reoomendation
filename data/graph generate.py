import pandas as pd
import networkx as nx

# 加载数据
songs = pd.read_csv('songs.csv')
users = pd.read_csv('users.csv')
playlists = pd.read_csv('playlists.csv')

# 创建图
G = nx.Graph()

# 添加节点和边
for _, row in songs.iterrows():
    G.add_node(row['song_id'], type='song', name=row['title'])
    G.add_edge(row['song_id'], row['artist_id'], type='created_by')
    G.add_edge(row['song_id'], row['album_id'], type='belongs_to')

for _, row in playlists.iterrows():
    G.add_node(row['playlist_id'], type='playlist')
    for song_id in row['song_ids']:
        G.add_edge(row['playlist_id'], song_id, type='contains')

for _, row in users.iterrows():
    G.add_node(row['user_id'], type='user')
    for playlist_id in row['playlist_ids']:
        G.add_edge(row['user_id'], playlist_id, type='created')

# 打印图信息
print(nx.info(G))










# 定义元路径生成函数
def generate_meta_paths(G, start_node, max_length):
    paths = []
    def dfs(current_path):
        if len(current_path) > max_length:
            return
        last_node = current_path[-1]
        for neighbor in G.neighbors(last_node):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                paths.append(new_path)
                dfs(new_path)
    dfs([start_node])
    return paths

# 示例：生成从特定用户节点出发的元路径
start_node = 'user_1'
meta_paths = generate_meta_paths(G, start_node, 3)
print(meta_paths)

