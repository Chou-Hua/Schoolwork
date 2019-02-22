import facebook # pip install facebook-sdk
import json
import requests


# A helper function to pretty-print Python objects as JSON

def pp(o): 
    print (json.dumps(o, indent=1))

# Create a connection to the Graph API with your access token
ACCESS_TOKEN= ''
print("請輸入想查詢的FB ID:")
id=input()
graph = facebook.GraphAPI(ACCESS_TOKEN)
#posts = graph.get_connections(id, connection_name = 'posts')
games = graph.get_connections(id,connection_name='games')
#television= graph.get_connections(id,connection_name='television')

print("---------------------------------------------------")
print("喜歡的遊戲:")
gamedata=[]
for game in games['data']:
    if'name' in game :
     gamedata.append(game['name'])
print(gamedata)
     #print(game['name'])
print('----------------------------------------------------')
s1 = set(gamedata)

Cardgames = ['爐石戰記','Hearthstone','闇影詩章','Shadowvers','刀塔傳奇','御姬之翼','真神Online','神劍女孩S','百萬亞瑟王 Million Arthur','爐邊打狗-Hearthstone Takao','遊戲王-怪獸之決鬥'
             ,'','','','','','','','','','','','']
s2 = set(Cardgames)

DOTA = ['DOTA2','LOL','英雄聯盟','League of Legends','英雄聯盟- 開心遊戲網-heha戰隊','暴雪英霸','英雄聯盟基地 - 嚕報','最強聯盟Best League','Garena 傳說對決','英雄聯盟小劇場',
        '魔獸爭霸III：信長之野望','阿瓦隆之王 King of Avalon','','','','','','']
s3 = set(DOTA)

FPS = ['BF1','Garena A.V.A 戰地之王','Team Fortress 2','WARFRAME','百變兵團 Avatar Star','藍星戰記OnLine','鬥陣特攻','鬥陣大亂鬥','CS Online','','','','','','','','','']
s4 = set(FPS)

MMORPG = ['黑色沙漠','墨術 Magink','魔物學園Monsters','魔物獵人FRONTIER G','Garena 流亡黯道','快樂玩《封印者：CLOSERS》','飄流幻境','Orbit Legends - 星環守護者','魔王與公主',
          '乖離性百萬亞瑟王','劍靈 Blade & Soul','【狩龍戰紀】Online','【幻想神域】Online','大笑江湖','依露娜戰紀Online（永久免費）','少女前線','Pixel Starships','三國志',
          '我們的甲子園','黑色沙漠 Black Desert Online','上古世紀ArcheAge','勇者sama','格林筆記','萬千回憶 Thousand Memories','Efunfun掛機Q傳','【星界神話】Online','Deadbreed'
          ,'全民掛機','神奇寶貝系列 Pokémon','Garena 新瑪奇英雄傳','Final Fantasy III','Kingdom Knights - 王國騎士團','三國群英傳mobile','Chain Chronicle','','','']
s5 = set(MMORPG)

phonegames = ['神魔之塔','Doodle Jump','妹妹玩大俠','部落衝突','熾天使-神魔之塔攻略網','神魔助手','Gameloft','Mushroom Garden','飄流幻境 手機版','妃十三學園 Alternative Girls',
              '有殺氣童話 - 姐不是好惹der','女神聯盟手遊-i can','怪物彈珠 - Monster Strike','航海衝突','神魔之塔開心遊戲網攻略專區','墨術',''
              ,'','','','','','','']
s6 = set(phonegames)

Puzzle = ['Cake5','Transport Fever','鋼鐵雄心IV','Hearts of Iron','Hearts of Iron IV','']
s7 = set(Puzzle)

action = ['滾滾飛球','職棒總教頭','Mount & Blade','飢餓地城 HungerDungeon','爆爆王','跑跑卡丁车','全民打棒球 Online','跑跑卡丁車官方粉絲團']
s8 = set(action)


print("可能感興趣的遊戲類型:")
if s1 & s2:
    print("卡牌遊戲")
if s1 & s3:
    print("DOTA遊戲")
if s1 & s4:
    print("射擊遊戲")
if s1 & s5:
    print("角色扮演遊戲")
if s1 & s6 & s2:
    print("手機遊戲")
if s1 & s7:
    print("益智遊戲")    

