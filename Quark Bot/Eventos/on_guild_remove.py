import nextcord
import os
import asyncio
from nextcord.ext import commands


class on_guild_remove(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        
    
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data/{}.json'.format(guild.id)) in [True]:
            
            await asyncio.sleep(5)  
        
            os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data/{}.json'.format(guild.id)) 
            
            
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Eventos/data/{}.json'.format(guild.id)) in [True]:
            
            await asyncio.sleep(5) 
            
            os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Eventos/data/{}.json'.format(guild.id)) 
            

        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(guild.id)) in [True]:
            
            await asyncio.sleep(5) 
            
            os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(guild.id))
               
            
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(guild.id)) in [True]:
            
            await asyncio.sleep(5) 
            
            os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(guild.id)) 
            
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(guild.id)) in [True]:
            
            await asyncio.sleep(5)
            
            os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(guild.id))

        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(guild.id)) in [True]:

            await asyncio.sleep(5)

            os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(guild.id))
        
            
            
def setup(bot : commands.Bot):
    
    bot.add_cog(on_guild_remove(bot))                   