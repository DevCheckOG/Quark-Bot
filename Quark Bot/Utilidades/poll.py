import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime




class poll(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    @slash_command(name= 'poll', description= 'Crea encuentas personalizadas.')
    async def poll(self, interaction : nextcord.Interaction, opciones_type : str = SlashOption(
        
        name= 'opciones',
        description= 'Elije una opción, para la cantidad de preguntas de la encuesta',
        required= True,
        choices= ['1️⃣ Propuesta', '2️⃣ Propuestas', '3️⃣ Propuestas', '4️⃣ Propuestas'] 
        
    ),
                   
    mention : nextcord.Role = SlashOption(
        
        name= 'rol_de_encuentas',
        description= 'Nombra el rol de encuentas para avisarle a los usuarios',
        required= False
        
    )):
        
        if interaction.user.guild_permissions.administrator in [True]:
            
            match opciones_type:
                
                case '1️⃣ Propuesta':
                    
                    class One_Aswer(nextcord.ui.Modal):
                        
                        
                        def __init__ (self):
                            
                            super().__init__(
                                
                                title= '✅ | Poll',
                                timeout= None
                                
                            )
                            
                            self.aswer_one = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 1',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la única propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_one)
                            
                        async def callback(self, interaction: nextcord.Interaction) -> None:
                            
                            aswer_unic = self.aswer_one.value
                            
                            embed_aswer_poll = nextcord.Embed(
                                
                                title= '✅ | Poll',
                                description= '''
                                
1️⃣ | **{}**

'''.format(aswer_unic),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()    
                                
                            )
                            
                            embed_aswer_poll.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                            
                            embed_one = await interaction.channel.send(embed = embed_aswer_poll)
                            
                            await embed_one.add_reaction('👍')
                            await embed_one.add_reaction('👎')
                            
                            if mention is not None:
                                
                                await interaction.channel.send(content= '{}'.format(mention.mention))
                                
                            return    
                            
                        
                    
                    
                    modal_one = One_Aswer()
                    
                    return await interaction.response.send_modal(modal= modal_one)        
                
                case '2️⃣ Propuestas':
                    
                    class Two_Aswer(nextcord.ui.Modal):
                        
                        
                        def __init__ (self):
                            
                            super().__init__(
                                
                                title= '✅ | Poll'
                                
                            )
                            
                            self.aswer_one = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 1',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la primera propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_one)
                            
                            self.aswer_two = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 2',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la segunda propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_two)
                            
                        async def callback(self, interaction: nextcord.Interaction) -> None:
                            
                            aswer_one_pr = self.aswer_one.value
                            
                            aswer_two_pr = self.aswer_two.value
                            
                            embed_aswer_poll = nextcord.Embed(
                                
                                title= '✅ | Poll',
                                description= '''
                                
1️⃣ | **{}**

2️⃣ | **{}**

'''.format(aswer_one_pr, aswer_two_pr),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()    
                                
                            )
                            
                            embed_aswer_poll.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                            
                            embed_two = await interaction.channel.send(embed = embed_aswer_poll)
                            
                            await embed_two.add_reaction('1️⃣')
                            await embed_two.add_reaction('2️⃣')
                        
                            if mention is not None:
                                
                                await interaction.channel.send(content= '{}'.format(mention.mention))
                            
                            return
                            
                        
                    
                    
                    modal_two = Two_Aswer()
                    
                    return await interaction.response.send_modal(modal= modal_two) 
                
                case '3️⃣ Propuestas':
                    
                    class Three_Aswer(nextcord.ui.Modal):
                        
                        
                        def __init__ (self):
                            
                            super().__init__(
                                
                                title= '✅ | Poll'
                                
                            )
                            
                            self.aswer_one = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 1',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la primera propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_one)
                            
                            self.aswer_two = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 2',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la segunda propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_two)
                            
                            self.aswer_three = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 3',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la tercera propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_three)
                            
                        async def callback(self, interaction: nextcord.Interaction) -> None:
                            
                            aswer_one_pr = self.aswer_one.value
                            
                            aswer_two_pr = self.aswer_two.value
                            
                            aswer_three_pr = self.aswer_three.value
                            
                            embed_aswer_poll = nextcord.Embed(
                                
                                title= '✅ | Poll',
                                description= '''
                                
1️⃣ | **{}**

2️⃣ | **{}**

3️⃣ | **{}**

    '''.format(aswer_one_pr, aswer_two_pr, aswer_three_pr),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()    
                                
                            )
                            
                            embed_aswer_poll.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                            
                            embed_aswer_poll.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                            
                            embed_three = await interaction.channel.send(embed = embed_aswer_poll)
                            
                            await embed_three.add_reaction('1️⃣')
                            await embed_three.add_reaction('2️⃣')
                            await embed_three.add_reaction('3️⃣')
                            
                            if mention is not None:
                                
                                await interaction.channel.send(content= '{}'.format(mention.mention))
                            
                            return
                            
                        
                    
                    
                    modal_three = Three_Aswer()
                    
                    return await interaction.response.send_modal(modal= modal_three) 
                
                case '4️⃣ Propuestas':
                    
                    class Four_Aswer(nextcord.ui.Modal):
                        
                        
                        def __init__ (self):
                            
                            super().__init__(
                                
                                title= '✅ | Poll'
                                
                            )
                            
                            self.aswer_one = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 1',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la primera propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_one)
                            
                            self.aswer_two = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 2',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la segunda propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_two)
                            
                            self.aswer_three = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 3',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la tercera propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_three)
                            
                            self.aswer_four = nextcord.ui.TextInput(
                                
                                label= 'Propuesta 4',
                                required= True,
                                min_length= 1,
                                max_length= 200,
                                placeholder= 'Escribe la cuarta propuesta de la encuesta.'
                                
                            )
                            
                            self.add_item(self.aswer_four)
                            
                        async def callback(self, interaction: nextcord.Interaction) -> None:
                            
                            aswer_one_pr = self.aswer_one.value
                            
                            aswer_two_pr = self.aswer_two.value
                            
                            aswer_three_pr = self.aswer_three.value
                            
                            aswer_four_pr = self.aswer_four.value
                            
                            embed_aswer_poll = nextcord.Embed(
                                
                                title= '✅ | Poll',
                                description= '''
                                
1️⃣ | **{}**

2️⃣ | **{}**

3️⃣ | **{}**

4️⃣ | **{}**

    '''.format(aswer_one_pr, aswer_two_pr, aswer_three_pr, aswer_four_pr),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()    
                                
                            ) 
                    
                            embed_aswer_poll.set_thumbnail(url = 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                    
                            embed_aswer_poll.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')  
                            
                            embed_four = await interaction.channel.send(embed = embed_aswer_poll)
                            
                            await embed_four.add_reaction('1️⃣')
                            await embed_four.add_reaction('2️⃣')
                            await embed_four.add_reaction('3️⃣')
                            await embed_four.add_reaction('4️⃣')
                            
                            if mention is not None:
                                
                                await interaction.channel.send(content= '{}'.format(mention.mention))
                            
                            return
                            
                    
                    modal_four = Four_Aswer()
                    
                    return await interaction.response.send_modal(modal= modal_four) 
                
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
    
    bot.add_cog(poll(bot))                  