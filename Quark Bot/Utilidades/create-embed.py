import nextcord
import asyncio
from nextcord.ext import commands
from nextcord import PermissionOverwrite
from nextcord import slash_command, SlashOption
from nextcord.utils import get
from nextcord.ui import Button, View
from datetime import datetime


class createembed(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
        
    @slash_command(name= 'create-embed', description= 'Crea embeds personalizados.')
    async def createembed(self, interaction : nextcord.Interaction):
        
        if interaction.user.guild_permissions.administrator in [True]:
        
            class ModalEmbed(nextcord.ui.Modal):
        
                def __init__(self):
                    
                    super().__init__(
                        
                        "🚧 | Create-Embed"
                        
                    )

                    self.name = nextcord.ui.TextInput(
                        
                        label="Titulo",
                        placeholder= 'Escribe el titulo del embed.',
                        required= True,
                        min_length=1,
                        max_length=50
                        
                    )
                    
                    self.add_item(self.name)

                    self.description = nextcord.ui.TextInput(
                        
                        label="Descripción",
                        style=nextcord.TextInputStyle.paragraph,
                        placeholder="Escribe la descripción del embed.",
                        required=True,
                        min_length= 1,
                        max_length=2000
                        
                    )
                    
                    self.add_item(self.description)
                    
                    self.footer = nextcord.ui.TextInput(
                        
                        label= 'Pie del embed',
                        placeholder= 'Escribe el pie del embed (Footer).',
                        required= True,
                        min_length= 1,
                        max_length= 50
                        
                    )
                    
                    self.add_item(self.footer)
                    
                    self.img = nextcord.ui.TextInput(
                        
                        label= 'Imagen del emed',
                        placeholder= 'Escribe la url de la image del embed.',
                        required= False,
                        min_length= 1,
                        max_length= 300
                        
                    )
                    
                    self.add_item(self.img)
                    
                async def callback(self, interaction: nextcord.Interaction) -> None:
                    
                    titulo = self.name.value
                    descripcion = self.description.value
                    pie = self.footer.value
                    img = self.img.value
                    
                    embed_create = nextcord.Embed(
                        
                        title= '{}'.format(titulo),
                        description= '{}'.format(descripcion),
                        color= nextcord.Colour.brand_green(),
                        timestamp= datetime.now()
                        
                    )
                            
                    embed_create.set_footer(text= '{}'.format(pie))
                    
                    mensaje_edit = await interaction.send(embed = embed_create)
                    
                    if img is not None:
                        
                        embed_create = nextcord.Embed(
                        
                            title= '{}'.format(titulo),
                            description= '{}'.format(descripcion),
                            color= nextcord.Colour.brand_green(),
                            timestamp= datetime.now()
                        
                        )
                            
                        embed_create.set_footer(text= '{}'.format(pie))
                        
                        embed_create.set_image(url= '{}'.format(img))
                    
                        try:
                            
                            await asyncio.sleep(1)
                            await mensaje_edit.edit(embed = embed_create)
                            
                        except:
                            
                            embed_create = nextcord.Embed(
                        
                                title= '{}'.format(titulo),
                                description= '{}'.format(descripcion),
                                color= nextcord.Colour.brand_green(),
                                timestamp= datetime.now()
                        
                            )
                            
                            embed_create.set_footer(text= '{}'.format(pie))
                            
                            await asyncio.sleep(1)
                            await mensaje_edit.edit(embed= embed_create)
                            
                            embed_error_img = nextcord.Embed(
                                
                                title= '❌ | URL error',
                                description= 'Al parecer el link es inválido 😑',
                                color= nextcord.Colour.red(),
                                timestamp= datetime.now()
                                
                            )
                            
                            embed_error_img.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                            
                            await interaction.send(embed = embed_error_img)
                            
                            
                    embed_edit = nextcord.Embed(
                        
                        title= '✅ | Edit',
                        description= 'Puedes editar el embed desde aqui.',
                        color= nextcord.Colour.brand_green(),
                        timestamp= datetime.now()
                        
                    )
                    
                    embed_edit.set_footer(text= 'Creado por DevCheck#4611')  
                    
                    button_edit_color = Button(
                        
                        label= 'Edita el color',
                        emoji= '✍️',
                        style= nextcord.ButtonStyle.gray

                    )
                    
                    button_send = Button(
                        
                        label= 'Cargar Mensaje',
                        emoji= '📧',
                        style= nextcord.ButtonStyle.gray

                    )
                    
                    view = View(timeout= None)
                    view.add_item(button_edit_color)
                    view.add_item(button_send) 
                    
                    async def button_color_call(interaction : nextcord.Interaction):
                    
                        class dropcolor (nextcord.ui.Select):
                            
                            def __init__ (self):
                                
                                options = [
                                    
                                    nextcord.SelectOption(label= '🟢 Verde'),
                                    nextcord.SelectOption(label= '🔴 Rojo'),
                                    nextcord.SelectOption(label= '🟡 Oro'),
                                    nextcord.SelectOption(label= '💀 Random')
                                    
                                ]
                                
                                super().__init__(placeholder= 'Elige el color del embed', min_values= 1, max_values= 1, options= options)
                                
                                
                            async def callback(self, interaction: nextcord.Interaction):
                                
                                if '🟢 Verde' in self.values:
                                
                                    embed_edit_two = nextcord.Embed(
                                        
                                        title= '{}'.format(titulo),
                                        description= '{}'.format(descripcion),
                                        color= nextcord.Colour.green(),
                                        timestamp= datetime.now()
                                        
                                    )
                                
                                    embed_edit_two.set_footer(text= '{}'.format(pie))
                            
                                    embed_edit_two.set_image(url= '{}'.format(img))
                                    
                                    try:
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                        
                                        embed_color_green = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **🟢 Verde**',
                                            color= nextcord.Colour.green()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_green, delete_after= 30)
                                        
                                    except:
                                        
                                        embed_edit_two.set_image(url= None)
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                        
                                        embed_color_green = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **🟢 Verde**',
                                            color= nextcord.Colour.green()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_green, delete_after= 30)
                                        
                                        
                                elif '🔴 Rojo' in self.values:     
                                    
                                    
                                    embed_edit_two = nextcord.Embed(
                                        
                                        title= '{}'.format(titulo),
                                        description= '{}'.format(descripcion),
                                        color= nextcord.Colour.red(),
                                        timestamp= datetime.now()
                                        
                                    )
                                
                                    embed_edit_two.set_footer(text= '{}'.format(pie))
                                    
                                    embed_edit_two.set_image(url= '{}'.format(img))
                                    
                                    try:
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                    
                                        embed_color_red = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **🔴 Rojo**',
                                            color= nextcord.Colour.red()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_red, delete_after= 30)
                                    
                                    except:
                                        
                                        embed_edit_two.set_image(url= None)
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                    
                                        embed_color_red = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **🔴 Rojo**',
                                            color= nextcord.Colour.red()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_red, delete_after= 30)
                                        
                                        
                                            
                                        
                                        
                                elif '🟡 Oro' in self.values:  
                                    
                                    
                                    embed_edit_two = nextcord.Embed(
                                        
                                        title= '{}'.format(titulo),
                                        description= '{}'.format(descripcion),
                                        color= nextcord.Colour.gold(),
                                        timestamp= datetime.now()
                                        
                                    )
                                
                                    embed_edit_two.set_footer(text= '{}'.format(pie))

                                    embed_edit_two.set_image(url= '{}'.format(img))
                                    
                                    try:
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                    
                                        embed_color_gold = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **🟡 Oro**',
                                            color= nextcord.Colour.gold()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_gold, delete_after= 30)
                                        
                                    except:
                                        
                                        embed_edit_two.set_image(url= None)
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                    
                                        embed_color_gold = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **🟡 Oro**',
                                            color= nextcord.Colour.gold()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_gold, delete_after= 30)
                                        
                                            
                                elif '💀 Random' in self.values:   
                                    
                                    embed_edit_two = nextcord.Embed(
                                        
                                        title= '{}'.format(titulo),
                                        description= '{}'.format(descripcion),
                                        color= nextcord.Colour.random(),
                                        timestamp= datetime.now()
                                        
                                    )
                                
                                    embed_edit_two.set_footer(text= '{}'.format(pie))
                                    
                                    embed_edit_two.set_image(url= '{}'.format(img))
                                    
                                    try:
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                    
                                        embed_color_random = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **💀 Random**',
                                            color= nextcord.Colour.random()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_random, delete_after= 30)
                                        
                                    except:
                                        
                                        embed_edit_two.set_image(url= None)
                                        
                                        await asyncio.sleep(1)
                                        await mensaje_edit.edit(embed= embed_edit_two)
                                    
                                        embed_color_random = nextcord.Embed(
                                            
                                            description= 'Elegiste el color **💀 Random**',
                                            color= nextcord.Colour.random()
                                            
                                        )
                                    
                                        await interaction.response.send_message(embed= embed_color_random, delete_after= 30)
                                        
                                             
                        class dropcolorview (nextcord.ui.View):
                            
                            def __init__ (self):
                                
                                super().__init__()
                                self.add_item(dropcolor())
                                
                        
                        view = dropcolorview()
                        
                        
                        embed_select_color = nextcord.Embed(
                            
                            title= '✅ | Color Select',
                            description= 'Elige algún color que que te guste:',
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                            
                        )
                        
                        embed_select_color.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                        
                        return await interaction.response.send_message(embed= embed_select_color, view= view)        
                            
                                        
                
                    button_edit_color.callback = button_color_call
                    
                    async def button_send_callback (interaction : nextcord.Interaction):
                        
                        embed_send_message = nextcord.Embed(
                            
                            title= '✅ | /send',
                            description= 'Utilize /send para enviar el mensaje a un canal',
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                            
                        )
                        
                        embed_send_message.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                        
                        return await interaction.response.send_message(embed = embed_send_message)
                        
                    
                    button_send.callback = button_send_callback
                    
                    await interaction.channel.send(embed = embed_edit, view= view)
                    
            modal = ModalEmbed()
            
            await interaction.response.send_modal(modal = modal) 
        
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
    
    bot.add_cog(createembed(bot))    