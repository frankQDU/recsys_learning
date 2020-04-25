import os
import numpy as np
import pandas as pd

from os.path import join


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def cal_user_sim_matrix(df):
    # 倒排表
    movie_user = df.groupby(by=['movieId'])['userId'].unique().to_dict()
    userIds = df['userId'].unique().tolist()

    # 基于倒排计算相似矩阵
    user_sim_matrix = {}
    # 初始化相似矩阵
    for userId in userIds:
        user_sim_matrix[userId] = {}
        for other_userId in userIds:
            user_sim_matrix[userId][other_userId] = 0

    # 计算相似矩阵

    pass


def recommend(parameter_list):
    pass


if __name__ == '__main__':
    file_path = '/mnt/ml-latest-small/ratings.csv'
    df = pd.read_csv(file_path)
    # print(df.head())

