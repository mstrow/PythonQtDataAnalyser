import pandas as pd

class DataHandler:
    """
    Imports, merges, stores and save the dataframe from the filesystem


    """
    def __init__(self):
        self.dataframe = pd.DataFrame(data=[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]])

    def Open(self, filename="data/Earthquakes1.csv", cols=["magnitude"]):
        self.dataframe = pd.read_csv(filename,
                                     usecols=cols)
        self.dataframe['index'] = range(1, len(self.dataframe) + 1)
        self.dataframe = self.dataframe[['index', cols[0]]]
        self.dataframe.set_index('index')

    def Merge(self, filename="data/Earthquakes2.csv", cols=["magnitude"]):
        df2 = pd.read_csv(filename,
                          usecols=cols)

        self.dataframe = self.dataframe.append(df2)

        self.dataframe['index'] = range(1, len(self.dataframe) + 1)
        self.dataframe = self.dataframe[['index', cols[0]]]
        self.dataframe.set_index('index')

    def Save(self, filename):
        self.dataframe.to_csv(filename, encoding='utf-8')



