import discord
from discord.ext import commands
from typing import List
import getpass
import os
import time


## enables the bot to do thing like write messages and react to commands
intents = discord.Intents.default()
intents.presences = True  
intents.members = True    
intents = discord.Intents.default()
intents.message_content = True  


bot_activity = discord.Client(intents=intents)

@bot_activity.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='/about'))

##opens the order file for the bot
# with open('que_orders.txt', 'r+') as f:   
#     orders = f.read()

#     print(orders)


## Initialize the bot
bot = commands.Bot(command_prefix='/que ', intents=intents)
bothelp = commands.Bot (command_prefix='/', intents=intents)


                        # orders = [
                        #     'Mr B has ordered 15 bricks paid: yes',
                        #     'John Tea has ordered 30 bricks paid: no',
                        #     'Lucas Bolts has ordered 30 Bricks paid: yes',
                        #     'Bill Rose has ordered 30 bricks paid: no',
                        #     'Streetrag Lucchese has ordered 30 bricks paid: yes',
                        #     'Rod Drako has ordered 30 Bricks Paid: yes',
                        #     'Dino Bong has ordered 30 Bricks Paid: yes',
                        #     'Tozai Cherry has ordered 30 Bricks paid: yes',
                        # ]
                        ##needs to be done trough a file so it saves


@bot.command (name='help_me')
async def show(ctx):
    commands = "Commands with /que prefix \n /que show - post current que \n /que add (First name) (Second Name) (Ammount) (Was the order paid? - yes/no) \n /que clear - Wipes the entire que"
    await ctx.send (commands)
    print (commands)

##showing current que
@bot.command(name='show') 
async def show(ctx):
    with open('que_orders.txt', 'r+') as f:   
        orders = f.read()

        print(orders)
        await ctx.send(orders)
        f.close
        


#attempt for que add
@bot.command (name= 'add')
async def add(ctx, user_input1, user_input2, user_input3, user_input4):
    # if user_input1 == None:
    #     await ctx.send ("please enter the name of the customer")
    # elif user_input2 == None:
    #     await ctx.send ("please enter the ammount of bricks that were ordered")
    # elif user_input3 == None:
    #     await ctx.send ("please enter if the order was paid or not")

    order = f"{user_input1} {user_input2} has ordered {user_input3} bricks. Paid: {user_input4}"
    with open('que_orders.txt', 'a') as que:
        que.write (order + '\n')


        await ctx.send(f"order for {user_input3} bricks made by {user_input1} {user_input2} has been added to the que")
        que.close


#wipes the que
@bot.command (name='clear')
async def clear(ctx):
    with open('que_orders.txt', 'w') as file:
        file.write("This is the current que:"'\n')
        await ctx.send("The que has been cleared")






## attempt for a welcome messages when a user joins the server
@bot.event
async def on_member_join (member):
    channel = bot.get_channel('1019201774025969737')
    await channel.send ("Welcome to Orion Weed INC. We are pleased to have you here, you can choose your roles in channel")

bot.run('MTIxNDE0MTMyMTUxODc4NDUzMg.GVhUkA.iH43jxHnuO2ilZ9Mz3KGJSHvVjbJXTcFteqr3Q')
# bot.run('MTE5OTMwODg4MjgyOTM5ODExNw.Ggr1JN.NUH2kCZ1TbdRZEYBYFPJ1Py6bA-RPCS19qKQlw') ## test bot









# orders_add = open ('que_orders', 'a')

# @bot.command(name='que')  ##adding to que
# async def add_to_queue(ctx, user_input1, user_input2, user_input3):
#     order = f"{user_input1} has ordered {user_input2} bricks. Paid?: {user_input3}"
#     orders.append(orders_add)
#     await ctx.send(f"Order added to the queue: {order}")

#     orders == '/n', orders + user_input1 +user_input2

    # list.add (user_input1, user_input2, user_input3)

    # new_order = ['', user_input1, user_input2, user_input3]

    # with open('que_orders', 'r+') as f:
    #     content = f.read()
    #     f.write(content.replace ())
    





# @bot.command (name='que_add')
# async def add(ctx, input1, input2):
#     await ctx.add(orders)


# # Command to show the current queue ## not functional
# @bot.command(name='showque')
# async def show_queue(ctx):
#     if not orders:
#         await ctx.send("Queue is empty.")
#     else:
#         queue_message = "\n".join(orders)
#         await ctx.send(f"Current queue:\n{queue_message}")













### possible solution to que add
# class que_add (commands.FlagConverter):
#     name: str
#     ammount: int 

# @commands.command(name=que_add)
# async def add(ctx, *, flags: que_add):
#     for member in flags.members:
#         await member.send(name=flags.name, ammount_of_bricks=flags.ammount)
# @bot.command (name=que_add)
# async def add(ctx, *, flags: que_add):
#     for member in flags.members:
#         await member.send(name=flags.name, ammount_of_bricks=flags.ammount)












# user_input = ["1,2"]

# bot.command (name='que')
# async def _que(var1: str, var2: str):
#     user_input.append ((var1, var2))
#     print ("added to que")

# @bot.command()
# async def test(ctx, *, arg):
#     await ctx.send(arg)


# bot.command 
# async def showque():
#     print [user_input]

# # Load the extension (cog)
# async def load_cog():
#     await bot.load_extension("cogs.que")  # Replace "que" with the actual filename
#     print("Cog loaded successfully!")

# user_inputs = []

# bot.command()
# async def que(ctx, var1: str, var2: str):
#     """
#     Usage: /que <var1> <var2>
#     Stores two variables inputted by the user.
#     """
#     user_inputs.append((var1, var2))
#     await ctx.send(f"Variables '{var1}' and '{var2}' added to the list!")

# @bot.command()
# async def que(ctx, var1: str, var2: str):
#     print(f"Received command: /que {var1} {var2}")



# import discord, datetime, time
# from discord.ext import commands
# from datetime import date, datetime


# intents = discord.Intents.default()
# intents.presences = True  # Enable presence intent
# intents.members = True    # Enable members intent
# intents = discord.Intents.default()
# intents.message_content = True  # Enable message content intent



# prefix = "!!"
# client = commands.Bot(command_prefix=prefix, case_insensitive=True)

# times_used = 0

# @client.event
# async def on_ready():
#   print(f"I am ready to go - {client.user.name}")
#   await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{client.command_prefix}python_help. This bot is made by drakeerv."))

# @client.command(name="ping")
# async def _ping(ctx):
#   global times_used
#   await ctx.send(f"Ping: {client.latency}")
#   times_used = times_used + 1

# @client.command(name="time")
# async def _time(ctx):
#   global times_used
#   from datetime import date, datetime

#   now = datetime.now()

#   if (now.strftime("%H") <= "12"):
#     am_pm = "AM"
#   else:
#     am_pm = "PM"

#   datetime = now.strftime("%m/%d/%Y, %I:%M")

#   await ctx.send("Current Time:" + ' '  + datetime + ' ' + am_pm)
#   times_used = times_used + 1

# @client.command(name="times_used")
# async def _used(ctx):
#   global times_used
#   await ctx.send(f"Times used since last reboot:" + ' ' + str(times_used))
#   times_used = times_used + 1

# @client.command(name="command") #THIS LINE
# async def _command(ctx):
#   global times_used
#   await ctx.send(f"y or n")
#   times_used = times_used + 1

# @client.command(name="python_help")
# async def _python_help(ctx):
#   global times_used
#   msg = '\r\n'.join(["!!help: returns all of the commands and what they do.",
#                      "!!time: returns the current time.",
#                      "!!ping: returns the ping to the server."])
#   await ctx.send(msg)
#   times_used = times_used + 1



# client.run("MTE5OTMwODg4MjgyOTM5ODExNw.Ggr1JN.NUH2kCZ1TbdRZEYBYFPJ1Py6bA-RPCS19qKQlw")