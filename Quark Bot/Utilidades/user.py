import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime




class user(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot  
        
        
    @slash_command(name= 'user', description= 'Obtén la información de un usuario.') 
    async def user (self, interaction : nextcord.Interaction, usuario : nextcord.Member = SlashOption(
        
        name= 'usuario_del_servidor',
        description= 'Nombra el usuario del servidor',
        required= False,
        default= None
        
        
    )):
        
        if usuario in [None]:
            
            usuario = interaction.user
            
        
        lista_roles = []    
            
        for rol in usuario.roles:
            
            if rol.name != '@everyone':
                
                lista_roles.append(rol.mention)
                
                
        lista_convertida_roles = ' '.join(lista_roles)  
        
        
        if usuario.bot == True:
            
            estado_bot = 'Verdadero'
            
        else:
            
            estado_bot = 'Falso'              
            
        
        embed_user = nextcord.Embed(
            
            
            title= '✅ | Usuario',
            description= '''
            
`Usuario:` {}

`Discriminador:` **#{}**

`Roles:` {}

`ID:` **{}**

`Bot?:` **{}**

`Cuenta Creada:` **{}**            
            
            '''.format(usuario.mention, usuario.discriminator, lista_convertida_roles, usuario.id, estado_bot, usuario.created_at.date()),
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()
            
            
        ) 
        
        if usuario.avatar is not None:
            
            embed_user.set_thumbnail(url= usuario.avatar)
            
        else:
            
            embed_user.set_thumbnail(url= usuario.default_avatar)    
        
        embed_user.set_author(name= '{}'.format(self.bot.user), icon_url= self.bot.user.avatar)
  
        embed_user.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
        
        return await interaction.response.send_message(embed= embed_user)       
    
    
def setup(bot : commands.Bot):
    
    bot.add_cog(user(bot))      