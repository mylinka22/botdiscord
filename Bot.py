import discord
from discord.ext import commands
import datetime
today = datetime.datetime.today()

TOKEN = 'Njk1NjQxNTQxMTA4MTcwODEz.XrVwEw.Nbi5FfwpxubOMIJrS4m3rIvSHK8'
bot = commands.Bot(command_prefix='*')

def Dpl(arg):
    f = open('base.txt', 'r')
    baseDS = f.read()
    f.close()
    base = baseDS.split("\n")
    #print(base)
    for people in range(len(base)):
        # print(base[people].split(" "))
        #print(arg.split("_"))
        #print(base[people].split("_"))
        if arg.split("_")[0] == base[people].split(" ")[0] and arg.split("_")[1] == base[people].split(" ")[1]:
            #print(1)
            lenm = len(base[people].split(" ")[-1])
            #print(lenm)
            #print(base[people][-lenm:])
            #print(int(base[people][-lenm:]) + int(arg.split("_")[2]))
            #print(base[people][:-lenm])
            base[people] = base[people][:-lenm] + str(int(base[people][-lenm:]) + int(arg.split("_")[2]))
            print("ДЕПОЗИТ {} {} СУММА ПЛЮС {}".format(arg.split("_")[0], arg.split("_")[1], arg.split("_")[2]))
            # print(people)
            #break
    f = open('base.txt', 'w')
    for people in range(len(base)):
        f.write(base[people] + '\n')
    f.close()
    f = open('base.txt', 'r')
    base = f.read()
    f.close()
    return base

def Dmi(arg):
    f = open('base.txt', 'r')
    baseDS = f.read()
    f.close()
    base = baseDS.split("\n")
    #print(base)
    for people in range(len(base)):
        # print(base[people].split(" "))
        #print(arg.split("_"))
        #print(base[people].split("_"))
        if arg.split("_")[0] == base[people].split(" ")[0] and arg.split("_")[1] == base[people].split(" ")[1]:
            #print(1)
            lenm = len(base[people].split(" ")[-1])
            #print(lenm)
            #print(base[people][-lenm:])
            #print(int(base[people][-lenm:]) + int(arg.split("_")[2]))
            #print(base[people][:-lenm])
            base[people] = base[people][:-lenm] + str(int(base[people][-lenm:]) - int(arg.split("_")[2]))
            print("ДЕПОЗИТ {} {} СУММА МИНУС {}".format(arg.split("_")[0], arg.split("_")[1], arg.split("_")[2]))
            # print(people)
            #break
    f = open('base.txt', 'w')
    for people in range(len(base)):
        f.write(base[people] + '\n')
    f.close()
    f = open('base.txt', 'r')
    base = f.read()
    f.close()
    return base

def Kpl(arg):
    dat = "[" + str(today.strftime("%H:%M_%d.%m.%Y"))[:-2] + "]"
    f = open('base2.txt', 'r')
    baseDS = f.read()
    f.close()
    base = baseDS.split("\n")
    #print(base)
    for people in range(len(base)):
        # print(base[people].split(" "))
        #print(arg.split("_"))
        #print(base[people].split("_"))
        if arg.split("_")[0] == base[people].split(" ")[0] and arg.split("_")[1] == base[people].split(" ")[1]:
            #print(1)
            lenm = len(base[people].split(" ")[-1])
            #print(lenm)
            #print(base[people][-lenm:])
            #print(int(base[people][-lenm:]) + int(arg.split("_")[2]))
            #print(base[people][:-lenm])
            base[people] = base[people][:-lenm] + str(int(base[people][-lenm:]) + int(arg.split("_")[2])) + " " + dat
            print("ДОЛГ {} {} СУММА {}".format(arg.split("_")[0], arg.split("_")[1], arg.split("_")[2]))
            # print(people)
            #break
    f = open('base2.txt', 'w')
    for people in range(len(base)):
        f.write(base[people] + '\n')
    f.close()
    f = open('base2.txt', 'r')
    base = f.read()
    f.close()
    return base


def Knu(arg):
    f = open('base2.txt', 'r')
    baseDS = f.read()
    f.close()
    base = baseDS.split("\n")
    #print(base)
    for people in range(len(base)):
        # print(base[people].split(" "))
        #print(arg.split("_"))
        #print(base[people].split("_"))
        if arg.split("_")[0] == base[people].split(" ")[0] and arg.split("_")[1] == base[people].split(" ")[1]:
            #print(1)
            lenm = len(base[people].split(" ")[-1])
            if lenm != 0:
                lenm += len(base[people].split(" ")[-2]) + 1
            #print(lenm)
            #print(base[people][-lenm:])
            #print(base[people][:-lenm])
            base[people] = base[people][:-lenm] + "0"
            print("ДОЛГ {} {} СНЯТ".format(arg.split("_")[0], arg.split("_")[1]))
            # print(people)
            #break
    f = open('base2.txt', 'w')
    for people in range(len(base)):
        f.write(base[people] + '\n')
    f.close()
    f = open('base2.txt', 'r')
    base = f.read()
    f.close()
    return base

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def Dplus(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(Dpl(arg))  # отправляем обратно аргумент

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def Dminus(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(Dmi(arg))  # отправляем обратно аргумент

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def Kplus(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(Kpl(arg))  # отправляем обратно аргумент

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def Knull(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(Knu(arg))  # отправляем обратно аргумент


bot.run(TOKEN)

#pl("Max Grozny 35000")