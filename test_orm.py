# -*- coding: utf-8 -*-
import db_definition_orm
from ParserCongreso import parse_acta_congreso

if __name__ == "__main__":
    with open('test_cases/Ejemplo_Acta_Congreso_2.html','r') as f_acta:
        data = parse_acta_congreso( f_acta)
        for item,key in zip(data.values(),data.keys()):
            print u"" + item +" : " + key

