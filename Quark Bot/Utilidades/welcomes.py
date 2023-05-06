import json
import os
import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class welcomes(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'welcomes', description= 'Envia un mensaje personalizdo cuando entre un usuario al servidor.')
    async def welcomes(self, interaction : nextcord.Interaction, status : str = SlashOption(
        
        name= 'activar_o_desactivar',
        description= 'Elige si activas o desactivas el sistema',
        required= True,
        choices= ['🟢 Activar', '🔴 Desactivar']
        
    ),
                                     
    canal_welcome : nextcord.TextChannel = SlashOption(
        
        name= 'canal_de_bienvenidas',
        description= 'Nombra el canal donde se va enviar el mensaje',
        required= True
          
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            match status:
                
                case '🟢 Activar':
                    
                    class SetupWelcome(nextcord.ui.Modal):
                        
                        def __init__ (self):
                            
                            super().__init__(
                                
                                title= '✅ | Welcomes'
                                
                            )
                            
                            self.titulo = nextcord.ui.TextInput(
                                
                                label= 'Titulo',
                                required= True,
                                min_length= 1,
                                max_length= 100,
                                placeholder= 'Escribe el titulo del mensaje, variables = {name}'
                                
                            )
                            
                            self.add_item(self.titulo)
                            
                            self.desc = nextcord.ui.TextInput(
                                
                                label= 'Descripción',
                                required= True,
                                min_length= 1,
                                max_length= 3000,
                                placeholder= 'Escribe la descripción del mensaje, variables = {mention}, {name}, {channel.ID}',
                                style= nextcord.TextInputStyle.paragraph
                                
                            )
                            
                            self.add_item(self.desc)
                            
                            self.color = nextcord.ui.TextInput(
                                
                                label= 'Color',
                                required= True,
                                min_length= 1,
                                max_length= 100,
                                placeholder= 'Azul, Verde, Rojo, Oro, Random'
                            
                            )
                            
                            self.add_item(self.color)
                            
                            self.img = nextcord.ui.TextInput(
                                
                                label= 'Imagen',
                                required= False,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe un Link de imagen para el mensaje'
                                
                            )
                            
                            self.add_item(self.img)
                            
                        async def callback(self, interaction: nextcord.Interaction) -> None:
                            
                            titulo = self.titulo.value
                            desc = self.desc.value
                            color = self.color.value
                            img = self.img.value
                            
                            if img == '':
                                            
                                img = None
                            
                            if color in ['Azul', 'Verde', 'Rojo', 'Oro', 'Random']:
                            
                                if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(interaction.guild_id)) in [True]:
                                    
                                    with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(interaction.guild_id), 'r') as read:
                                        
                                        config = json.load(read)
                                        config['STATUS'] = True
                                        config['CANAL'] = canal_welcome.id
                                        config['Titulo'] = '{}'.format(titulo)
                                        config['desc'] = '{}'.format(desc)
                                        config['color'] = '{}'.format(color)
                                        config['img'] = img
                                        
                                        
                                    with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(interaction.guild_id), 'w') as write:
                                        
                                        json.dump(config, write, indent= 8)
                                        
                                    write.close()  
                                    
                                    embed_update_welcome = nextcord.Embed(
                                        
                                        title= '⚙️ | Welcomes Update',
                                        description= 'Se actualizo los datos del sistema de bienvenidas',
                                        color= nextcord.Colour.yellow(),
                                        timestamp= datetime.now()
                                    
                                    )  
                                    
                                    embed_update_welcome.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                    
                                    if interaction.guild.icon is not None:
                                        
                                        embed_update_welcome.set_thumbnail(url= interaction.guild.icon)
                                        
                                    return await interaction.send(embed= embed_update_welcome)    
                                
                                else:
                                    
                                    ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/', '{}.json'.format(interaction.guild_id))
                                    
                                    with open(ruta, 'w') as write:
                                        
                                        dict_embed_welcome = {
                                            
                                            'STATUS' : True,
                                            'CANAL' : canal_welcome.id,
                                            'Titulo' : '{}'.format(titulo),
                                            'desc' : '{}'.format(desc),
                                            'color' : '{}'.format(color),
                                            'img' : img 
                                            
                                        }
                                        
                                        json.dump(dict_embed_welcome, write, indent= 8)
                                        
                                    write.close() 
                                    
                                    embed_create_welcome = nextcord.Embed(
                                        
                                        title= '✅ | Welcomes Create',
                                        description= 'Se establecio el sistema de bienvenidas en el canal que indicaste.',
                                        color= nextcord.Colour.blue(),
                                        timestamp= datetime.now()
                                        
                                    )   
                                    
                                    embed_create_welcome.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                    
                                    if interaction.guild.icon is not None:
                                        
                                        embed_create_welcome.set_thumbnail(url= interaction.guild.icon)    
                                
                                    return await interaction.send(embed = embed_create_welcome)
                            
                            else:
                                
                                embed_color_invalid = nextcord.Embed(
                                    
                                    title= '❌ | Welcomes Error',
                                    description= 'Debes escribir un color válido',
                                    color= nextcord.Colour.red(),
                                    timestamp= datetime.now()
                                    
                                )            
                        
                                embed_color_invalid.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                
                                return await interaction.send(embed = embed_color_invalid)
                    
                    modal = SetupWelcome()
                    
                    return await interaction.response.send_modal(modal= modal)        
                            
                case '🔴 Desactivar':
                    
                    if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(interaction.guild_id)) in [True]:
                        
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(interaction.guild_id), 'r') as read:
                            
                            config = json.load(read)
                            config['STATUS'] = False
                            config['CANAL'] = False
                            config['Titulo'] = False
                            config['desc'] = False
                            config['color'] = False
                            config['img'] = None
                            
                        with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(interaction.guild_id), 'w') as write:
                        
                
                            json.dump(config, write, indent= 8)
                            
                        write.close()   
                            
                        embed_disable_welcome = nextcord.Embed(
                            
                            title= '✅ | Welcome Disable',
                            description= 'Se desactivo el sistema de Bienvenidas en el servidor',
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                    
                        )   
                        
                        embed_disable_welcome.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
                        embed_disable_welcome.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.send(embed= embed_disable_welcome) 
                            
                    else:
                        
                        embed_no_existed_welcome = nextcord.Embed(
                            
                            title= '❌ | Welcome Error',
                            description= 'Para desactivar el sistema de Bienvenidas debes crear uno como mínimo',
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                        
                        )           
                            
                        embed_no_existed_welcome.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
                        embed_no_existed_welcome.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                        
                        return await interaction.send(embed= embed_no_existed_welcome)
                            
                 
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
    
    bot.add_cog(welcomes(bot))                               
                                 