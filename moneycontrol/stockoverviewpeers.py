import requests
from bs4 import BeautifulSoup
import csv

def stock_overview_part_1(cmpny_url):
    url = cmpny_url
    response = requests.get(url)
    mycontent = response.content
    soup = BeautifulSoup(mycontent,"html.parser")
    stock_info_lst = {}
    stock = soup.find("div",class_="inid_name")

    stock_name = stock.find("h1").text.strip()
    sector = stock.find("a").text.strip()
    current_price = soup.find("div",class_="pcstkspr nsestkcp bsestkcp futstkcp optstkcp").text.strip()
    open_ = soup.find("td",class_="nseopn bseopn").text.strip()
    prev_close = soup.find("td",class_="nseprvclose bseprvclose").text.strip()
    uc_limit = soup.find("td",class_="nseupper_circuit_limit bseupper_circuit_limit").text.strip()
    lc_limit = soup.find("td",class_="nselower_circuit_limit bselower_circuit_limit").text.strip()
    volume = soup.find("td",class_="nsevol bsevol").text.strip()
    
    
    stock_info_lst["stock_name"] = stock_name
    stock_info_lst["sector"] = sector
    stock_info_lst["current_price"] = current_price
    stock_info_lst["open_"] = open_
    stock_info_lst["prev_close"]=prev_close
    stock_info_lst["uc_limit"]= uc_limit
    stock_info_lst["lc_limit"]=lc_limit
    stock_info_lst["volume"]=volume
    
    return stock_info_lst


def stock_overview_part_2(cmpny_url):
    url = cmpny_url
    response = requests.get(url)
    mycontent = response.content
    soup = BeautifulSoup(mycontent,"html.parser")
    stock_info_lst = {}
    stock = soup.find("div",class_="inid_name")

    stock_name = stock.find("h1").text.strip()
    sector = stock.find("a").text.strip()    
    vwap = soup.find("td",class_="nsevwap bsevwap").text.strip()
   
    market_capt = soup.find("td",class_="nsemktcap bsemktcap").text.strip()
    face_val = soup.find("td",class_="nsefv bsefv").text.strip()
    ttm_eps = soup.find("td",class_="nseceps bseceps").text.strip()
    ttm_pe = soup.find("td",class_="nsepe bsepe").text.strip()
    sector_pe = soup.find("td",class_="nsesc_ttm bsesc_ttm").text.strip()

    stock_info_lst["stock_name"] = stock_name
    stock_info_lst["sector"] = sector
    stock_info_lst["vwap"]=vwap
    stock_info_lst["market_capt"]=market_capt
    stock_info_lst["face_val"]=face_val
    stock_info_lst["ttm_eps"]=ttm_eps
    stock_info_lst["ttm_pe"]=ttm_pe
    stock_info_lst["sector_pe"]=sector_pe
    
    return stock_info_lst


def stock_overview_part_3(cmpny_url):
    url = cmpny_url
    response = requests.get(url)
    mycontent = response.content
    soup = BeautifulSoup(mycontent,"html.parser")
    stock_info_lst = {}
    stock = soup.find("div",class_="inid_name")

    stock_name = stock.find("h1").text.strip()
    sector = stock.find("a").text.strip()    
    book_value_pershare = soup.find("td",class_="nsebv bsebv").text.strip()
    p_to_b = soup.find("td",class_="nsepb bsepb").text.strip()
    dividend_yield = soup.find("td",class_="nsedy bsedy").text.strip()
    p_to_c = soup.find("td",class_="nsep_c bsep_c").text.strip()

    stock_info_lst["stock_name"] = stock_name
    stock_info_lst["sector"] = sector
    stock_info_lst["book_value_pershare"]=book_value_pershare
    stock_info_lst['p/b'] = p_to_b
    stock_info_lst['dividend_yeild'] = dividend_yield
    stock_info_lst['p_to_c'] = p_to_c


    return stock_info_lst

# print(stock_overview_part_1('http://www.moneycontrol.com/india/stockpricequote/autolcvshcvs/tatamotors/TM03'))