import json
import os
import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class verify (commands.Cog):

    def __init__(self, bot : commands.Bot):

        self.bot = bot

    @slash_command(name= 'verify', description= 'Activa el sistema de verificación por usuario.')
    async def verify(self, interaction : nextcord.Interaction, status : str = SlashOption(

        name= 'activar_o_desactivar',
        description= 'Seleciona si desactivas el sistema o activas el sistema de verificación',
        required= True,
        choices= ['🟢 Activar', '🔴 Desactivar']

    ),

    rol : nextcord.Role = SlashOption(

        name= 'rol_a_asignar',
        description= 'Nombra el rol que va ser asignado al usuario',
        required= True

    ),

    size : int = SlashOption(

        name= 'tamaño_del_tamaño',
        description= 'Tamaño del código que va ser enviado a los usuarios',
        required= True

    ),
    
    canal_de_verificacion : nextcord.TextChannel = SlashOption(
        
        name= 'canal_de_verificación',
        description= 'Nombra el canal de verificación',
        required= True
        
    )):


        if interaction.user.guild_permissions.administrator in [True]:

            if size >= 20:

                embed_no_valid_contra = nextcord.Embed(

                    title= '❌ | Verify Error',
                    description= 'No puedes configurar más de 20 cáracteres para la contraseña',
                    color= nextcord.Colour.red(),
                    timestamp= datetime.now()

                )

                embed_no_valid_contra.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                embed_no_valid_contra.set_footer(text='Creado por DevCheck#4611',
                                         icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                return await interaction.response.send_message(embed= embed_no_valid_contra)

            else:

                match status:

                    case '🟢 Activar':

                        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(interaction.guild_id)) in [True]:

                            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(interaction.guild_id), 'r') as read:

                                config = json.load(read)

                                config['STATUS'] = True
                                config['ROL'] = rol.id
                                config['SIZE'] = size
                                config['SERVER'] = interaction.guild_id
                                config['CHANNEL'] = canal_de_verificacion.id

                            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(interaction.guild_id), 'w') as write:

                                json.dump(config, write, indent= 4)

                            write.close()

                            embed_update_verify = nextcord.Embed(

                                title= '✅ | Verify Update',
                                description= 'Se actualizo los datos del sistema de verificación',
                                color= nextcord.Colour.yellow(),
                                timestamp= datetime.now()

                            )

                            embed_update_verify.set_author(name='{}'.format(self.bot.user),
                                                           icon_url=self.bot.user.avatar)

                            embed_update_verify.set_footer(text='Creado por DevCheck#4611',
                                                           icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                            return await interaction.response.send_message(embed= embed_update_verify)

                        else:

                            ruta = os.path.join('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/', '{}.json'.format(interaction.guild_id))

                            with open(ruta, 'w') as write:

                                dict_config = {

                                    'STATUS' : True,
                                    'ROL' : rol.id,
                                    'SIZE' : size,
                                    'SERVER' : interaction.guild_id,
                                    'CHANNEL' : canal_de_verificacion.id

                                }

                                json.dump(dict_config, write, indent= 4)

                            write.close()

                            embed_create_verify = nextcord.Embed(

                                title= '✅ | Verify Create',
                                description= 'Se activo el sistema de verificación, aparte un canal dedicado para verificación con acceso a @everyone',
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()

                            )

                            embed_create_verify.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                            embed_create_verify.set_footer(text='Creado por DevCheck#4611',
                                                 icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                            return await interaction.response.send_message(embed= embed_create_verify)

                    case '🔴 Desactivar':

                        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(interaction.guild_id)) in [True]:

                            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(interaction.guild_id), 'r') as read:

                                config = json.load(read)

                                config['STATUS'] = False
                                config['ROL'] = False
                                config['SIZE'] = False
                                config['SERVER'] = False
                                config['CHANNEL'] = False

                            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(interaction.guild_id), 'w') as write:

                                json.dump(config, write, indent= 4)

                            write.close()

                            embed_disable_verify = nextcord.Embed(

                                title= '✅ | Verify Disable',
                                description= 'Se desactivo el sistema de verificación en el servidor',
                                color= nextcord.Colour.red(),
                                timestamp= datetime.now()

                            )

                            embed_disable_verify.set_author(name='{}'.format(self.bot.user),
                                                               icon_url=self.bot.user.avatar)

                            embed_disable_verify.set_footer(text='Creado por DevCheck#4611',
                                                               icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                            return await interaction.response.send_message(embed= embed_disable_verify)

                        else:

                            embed_no_verify_actived = nextcord.Embed(

                                title= '❌ | Verify Error',
                                description= 'Debes activar primero el sistema de verificación',
                                color= nextcord.Colour.red(),
                                timestamp= datetime.now()

                            )

                            embed_no_verify_actived.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                            embed_no_verify_actived.set_footer(text='Creado por DevCheck#4611',
                                                 icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                            return await interaction.response.send_message(embed= embed_no_verify_actived)



        else:

            embed_noperms = nextcord.Embed(

                title='❌ | SIN PERMISOS',
                description='No tienes permisos suficientes para utilizar este comando.',
                color=nextcord.Colour.red(),
                timestamp=datetime.now()

            )

            embed_noperms.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

            embed_noperms.set_footer(text='Creado por DevCheck#4611',
                                     icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

            button_noperms = Button(

                label= 'Soporte',
                emoji= '⚙️',
                style= nextcord.ButtonStyle.gray,
                url= 'https://discord.gg/Gs5FwKHTCW'

            )

            view = View()
            view.add_item(button_noperms)

            return await interaction.response.send_message(embed=embed_noperms, view=view)


def setup(bot: commands.Bot):
    bot.add_cog(verify(bot))
