import urllib.request
import json    # or `import simplejson as json` if on Python < 2.6
from operator import itemgetter

def reversegeocode(XYstring):
    obj = dict()
    client_id = "XORQXLjnF_42QQm3fDA2"
    client_secret = "KTrLgc2JfY"
    encText = urllib.parse.quote(XYstring)
    url = "https://openapi.naver.com/v1/map/reversegeocode?query=" + encText # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    try:
        response = urllib.request.urlopen(request)
    except:
        print('api요청이 응답하지 않습니다.')
    else:
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            obj = json.loads(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    finally:
        return obj
def XYtoAddressList( XYstring ):
    retlist = list()
    obj=reversegeocode(XYstring)
    if len(obj) == 0:
        return retlist
    numItem = obj['result']['total']
    for i in range (0, numItem) :
        if obj['result']['items'][i]['isAdmAddress']:
            retlist.append(obj['result']['items'][i]['address'])
    return retlist
def XYtoAddrdetailList( XYstring ):
    retlist = list()
    obj=reversegeocode(XYstring)
    if len(obj) == 0:
        return retlist
    numItem = obj['result']['total']
    for i in range (0, numItem) :
        retlist.append(obj['result']['items'][i]['addrdetail'])
    return retlist
def get_dong(e):
    XYStr=str(e.x) + str(',') +str(e.y)
    addrlist = XYtoAddrdetailList(XYStr)
    for addr in addrlist:
        if addr['dongmyun'] == '':
            pass
        else:
            return addr['dongmyun']
    return 'error'

# coding=utf-8
def is_number_address(rest):
    try:
        num =rest.replace( '-', '' )
        num = num.replace( ',', '' )
        num = num.replace(' ','')
        float(num)
        return True #num을 float으로 변환할 수 있는 경우
    except ValueError: #num을 float으로 변환할 수 없는 경우
        return False


def get_numAddr(e):
    XYStr=str(e.x) + str(',') +str(e.y)
    addrlist = XYtoAddrdetailList(XYStr)
    for addr in addrlist:
        if is_number_address(addr['rest']):
            num = addr['rest'].replace( ',', '' )
            num = num.replace( ' ', '' )
            return num
    return 'error'


def get_name( e ) :
    mycollapsedstring = ' '.join(e.address.split())
    name = mycollapsedstring.split(' ')[-1]
    return name


def tradeDataSort(tradeDataDic):

   # tradeDataDic = [{'price':'Homer', 'ymd':'39'}, {'price':'Bart', 'ymd':'10'}] test input


    dicLen = len(tradeDataDic)

    for i in range ( dicLen ):
        tradeDataDic[i]['ymd'] = int(tradeDataDic[i]['ymd'])     # string 일때 int로 변형

    newlist = sorted(tradeDataDic, key=itemgetter('ymd'), reverse=False)
    label_list=[]
    data_list=[]
    for item in newlist:
        label_list.append(str(item['ymd']))
        data_list.append(int(item['price']))
    return label_list , data_list
if __name__ =="__main__":
    print (XYtoAddrdetailList("126.8397859,37.4991205"))
