import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime

class arqui(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'arqui', description= 'Obtén una detallada información mía.') 
    async def arqui (self, interaction : nextcord.Interaction):
        
        creador = await self.bot.fetch_user(984246896975552523)
        
        lista_member = []
        
        total_members = 0
        
        for guild in self.bot.guilds:
            
            total_members += guild.member_count
            
        lista_member.append(str(total_members))    
        
        embed_arqui = nextcord.Embed(
            
            title= '✅ | Arqui',
            description= '''
            
`Creador:` {}   

`Nombre:` **{}**

`ID:` **{}**         
            
`Servidores:` **{}**

`Miembros:` **{}**

`Versión:` **v0.99**

`Soporte:` [Soporte de Arqui](https://discord.gg/Gs5FwKHTCW)

`Source Code (Open Source):` [Código Fuente](https://github.com/DevCheckOG/Arqui-Bot)
 
`Libreria:` **NextCord**            
            
            '''.format(creador.mention, self.bot.user.name, self.bot.user.id, len(self.bot.guilds), lista_member[0]),
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
            
        )
        
        embed_arqui.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
        embed_arqui.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
        
        embed_arqui.set_thumbnail(url= self.bot.user.avatar)
        
        return await interaction.response.send_message(embed= embed_arqui)
    
def setup(bot : commands.Bot):
    
    bot.add_cog(arqui(bot))                    
                          
           
