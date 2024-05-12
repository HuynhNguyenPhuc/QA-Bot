class LogicalForm:
    def __init__(self, grammatical_relation):
        self.grammatical_relation = grammatical_relation

    def process(self):
        output = ""
        if "WH_count MH ?m1" in self.grammatical_relation:
            output += "(WH_count MH ?m1)"
        elif "EACH ?m1" in self.grammatical_relation:
            output += "(EACH ?m1)"
        elif "YES-NO" in self.grammatical_relation:
            output += "(YES-NO)"
        else:
            output += "(YES-NO)"
        output += ("(& ")
        if "NEGATIVE" in self.grammatical_relation:
            output += "(NEGATIVE)"
        if "SINGLE" in self.grammatical_relation:
            output += "(SINGLE)"
        mh_relation = list(filter(lambda x: x.startswith("MH"), self.grammatical_relation))
        mh_name = list(filter(lambda x: "=" in x, mh_relation))
        if mh_name:
            for name in mh_name:
                output += "(" + name + ")"
        else:
            for relation in set(mh_relation):
                output += "(" + relation + ")"
        msmh_relation = list(filter(lambda x: x.startswith("MSMH"), self.grammatical_relation))
        msmh_num = list(filter(lambda x: "=" in x, msmh_relation))
        if msmh_num:
            for num in msmh_num:
                output += "(" + num + ")"
        else:
            for relation in msmh_relation:
                output += "(" + relation + ")"

        hk_relation = list(filter(lambda x: x.startswith("HK"), self.grammatical_relation))
        hk_num = list(filter(lambda x: "=" in x, hk_relation))
        if hk_num:
            if len(hk_num) == 2:
                output += "(HK = 12)"
            else:
                for num in hk_num:
                    output += "(HK =" + num.split("=")[-1] + ")"
        else:
            for relation in hk_relation:
                output += "(" + relation + ")"

        nh_relation = list(filter(lambda x: x.startswith("NH"), self.grammatical_relation))
        nh_num = list(filter(lambda x: "=" in x, nh_relation))
        if nh_num:
            for num in nh_num:
                output += "(NH =" + num.split("=")[1] + ")"
        else:
            for relation in nh_relation:
                output += "(" + relation + ")"
        
        output += ")"
        if output.startswith("(EACH"):
            start = output.split("(&")[0]
            temp = output.split("(&")[-1].strip()
            if not temp.startswith("(MH"):
                output = start + "(& (MH ?m1)" + temp
        return output