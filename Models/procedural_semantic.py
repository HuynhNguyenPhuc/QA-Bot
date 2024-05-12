class ProceduralSemantic():
    @staticmethod   
    def process(logical_form):
        logical_form = logical_form.strip()
        temp = logical_form.split("(&")[-1]
        temp = temp.strip()
        if logical_form.startswith("(EACH"):
            return f"ITERATE ?m1 (CHECK_ALL_TRUE {temp}"
        elif logical_form.startswith("(WH_count"):  
            return f"PRINT_ALL ?m1 (CHECK_ALL_TRUE {temp}"
        elif logical_form.startswith("(YES-NO"):
            return f"YES-NO (CHECK_ALL_TRUE {temp}"
        else:
            return ""
