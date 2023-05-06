import nextcord
from nextcord.ext import commands
from nextcord import slash_command
from nextcord.ui import Button, View
from datetime import datetime


class invitame(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        self.bot = bot
        
        
    @slash_command(name= 'invitame', description= 'Invitame a tu servidor.')
    async def invitame(self, interaction : nextcord.Interaction):
        
        embed_invitame = nextcord.Embed(
            
            title= '✅ | Invitame',
            description= '''

Puedes invitarme por medio del link:       
__[Invitación](https://discord.com/api/oauth2/authorize?client_id=1079159577473462312&permissions=8&scope=bot)__
            
            ''',
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
            
        ) 
        
        embed_invitame.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
        embed_invitame.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
        
        button_invitame = Button(
            
            label= 'Soporte',
            emoji= '⚙️',
            style= nextcord.ButtonStyle.gray,
            url= 'https://discord.gg/Gs5FwKHTCW'
        
        )
        
        view = View()
        
        view.add_item(button_invitame)
        
        return await interaction.response.send_message(embed = embed_invitame, ephemeral= True, view= view)  
    
    
    
    
def setup(bot : commands.Bot):
    
    bot.add_cog(invitame(bot))    