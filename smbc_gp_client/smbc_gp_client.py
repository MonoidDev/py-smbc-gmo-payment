import requests
from enum import Enum

def serialize_response(response):
    data = dict()
    params = response.text.split("&")
    for param in params:
        (key, value) = param.split("=")
        data[key] = value
    return data

ENTRY_TRAN_PATH = '/EntryTran.idPass'
EXEC_TRAN_PATH = '/ExecTran.idPass'
SECURE_TRAN_PATH = '/SecureTran.idPass'
SECURE_TRAN2_PATH = '/SecureTran2.idPass'
ALTER_TRAN_PATH = '/AlterTran.idPass'
CHANGE_TRAN_PATH = '/ChangeTran.idPass'
SEARCH_TRADE_PATH = '/SearchTrade.idPass'

class SmbcGpClient():

    base_url = "https://pt01.smbc-gp.co.jp/payment"

    def __init__(self):
        print("init smbc-gp client success")
    
    def __init__(self, base_url):
        self.base_url = base_url
        print("init smbc-gp client success")

    """
    0. 创建交易

    1. 执行交易 - 不使用会员 ID (卡号/token/google token/3ds1.0/3ds2.0)
    3. 执行交易 - 使用 会员 ID (卡号/token/google token/3ds1.0/3ds2.0)
    4. 执行交易 - 3DS 1.0 认证后执行
    5. 执行交易 - 3DS 2.0 认证后执行

    7. 交易变更
    8. 金额变更

    9. 交易状态查询
    """

    def create_transaction(self, shopId, shopPass, orderId, jobCd, amount, tax, 
            itemCode='0000990', tdFlag=0, tdTenantName='', tds2Type=1, tdRequired=0):
        """
        To create a transation. Similar to login.

        Args:
            - shopId: shopId is issued by smbc-gp, beginning with tshop*.
            - shopPass: shopPass is issued by smbc-gp, should be 8 char.
            - orderId: orderId is used to identify a transaction.
            - jobCd: processing category. Available values are CHECK(validity check)/CAPTURE(immediate sales)/AUTH(temparary sales)/SAUTH(simple authorization)
            - itemCode: product code, default '0000990'
            - amount: transaction amount
            - tax: transaction tax
            - tdFlag: whether to use 3DS
            - tdTenantName: show the shop name with base64 encoded
            - tds2Type: determine what to do next if 3DS2.0 is not supported
            - tdRequired: whether to use 3DS when executing transaction

        Returns:
            - AccessId
            - AccessPass
            - ErrCode
            - ErrInfo
        """
        url = self.base_url + ENTRY_TRAN_PATH
        data = {
            'ShopID': shopId, 
            'ShopPass': shopPass, 
            'OrderID': orderId, 
            'JobCd': jobCd,
            'ItemCode': itemCode,
            'Amount': amount,
            'Tax': tax,
            'TdFlag': tdFlag,
            'TdTenantName': tdTenantName,
            'Tds2Type': tds2Type,
            'TdRequired': tdRequired
        }
        return serialize_response(requests.post(url, data=data))

    def execute_transaction(self, accessId, accessPass, orderId, 
            method, payTimes, 
            cardNo, expire, holderName, securityCode, 
            token, pin, httpAccept, httpUserAgent, deviceCategory, 
            clientField1, clientField2, clientField3, clientFieldFlag, tokenType):
        """
        Execute a transaction without member id.

        Args:
            - accessId: returned by create transaction api.
            - accessPass: returned by create transaction api.
            - orderId: orderId is used to identify a transaction.
            - method: 1(一括)/2(分割)/3(ボーナス一括)/4(ボーナス分割)/5(リボ).
            - payTimes: set when method=2/4.
            - cardNo: credit card number.
            - expire: credit card expire time.
            - holderName: credit card holder name.
            - securityCode: credit card security code.
            - token: 
            - pin: 
            - httpAccept: use when enable 3DS.
            - httpUserAgent: use when enable 3DS.
            - deviceCategory: 0(PC)/1(携帯装置). use when enable 3DS.
            - clientField1: free field.
            - clientField2: free field.
            - clientField3: free field.
            - clientFieldFlag: if returns back. 0(no)/1(yes).
            - tokenType: 1(card service)/2(google pay).
        
        Returns:

        when not use 3DS:
            - ACS: value 0.
            - OrderID:
            - Forward:
            - Method:
            - PayTimes:
            - Approve:
            - TranID:
            - TranDate:
            - CheckString:
            - ClientField1:
            - ClientField2:
            - ClientField3:
            - ErrCode:
            - ErrInfo:

        when use 3DS 1.0:  
            - ACS: value 1.
            - ACSUrl:
            - PaReq:
            - MD:
            - ErrCode:
            - ErrInfo:

        when use 3DS 2.0:  
            - ACS: value 2.
            - RedirectUrl:
            - ErrCode:
            - ErrInfo:
        """
        url = self.base_url + EXEC_TRAN_PATH
        data = {
            'AccessID': accessId,
            'AccessPass': accessPass,
            'OrderID': orderId,
            'Method': method,
            'PayTimes': payTimes,
            'CardNo': cardNo,
            'Expire': expire,
            'HolderName': holderName,
            'SecurityCode': securityCode,
            'Token': token,
            'PIN': pin,
            'HttpAccept': httpAccept,
            'HttpUserAgent': httpUserAgent,
            'DeviceCategory': deviceCategory,
            'ClientField1': clientField1,
            'ClientField2': clientField2,
            'ClientField3': clientField3,
            'ClientFieldFlag': clientFieldFlag,
            'TokenType': tokenType,
        }
        return serialize_response(requests.post(url, data=data))

    def execute_transaction_with_member(self, accessId, accessPass, orderId, 
            method, payTimes, siteId, sitePass, memberId, seqMode, 
            cardSeq, cardPass, securityCode, 
            httpAccept, httpUserAgent, deviceCategory, 
            clientField1, clientField2, clientField3):
        """
        Execute a transaction with member id.

        Args:
            - accessId: returned by create transaction api.
            - accessPass: returned by create transaction api.
            - orderId: orderId is used to identify a transaction.
            - method: 1(一括)/2(分割)/3(ボーナス一括)/4(ボーナス分割)/5(リボ).
            - payTimes: set when method=2/4.
            - siteId: issued by smbc-gp.
            - sitePass: issued by smbc-gp.
            - memberId: 
            - seqMode: 0(logic)/1(physics)
            - cardSeq:
            - cardPass:
            - securityCode:
            - httpAccept: use when enable 3DS.
            - httpUserAgent: use when enable 3DS.
            - deviceCategory: 0(PC)/1(携帯装置). use when enable 3DS
            - clientField1: free field.
            - clientField2: free field.
            - clientField3: free field.
            - clientFieldFlag: if returns back. 0(no)/1(yes)

        Returns:

        when not use 3DS:
            - ACS: value 0.
            - OrderID:
            - Forward:
            - Method:
            - PayTimes:
            - Approve:
            - TranID:
            - TranDate:
            - CheckString:
            - ClientField1:
            - ClientField2:
            - ClientField3:
            - ErrCode:
            - ErrInfo:

        when use 3DS 1.0:
            - ACS: value 1.
            - ACSUrl:
            - PaReq:
            - MD:
            - ErrCode:
            - ErrInfo:

        when use 3DS 2.0:
            - ACS: value 2.
            - RedirectUrl:
            - ErrCode:
            - ErrInfo:
        """
        url = self.base_url + EXEC_TRAN_PATH
        data = {
            'AccessID': accessId, 
            'AccessPass': accessPass, 
            'OrderID': orderId,
            'Method': method,
            'PayTimes': payTimes,
            'SiteID': siteId,
            'SitePass': sitePass,
            'MemberID': memberId,
            'SeqMode': seqMode,
            'CardSeq': cardSeq,
            'CardPass': cardPass,
            'SecurityCode': securityCode,
            'HttpAccept': httpAccept,
            'HttpUserAgent': httpUserAgent,
            'DeviceCategory': deviceCategory,
            'ClientField1': clientField1,
            'ClientField2': clientField2,
            'ClientField3': clientField3,
        }
        return serialize_response(requests.post(url, data=data))

    def execute_transaction_after_3ds1(self, paRes, md):
        """
        Execute transaction after 3DS 1.0 verification

        Args:
            - paRes: returned by 3DS 1.0 screen.
            - md: returned by 3DS 1.0 screen.
        
        Returns:
            - OrderID:
            - Forward:
            - Method:
            - PayTimes:
            - Approve
            - TranID
            - TranDate
            - CheckString
            - ClientField1:
            - ClientField2:
            - ClientField3:
            - ErrCode:
            - ErrInfo:
        """
        url = self.base_url + SECURE_TRAN_PATH
        data = {
            'PaRes': paRes,
            'MD': md,
        }
        return serialize_response(requests.post(url, data=data))

    def execute_transaction_after_3ds2(self, accessId, accessPass):
        """
        Execute transation after 3DS 2.0 verification.

        Args:
            - accessId:
            - accessPass:
        
        Returns:
            - OrderID:
            - Forward:
            - Method:
            - PayTimes:
            - Approve
            - TranID
            - TranDate
            - CheckString
            - ClientField1:
            - ClientField2:
            - ClientField3:
            - ErrCode:
            - ErrInfo:
        """
        url = self.base_url + SECURE_TRAN2_PATH
        data = {
            'AccessID': accessId,
            'AccessPass': accessPass,
        }
        return serialize_response(requests.post(url, data=data))

    def modify_transaction(self, shopId, shopPass, accessId, accessPass, jobCd, amount, tax, method, payTimes):
        url = self.base_url + ALTER_TRAN_PATH
        data = {
            'ShopID': shopId,
            'ShopPass': shopPass,
            'AccessID': accessId,
            'AccessPass': accessPass,
            'JobCd': jobCd,
            'Amount': amount,
            'Tax': tax,
            'Method': method,
            'PayTimes': payTimes,
        }
        return serialize_response(requests.post(url, data=data))

    def modify_transaction_amount(self, shopId, shopPass, accessId, accessPass, jobCd, amount, tax):
        url = self.base_url + CHANGE_TRAN_PATH
        data = {
            'ShopID': shopId,
            'ShopPass': shopPass,
            'AccessID': accessId,
            'AccessPass': accessPass,
            'JobCd': jobCd,
            'Amount': amount,
            'Tax': tax,
        }
        return serialize_response(requests.post(url, data=data))

    def search_transaction(self, shopId, shopPass, orderId, useSiteMaskLevel, useFloatinMask):
        url = self.base_url + SEARCH_TRADE_PATH
        data = {
            'ShopID': shopId,
            'ShopPass': shopPass,
            'OrderID': orderId,
            'UseSiteMaskLevel': useSiteMaskLevel,
            'UseFloatMask': useFloatinMask,
        }
        return serialize_response(requests.post(url, data=data))
