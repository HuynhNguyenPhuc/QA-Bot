class DependencyParser:
    def __init__(self, lexicons):
        self.lexicons = lexicons
        self.stack = ['root']
        self.complete = False

    def parse(self):
        dependencies = []
        while not self.complete:
            operation, dependency = self.transition()
            if operation == "complete":
                self.complete = True
                continue
            elif operation == "shift":
                lexicon = self.lexicons.pop(0)
                self.stack.append(lexicon)
            elif operation == "reduce":
                self.stack.pop()
            elif operation == "left_arc":
                dependencies.append((dependency, (self.lexicons[0], self.stack[-1])))
                self.stack.pop()
            elif operation == "right_arc":
                dependencies.append((dependency, (self.stack[-1], self.lexicons[0])))
                lexicon = self.lexicons.pop(0)
                self.stack.append(lexicon)
                

        return dependencies
            

    def transition(self):
        if not self.lexicons:
            return "complete", None
        
        if self.lexicons[0] == "?":
            if self.stack[-1] == 'root':
                return "shift", None
            elif self.stack[-1] != "dạy":
                return "reduce", None
            else: 
                return "right_arc","query"

        if self.stack[-1] == "root":
            if self.lexicons[0] == "dạy":
                return "right_arc", "root"
            else: 
                return "shift", None
        
        if self.stack[-1] == "bao nhiêu":
            if self.lexicons[0] == "môn học":
                return "left_arc","wh_count"
            else: return "shift", None

        if self.stack[-1] == "môn học":
            if self.lexicons[0] == "dạy":
                return "left_arc", "dobj"
            elif self.lexicons[0] in ["mã số", "mã"]:
                return "right_arc", "id_mod"
            elif self.lexicons[0] == "quản lý dữ liệu doanh nghiệp":
                return "right_arc", "name_mod"
            else: return "shift", None
        
        if self.stack[-1] == "dạy":
            if self.lexicons[0] == "học kỳ":
                return "right_arc","hk_time"
            else: return "shift", "query"

        if self.stack[-1] == "học kỳ":
            if self.lexicons[0] in ["1", "2"]:
                return "right_arc", "num_hk"
            elif self.lexicons[0] == "năm học":
                return "right_arc","nh_mod"
            else: return "shift", None

        if self.stack[-1] == "năm học":
            if self.lexicons[0] in ["1", "2"]:
                return "right_arc","num_nh"
            else: 
                return "shift", None

        if self.stack[-1] == "cho biết":
            if self.lexicons[0] in ["tên môn học", "môn học"]:
                return "left_arc","give_each"
            else: 
                return "shift", None
        
        if self.stack[-1] in ["mã số", "mã"]:
            if self.lexicons[0] == "môn học" and self.lexicons[1] != "mã số":
                return "left_arc","id_mod"
            if self.lexicons[0].isdigit() and len(self.lexicons[0])>1:
                return "right_arc","num_id"

        if self.stack[-1] in ["1", "2", "một", "hai"]:
            if self.lexicons[0] == "học kỳ":
                return "left_arc","num_det"
            if self.lexicons[0] == "năm học":
                return "left_arc", "num_nh_det"
            
        if self.stack[-1] == "không":
            if self.lexicons[0] == "dạy":
                return "left_arc", "neg"
             
        if self.stack[-1] == "tên":
            if self.lexicons[0] == "môn học":
                return "left_arc", "name_mod"
            elif self.lexicons[0] == "mã số":
                return "shift", None

        return "reduce", None
