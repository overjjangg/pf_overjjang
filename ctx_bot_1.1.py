import asyncio
import discord
import random
import tkinter
from multiprocessing import Process



    
app = discord.Client()


token = "token"
calcResult = 0
money_count = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("버짱아 혹은 버짱아 도움을 입력하새요!") #새로운 코드
    await app.change_presence(status=discord.Status.online, activity=game) #바뀜
    await bt(['요구루퉁 머꼬싶따', '버짱아 혹은 버짱아 도움을 입력하새요!','예ㅖㅖㅖㅖㅖ스'])
@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('버짱아'):
        if len(message.content) == 3:
            ranans = random.randint(1,3)
            if ranans == 1:    
                await message.channel.send("넵")
            elif ranans == 2:
                await message.channel.send("네?")
            elif ranans == 3:
                await message.channel.send("zz..z ? 네!")
        else:
            if message.content.split()[1] == "도움":
                hbed=discord.Embed(title="도움", description="도움말.", color=0x00aaaa)
                hbed.set_author(name="{}".format(message.author) ,icon_url=message.author.avatar_url)
                hbed.add_field(name="재작자", value="overjjang_kr", inline=True)
                hbed.add_field(name="명령어", value="`x`\n`이름`\n`정보`\n`동전`\n`주사위 숫자`\n`hk`", inline=True)
                hbed.set_footer(text="작성자:overjjang_kr#2683")
                await message.channel.send(embed=hbed)
            if message.content.split()[1] == "정보":
                await message.channel.send("버짱이입니다 게발자님이신 오버짱님께서 따왔죠!")
            if message.content.split()[1] == "동전":
                ran = random.randint(1,2)
                if ran == 1:
                    await message.channel.send("앞면!")
                elif ran == 2:
                    await message.channel.send("뒷면!")
            if message.content.split()[1] == "주사위":
                if len(message.content) == 7:
                    dic = random.randint(1,6)
                    await message.channel.send(dic)
                elif len(message.content) >= 8:
                    dicl = message.content.split()[2]
                    dicf = random.randint(1,int(dicl))
                    await message.channel.send(dicf)
                else:
                    await message.channel.send("숫자를 입력해 주새요!")
            if message.content.split()[1] == "이름":
                ranname = random.randint(1,3)
                if ranname == 1:    
                    await message.channel.send("이름이... 어디보자...{}님?".format(message.author.mention))
                elif ranname == 2:
                    await message.channel.send("{}님?".format(message.author.mention))
                elif ranname == 3:
                    await message.channel.send("너의이름은... {}".format(message.author.mention))
            if message.content.split()[1] == "x":
                imran = random.randint(1,100)
                if imran == 1:
                    await message.channel.send("joy를 표합니다...")
                else:
                    await message.channel.send("조의를 표합니다...")
            if message.content.split()[1] == "심심해":
                semran = random.randint(1,1)
                semran = semran + 1
                await message.channel.send("xkcd를 읽어보새요!\nhttps://xkcd.com/")
            if message.content.split()[1] == "개발자":
                await message.channel.send("오버짱님이죠! ~~매우 잘생기셨답니다~~")
            if message.content.split()[1] == "hk":
                await message.channel.send("HK for devloper\nhttps://discord.gg/HKDev")
            if message.content.split()[1] == "레몬":
                await message.channel.send("요즘 근황:야생 컨탠츠가 부족하내")
            if message.content.split()[1] == "큐브":
                await message.channel.send("하이퍼큐브!")
            if message.content.split()[1] == "오버짱":
                jjangran = random.randint(1,2)
                if jjangran == 1:
                    await message.channel.send("요즘근황22:야생에 빠졋... ?")
                else:
                    await message.channel.send("에???????")
            
            
            
            if message.content.split()[1] == "돈":
                f = open("Name.txt", 'r' ,encoding='UTF8')
                r = open("Momey.txt", 'r' ,encoding='UTF8')
                f_ID = open("userID.txt", 'r', encoding='UTF8')
                if len(message.content) == 5:
                    user_name = str(message.author)
                    money_count = -1
                    while True:
                        money_count = money_count + 1
                        line = f.readline()
                        if user_name.strip() == str(line).strip():
                            m_line = r.readlines()
                            p_money = m_line[money_count].strip()
                            await message.channel.send("{}님의 잔고는 ".format(message.author.mention) + p_money + "코인입니다")
                            break
                        if not line:
                            await message.channel.send("아직 '버짱은행'에 가입하기 않으셨근요! `버짱아 은행`을 통해 가입해주새요!")
                            break
                elif len(message.content) >= 20:
                    user_name = str(message.content)[6:]
                    print(user_name)
                    money_count = -1
                    while True:
                        money_count = money_count + 1
                        line = f_ID.readline()
                        if user_name.strip() == str(line).strip():
                            m_line = r.readlines()
                            p_money = m_line[money_count].strip()
                            ID_name = f.readlines()[money_count]
                            print(ID_name)
                            await message.channel.send("@" + ID_name + "님의 잔고는 " + p_money + "코인입니다")
                            break
                        if not line:
                            await message.channel.send("아직 '버짱은행'에 가입하기 않으셨근요! `버짱아 은행`을 통해 가입해주새요!")
                            break
                else:
                    await message.channel.send("`버짱아 돈` 아니면 `버짱아 돈 ID`를 입력하새요!")
                f.close()
                r.close()
                f_ID.close()
                money_count=0
            if message.content.split()[1] == "은행":
                f_a = open("Momey.txt",'a',encoding='UTF8')
                f_r = open("Name.txt",'r',encoding='UTF8')
                fm_r = open("Name.txt",'a',encoding='UTF8')
                f_ID = open("userID.txt", 'a', encoding='UTF8')
                user_name = str(message.author)
                User_ID = str(message.id)
                money_count = -1
                while True:
                    money_count = money_count + 1
                    line = f_r.readline()
                    if user_name.strip() == str(line).strip():
                        await message.channel.send("이미 가입되있습니다")
                        break
                    if not line:
                        bank_rbed = discord.Embed(title="버짱은행 가입", description="가입중...", color=0x00aaaa)
                        await message.channel.send(embed=bank_rbed)
                        fm_r.write(user_name+"\n")
                        f_a.write('100'+"\n")
                        f_ID.write(User_ID+"\n")
                        bank_sbed=discord.Embed(title="가입성공!", description="이제 버짱아 돈으로 당신의 잔고를 확인하새요!", color=0x00aaaa)
                        await message.channel.send(embed=bank_sbed)
                        break
                f_a.close()
                f_r.close()
                fm_r.close()
                money_count=0
            if message.content.split()[1] == "배급":
                money_plus_r = open("Momey.txt",'r', encoding='UTF8')
                name_plus_r = open("Name.txt",'r', encoding='UTF8')
                replace_line = money_plus_r.readlines()
                user_name = str(message.author)
                money_count = -1
                while True:
                    money_count = money_count + 1
                    line = name_plus_r.readline()
                    if user_name.strip() == str(line).strip():
                        if int(replace_line[money_count]) < 10:
                            replace_line[money_count] = str(int(replace_line[money_count]) + 50) + str("\n")
                            with open('Momey.txt', 'w') as file:
                                file.writelines(replace_line)
                            await message.channel.send("도박중독 콜샌터는 1336(돈이 50원 지급되었습니다)")
                            break
                        else:
                            await message.channel.send("이미 돈이 충분하시군요!")
                            break
                    elif not line:
                        await message.channel.send("아직 '버짱은행'에 가입하기 안으셨근요! 버짱아 은행을 통해 가입해주새요!")
                        break
            
            if message.content.split()[1] == "도박":
                if len(message.content) == 6:
                    await message.channel.send("얼마를 거실건지 말슴해 주새요")
                elif len(message.content) >= 8:
                    dobac_ran = random.randint(1,100)
                    await message.channel.send("도박중...")
                    money_plus_r = open("Momey.txt",'r', encoding='UTF8')
                    name_plus_r = open("Name.txt",'r', encoding='UTF8')
                    replace_line = money_plus_r.readlines()
                    user_name = str(message.author)
                    money_count = -1
                    double_money = message.content[7:]
                    
                    print(double_money)
                    while True:
                        money_count = money_count + 1
                        
                        line = name_plus_r.readline()
                        if user_name.strip() == str(line).strip():
                            if int(double_money) > int(replace_line[money_count]):
                                await message.channel.send("돈이 없습니다")
                                break
                            elif dobac_ran >= 50:
                                replace_line[money_count] = str(int(replace_line[money_count]) + int(double_money)) + str("\n")
                                print(replace_line[money_count])
                                with open('Momey.txt', 'w') as file:
                                    file.writelines(replace_line)
                                await message.channel.send("도박 성공!(돈 2배!)")
                                p_money = replace_line[money_count].strip()
                                await message.channel.send("{}님의 잔고: ".format(message.author.mention) + p_money + "코인")
                                break
                            elif dobac_ran < 50:
                                replace_line[money_count] = str(int(replace_line[money_count]) - int(double_money)) + str("\n")
                                print(replace_line[money_count])
                                p_money = replace_line[money_count].strip()
                                with open('Momey.txt', 'w') as file:
                                    file.writelines(replace_line)
                                await message.channel.send("도박 실패!(돈 모두 잃음!)")
                                await message.channel.send("{}님의 잔고: ".format(message.author.mention) + p_money + "코인")
                                break
                            
                        if not line:
                            await message.channel.send("도박을 하시려면 은행에 가입하셔야합니다! '버짱아 은행' 을 통해 은행에 가입해주새요!")
                            break               
                money_count=0
                money_plus_r.close()
                name_plus_r.close()

                



                
    
def main():
    pass


async def bt(games):
    await app.wait_until_ready()

    while not app.is_closed():
        for g in games:
            await app.change_presence(status = discord.Status.online, activity = discord.Game(g))
            await asyncio.sleep(10)   
app.run(token)