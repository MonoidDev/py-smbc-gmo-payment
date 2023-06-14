import os
import sys
sys.path.append("..")
from smbc_gp_client.smbc_gp_client import SmbcGpClient
import requests
# from smbc_gp_client.smbc_gp_client import SmbcGpClient

SHOP_ID = os.environ['SMBC_SHOP_ID']
SHOP_PASS = os.environ['SMBC_SHOP_PASS']

client = SmbcGpClient("https://pt01.smbc-gp.co.jp/payment")
r = client.create_transaction(
    shopId=SHOP_ID, shopPass=SHOP_PASS, orderId="order003", 
    jobCd="AUTH", itemCode="0000990", 
    amount=10, tax=1, tdFlag=0, 
    tdTenantName="123", tds2Type=1, tdRequired=0
    )
print(r)
