# Lista de nombres de las columnas
columns = [
    "ADDRCOMM", "AUGRP", "BIRTHDT", "BIRTHDT_STATUS", "BIRTHPL", "BPEXT", "BPKIND",
    "BP_EEW_DUMMY", "BP_SORT", "BU_GROUP", "BU_LANGU", "BU_LOGSYS", "BU_SORT1",
    "BU_SORT2", "CHDAT", "CHILDREN", "CHTIM", "CHUSR", "CLIENT", "CNDSC", "CNTAX",
    "CONTACT", "CRDAT", "CRTIM", "CRUSR", "DB_KEY", "DEATHDT", "EMPLO", "FOUND_DAT",
    "GENDER", "IND_SECTOR", "INITIALS", "IS_ORG_CENTRE", "JOBGR", "KBANKL", "KBANKS",
    "LANGU_CORR", "LEGAL_ENTY", "LEGAL_ORG", "LIQUID_DAT", "LOCATION_1", "LOCATION_2",
    "LOCATION_3", "MARST", "MC_NAME1", "MC_NAME2", "MEM_HOUSE", "MILVE", "NAMCOUNTRY",
    "NAME1_TEXT", "NAMEFORMAT", "NAMEMIDDLE", "NAME_FIRST", "NAME_GRP1", "NAME_GRP2",
    "NAME_LAST", "NAME_LAST2", "NAME_LST2", "NAME_ORG1", "NAME_ORG2", "NAME_ORG3",
    "NAME_ORG4", "NATIO", "NATPERS", "NICKNAME", "NOT_LG_COMPETENT", "NOT_RELEASED",
    "NUC_SEC", "PARTGRPTYP", "PARTNER", "PARTNER_GUID", "PAR_REL", "PERNO", "PERSNUMBER",
    "PREFIX1", "PREFIX2", "PRINT_MODE", "RATE", "SOURCE", "TD_SWITCH", "TITLE",
    "TITLE_ACA1", "TITLE_ACA2", "TITLE_LET", "TITLE_ROYL", "TYPE", "VALID_FROM",
    "VALID_TO", "XBLCK", "XDELE", "XPCPT", "XSEXF", "XSEXM", "XSEXU", "XUBNAME"
]

# Generar las líneas de SQL
sql_lines = []
for column in columns:
    line = f'CASE WHEN COUNT(CASE WHEN "{column}" IS NOT NULL THEN 1 END) > 0 THEN \'{column}\' ELSE NULL END AS {column}'
    sql_lines.append(line)
   
# Unir las líneas en una sola cadena separadas por comas y saltos de línea
sql_query = ',\n  '.join(sql_lines)

# Añadir la cláusula FROM al final
sql_query = f"{sql_query}\nFROM\n  \"TABLE\";"

# Imprimir el resultado
print(sql_query)
