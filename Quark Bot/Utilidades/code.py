import json
import os
import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime


class code(commands.Cog):

    def __init__(self, bot : commands.Bot):

        self.bot = bot


    @slash_command(name= 'code', description= 'Código de verificación del MD.')
    async def code(self, interaction : nextcord.Interaction, code : str = SlashOption(

        name= 'código',
        description= 'Pega el Código de verificación',
        required= True

    )):

        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-user-verify/{}.json'.format(interaction.user.id)) in [True]:

            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-user-verify/{}.json'.format(interaction.user.id), 'r') as read:

                config = json.load(read)

                id_user = interaction.guild.get_member(config['USER-ID'])
                password = config['PASS']
                rol = interaction.guild.get_role(config['ROL'])

                if id_user in [interaction.user] and password == code:

                    try:

                        await interaction.user.add_roles(rol)

                    except:

                        embed_error_verify = nextcord.Embed(

                            title='❌ | Code Error',
                            description='Contacta con un Owner o Staff, no puedo añadirte el rol porque mi rol esta muy abajo',
                            color=nextcord.Colour.red(),
                            timestamp=datetime.now()

                        )

                        embed_error_verify.set_author(name='{}'.format(self.bot.user),
                                                      icon_url=self.bot.user.avatar)

                        embed_error_verify.set_footer(text='Creado por DevCheck#4611',
                                                      icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                        return await interaction.response.send_message(embed=embed_error_verify, ephemeral=True)

                    else:


                        embed_verify = nextcord.Embed(

                            title='✅ | Verify',
                            description='Verificación completa, rol asignado: {}'.format(rol.mention),
                            color=nextcord.Colour.blue(),
                            timestamp=datetime.now()

                        )

                        embed_verify.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                        embed_verify.set_footer(text='Creado por DevCheck#4611',
                                                icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                        return await interaction.response.send_message(embed=embed_verify, ephemeral=True)

                else:

                    embed_error_incorrect = nextcord.Embed(

                        title= '❌ | Code Error',
                        description= 'La contraseña esta incorrecta o no existes en mi base datos',
                        color= nextcord.Colour.red(),
                        timestamp= datetime.now()

                    )

                    embed_error_incorrect.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                    embed_error_incorrect.set_footer(text='Creado por DevCheck#4611',
                                                  icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                    return await interaction.response.send_message(embed= embed_error_incorrect, ephemeral= True)

        else:

            embed_no_verify = nextcord.Embed(

                title= '❌ | Code Error',
                description= 'Solo puedes verificarte una vez cuando entras al servidor',
                color= nextcord.Colour.red(),
                timestamp= datetime.now()

            )

            embed_no_verify.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

            embed_no_verify.set_footer(text='Creado por DevCheck#4611',
                                               icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

            return await interaction.response.send_message(embed=embed_no_verify, ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(code(bot))