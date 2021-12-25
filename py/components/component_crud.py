from typing import Optional, Any, List
from __future__ import annotations

class ComponentCrud:

    def __init__(self):
        self.__table = ""
        self.__arinsertfv = []
        self.__arupdatefv = []
        self.__arpks = []
        self.__argetfields = []
        self.__arjoins = []
        self.__arands = []
        self.__arorderby = []
        self.__arhaving = []
        self.__groupby = []
        self.__arnumeric = [] #campos trtados como numeros para evitar '' en los insert/update
        self.__arlimit = []
        self.__sql = ""
        self.__querycomment = ""
        self.__isfoundrows = False
        self.__isdistinct = False


    def get_select_from(self)->str:
        self.__sql = "-- get_selectfrom"
        if not self.__table or not self.__argetfields:
            return self.__sql
        querycomment = self.__querycomment if self.__querycomment else ""
        self.__sql = f"{querycomment} SELECT "
        if self.__isfoundrows:
            self.__sql += f"SQL_CAL_FOUND_ROWS "

        if self.__isdistinct:
            self.__sql += f"DISTINCT "

        self.__sql += ", ".join(self.__argetfields)
        self.__sql += f"FROM {self.__table}"
        self.__sql += self.__get_joins()

        ands = []
        for d_pk in self.__arpks:
            field = d_pk.get("field",None)
            if not field:
                continue

            value = d_pk.get("value",None)
            if value == None:
                ands.append(f"{field} IS null")
            elif field in self.__arnumeric:
                ands.append(f"{field} = {value}")
            else:
                ands.append(f"{field} = '{value}'")

        ands += self.__arands
        self.__sql += " WHERE " + " AND ".join(ands) if ands else ""
        self.__sql += self.__get_groupby()
        self.__sql += self.__get_having()
        self.__sql += self.__get_orderby()
        self.__sql += self.__get_limit()
        
        return self.__sql


    def __get_joins(self)-> str:
        strjoins = " " + "\n".join(self.__arjoins) if self.__arjoins else ""
        return strjoins

    def __get_groupby(self)-> str:
        strgroupby = " GROUP BY " + ",".join(self.__argroupby) if self.__argroupby else ""
        return strgroupby

    def __get_having(self)-> str:
        strhaving = " HAVING " + ",".join(self.__arhaving) if self.__arhaving else ""
        return strhaving

    def __get_orderby(self)-> str:
        strorderby = " ORDER BY " + ",".join(self.__arorderby) if self.__arorderby else ""
        return strorderby

    def __get_limit(self)-> str:
        strlimit = " LIMIT " + ",".join(self.__arlimit) if self.__arlimit else ""
        """
        * si por ejemplo deseo paginar de 10 en 10
        * para la pag:
        *  1 sería LIMIT 0,10   -- 1 a 10
        *  2 LIMIT 10,10        -- 11 a 20
        *  3 LIMIT 20,10        -- 21 a 30
        """
        return strlimit

    def set_table(self, name:str) -> ComponentCrud:
        self.__table = name
        return self

    def set_comment(self, comment:str) -> ComponentCrud:
        self.__comment = comment
        return self

    def add_insert_fv(self, field:str, value:Any, dosanitize:bool=True) -> ComponentCrud:
        self.__arinsertfv.append({
            "field": field,
            "value": self.get_sanitized(value) if dosanitize else value
        })
        return self

    def add_update_fv(self, field:str, value:Any, dosanitize:bool=True) -> ComponentCrud:
        self.__arupdatefv.append({
            "field": field,
            "value": self.get_sanitized(value) if dosanitize else value
        })
        return self

    def set_getfields(self, arfields: List[str]) -> ComponentCrud:
        self.__argetfields = arfields
        return self

    def add_getfield(self, field:str) -> ComponentCrud:
        self.__argetfields.append(field)
        return self

    def set_joins(self, joins: List[str]) -> ComponentCrud:
        self.__arjoins = joins
        return self

    def set_orderby(self, orderbys: List[str]) -> ComponentCrud:
        self.__arorderby = orderbys
        return self

    def set_groupby(self, groupbys: List[str]) -> ComponentCrud:
        self.__argroupby = groupbys
        return self

    def set_having(self, havings: List[str]) -> ComponentCrud:
        self.__arhaving = havings
        return self



    def get_sanitized(self, value:str) -> Optional[str]:
        if value == None:
            return None
        return value.replace("'","\'")

    def is_distinct(self, ison:bool=True) -> ComponentCrud:
        self.__isdistinct = ison
        return self

    def is_foundrows(self, ison:bool=True) -> ComponentCrud:
        self.__isfoundrows = ison
        return self

    def add_numeric(self, fieldname:str) -> ComponentCrud:
        self.__arnumeric.append(fieldname)
        return self

    def add_numeric(self, fieldname:str) -> ComponentCrud:
        self.__arnumeric.append(fieldname)
        return self
