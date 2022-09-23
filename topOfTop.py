import pandas as pd
import funtions as func
import os
from datetime import date

def submitFile(pPath, bPath, listType):
    osPath = os.path
    if(osPath.isfile(pPath) & osPath.isfile(bPath)):
        premium = pd.read_excel(pPath)
        basic = pd.read_excel(bPath)
        
        premium = func.soltData(premium)
        basic = func.soltData(basic)

        lists = pd.merge(premium,basic, how='outer',on='구매자명')
        lists.fillna(0, inplace=True)
        lists["상품명_x"] = "프리미엄 슈케이스"
        lists["상품명_y"] = "베이직 슈케이스"

        lists['총구매금액'] = lists["구매금액_x"] + lists["구매금액_y"]
        lists = lists.astype({"수량_x":"int", "구매금액_x":"int", "수량_y":"int", "구매금액_y":"int", "총구매금액":"int"})
        if listType == 0:
            lists = lists.sort_values(by=lists.columns[-1], ascending=False)
        elif listType == 1:
            print(listType)
        else:
            print(listType)
        return lists.values.tolist()
    else:
        return []
def saveFile(value):
    df = pd.DataFrame(columns=["구매자명", "상품명x", "수량x", "구매금액x", "상품명y", "수량y", "구매금액y", "총구매금액"], data=value)
    toDay = date.today()
    df.to_excel('./{}-챌린저.xlsx'.format(toDay))