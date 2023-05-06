import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class purge(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'purge', description='Elimina mensajes de un canal.')
    async def purge(self, interaction : nextcord.Interaction, message_int : int = SlashOption(
        
        name= 'cantidad',
        description= 'Cantidad de mensajes a eliminar',
        required= True

    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            if message_int in [0]:
                
                embed_zero_purge = nextcord.Embed(
                    
                    title= '❌ | Purge Error',
                    description= 'No puedo eliminar {} mensajes 😠'.format(message_int),
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                    
                )
                
                embed_zero_purge.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
                embed_zero_purge.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                
                return await interaction.response.send_message(embed = embed_zero_purge)
            
            elif message_int >= 100:
                
                embed_max_purge = nextcord.Embed(
                    
                    title= '❌ | Purge Error',
                    description= 'No puedo eliminar más de 100 mensajes 😠',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                    
                )
                
                embed_max_purge.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
                embed_max_purge.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                
                return await interaction.response.send_message(embed = embed_max_purge)
            
            else:

                embed_delete_messages = nextcord.Embed(

                    title= '✅ | Purge',
                    description= 'Esta iniciando la purga de mensajes...',
                    color= nextcord.Colour.blue(),
                    timestamp= datetime.now()

                )

                embed_delete_messages.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                embed_delete_messages.set_footer(text='Creado por DevCheck#4611',
                                       icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                await interaction.response.send_message(embed= embed_delete_messages)

                messages_limit = await interaction.channel.history(limit= message_int).flatten()

                for message in messages_limit:

                    await asyncio.sleep(1)
                    await message.delete()

                embed_purge = nextcord.Embed(

                    title='✅ | Purge',
                    description='''

Autor: {}

Mensajes eliminados: **{}**                    

                                    '''.format(interaction.user.mention, len(messages_limit)),
                    color=nextcord.Colour.blue(),
                    timestamp=datetime.now()

                )

                embed_purge.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                embed_purge.set_footer(text='Creado por DevCheck#4611',
                                       icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                return await interaction.channel.send(embed = embed_purge)
                

                
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
    
    bot.add_cog(purge(bot))                              