import pandas as pd
import numpy as np

def getListChange(path,col1,col2):
    _lists = pd.read_excel(path)
    _lists[col1] = _lists[col1]+_lists[col2]
    _lists = _lists.drop(columns=[col2])
    print(_lists)
    return _lists

def twoColMultiply(data, col1,col2, list1, list2):
    condlist = [ (data[col1].str.contains(pat=requirement, regex=False)) for requirement in list1]
    choicelist = [ (list2[value] * data[col2]) for value in range(len(list1))]
    _calculator = np.select(condlist, choicelist, default=0)
    return _calculator

def allDataAdd(data,customers,col1,col2):
    _result = pd.DataFrame(columns=[col1,col2])
    for name in customers:
        _allList = data[data[col1] == name]
        total = _allList[col2].sum()
        _result.loc[len(_result)] = [name, total]
    return _result.sort_values(col2,ascending=False)

def soltData(data):
    _result = data
    _result = _result[~_result['주문상태'].isin(['취소','반품'])]
    _result = _result[_result['상품명'].str.contains('슈박스')]
    _result['구매자명'] = _result['구매자명']+_result['구매자ID']
    _result = _result.groupby(['구매자명', '상품명'])['수량'].sum()
    _result = _result.reset_index()
    _result['구매금액'] = twoColMultiply(_result,'상품명','수량',['프리미엄','잔디매트'],[14900,10900])
    return _result