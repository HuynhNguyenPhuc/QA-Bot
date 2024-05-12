class GrammaticalRelation:
    def __init__(self, dependencies):
        self.dependencies = dependencies

    def process(self):
        results = []
        mh_index = 0
        msmh_index = 0
        msmh_det_index = 0
        for dependency in self.dependencies:
            if dependency[0] == 'root' or dependency[0] == 'query':
                continue
            elif dependency[0] == 'wh_count':
                results.append("WH_count MH ?m1")
            elif dependency[0] == 'give_each':
                results.append("EACH ?m1")
            elif dependency[0] == 'dobj':
                mh_index += 1
                results.append(f"MH ?m{mh_index}")
            elif dependency[0] == 'nh_mod':
                results.append("NH ?nh")
            elif dependency[0] == 'num_nh':
                results.append(f"NH nh = {dependency[1][1]}")
            elif dependency[0] == 'hk_time':
                results.append("HK ?hk")
            elif dependency[0] == 'num_det':
                results.append(f"HK num = 12")
            elif dependency[0] == 'num_nh_det':
                if dependency[1][1] in ["1", "một"]:
                    results.append("NH nh = 1 xor 2")
                else:
                    results.append("NH nh = 12")
            elif dependency[0] == 'num_hk':
                results.append(f"HK hk = {dependency[1][1]}")
            elif dependency[0] == 'num_hk_det':
                results.append("HK hk = 12")
            elif dependency[0] == 'id_mod':
                msmh_index += 1
                results.append(f"MSMH ?ms{msmh_index}")
            elif dependency[0] == 'name_mod':
                results.append("MH ?m1")
            elif dependency[0] == 'num_id':
                msmh_det_index += 1
                results.append(f"MSMH ms{msmh_det_index} = {dependency[1][1]}")
            elif dependency[0] == 'course_name':
                results.append(f"MH m1 = {dependency[1][1]}")
            elif dependency[0] == 'neg':
                results.append('NEGATIVE')
            elif dependency[0] == 'single':
                results.append('SINGLE')
            elif dependency[0] == 'yes-no':
                results.append("YES-NO")
        return results

