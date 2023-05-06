import nextcord
import os
import json
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from datetime import datetime
from nextcord.ui import Button, View



class avatar(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
        
    @slash_command(name= 'avatar', description= 'Obtén el avatar de un usuario.')    
    async def avatar(self, interaction : nextcord.Interaction, usuario : nextcord.Member = SlashOption(
        
        name= 'usuario_del_avatar',
        description= 'Nombra a un usuario para obtener su avatar',
        required= False
        
    )):
        
        if usuario is None:
            
            usuario = interaction.user
            
        
        embed_avatar = nextcord.Embed(
            
            title= '✅ | Avatar',
            description= 'El avatar del usuario {}'.format(usuario.mention),
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
                
        )
        
        embed_avatar.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
        embed_avatar.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
        
        if usuario.avatar is not None:
            
            avatar_url = usuario.avatar
            
            embed_avatar.set_image(url= usuario.avatar)
            
        else:
            
            avatar_url = usuario.default_avatar
            
            embed_avatar.set_image(url= usuario.default_avatar)     
            
            
        button_avatar_url = Button(
            
            label= 'Avatar URL',
            style= nextcord.ButtonStyle.gray,
            url= '{}'.format(avatar_url)
            
        )  
        
        view = View()
        
        view.add_item(button_avatar_url)
        
        return await interaction.response.send_message(embed = embed_avatar, view= view)
    
    
def setup(bot : commands.Bot):
    
    bot.add_cog(avatar(bot))        
