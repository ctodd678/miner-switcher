import subprocess
import configparser
import os, time, subprocess, shlex
import requests, json, urllib
import errno, signal


#*SET HASHRATE VALUES HERE
ETHHASH = 136
XMRHASH = 48
PRICEURL = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,XMR&tsyms=BTC,USD,CAD&api_key="




def get_profitabilities():
   eth_url = "https://www.cryptocompare.com/mining/calculator/eth?HashingPower="
   eth_url = eth_url + ETHHASH
   eth_url = eth_url + "&HashingUnit=MH%2Fs&PowerConsumption=140&CostPerkWh=0.00&MiningPoolFee=1"

   rvn_url = "https://www.cryptocompare.com/mining/calculator/xmr?HashingPower="
   rvn_url = rvn_url + XMRHASH
   rvn_url = rvn_url + "&HashingUnit=KH%2Fs&PowerConsumption=0&CostPerkWh=0.00&MiningPoolFee=1"

   eth_profitability = 0
   rvn_profitability = 0



def getMostProfitableCoin():
    uri = get_uri()
    print("[AutoSwitch] "+"URL:",uri)
    #get_coin_algo_list(data)
    #data = json.load(urllib.request.urlopen(uri))
    r = requests.get(uri)
    data = r.json()
    #print("[AutoSwitch] "+data['coins'])
    performers = get_performance(data['coins'])
    return performers


def main():
    print("Welcome to MINER-SWITCHER")

    eth_running = 0
    xmr_running = 0
    eth_profitable = 0
    xmr_profitable = 0


    price_request = requests.get(PRICEURL)
    price_data = price_request.json()
    eth_json = price_data['ETH']
    xmr_json = price_data['XMR']

    #print(price_data) PRICE DATA JSON

    try:
        while True:

            print("\nPress Ctrl + C to end auto miner script.")
            print("\033[0;32m")
            print("\n[ETHEREUM PRICES]")
            print("BTC: " , eth_json['BTC'])
            print("USD: " , eth_json['USD'])
            print("CAD: " , eth_json['CAD'])

            print("\n[MONERO PRICES]")
            print("BTC: " , xmr_json['BTC'])
            print("USD: " , xmr_json['USD'])
            print("CAD: " , xmr_json['CAD'])
            print("\033[0;0m")

            if(eth_profitable == 1 && eth_running == 0):
                closeRunningMiner()
                subprocess.call([r'C:\\Users\\ctodd\Desktop\\PhoenixMiner_5.4c_Windows\start_miner.bat']) #NOTE: THIS PATH WILL NEED TO BE CHANGED DEPENDING ON WHERE YOUR MINER START BATCH IS
            elif(xmr_profitable == 1 && xmr_running == 0):
                closeRunningMiner()
                subprocess.call([r'C:\\Users\\ctodd\Desktop\\TRM\start_xmr.bat']) #NOTE: THIS PATH WILL NEED TO BE CHANGED DEPENDING ON WHERE YOUR MINER START BATCH IS
            elif(miner_running == 0): #start eth mining if nothing else is running
                subprocess.call([r'C:\\Users\\ctodd\Desktop\\PhoenixMiner_5.4c_Windows\start_miner.bat']) #NOTE: THIS PATH WILL NEED TO BE CHANGED DEPENDING ON WHERE YOUR MINER START BATCH IS

            time.sleep(30) #*POLLING TIME
    
    except KeyboardInterrupt:
        print("Ending program...")
        pass

    

if __name__ == "__main__":
    main()