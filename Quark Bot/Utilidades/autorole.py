import nextcord
import os
import json
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from datetime import datetime
from nextcord.ui import Button, View



class autorole(commands.Cog):
    
    def __init__(self, bot : commands.Bot):
        
        self.bot = bot
        
        
    @slash_command(name= 'autorole', description= 'Autorol al entrar al servidor.')
    async def autorole(self, interaction : nextcord.Interaction, activar : str = SlashOption(
        
        name= 'activar_o_desactivar',
        description= 'Activa o desactiva el autorole',
        required= True,
        choices= ['🟢 Activar', '🔴 Desactivar']  
        
    ), 
    
    tipo : str = SlashOption(
        
        name= 'tipo_de_autorol',
        description= 'Selecciona el tipo de autorol',
        required= True,
        choices= ['🤖 Bots', '🙃 Usuarios']
         
    ),
                       
    rol_asignar : nextcord.Role = SlashOption(
        
        name= 'rol_a_asignar',
        description= 'Nombra el rol a asignar',
        required= True
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            
            match activar:
                
                case '🟢 Activar':
            
                    match tipo:
                        
                        case '🤖 Bots':
                            
                            if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id)) in [True]:
                            
                                with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id), 'r') as read:
                                    
                                    config = json.load(read)
                                    
                                    config['BOT_ROLE'] = rol_asignar.id
                                    config['ACTIVATE'] = True
                                    
                                with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id), 'w') as write:
                                    
                                    json.dump(config, write, indent= 6)    
                                    
                                write.close()
                                
                                embed_update_set_role_bot = nextcord.Embed(
                                    
                                    title= '⚙️ | Autorole Update',
                                    description= 'Ahora cuando entren Bots, se les asignará el rol que indicaste.',
                                    color= nextcord.Colour.yellow(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                                embed_update_set_role_bot.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                                embed_update_set_role_bot.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                
                                return await interaction.response.send_message(embed= embed_update_set_role_bot)
                            
                            else:
                                
                                ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/', '{}.json'.format(interaction.guild_id))
                                
                                with open(ruta, 'w') as write:
                                    
                                    dict_roles = {
                                        
                                        'ACTIVATE' : True,
                                        'BOT_ROLE' : rol_asignar.id,
                                        'USER_ROLE' : False 
                                    
                                    }
                                    
                                    json.dump(dict_roles, write, indent= 6)
                                    
                                write.close()
                                
                                embed_create_set_role_bot = nextcord.Embed(
                                    
                                    title= '✅ | Autorole Create',
                                    description= 'Ahora cuando entren Bots, se les asignará el rol que indicaste.',
                                    color= nextcord.Colour.blue(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                                embed_create_set_role_bot.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                                embed_create_set_role_bot.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                
                                return await interaction.response.send_message(embed= embed_create_set_role_bot)
                            
                        case '🙃 Usuarios':
                            
                            if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id)) in [True]:
                            
                                with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id), 'r') as read:
                                    
                                    config = json.load(read)
                                    
                                    config['USER_ROLE'] = rol_asignar.id
                                    config['ACTIVATE'] = True
                                    
                                with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id), 'w') as write:
                                    
                                    json.dump(config, write, indent= 6)    
                                    
                                write.close()
                                
                                embed_update_set_role_user = nextcord.Embed(
                                    
                                    title= '⚙️ | Autorole Update',
                                    description= 'Ahora cuando entren Usuarios, se les asignará el rol que indicaste.',
                                    color= nextcord.Colour.yellow(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                                embed_update_set_role_user.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                                embed_update_set_role_user.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                
                                return await interaction.response.send_message(embed= embed_update_set_role_user)
                            
                            else:
                                
                                ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/', '{}.json'.format(interaction.guild_id))
                                
                                with open(ruta, 'w') as write:
                                    
                                    dict_roles = {
                                        
                                        'ACTIVATE' : True,
                                        'BOT_ROLE' : False,
                                        'USER_ROLE' : rol_asignar.id 
                                    
                                    }
                                    
                                    json.dump(dict_roles, write, indent= 6)
                                    
                                write.close()
                                
                                embed_create_set_role_user = nextcord.Embed(
                                    
                                    title= '✅ | Autorole Create',
                                    description= 'Ahora cuando entren Usuarios, se les asignará el rol que indicaste.',
                                    color= nextcord.Colour.blue(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                                embed_create_set_role_user.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                                embed_create_set_role_user.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                
                                return await interaction.response.send_message(embed= embed_create_set_role_user)
                            
                case '🔴 Desactivar':
                    
                    if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id)) in [True]:
                            
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(interaction.guild_id), 'w') as write:
                            
                            dict_roles = {
                                        
                                'ACTIVATE' : False,
                                'BOT_ROLE' : False,
                                'USER_ROLE' : False
                                    
                            }
                                    
                            json.dump(dict_roles, write, indent= 6)
                                    
                        write.close()
                        
                        embed_desactivate_autorol = nextcord.Embed(
                            
                            title= '✅ | Autorole Disable',
                            description= 'Se desactivo el sistema autorol',
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                            
                        )
                        
                        embed_desactivate_autorol.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                        embed_desactivate_autorol.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                
                        return await interaction.response.send_message(embed= embed_desactivate_autorol)
                            
                    else:
                        
                        embed_no_created_autorole = nextcord.Embed(
                            
                            title= '❌ | Autorole Error',
                            description= 'Debes crear almenos un autorol para desactivar el sistema autorol',
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                              
                        )
                        
                        embed_no_created_autorole.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                        embed_no_created_autorole.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                
                        return await interaction.response.send_message(embed= embed_no_created_autorole)
                    
                    
        else:
            
            embed_noperms = nextcord.Embed(
                
                title= '❌ | SIN PERMISOS',
                description= 'No tienes permisos suficientes para utilizar este comando.',
                color= nextcord.Colour.red(),
                timestamp= datetime.now()
                
            )    
            
            if interaction.user.avatar is not None:
                
                embed_noperms.set_author(name= '{}'.format(interaction.user), icon_url= interaction.user.avatar)
                
            else:
                
                embed_noperms.set_author(name= '{}'.format(interaction.user), icon_url= interaction.user.default_avatar)   
                
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
    
    bot.add_cog(autorole(bot))                