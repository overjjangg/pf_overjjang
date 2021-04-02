print('loding')
import discord
import datetime
import random
class chatbot(discord.Client):
    async def on_ready(self):
        game = discord.Game("~도움 ,예도 이제 1살임")#'게임'부분의 글을 게임으로 합니다.
        await client.change_presence(status=discord.Status.online, activity=game)
        print('overbot online')
    async def on_message(self, message):
        if message.author.bot:
            return None
        if message.content == "~핑":
            channel = message.channel
            pingbed = discord.Embed(title =":ping_pong:퐁!", description ="{}님의 핑은\n".format(message.author.mention) + str(client.latency) + 's', color = 0x00ff00)
            await message.channel.send(embed=pingbed)
            return None
        if message.content == "~test":
            channel = message.channel
            await message.channel.send("태스팅 기능이 없음")
        if message.content == "~도움":
            channel = message.channel
            helpbed=discord.Embed(title = '도움!', description = '~핑\n~시간\n~hk\n~파이선\n~cal x (+,-,*,/) y', color = 0x00ffff)
            helpbed.set_image(url="https://lh3.googleusercontent.com/proxy/Bas2nQlzVt9VaqRmNUy6fYZQOiy-BztDhR2_nKErM1emPcPCkquQg28DSTxPUS6Y9TRT28xTg0Q0-7WKLEL4ZgisFYGyFhmPpbgf7cXIOmwvji43GTxYf6ESRIInqG7AOPsdWA5X0p5GHQ66cpo")
            await message.channel.send(embed=helpbed)
            return None
        if message.content == "~시간":
            channel = message.channel
            timebed = discord.Embed(title="시간", timestamp=datetime.datetime.utcnow(), color = 0x00ffff)
            await message.channel.send(embed=timebed)
            return None
        if message.content == "overbot":
            channel = message.channel
            menbed = discord.Embed(title='앗! 부르셨나용?',description = '안녕하세요! 다기능 채팅봇\n***overbot***\n입니당!\n접두사는~입니당!\n만든사람:overjjang_kr\n||아잉아잉||', color = 0x00ffff)
            await message.channel.send(embed=menbed)
            return None
        if message.content == "~파이선":
            channel = message.channel
            pybed = discord.Embed(title='파이선 링크를 보내 드리겠습니다!',description = 'python', color = 0x00ffff,url="https://www.python.org/")
            pybed.set_thumbnail(url="https://t1.daumcdn.net/cfile/blog/999BD6335C1F7AD22D")
            await message.channel.send(embed=pybed)
            return None
        if message.content == '~hk':
            channel = message.channel
            hkbed = discord.Embed(title='Hk',description = 'HK for developer', color = 0x00ffff,url="https://discord.gg/HKDev")
            await message.channel.send(embed=hkbed)
            return None
        if message.content.startswith('~cal'):
            channel = message.channel
            if len(message.content) >= 9:
                inpf = message.content.split()[1]
                inpm = message.content.split()[2]
                inpl = message.content.split()[3]
                if inpm == '+':
                    if float(inpf) - int(inpf) != 0 or float(inpl) - int(inpl) != 0:
                        float(inpf)
                        float(inpl)
                        calf = float(inpf) + float(inpl)
                        calbed = discord.Embed(title='계산',description = '계산"\n`' + str(float(inpf))  + " + " + str(float(inpf))  + "`\n결과:\n`" + str(float(calf)) + "`", color = 0x00ffff)
                    else:
                        int(inpf)
                        int(inpl)
                        calf = int(inpf) + int(inpl)
                        calbed = discord.Embed(title='계산',description = '계산"\n`' + str(int(inpf)) + " + " + str(int(inpl)) + "`\n결과:\n`" + str(int(calf)) + "`", color = 0x00ffff)
                elif inpm == '-':
                    if float(inpf) - int(inpf) != 0 or float(inpl) - int(inpl) != 0:
                        float(inpf)
                        float(inpl)
                        calf = float(inpf) - float(inpl)
                        calbed = discord.Embed(title='계산',description = '계산"\n`' + str(float(inpf))  + " - " + str(float(inpf))  + "`\n결과:\n`" + str(float(calf)) + "`", color = 0x00ffff)
                    else:
                        int(inpf)
                        int(inpl)
                        calf = int(inpf) - int(inpl)
                        int(calf)
                        calbed = discord.Embed(title='계산',description = '계산"\n`' + str(int(inpf)) + " - " + str(int(inpl)) + "`\n결과:\n`" + str(int(calf)) + "`", color = 0x00ffff)
                elif inpm == '*' or inpm == "x":
                    if float(inpf) - int(inpf) != 0 or float(inpl) - int(inpl) != 0:
                        float(inpf)
                        float(inpl)
                        calf = float(inpf) * float(inpl)
                        calbed = discord.Embed(title='계산',description = '계산"\n`' + str(float(inpf))  + " * " + str(float(inpf))  + "`\n결과:\n`" + str(float(calf)) + "`", color = 0x00ffff)
                    else:
                        int(inpf)
                        int(inpl)
                        calf = int(inpf) * int(inpl)
                        int(calf)
                        calbed = discord.Embed(title='계산',description = '계산"\n`' + str(int(inpf)) + " * " + str(int(inpl)) + "`\n결과:\n`" + str(int(calf)) + "`", color = 0x00ffff)
                elif inpm == '/':
                    if inpl == 0:
                        calbed = discord.Embed(title='에러',description = '0은 영원히 0으로 나눌수 없습니당', color = 0x00ffff)
                    else:
                        if float(inpf) - int(inpf) != 0 or float(inpl) - int(inpl) != 0:
                            float(inpf)
                            float(inpl)
                            calf = float(inpf) * float(inpl)
                            calbed = discord.Embed(title='계산',description = '계산"\n`' + str(float(inpf)) + " / " + str(float(inpf))  + "`\n결과:\n`" + str(float(calf)) + "`", color = 0x00ffff)
                        else:
                            int(inpf)
                            int(inpl)
                            calf = int(inpf) / int(inpl)
                            int(calf)
                            calbed = discord.Embed(title='계산',description = '계산"\n`' + str(int(inpf)) + " / " + str(int(calf)) + "`\n결과:\n`" + str(int(calf)) + "`", color = 0x00ffff)
            else:
                calbed = discord.Embed(title='계산',description = "입력하실때는 숫자와 부호 사이를 띄어쓰기를 해 주새요", color = 0x00ffff)
            await message.channel.send(embed=calbed)
        if message.content == "~재작자":
            dvbed = discord.Embed(title='개발자',description = "overjjang_kr#2683\n~~만들기 급나 어렵내... 휴~~", color = 0x00ffff)
            await message.channel.send(embed=dvbed)
if __name__ == "__main__":
    client = chatbot()
    client.run("~~~")
    
