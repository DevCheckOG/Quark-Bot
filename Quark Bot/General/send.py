import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from datetime import datetime
from nextcord.ui import Button, View



class send(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot


    @slash_command(name= 'send', description= 'Envia mensajes a cualquier canal del servidor.')   
    async def send(self, interaction : nextcord.Interaction, id_message : str = SlashOption(
        
        name= 'id_del_mensaje',
        description= 'ID del mensaje a enviar',
        required= True
        
    ),
                   
    channel_origin : nextcord.TextChannel = SlashOption(
        
        name= 'canal_de_origen',
        description= 'Canal dónde se encuentra el mensaje',
        required= True
        
    ),
                   
    channel_send : nextcord.TextChannel = SlashOption(
        
        name= 'canal_a_enviar',
        description= ' Canal a dónde se va enviar el mensaje',
        required= True
    
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
        
            try:
                
                if id_message.isnumeric() in [True]:
                    
                    id_message_convert = int(id_message)
                    embed_search = await channel_origin.fetch_message(id_message_convert)
                    
                    try:
                        
                        embed_extract = embed_search.embeds[0]
                        
                        channel_get_send = self.bot.get_channel(channel_send.id)
                    
                        await channel_get_send.send(embed = embed_extract)
                        
                    except:
                        
                        message_extract = embed_search.content    

                        channel_get_send = self.bot.get_channel(channel_send.id)
                    
                        await channel_get_send.send(content = '{}'.format(message_extract))
                    
                    embed_send_complete = nextcord.Embed(
                        
                        title= '✅ | Send',
                        description= 'Se envio correctamente el mensaje **{}** al canal {}'.format(embed_search.id, channel_get_send.mention),
                        color= nextcord.Colour.blue(),
                        timestamp= datetime.now()
                        
                    )
                    
                    embed_send_complete.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                    
                    embed_send_complete.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                    
                    return await interaction.response.send_message(embed= embed_send_complete)
                    
                else:
                    
                    embed_send_err = nextcord.Embed(
                        
                        title= '❌ | Send error',
                        description= 'No puedes escribir palabras en el ID 😠',
                        color= nextcord.Colour.red(),
                        timestamp= datetime.now()
                        
                    )
                    
                    embed_send_err.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                    
                    embed_send_err.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                    
                    return await interaction.response.send_message(embed= embed_send_err)
                
            except:
                
                embed_not_found_message = nextcord.Embed(
                    
                    title= '❌ | Send error',
                    description= 'No pude encontrar en mensaje, asegurese de seguir bien los pasos 😕',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                        
                )    
                
                embed_not_found_message.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                    
                embed_not_found_message.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                    
                return await interaction.response.send_message(embed= embed_not_found_message)
    
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
    
    bot.add_cog(send(bot))                  