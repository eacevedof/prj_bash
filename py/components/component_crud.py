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
        self.__argroupby = []
        self.__arnumeric = []
        self.__arlimit = []
        self.__sql = ""
        self.__querycomment = ""
        self.__isfoundrows = False
        self.__isdistinct = False


    def get_select_from(self):
        self.__sql = "-- get_selectfrom"
        if not self.__table or not self.__argetfields:
            return self.__sql
        querycomment = self.__querycomment if self.__querycomment else ""


