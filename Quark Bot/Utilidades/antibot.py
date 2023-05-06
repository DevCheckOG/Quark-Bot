import json
import os
import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class antibot (commands.Cog):
    
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    
    @slash_command(name= 'antibot', description= 'Activa el sistema antibots.')
    async def antibot(self, interaction : nextcord.Interaction, status : str = SlashOption(
        
        name= 'activar_o_desactivar',
        description= 'Selecciona si quieres desactivarlo o activarlo',
        choices= ['🔵 Activar', '🔴 Desactivar']
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            match status:
                
                case '🔵 Activar':
            
                    if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(interaction.guild_id)) in [True]:
                        
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(interaction.guild_id), 'r') as read:
                            
                            config = json.load(read)
                            
                            config['ESTADO'] = True
                            
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(interaction.guild_id), 'w') as write:
                            
                            json.dump(config, write, indent= 3)
                            
                        write.close()
                        
                        embed_active_antibot_update = nextcord.Embed(
                            
                            title= '⚙️ | Antibot Update',
                            description= 'Se actualizo el antibot en **{}**'.format(status),
                            color= nextcord.Colour.yellow(),
                            timestamp= datetime.now()
                        
                        )   
                        
                        embed_active_antibot_update.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                        embed_active_antibot_update.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.response.send_message(embed= embed_active_antibot_update)
                    
                    else:
                        
                        ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/', '{}.json'.format(interaction.guild_id))
                        
                        with open(ruta, 'w') as write:
                            
                            dict_antibot = {
                                
                                'ESTADO' : True    
                                
                            }
                            
                            json.dump(dict_antibot, write, indent= 3)
                            
                        write.close()
                        
                        embed_active_antibot = nextcord.Embed(
                            
                            title= '✅ | Antibot Create',
                            description= 'Se configuro el antibot en **{}**'.format(status),
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                        
                        )   
                        
                        embed_active_antibot.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                        embed_active_antibot.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.response.send_message(embed= embed_active_antibot)
                    
                case '🔴 Desactivar':
                    
                    if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(interaction.guild_id)) in [True]:
                        
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(interaction.guild_id), 'r') as read:
                            
                            config = json.load(read)
                            
                            config['ESTADO'] = False
                            
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(interaction.guild_id), 'w') as write:
                            
                            json.dump(config, write, indent= 3)
                            
                        write.close()
                        
                        embed_disable_antibot_update = nextcord.Embed(
                            
                            title= '✅ | Antibot Disable',
                            description= 'Se actualizo el antibot en **{}**'.format(status),
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                        
                        )   
                        
                        embed_disable_antibot_update.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                        embed_disable_antibot_update.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.response.send_message(embed= embed_disable_antibot_update)
                    
                    else:
                        
                        ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/', '{}.json'.format(interaction.guild_id))
                        
                        with open(ruta, 'w') as write:
                            
                            dict_antibot = {
                                
                                'ESTADO' : False    
                                
                            }
                            
                            json.dump(dict_antibot, write, indent= 3)
                            
                        write.close()
                        
                        embed_disable_create_antibot = nextcord.Embed(
                            
                            title= '✅ | Antibot Disable',
                            description= 'Se configuro el antibot en **{}**'.format(status),
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                        
                        )   
                        
                        embed_disable_create_antibot.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                        embed_disable_create_antibot.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.response.send_message(embed= embed_disable_create_antibot)
                    
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
    
    bot.add_cog(antibot(bot))            
        
             