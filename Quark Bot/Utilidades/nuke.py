import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime

class nuke(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        

    @slash_command(name= 'nuke', description= 'Explota un canal.') 
    async def nuke(self, interaction : nextcord.Interaction, canal : nextcord.TextChannel = SlashOption(
        
        name= 'canal_a_explotar',
        description= 'Nombra el canal a explotar',
        required= False,
        default= None

    )):
        
        
        if interaction.user.guild_permissions.administrator in [True]:
        
            try:
                
                if canal in [None]:
                
                    channel_clone = await interaction.channel.clone()
                    await asyncio.sleep(1)
                    await channel_clone.edit(position = interaction.channel.position)
                    
                    embed_nuke = nextcord.Embed(
                
                        title= '✅ | Nuke',
                        description= '{} exploto el canal **{}**'.format(interaction.user.mention, channel_clone.mention),
                        timestamp= datetime.now(),
                        color= nextcord.Colour.blue()
                
                    )    
            
                    embed_nuke.set_image(url = 'https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif')
                    
                    embed_nuke.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                                
                    embed_nuke.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                    
                    await channel_clone.send(embed = embed_nuke)
                    return await interaction.channel.delete()
                
                else:
                    
                    channel_clone = await canal.clone()
                    await channel_clone.edit(position = canal.position)
                    
                    embed_nuke_response = nextcord.Embed(
                        
                        title= '✅ | Nuke',
                        description= 'Exploto el canal **{}**'.format(channel_clone.mention),
                        color= nextcord.Colour.blue(),
                        timestamp= datetime.now()
                        
                    )
                    
                    embed_nuke_response.set_image(url = 'https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif')
            
                    embed_nuke_response.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                                
                    embed_nuke_response.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                            
                    await interaction.response.send_message(embed= embed_nuke_response)
                    return await canal.delete()
            
            except:

                await channel_clone.delete()
                
                embed_error_nuke = nextcord.Embed(
                    
                    title= '❌ | Nuke Error',
                    description= 'No puedo explotar canales requeridos por Discord 😑',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                    
                )
                
                embed_error_nuke.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                embed_error_nuke.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                
                return await interaction.response.send_message(embed = embed_error_nuke)
        
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
    
    bot.add_cog(nuke(bot))    