import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class unban(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'unban', description='Perdona el ban de un usuario.')
    async def unban(self, interaction : nextcord.Interaction, user : str = SlashOption(
        
        name= 'usuario_a_desbanear',
        description= 'ID del usuario de desbanear',
        required= True
        
    ),
                    
    reason : str = SlashOption(
        
        name= 'razón_del_desbaneo',
        description= 'Razón del desbaneo',
        required= False,
        default= None
        
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            if reason == None:
                
                reason = 'No especifico una razón'
                
            
            if user.isnumeric() == True:
            
                if user in [interaction.user.id] or user in [self.bot.user.id]:
                    
                    embed_no_admited_unban = nextcord.Embed(
                        
                        title= '❌ | Unban error',
                        description= 'Deberias no poder desbanearte o desbanearme 😂',
                        color= nextcord.Colour.red(),
                        timestamp= datetime.now()
                        
                    )
                    
                    embed_no_admited_unban.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                            
                    embed_no_admited_unban.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                    
                    return await interaction.response.send_message(embed= embed_no_admited_unban)
                
                else:
                    
                    unban_user = await self.bot.self_user(int(user))
                    
                    if unban_user is not None:
                    
                        embed_unban = nextcord.Embed(
                            
                            title= '✅ | Unban',
                            description= '''
                            
`Usuario:` 
{}

`Autor:`
{}

`Razón:`
**{}**                
                            
                            '''.format(unban_user.mention, interaction.user.mention, reason),
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                            
                            
                        )
                        
                        embed_unban.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                                
                        embed_unban.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                        
                        if unban_user.avatar is not None:
                            
                            embed_unban.set_thumbnail(url = unban_user.avatar)
                            
                        else:
                            
                            embed_unban.set_thumbnail(url= unban_user.default_avatar)    
                        
                        try:
                            
                            await interaction.guild.unban(unban_user, reason= reason) 
                            
                        except:
                            
                            embed_error_unban = nextcord.Embed(
                                
                                title= '❌ | Unban error',
                                description= 'El usuario {} no esta baneado'.format(unban_user.mention),
                                color= nextcord.Colour.red(),
                                timestamp= datetime.now()
                                
                            )   
                            
                            embed_error_unban.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                                
                            embed_error_unban.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                                
                            return await interaction.response.send_message(embed= embed_error_unban)
                            
                                        
                        return await interaction.response.send_message(embed= embed_unban)
                    
                    else:
                        
                        embed_error_unban_error_member = nextcord.Embed(
                            
                            title= '❌ | Unban',
                            description= 'El usuario no existe'.format(unban_user.mention),
                            color= nextcord.Colour.red(),
                            timestamp= datetime.now()
                            
                        )
                        
                        embed_error_unban_error_member.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                                
                        embed_error_unban_error_member.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                                
                        return await interaction.response.send_message(embed= embed_error_unban_error_member)
                    
                
            else:
                
                embed_error_unban_id = nextcord.Embed(
                    
                    title= '❌ | Unban error',
                    description= 'Ey!, No escribas palabras en el ID 😠',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()
                    
                )
                
                embed_error_unban_id.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)   
                            
                embed_error_unban_id.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                                    
                return await interaction.response.send_message(embed= embed_error_unban_id)
            
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
    
    bot.add_cog(unban(bot))                               
                    
            
              
                
            
                 