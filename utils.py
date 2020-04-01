def plot(features, data, get_deps=0, target=None, kind='scatter'):
    if get_deps:
        import matplotlib.pyplot as plt
        import seaborn as sns

    fig, ax = plt.subplots(1, 4, figsize=(20, 4))
    col_count = 0
    if kind == 'scatter':
        plot = sns.scatter
    elif kind == 'count':
        plot = sns.countplot
    elif kind == 'box':
        plot == sns.boxplot 
    else:
        bar = sns.barplot
    
    # start plotting 4 figures at a time
    for ftr in features:
        plot(x=ftr, y='SalePrice', data=data, ax=ax[col_count])
        col_count += 1
    plt.tight_layout()
    plt.show()
    plt.close()
    
# divide a dataframe into several subsets(small dataframes) based on a column value
# feature: categorical column based on which subset should be made
# target: Columnon which subset to  be made
# data: dataframe
def cut_by_column(feature=None, target=None, data=None):
    cut_vals = data[feature].unique()
    if target is not None:
        return [data.loc[data[feature]== i, target] for i in cut_vals]
    else:
        return [data.loc[data[feature]== i,] for i in cut_vals]