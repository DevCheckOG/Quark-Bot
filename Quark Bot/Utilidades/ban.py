import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class ban (commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'ban', description= 'Banea a un usuario del servidor.')  
    async def ban (self, interaction : nextcord.Interaction, user : nextcord.Member = SlashOption(
        
        name= 'usuario_a_banear',
        description= 'Nombra el usuario de banear',
        required= True        
        
    ),  
                   
    elimate_message : str = SlashOption(
        
        name= 'mensajes_a_eliminar',
        description= 'Elimina los mensajes del usuario',
        required= False,
        choices= ['🟢 1 día', '🟢 2 días', '🟢 3 días', '🟡 4 días', '🟡 5 días', '🔴 6 días', '🔴 7 días']
        
    ),                      
                   
    reason : str = SlashOption(
        
        name= 'razón_del_baneo',
        description= 'Razón del baneo de usuario',
        required= False
        
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            
            embed_ban_error = nextcord.Embed(
                                
                title= '❌ | Ban error',
                description= 'No puedo banear a ese usuario, el tiene un rol más alto',
                color= nextcord.Colour.red(),
                timestamp= datetime.now()
                        
            )
                    
            embed_ban_error.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                                
            embed_ban_error.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
            
            
            if elimate_message in [None]:
                    
                try:
                    
                    await user.ban(reason= reason)
                    elimate_message = 'Ninguno'
                        
                except:
                        
                    return await interaction.response.send_message(embed = embed_ban_error)
            
        
            if reason in [None]:
                
                reason = 'No especifico una razón'
                
            if user in [interaction.user] or user in [self.bot.user]:
                
                embed_user_or_bot = nextcord.Embed(
                    
                    title= '❌ | Ban error',
                    description= 'No puedes banearme o banearte 😠',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()                    
                    
                )
                
                embed_user_or_bot.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                embed_user_or_bot.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                
                return await interaction.response.send_message(embed = embed_user_or_bot)
            
            else:
                
                embed_ban_hammer = nextcord.Embed(
                    
                    title= '✅ | Ban',
                    description= '''
                 
Usuario: {} 

Autor: {}

Tiempo de mensajes eliminados: **{}**

Razón: **{}**                
                
                    '''.format(user.mention, interaction.user.mention, elimate_message, reason),
                    color= nextcord.Colour.blue(),
                    timestamp= datetime.now()
                    
                )
                
                if user.avatar is not None:
                    
                    embed_ban_hammer.set_thumbnail(url = user.avatar)
                    
                else:
                    
                    embed_ban_hammer.set_thumbnail(url = user.default_avatar)    
                
                
                embed_ban_hammer.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                embed_ban_hammer.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                           
                match elimate_message:
                    
                    case '🟢 1 día':
                        
                        try: 
                               
                            await user.ban(reason= reason, delete_message_days= 1)
                        
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                            
                            
                    
                    case '🟢 2 días':
                        
                        try:
                            
                            await user.ban(reason= reason, delete_message_days= 2)
                            
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                    
                    case '🟢 3 días':
                        
                        try:
                            
                            await user.ban(reason= reason, delete_message_days= 3)
                            
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                    
                    case '🟡 4 días':
                        
                        try:
                            
                            await user.ban(reason= reason, delete_message_days= 4)
                            
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                    
                    case '🟡 5 días':
                        
                        try:
                        
                            await user.ban(reason= reason, delete_message_days= 5)
                            
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                    
                    case '🔴 6 días':
                        
                        try:
                        
                            await user.ban(reason= reason, delete_message_days= 6)
                            
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                    
                    case '🔴 7 días':
                        
                        try:
                            
                            await user.ban(reason= reason, delete_message_days= 7)
                            
                        except:
                            
                            return await interaction.response.send_message(embed = embed_ban_error)
                    
            return await interaction.response.send_message(embed = embed_ban_hammer)        
                        
                        
                
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
    
    bot.add_cog(ban(bot))                       