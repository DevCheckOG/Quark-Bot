import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime


class nick(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'nick', description= 'Cambia el nick de un usuario.')
    async def nick(self, interaction : nextcord.Interaction, 
                               
    nick : str = SlashOption(
        
        name= 'nuevo_nick',
        description= 'Escriba el nuevo Nick',
        required= True
        
    ),
                   
    usuario : nextcord.Member = SlashOption(
        
        name= 'usuario_del_nick',
        description= 'Nombra el usuario ha cambiar el nick',
        required= False
        
    )):
        
        if interaction.user.guild_permissions.manage_nicknames in [True]:
            
            if usuario in [None]:
                
                usuario = interaction.user
                
            try:
                    
                after_nick = await usuario.edit(nick= nick) 
                
            except:
                
                embed_error_edit = nextcord.Embed(
                    
                    title= '❌ | Nick Error',
                    description= 'El usuario tiene un rol más alto que el mio',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                     
                )      
                
                embed_error_edit.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
                embed_error_edit.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                
                return await interaction.response.send_message(embed= embed_error_edit)
                
            embed_edit_nick = nextcord.Embed(
                
                title= '✅ | Nick',
                description= '''
                
                
Autor: {}

Usuario: {}              
                
Nombre nuevo: **{}**                                
                
                '''.format(interaction.user.mention, usuario.mention, after_nick.nick),
                color= nextcord.Colour.blue(),
                timestamp= datetime.now()
                
            )        
            
            embed_edit_nick.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
            embed_edit_nick.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
            
            if usuario.avatar is not None:
                
                embed_edit_nick.set_thumbnail(url= usuario.avatar)
                
            else:
                
                embed_edit_nick.set_thumbnail(url= usuario.default_avatar)    
            
            return await interaction.response.send_message(embed= embed_edit_nick) 
            
        else:
                
            embed_noperms = nextcord.Embed(
                
                title= '❌ | SIN PERMISOS',
                description= 'No tienes permisos suficientes para utilizar este comando.',
                color= nextcord.Colour.red(),
                timestamp= datetime.now()
                
            )    
            
                  
            embed_noperms.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
            embed_noperms.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
            
            
            button_noperms = Button(
                
                label= 'Soporte',
                emoji= '⚙️',
                style= nextcord.ButtonStyle.gray,
                url= 'https://discord.gg/Gs5FwKHTCW'
                
            )
            
            view = View()
            view.add_item(button_noperms)
            
            return await interaction.response.send_message(embed = embed_noperms, view= view ,ephemeral= True)
        

def setup(bot : commands.Bot):
    
    bot.add_cog(nick(bot))    