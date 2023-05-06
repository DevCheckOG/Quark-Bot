import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime


class server(commands.Cog):

    def __init__ (self, bot : commands.Bot):

        self.bot = bot

    @slash_command(name= 'server', description= 'Obtén información del servidor dónde estes.')
    async def server(self, interaction : nextcord.Interaction):

        lista_roles = []

        for role in interaction.guild.roles:

            if role.name != interaction.guild.default_role.name:

                lista_roles.append(role.mention)

        if len(lista_roles) == 0:

            lista_roles.append('Ningún rol válido')

        lista_text = []
        lista_voice = []

        for channel_text in interaction.guild.text_channels:

            lista_text.append(channel_text.name)

        for channel_voice in interaction.guild.voice_channels:

            lista_voice.append(str(channel_voice.id))

        embed_server = nextcord.Embed(

            title= '✅ | Server',
            description= '''
            
`Nombre:` **{}** 

`ID:` **{}**

`Owner:` {}

`Roles:` {}

`Miembros:` **{}**

`Canales de Texto y Voz:`  **{} | {}**

`Creado:` **{}**         
            
            '''.format(interaction.guild.name, interaction.guild_id, interaction.guild.owner.mention, ' '.join(lista_roles), interaction.guild.member_count, len(lista_text), len(lista_voice), interaction.guild.created_at.date()),
            color= nextcord.Colour.blue(),
            timestamp= datetime.now()

        )

        embed_server.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

        embed_server.set_footer(text='Creado por DevCheck#4611',
                               icon_url='https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

        if interaction.guild.icon is not None:

            embed_server.set_thumbnail(url= interaction.guild.icon)

        return await interaction.response.send_message(embed= embed_server)



def setup(bot: commands.Bot):
    bot.add_cog(server(bot))

