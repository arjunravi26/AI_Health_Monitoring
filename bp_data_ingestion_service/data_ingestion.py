import pandas as pd
import scipy.io

class DataIngestion:
    def __init__(self, data_path):
        self.data_path = data_path

    def ingest_data(self):
        self.bp_data = scipy.io.loadmat(self.data_path)
        print(self.bp_data.keys())
        print(self.bp_data['p'][:1])

if __name__ == "__main__":
    data_ingestion = DataIngestion(data_path='data/bp/part_2.mat')
    data_ingestion.ingest_data()
