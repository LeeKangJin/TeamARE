
def intcode_to_lawdcd( i ):
    return {
        '1':'11680',
        '2': '11740',
        '3': '11305',
        '4': '11500',
        '5': '11620',
        '6': '11215',
        '7': '11530',
        '8': '11545',
        '9': '11350',
        '10': '11320',
        '11': '11230',
        '12': '11590',
        '13': '11440',
        '14': '11410',
        '15': '11650',
        '16': '11200',
        '17': '11290',
        '18':'11710',
        '19': '11470',
        '20': '11560',
        '21': '11170',
        '22': '11380',
        '23': '11110',
        '24': '11140',
        '25': '11260'

    }.get(i, '11110') #default

def byupjungdong(guvar,dongvar):
    dongNameList =[
        ['개포동','논현동','대치동','도곡동','삼성동','세곡동','수서동','신사동','압구정동','역삼동','율현동','일원동','자곡동','청담동'],
        ['강일동','고덕동','길동','둔촌동','명일동','상일동','성내동','암사동','천호동'],
        ['미아동','번동','수유동','우이동'],
        ['가양동','개화동','공항동','과해동','내발산동','등촌동','마곡동','방화동','염창동','오곡동','오새동','외발산동','화곡동'],
        ['남현동','봉천동','신림동'],
        ['광장동','구의동','군자동','능동','자양동','중곡동','화양동'],
        ['가리봉동','개봉동','고척동','구로동','궁동','신도림동','오류동','온수동','천왕동','항동'],
        ['가산동','독산동','시흥동'],
        ['공릉동','상계동','월계동','중계동','하계동'],
        ['도봉동','방학동','쌍문동','창동'],
        ['답십리동','신설동','용두동','이문동','장안동','전농동','재기동','청량리동','회기동','휘경동'],
        ['노량진동','대방동','사당동','상도동','신대방동','흑석동'],
        ['공덕동','구수동','노고산동','당인동','대흥동','도화동','동교동','마포동','망원동','상수동','상암동','서교동','성산동','신공덕동','신수동','신정동','아현동','연남동','염리동','용강동','중동','창전동','합정동'],
        ['남가좌동','북가좌동','냉천동','북아현동','신촌동','연희동','천연동','홍은동','홍재동'],
        ['내곡동','반포동','방배동','서초동','양재동','염곡동','잠원동'],
        ['마장동','사근동','송정동','옥수동','용답동','응봉동','해당동'],
        ['길음동','돈암동','석관동','성북동','장위동','정릉동','종암동'],
        ['풍납동','가락동','거여동','마천동','문전동','방이동','삼정동','석촌동','송파동','신천동','오금동','장실동','장지동'],
        ['목동','신월동','신정동'],
        ['당산동','대림동','도림동','신길동','양평동','영등포동'],
        ['갈월동','남영동','보광동','서빙고동','용문동','이촌동','이태원동','한남동','효창동','후암동'],
        ['갈현동','구산동','녹번동','대조동','불광동','수색동','신사동','역촌동','응암동','증산동','진관동'],
        ['가회동','견지동','공평동','교남동','구기동','낙원동','돈의동','묘동','무악동','봉익동','부암동','사직동','삼청동','소격동','숭인동','신교동','신영동','예지동','옥인동','와룡동','운니동','원남동','원서동','이화동','인사동','인의동','장사동','적선동','창신동','청운동','청진동','충신동','통인동','평창동','혜화동','효자동','효재동'],
        ['소공동','신당동','정동','중림동','황학동'],
        ['망우동','면목동','묵동','상봉동','신내동','중화동'],
    ]
    return dongNameList[guvar][dongvar]