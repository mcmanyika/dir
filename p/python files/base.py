__author__ = 'Manyika'

from django.db import connection, connections
import sys, traceback, re
from datetime import datetime, date
import hashlib
import string


class Base:
    def __init__(self):
        self.dictionary = dict()

        try:
            csr = connection.cursor()
            csr.execute('select dict_key, dict_val from t_dictionary')
            rwd = csr.fetchall()
            if rwd:
                for d in rwd: self.dictionary[d[0]] = d[-1]
        except:
            print sys.exc_info()

        self.dictionary['idefault_option'] = 0

    def get_rows(self, sql='', prms=tuple()):
        rws = list()
        if not sql: return rws

        try:
            csr = connection.cursor()

            if prms: csr.execute(sql, prms)
            else: csr.execute(sql)

            rws = csr.fetchall()
        except:
            print sys.exc_info()

        return rws 

    def get_rows_and_columns(self, sql='', prms=tuple()):
        data_set = list()

        if not sql:
            return data_set

        try:
            csr = connection.cursor()

            if prms:
                csr.execute(sql, prms)
            else:
                csr.execute(sql)

            rws = csr.fetchall()

            data_set.append([col[0] for col in csr.description])
            data_set.append(rws if rws else list())
        except:
            print sys.exc_info()

        return data_set

    def get_one_row(self, sql='', prms=tuple()):
        found = None
        if not sql: return found

        try:
            csr = connection.cursor()

            if prms: csr.execute(sql, prms)
            else: csr.execute(sql)

            found = csr.fetchone()
        except:
            print sys.exc_info()

        return found

    def get_one_row_and_columns(self, sql='', prms=tuple()):
        data_set = list()

        if not sql:
            return data_set

        try:
            csr = connection.cursor()

            if prms:
                csr.execute(sql, prms)
            else:
                csr.execute(sql)

            row = csr.fetchone()

            data_set.append([col[0] for col in csr.description])
            data_set.append(row if row else list())
        except:
            print sys.exc_info()

        return data_set

    def get_one_dict_row(self, sql='', prms=tuple()):
        row = None
        if not sql: return row

        try:
            csr = connection.cursor()

            if prms:
                csr.execute(sql, prms)
            else:
                csr.execute(sql)

            desc = csr.description
            xrow = csr.fetchone()

            if xrow:
                rw = dict(zip([col[0] for col in desc], xrow,))
                #rws = [dict(zip([col[0] for col in desc], rw)) for rw in csr.fetchall()]
                if rw: row = rw
        except:
            print sys.exc_info()

    def dictfetchall(self, sql='', prms=tuple()):
        rws = {}
        if not sql: return rws

        try:
            csr = connection.cursor()

            if prms: csr.execute(sql, prms)
            else: csr.execute(sql)

            desc = csr.description
            rws = [dict(zip([col[0] for col in desc], rw)) for rw in csr.fetchall()]
        except:
            print prms
            print sys.exc_info()

        return rws

    def get_dictionary_rows(self, sql='', prms=tuple()):
        rws = None
        if not sql: return rws

        try:
            csr = connection.cursor()

            if prms: csr.execute(sql, prms)
            else: csr.execute(sql)

            desc = csr.description
            rws = [dict(zip([col[0] for col in desc], rw)) for rw in csr.fetchall()]
        except:
            print sys.exc_info()

        return rws

    def clean_string(self, sval=''):
        txt = ''
        if sval:
            sitems = list()
            for x in sval:
                if x in string.printable[:-5]:
                    sitems.append(x)
            txt = ''.join(sitems)
        return txt

    def format_item(self, vl=None, dtfmt=''):
        v = vl
        if vl:
            if type(vl) == type(datetime.now()):
                v = vl.strftime(dtfmt) if dtfmt else vl.strftime('%d/%m/%Y')
            elif type(vl) == type(date.today()):
                v = vl.strftime(dtfmt) if dtfmt else vl.strftime('%d/%m/%Y')
            elif type(vl) == type(datetime.time(datetime.now())):
                v = vl.strftime(dtfmt) if dtfmt else vl.strftime('%H:%M:%f')
        else:
            if type(vl) == type(True): pass
            else: v = ''

        return v