import pandas as pd
import re

def convert(hk):
    if hk == "10":
        return "học kì 1"
    elif hk == "02":
        return "học kì 2"
    elif hk == "12":
        return "học kì 1, 2"
    else:
        return "không có học kì nào" 

class QueryProcessing():
    @staticmethod
    def process(query):
        result = {}
        if query.startswith("PRINT_ALL"):
            result["type"] = "PRINT_ALL"
        elif query.startswith("ITERATE"):
            result["type"] = "ITERATE"
        elif query.startswith("YES-NO"):
            result["type"] = "YES-NO"

        pattern = r'\([^()&]+\)'
        matches = re.findall(pattern, query)
        for i in matches:
            if i.startswith("(MH"):
                if "?" in i:
                    result["MH"] = []
                else:
                    if not result.get("MH", []):
                        result["MH"] = []
                    result["MH"].append(i.split("=")[-1].strip()[:-1])
            elif i.startswith("(MSMH"):
                if "?" in i:
                    result["MSMH"] = []
                else:
                    if not result.get("MSMH", []):
                        result["MSMH"] = []
                    result["MSMH"].append(i.split("=")[-1].strip()[:-1])
            elif i.startswith("(HK"):
                if "?" in i:
                    result["HK"] = None
                else:
                    result["HK"] = i.split("=")[-1].strip()[:-1]
            elif i.startswith("(NH"):
                if "?" in i:
                    result["NH"] = []
                else:
                    if not result.get("NH", []):
                        result["NH"] = []
                    result["NH"].append(i.split("=")[-1].strip()[:-1])
            else:
                result["require"] = i[1:-1] 
        return result

class Database:
    def __init__(self):
        data_types = {
            'TT': str,
            'Môn học': str,
            'MSMH': str,
            'NH1': str,
            'NH2': str
        }
        self.database = pd.read_csv("Input/course.csv", dtype=data_types)

    def query(self, q):
        info = QueryProcessing.process(q)
        if info.get("type", "null") == "PRINT_ALL":
            result = 0
            hk = info.get("HK", "null")
            nh = info.get("NH", "null")
            hk_case = ["12"]
            if hk == "1":
                hk_case.append("10")
            elif hk == "2":
                hk_case.append("02")

            if nh != "null":
                condition = True
                for i in nh:
                    condition = (self.database["NH" + i].isin(hk_case)) & condition
                result += self.database.loc[condition].shape[0]
            return f"Số lượng môn học thỏa mãn truy vấn là {result}."
        elif info.get("type", "null") == "ITERATE":
            result = "Kết quả của câu truy vấn là:\n"
            attributes = []
            conditions = []
            for i in info.keys():
                if i != 'type' and i != 'require':
                    if info[i] is None or info[i] == []:
                        attributes.append(i)
                    else:
                        conditions.append(i)
            records = None
            if len(conditions) == 2:
                hk = info.get("HK", "null")
                nh = info.get("NH", "null")
                hk_case = ["12"]
                if hk == "1":
                    hk_case.append("10")
                elif hk == "2":
                    hk_case.append("02")
                condition = True
                for i in nh:
                    condition = (self.database["NH" + i].isin(hk_case)) & condition
                records = self.database.loc[condition]
                attributes = ["Môn học" if attribute == "MH" else attribute for attribute in attributes]
                for _, row in records.iterrows():
                    for attribute in attributes:
                        if attribute == "Môn học":
                            result += "{} - ".format(row["Môn học"])
                        else:
                            result += "{}\n".format(row["MSMH"])
                return result
            else:
                condition = conditions[0]
                if condition == "MH" or condition == "MSMH":
                    conditionAttr = "Môn học" if condition == "MH" else "MSMH"
                    records = self.database.loc[self.database[conditionAttr].str.lower().isin(info[condition])]
                    returnAttribute = []
                    for i in attributes:
                        if i == "NH":
                            returnAttribute.extend(["NH1", "NH2"])
                        elif i == "HK":
                            continue
                        elif i == "MH":
                            returnAttribute.append("Môn học")
                        else:
                            returnAttribute.append(i)
                    for _, row in records.iterrows():
                        attributeOutput = []
                        for attribute in returnAttribute:
                            if attribute == "Môn học":
                                attributeOutput.append("Môn học: {}".format(row["Môn học"]))
                            elif attribute == "MSMH":
                                attributeOutput.append("MSMH: {}".format(row["MSMH"]))
                            else:
                                attributeOutput.append("dạy vào {} trong năm học {}".format(convert(row[attribute]), attribute[-1]))                
                    return result + ", ".join(attributeOutput)
                else:
                    if condition[0] == 'NH':
                        if info['NH'] == '1 xor 2':
                            if info['require'] == 'SINGLE':
                                pass

        elif info.get("type", "null") == "YES-NO":
            records = self.database.loc[self.database["MSMH"].isin(info["MSMH"])]
            if len(info["MSMH"]) == 2:
                nh1_column = records.loc[:, "NH1"].tolist()
                nh2_column = records.loc[:, "NH2"].tolist()
                if '00' in nh1_column or '00' in nh2_column:
                    return "NO"
                else:
                    if '12' in nh1_column or '12' in nh2_column:
                        return "YES"
                    if nh1_column[0] != nh1_column[1] or nh2_column[0] != nh2_column[1]:
                        return "NO"
                    return "YES"
            else:
                if info['NH'][0] == '1 xor 2':
                    nh1_column = records.loc[:, "NH1"].tolist()
                    nh2_column = records.loc[:, "NH2"].tolist()
                    if '12' not in [nh1_column[0], nh2_column[0]]:
                        return "NO"
                    return "YES"
                













