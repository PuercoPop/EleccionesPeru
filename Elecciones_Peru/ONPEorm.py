# -*- coding: utf-8 -*-
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

class ONPEorm():

    def __init__(self, db_type, db_name ):
        """
        Revisa si existe la base de datos,
        si la hay revisa si es consistente con el schema,
        si lo es
        """
        pass
    

    def write_acta():
        pass

