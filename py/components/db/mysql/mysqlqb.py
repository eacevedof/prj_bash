# el future permite hacer typehinting de la clase -> MysqlQB
from __future__ import annotations
from typing import Optional, Any, List


class MysqlQB:

    def __init__(self, table: str = ""):
        self.__comment = ""
        self.__table = table

        self.__argetfields = []
        self.__arnumeric = []  # campos tratados como numeros para evitar '' en los insert/update

        self.__arjoins = []
        self.__arands = []
        self.__arorderby = []
        self.__arhaving = []
        self.__argroupby = []
        self.__arlimit = []

        self.__arinsertfv = []
        self.__arupdatefv = []

        self.__isfoundrows = False
        self.__isdistinct = False

        self.__sql = ""

    def get_select(self) -> str:
        self.__sql = ""
        sql = "-- get_selectfrom"
        if not self.__table or not self.__argetfields:
            return sql

        comment = f"/*{self.__comment}*/" if self.__comment else ""
        sql = f"{comment} SELECT "
        if self.__isfoundrows:
            sql += f"SQL_CAL_FOUND_ROWS "

        if self.__isdistinct:
            sql += f"DISTINCT "

        sql += ", ".join(self.__argetfields)
        sql += f" FROM {self.__table} "
        sql += self.__get_joins()
        sql += " WHERE 1 "
        ands = self.__arands
        if ands:
            sql += "AND " + " AND ".join(ands) + " "
        sql += self.__get_groupby()
        sql += self.__get_having()
        sql += self.__get_orderby()
        sql += self.__get_limit()

        self.__sql = sql.strip()
        return self.__sql

    def get_insert(self) -> str:
        self.__sql = ""
        sql = "-- get_insert"
        if not self.__table:
            return sql

        comment = f"/*{self.__comment}*/" if self.__comment else ""
        sql = f"{comment} INSERT INTO {self.__table} "
        if not self.__arinsertfv:
            return sql

        fields = [item.get("field", "") for item in self.__arinsertfv]
        fields = ", ".join(fields)
        sql += f"({fields}) "
        values = [item.get("value") for item in self.__arinsertfv]
        aux = []
        for value in values:
            if value is None:
                aux.append("null")
            elif value in self.__arnumeric:
                aux.append(value)
            else:
                aux.append(f"'{value}'")
        sql += "VALUES (" + " ,".join(aux) + ")"
        self.__sql = sql
        return self.__sql

    def get_delete(self) -> str:
        self.__sql = ""
        sql = "-- get_delete"
        if not self.__table or not self.__arands:
            return sql

        comment = f"/*{self.__comment}*/" if self.__comment else ""
        sql = f"{comment} DELETE FROM {self.__table} "

        sql += "WHERE "
        ands = self.__arands
        if ands:
            sql += " AND ".join(ands)

        self.__sql = sql.strip()
        return self.__sql

    def get_update(self) -> str:
        self.__sql = ""
        sql = "-- get_update"
        if not self.__table or not self.__arands:
            return sql

        comment = f"/*{self.__comment}*/" if self.__comment else ""
        sql = f"{comment} UPDATE {self.__table} SET "
        if not self.__arupdatefv:
            return sql

        aux = []
        for dc in self.__arupdatefv:
            field = dc.get("field", "")
            if not field:
                continue
            value = dc.get("value")
            if value is None:
                aux.append(f"{field}=null")
            elif value in self.__arnumeric:
                aux.append(f"{field}={value}")
            else:
                aux.append(f"{field}='{value}'")

        sql += ", ".join(aux) + " "

        sql += "WHERE "
        ands = self.__arands
        if ands:
            sql += " AND ".join(ands)

        self.__sql = sql.strip()
        return self.__sql

    def get_truncate(self) -> str:
        self.__sql = ""
        sql = "-- truncate"
        if not self.__table:
            return sql

        comment = f"/*{self.__comment}*/" if self.__comment else ""
        sql = f"{comment} TRUNCATE TABLE {self.__table}"
        self.__sql = sql
        return self.__sql

    def __get_joins(self) -> str:
        tmp = MysqlQB.__get_unique(self.__arjoins)
        strjoins = " " + "\n".join(tmp) if tmp else ""
        return strjoins

    def __get_groupby(self) -> str:
        tmp = MysqlQB.__get_unique(self.__argroupby)
        strgroupby = " GROUP BY " + ", ".join(tmp) if tmp else ""
        return strgroupby

    def __get_having(self) -> str:
        tmp = MysqlQB.__get_unique(self.__arhaving)
        strhaving = " HAVING " + ", ".join(tmp) if tmp else ""
        return strhaving

    def __get_orderby(self) -> str:
        tmp = MysqlQB.__get_unique(self.__arorderby)
        strorderby = " ORDER BY " + ", ".join(tmp) if tmp else ""
        return strorderby

    def __get_limit(self) -> str:
        strlimit = " LIMIT " + ",".join(self.__arlimit) if self.__arlimit else ""
        """
        * si por ejemplo deseo paginar de 10 en 10
        * para la pag:
        *  1 sería LIMIT 0,10   -- 1 a 10
        *  2 LIMIT 10,10        -- 11 a 20
        *  3 LIMIT 20,10        -- 21 a 30
        """
        return strlimit

    def set_table(self, name: str) -> MysqlQB:
        self.__table = name
        return self

    def set_comment(self, comment: str) -> MysqlQB:
        self.__comment = comment
        return self

    def add_insert_fv(self, field: str, value: Any, dosanitize: bool = True) -> MysqlQB:
        self.__arinsertfv.append({
            "field": field,
            "value": self.get_sanitized(value) if dosanitize else value
        })
        return self

    def add_update_fv(self, field: str, value: Any, dosanitize: bool = True) -> MysqlQB:
        self.__arupdatefv.append({
            "field": field,
            "value": self.get_sanitized(value) if dosanitize else value
        })
        return self

    def set_getfields(self, fields: List[str]) -> MysqlQB:
        self.__argetfields = fields
        return self

    def add_getfield(self, field: str) -> MysqlQB:
        self.__argetfields.append(field)
        return self

    def set_joins(self, joins: List[str]) -> MysqlQB:
        self.__arjoins = joins
        return self

    def set_orderby(self, orderbys: List[str]) -> MysqlQB:
        self.__arorderby = orderbys
        return self

    def set_groupby(self, groupbys: List[str]) -> MysqlQB:
        self.__argroupby = groupbys
        return self

    def set_having(self, havings: List[str]) -> MysqlQB:
        self.__arhaving = havings
        return self

    def set_limit(self, ippage: int = 1000, iregfrom: int = 0) -> MysqlQB:
        self.__arlimit = []
        self.__arlimit.append(str(iregfrom))
        self.__arlimit.append(str(ippage))
        if ippage is None:
            self.__arlimit = []
        return self

    @staticmethod
    def get_sanitized(value: str) -> Optional[str]:
        if value is None:
            return None
        if isinstance(value, str):
            return value.replace("'", "\\'")
        return value

    @staticmethod
    def __get_unique(array: List) -> List:
        return list(set(array))

    def is_distinct(self, ison: bool = True) -> MysqlQB:
        self.__isdistinct = ison
        return self

    def is_foundrows(self, ison: bool = True) -> MysqlQB:
        self.__isfoundrows = ison
        return self

    def add_numeric(self, fieldname: str) -> MysqlQB:
        self.__arnumeric.append(fieldname)
        return self

    def add_and(self, strand: str) -> MysqlQB:
        self.__arands.append(strand)
        return self

    def add_and_in(self, field: str, values: List, isnum: bool = True) -> MysqlQB:
        values = list(set(values))
        strin = ",".join(values) if isnum else "','".join(values)
        strin = f"({strin})" if isnum else f"('{strin}')"
        self.__arands.append(f"{field} IN {strin}")
        return self

    def add_join(self, strjoin: str) -> MysqlQB:
        # to-do key argument
        self.__arjoins.append(strjoin)
        return self

    def add_orderby(self, field: str, sorder: str = "ASC") -> MysqlQB:
        self.__arorderby.append(f"{field} {sorder}")
        return self

    def add_groupby(self, field: str) -> MysqlQB:
        self.__argroupby.append(field)
        return self

    def add_having(self, field: str) -> MysqlQB:
        self.__arhaving.append(field)
        return self
