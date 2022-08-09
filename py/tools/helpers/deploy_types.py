class BEDEPLOYTYPE:
    NO_VENDOR = "no-vendor"
    NO_DB = "no-db"
    NO_CODE = "no-code"


class DEPLOYSTEP:
    GENERAL = "general"
    DB = "db"
    SOURCEBE = "sourcebe"
    SOURCEFRONT = "sourcefront"
    PICTURES = "pictures"


class DEPLOYMOMENT:
    PRE = "pre"
    POST = "post"


class DEPLOYOPTIONS:
    VENDOR_BY_COPY = "vendor-by-copy"
    DB_BY_MIGRATIONS = "db-by-migration"
