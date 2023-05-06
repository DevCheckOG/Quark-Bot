import nextcord
from nextcord.ext import commands
from nextcord import slash_command, SlashOption
from nextcord.ui import Button, View
from datetime import datetime



class calc(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
        
    @slash_command(name= 'calc', description= 'Calcula cualquier número.')
    async def calc(self, interaction : nextcord.Interaction):
        
        
        class Calculator (nextcord.ui.Modal):
            
            
            def __init__ (self):
                
                super().__init__(
                    
                    title= '🔢 | Calculadora'
                    
                )  
                
                self.op1 = nextcord.ui.TextInput(
                    
                    label= 'Operador 1',
                    placeholder= 'Escribe el primer número.',
                    required= True,
                    min_length= 1,
                    max_length= 100
                    
                )
                
                self.add_item(self.op1)
                
                self.operador = nextcord.ui.TextInput(
                    
                    label= 'Operador',
                    placeholder= '/, +, -, *',
                    required= True,
                    min_length= 1,
                    max_length= 1
                 
                ) 
                
                self.add_item(self.operador)
                
                self.op2 = nextcord.ui.TextInput(
                    
                    label= 'Operador 2',
                    placeholder= 'Escribe el segundo número.',
                    required= True,
                    min_length= 1,
                    max_length= 100
                     
                )
                
                self.add_item(self.op2)
                
            async def callback(self, interaction: nextcord.Interaction) -> None:
                
                
                if self.op1.value.isnumeric() in [True] and self.op2.value.isnumeric() in [True]:
                    
                    operador_1 = int(self.op1.value)
                    operador_2 = int(self.op2.value)
                    
                    match self.operador.value:
                        
                        case '/':
                            
                            try:
                                
                                embed_div = nextcord.Embed(
                                    
                                    title= '✅ | Calc /',
                                    description= '''
                                    
Números: **{}**, **{}** 

Resultado: **{}**                               
                            
                                    '''.format(operador_1, operador_2, round(operador_1 / operador_2)),
                                    color= nextcord.Colour.blue()
                                    
                                )
                                
                                embed_div.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                
                                return await interaction.send(embed = embed_div)
                            
                            except:
                                
                                embed_div = nextcord.Embed(
                                    
                                    title= '❌ | Calc error /',
                                    description= '''
                                    
Números: **Número Inválido**, **Número Inválido** 

Resultado: **Inválido | No puedo dividir entre 0 es indefinido**                               
                            
                                    ''',
                                    color= nextcord.Colour.red()
                                    
                                )
                                
                                embed_div.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                
                                return await interaction.send(embed = embed_div)
                        
                        case '+':
                            
                            embed_sum = nextcord.Embed(
                                
                                title= '✅ | Calc +',
                                description= '''
                                
Números: **{}**, **{}** 

Resultado: **{}**                                   
                                
                                '''.format(operador_1, operador_2, operador_1 + operador_2),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()
                                
                            )
                            
                            embed_sum.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                
                            return await interaction.send(embed = embed_sum)
                        
                        case '-':
                            
                            embed_res = nextcord.Embed(
                                
                                title= '✅ | Calc -',
                                description= '''
                                
Números: **{}**, **{}** 

Resultado: **{}**                                   
                                
                                '''.format(operador_1, operador_2, operador_1 - operador_2),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()
                                
                            )
                            
                            embed_res.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                
                            return await interaction.send(embed = embed_res)
                        
                        case '*':
                            
                            embed_mul = nextcord.Embed(
                                
                                title= '✅ | Calc *',
                                description= '''
                                
Números: **{}**, **{}** 

Resultado: **{}**                                   
                                
                                '''.format(operador_1, operador_2, operador_1 * operador_2),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()
                                
                            )
                            
                            embed_mul.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                                
                            return await interaction.send(embed = embed_mul)
                        
                        case _:
                            
                            embed_error_value_operador = nextcord.Embed(
                                
                                title= '❌ | Calc Error',
                                description= 'Escribe un operador válido',
                                color= nextcord.Colour.red(),
                                timestamp= datetime.now()
                                
                            )  
                            
                            embed_error_value_operador.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                            
                            return await interaction.send(embed = embed_error_value_operador)
                
                else:
                    
                    embed_error_value = nextcord.Embed(
                        
                        title= '❌ | Calc Error',
                        description= 'No puedo calcular letras o carácteres 😠',
                        color= nextcord.Colour.red(),
                        timestamp= datetime.now()
                        
                    )  
                
                    embed_error_value.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024') 
                    
                    return await interaction.send(embed = embed_error_value)
                
    
    
        modal = Calculator()
        
        return await interaction.response.send_modal(modal= modal)  
    
    
def setup(bot : commands.Bot):
    
    bot.add_cog(calc(bot))               
                     
                 