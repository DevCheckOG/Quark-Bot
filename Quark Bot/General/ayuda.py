import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from datetime import datetime
from nextcord.ui import Button, View



class ayuda(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'ayuda', description= 'Visualiza mi panel de ayuda.')  
    async def ayuda(self, interaction : nextcord.Interaction):
        
        embed_help_bot = nextcord.Embed(
            
            title= '🐍 | Menú de Ayuda',
            description= 'Gracias por invitarme a su servidor, informate de mis comandos',
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
             
        ) 
        
        embed_help_bot.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
        embed_help_bot.set_footer(text= 'Creado por DevCheck#4611', icon_url= self.bot.user.avatar)
                    
        embed_help_bot.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
               
        options = [
            
            nextcord.SelectOption(label= '🛡️ | Moderación'),
            nextcord.SelectOption(label= '🐍 | Utilidades')
            
        ] 
        
        select_menu = nextcord.ui.Select(placeholder= 'Elige una Opción', min_values= 1, max_values= 1, options= options)  
        
        async def callback (interaction : nextcord.Interaction):
            
            if '🛡️ | Moderación' in select_menu.values:
                
                embed_mod = nextcord.Embed(
                    
                    title= '🛡️ | Moderación',
                    description= '''
                    
{} ¡Puedes leer todos los comandos 
y sus funciones! 

`/antibot` : Activa el sistema antibots.

`/ban` : Banea a un usuario del servidor.

`/unban` : Perdona el ban de un usuario.

`/kick` : Expulsa a alguien del servidor.

`/nuke` : Explota un canal.

`/blacklist` : Bloquea malas palabras/links en el servidor.

`/purge` : Elimina mensajes de un canal.

`/nick` : Cambia el nick de un usuario.

` => Proximamente más contenido en Arqui#9588 <= `
                   
                    '''.format(interaction.user.mention),
                    color= nextcord.Colour.blue(),
                    timestamp= datetime.now()
                    
                )  
                
                embed_mod.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                embed_mod.set_footer(text= 'Creado por DevCheck#4611', icon_url= self.bot.user.avatar)
                            
                embed_mod.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                
                return await interaction.response.send_message(embed= embed_mod, ephemeral= True)
            
            elif '🐍 | Utilidades' in select_menu.values:
                
                embed_util = nextcord.Embed(
                    
                    title= '🐍 | Utilidades',
                    description= '''
                    
{} ¡Puedes leer todos los comandos 
y sus funciones! 

`/ayuda` : Visualiza mi panel de ayuda.

`/calc` : Calcula cualquier número.

`/send` : Envia mensajes a cualquier canal del servidor.

`/invitame` : Invitame a tu servidor.

`/poll` : Crea encuentas personalizadas.

`/avatar` : Obtén el avatar de un usuario.

`/createfy` : Crea verificación personalizada.

`/createmd` : Crea embeds personalizados.

`/createtk` : Crea tickets personalizados.

`/autorole` : Autorol al entrar al servidor.

`/sendmd` : Envia un mensaje al MD de un usuario.

`/arqui` : Obtén una detallada información mía.

`/welcomes` : Envia un mensaje personalizdo cuando entre un usuario al servidor.

`/verify` : Activa el sistema de verificación por usuario.

`/code` : Código de verificación del MD.

` => Proximamente más contenido en Arqui#9588 <= `
                   
                    '''.format(interaction.user.mention),
                    color= nextcord.Colour.brand_green(),
                    timestamp= datetime.now()
                    
                )  
                
                embed_util.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                        
                embed_util.set_footer(text= 'Creado por DevCheck#4611', icon_url= self.bot.user.avatar)
                            
                embed_util.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                
                return await interaction.response.send_message(embed= embed_util, ephemeral= True)
            
        
        select_menu.callback = callback
        
        view = View(timeout= None)
        view.add_item(select_menu)      
        
        return await interaction.response.send_message(embed= embed_help_bot, view= view, ephemeral= True)  
    
    
def setup(bot : commands.Bot):
    
    bot.add_cog(ayuda(bot))           