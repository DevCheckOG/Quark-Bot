import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class createdm(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'create-dm', description= 'Envia un mensaje al DM de un usuario.')
    async def createdm(self, interaction : nextcord.Interaction, usuario : nextcord.Member = SlashOption(
        
        name= 'usuario_del_md',
        description= 'Nombra el usuario a enviar el mensaje',
        required= True
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            class MD(nextcord.ui.Modal):
                
                def __init__ (self):
                    
                    super().__init__(
                        
                        title= '✅ | Create-DM'
                        
                    )
                    
                    self.text = nextcord.ui.TextInput(
                        
                        label= 'Mensaje',
                        required= True,
                        placeholder= 'Escriba el mensaje a enviar al usuario',
                        min_length= 1,
                        max_length= 3000,
                        style= nextcord.TextInputStyle.paragraph
                        
                    )
                    
                    self.add_item(self.text)
                    
                async def callback(self, interaction: nextcord.Interaction) -> None:
                    
                    user = interaction.guild.get_member(usuario.id)
                
                    mensaje = self.text.value
                    
                    embed_md = nextcord.Embed(
                        
                        title= '✅ | Mensaje',
                        description= '''
                        
Servidor: `{}`

Notificador: {}                        
                        
Mensaje:

**{}**                        
                    
                        '''.format(interaction.guild.name, interaction.user.mention, mensaje),
                        color= nextcord.Colour.blue(),
                        timestamp= datetime.now()   
                    
                    )
  
                    embed_md.set_footer(text= 'Mensaje enviado por {}'.format(interaction.user), icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                    
                    if interaction.guild.icon is not None:
                        
                        embed_md.set_thumbnail(url= interaction.guild.icon)
                        
                    else:
                        
                       embed_md.set_thumbnail(url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')    
                       
                    try:   
                        
                        channel_dm = user.dm_channel
                            
                        if channel_dm in [None]:
                                
                            channel_dm = await user.create_dm()
                        
                        await channel_dm.send(embed= embed_md) 
                        
                    except:
                        
                        embed_error_md = nextcord.Embed(
                            
                            title= '❌ | Create-DM',
                            description= 'El usuario {} tiene el md bloqueado'.format(user.mention),
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                            
                        )    
                        
                        embed_error_md.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                    
                        return await interaction.send(embed= embed_error_md)
                    
                    else:
                    
                        embed_md_finish = nextcord.Embed(
                            
                            title= '✅ | Create-DM',
                            description= 'Se le envio el mensaje al MD del usuario {}'.format(user.mention),
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                            
                        )   
                        
                        embed_md_finish.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.send(embed= embed_md_finish)
                
            modal = MD()    
                
            return await interaction.response.send_modal(modal= modal)        
        
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
            
            return await interaction.response.send_message(embed = embed_noperms, view= view)
        
        
def setup(bot : commands.Bot):
    
    bot.add_cog(createdm(bot))            
            