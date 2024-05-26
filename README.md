
# Graph Model Optimization for Music Recommendation

## Overview

This project explores the optimization of graph-based models for music recommendation systems. The aim is to enhance recommendation accuracy by refining the algorithmic framework to better capture user-music interactions. The implementation leverages the `NetworkX` and `StellarGraph` libraries to construct and analyze heterogeneous graphs representing user and music data.

## Objectives

- Construct a music recommendation system using heterogeneous graphs.
- Address challenges in existing graph-based techniques like efficiency and scalability.
- Optimize graph models to improve recommendation accuracy and user satisfaction.

## Research Questions

1. How can heterogeneous graphs be used to model relationships in music data?
2. What benefits do `StellarGraph` and `NetworkX` bring to music recommendation systems?
3. How do these optimizations influence user satisfaction and engagement?

## Methodology

### Libraries and Tools

- **NetworkX**: Used for basic graph operations and prototyping.
- **StellarGraph**: Handles large-scale graph data suitable for advanced machine learning tasks.
- **HinSAGE Algorithm**: Extends GraphSAGE to work with heterogeneous graph data, making it suitable for complex datasets.

### Data

The project uses the 30Music dataset, which includes user playlists, listening sessions, positive ratings, and more. This dataset is crucial for predicting user preferences and making playlist recommendations. https://recsys.deib.polimi.it/datasets/

### Graph Construction

1. **Neighborhood Sampling**: For each node, a fixed-size neighborhood is sampled, involving neighbors from different node types.
2. **Aggregation**: Features of the sampled neighbors are aggregated. In heterogeneous graphs, this can be type-specific.
3. **Concatenation and Final Prediction**: Embeddings of node pairs are concatenated and passed through a final estimator layer to produce the predicted score.

### Evaluation Metrics

- **Mean Squared Error (MSE)**
- **Mean Absolute Error (MAE)**
- **Root Mean Square Error (RMSE)**

## Results

- The model significantly outperformed the baseline in terms of MAE and RMSE.
- Visualization techniques like histograms and scatter plots were used to understand data patterns and relationships.

## Usage

### Requirements

- Python 3.x
- NetworkX
- StellarGraph
- Other dependencies as specified in the Jupyter notebook

### Running the Notebook

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Open and run the `Music_Recommendation.ipynb` notebook.

```bash
pip install -r requirements.txt
jupyter notebook Music_Recommendation.ipynb
```

### Code Structure

- **Data Preparation**: Loading and preprocessing the 30Music dataset.
- **Graph Construction**: Building heterogeneous graphs using NetworkX and StellarGraph.
- **Model Training**: Implementing the HinSAGE algorithm to train the recommendation model.
- **Evaluation**: Assessing model performance using MAE and RMSE.

## Conclusion

This project demonstrates the effectiveness of using optimized graph models for music recommendation systems. By leveraging `NetworkX` and `StellarGraph`, we can handle complex user-music interactions and provide personalized recommendations with improved accuracy.

