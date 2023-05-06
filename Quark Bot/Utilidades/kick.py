import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class kick(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    
    @slash_command(name= 'kick', description= 'Expulsa a alguien del servidor.')
    async def kick(self, interaction : nextcord.Interaction, user : nextcord.Member = SlashOption(
        
        name= 'usuario_a_expulsar',
        description= 'Nombra el usuario a expulsar',
        required= True
           
    ),
                   
                   
    reason : str = SlashOption(
        
        name= 'razón_de_la_expulsión',
        description= 'Razón del la expulsión',
        required= False
        
    )):
            
        if interaction.user.guild_permissions.administrator in [True]:
            
            if reason in [None]:
            
                reason = 'No especifico una razón' 
            
            if user in [interaction.user] or user in [self.bot.user]:
                
                embed_no_kick_error = nextcord.Embed(
                    
                    title= '❌ | Kick error',
                    description= 'No puedes expulsarme o expulsarte 😠',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                       
                )
                
                embed_no_kick_error.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                
                embed_no_kick_error.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                
                return await interaction.response.send_message(embed = embed_no_kick_error)
            
            else:
                    
                embed_kick = nextcord.Embed(
                        
                    title= '✅ | Kick',
                    description= '''
                        
Usuario: 
{}

Autor:
{}

Razón:
**{}**                
                        
                    '''.format(user.mention, interaction.user.mention, reason),
                    color= nextcord.Colour.blue(),
                    timestamp= datetime.now()
                           
                )
                    
                embed_kick.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                            
                embed_kick.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                    
                if user.avatar is not None:
                        
                    embed_kick.set_thumbnail(url = user.avatar)
                        
                else:
                        
                    embed_kick.set_thumbnail(url= user.default_avatar) 
                    
                try:    
                    
                    await user.kick(reason= reason)  
                    
                except:
                    
                    embed_kick_error = nextcord.Embed(
                    
                        title= '❌ | Kick error',
                        description= 'No puedo expulsar a ese usuario, el tiene un rol más alto',
                        color= nextcord.Colour.red(),
                        timestamp= datetime.now()
                       
                    )
                
                    embed_kick_error.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                    
                    embed_kick_error.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                    
                    return await interaction.response.send_message(embed = embed_kick_error)
                    
                return await interaction.response.send_message(embed = embed_kick)        
        
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
    
    bot.add_cog(kick(bot))                                   