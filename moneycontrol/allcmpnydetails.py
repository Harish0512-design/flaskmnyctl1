from . import namelink as nl
from . import stockoverviewpeers as sop

def all_cmpny_details_1():
    cmpnies = nl.cmpny_name_link()
    overview_details = []
    for key in cmpnies.keys():
        lnk = cmpnies[key]
        stock_overview = sop.stock_overview_part_1(lnk)
        overview_details.append(stock_overview)
    return overview_details

def all_cmpny_details_2():
    cmpnies = nl.cmpny_name_link()
    overview_details = []
    for key in cmpnies.keys():
        lnk = cmpnies[key]
        stock_overview = sop.stock_overview_part_2(lnk)
        overview_details.append(stock_overview)
    return overview_details

def all_cmpny_details_3():
    cmpnies = nl.cmpny_name_link()
    overview_details = []
    for key in cmpnies.keys():
        lnk = cmpnies[key]
        stock_overview = sop.stock_overview_part_3(lnk)
        overview_details.append(stock_overview)
    return overview_details


