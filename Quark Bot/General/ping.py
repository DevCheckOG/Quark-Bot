import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class ping(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
        
    @slash_command(name= 'ping', description= 'Visualiza el Ping del bot.')
    async def ping(self, interaction : nextcord.Interaction):
        
        embed_ping = nextcord.Embed(
            
            title= '✅ | Ping',
            description= '`¡Pong!` **{}ms**'.format(round(self.bot.latency, 1)),
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
            
        )    
        
        embed_ping.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
        embed_ping.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
        
        return await interaction.response.send_message(embed= embed_ping) 
    
    
def setup(bot: commands.Bot):
    bot.add_cog(ping(bot))        