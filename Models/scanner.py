from functools import reduce

class Scanner:
    @staticmethod
    def merge(first_token, second_token):
        if first_token == "cho" and second_token == "biết":
            return "cho biết"
        elif first_token == "bao" and second_token == "nhiêu":
            return "bao nhiêu"
        elif first_token == "môn" and second_token == "học":
            return "môn học"
        elif first_token == "học" and second_token == "kỳ":
            return "học kỳ"
        elif first_token == "năm" and second_token == "học":
            return "năm học"
        elif first_token == "mã" and second_token == "số":
            return "mã số"
        elif first_token == "tên" and second_token == "môn":
            return "tên môn"
        elif first_token == "tên môn" and second_token == "học":
            return "tên môn học"
        elif first_token != "" and first_token[0] == '"' and first_token[-1] != '"':
            return first_token + " " + second_token
        else:
            return second_token

    @staticmethod
    def get_lexicons(text):
        stopwords = [",", ":", "Có", "có", "được", "trong", "vào", \
                "thứ", "và", "cả", "nào"]
       
        for i in stopwords:
            text = text.replace(i, "")
        text = text.lower()
        text = text.strip()
        tokens = text.split(" ")
        tokens = [token for token in tokens if token != '']
        lexicons = reduce(lambda listTokens, token: listTokens + [Scanner.merge(listTokens[-1], token)] \
                            if not " " in Scanner.merge(listTokens[-1], token) \
                            else listTokens[:-1] + [Scanner.merge(listTokens[-1], token)], tokens, [''])
        lexicons.remove("")
        lexicons = list(map(lambda lexicon: lexicon[1:-1] if lexicon[0] == '"' and lexicon[-1] == '"' else lexicon, lexicons))
        return lexicons