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

# get a dataframe of all the columns and corresponding null values in percentages
def get_na_stats(dataframe):
    nas = dataframe.isna().sum()
    columns = nas.index
    values = nas.values / len(dataframe) * 100

    df = pd.DataFrame({
        'columns': columns,
        'values_': values.round(2)
    })
    return df.loc[df.values_ > 0, :].sort_values(by=['values_'], ascending=False).reset_index(drop=True)

def qqplot(x, plt):
    mean = x.mean()
    std = x.std()
    shape = x.shape
    a = np.random.normal(mean, std, shape)
    b = x.values

    # linspace generates evenly distributed numbers b/w start and end
    # third argument specifies count of numbers to generate
    percs = np.linspace(0, 100, x.shape[0])
    qn_a = np.percentile(a, percs)
    qn_b = np.percentile(b, percs)

    plt.plot(qn_a,qn_b, ls="", marker="o")

    x = np.linspace(np.min((qn_a.min(),qn_b.min())), np.max((qn_a.max(),qn_b.max())))
    plt.plot(x,x, color="k", ls="--")

#===============================================
# EXTENDING PANDAS DATAFRAME WITH CUSTOM METHODS
#===============================================
@pd.api.extensions.register_dataframe_accessor("custom")
class Custom:
    def __init__(self, pandas_obj):
#         self._validate(pandas_obj)
        self._obj = pandas_obj

    def screen_df(self):
        df = self._obj
        shape = df.shape
        nduplicate = df[df.duplicated()].shape[0]
        nnum_col = len(df.select_dtypes(exclude=[np.object]).columns)
        ncat_col = len(df.select_dtypes(include=[np.object]).columns)

        print(f'Shape: {shape}')
        print(f'no. of duplicates: {nduplicate}')
        print(f'no. of numerical features: {nnum_col}')
        print(f'no. of categorical features: {ncat_col}')

    def get_na_stats(self):
        df = self._obj
        nas = df.isna().sum()
        columns = nas.index
        values = nas.values / len(df) * 100

        na_df = pd.DataFrame({
            'columns': columns,
            'values_': values.round(2)
        })
        na_df = na_df.loc[na_df.values_ > 0, :]
        na_df = na_df.sort_values(by=['values_'],ascending=False).reset_index(drop=True)
        return na_df


ALPHABET_LEN = 26
if __name__ == '__main__':
    alien_ordered_string = input()
    string = input()
    assert len(alien_ordered_string) == ALPHABET_LEN

    dict_ = {}
    # get the corresponding index of each element
    for char in string:
        dict_[char] = alien_ordered_string.index(char.lower())

    # sort the dicitionary
    sorted_dict = sorted(dict_.items(), key=lambda x: (x[0],x[1]), reverse=True)
    new_string = ''
    for tup in sorted_dict:
        new_string += tup[0]

    print(new_string)

    test_string1 = 'wvutsrqponmlkjihgfedcbaxyz'
    test_string2 = 'camelCasE'

