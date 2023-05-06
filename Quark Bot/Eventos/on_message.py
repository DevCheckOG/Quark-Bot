import nextcord
import json
import os
import asyncio
from nextcord.ext import commands
from datetime import datetime



class on_message(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
        
    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author in [self.bot.user]:
            
            return
        
        else:
            
            if os.path.exists('/home/container/Eventos/data/{}.json'.format(message.guild.id)) in [True]:
                
                with open('/home/container/Eventos/data/{}.json'.format(message.guild.id), 'r') as read:
                    
                    data = json.load(read)
                    
                    links = data['LINKS']
                    palabras = data['PALABRAS']
                    canales = data['CANALES']
            
                    read.close()
                    
                    for link in links:
                        
                        if message.content.startswith(link):
                            
                            if message.channel.id == canales:
                                
                                return
                            
                            else:
                            
                                embed_no_links = nextcord.Embed(
                                    
                                    description= 'No esta permitido ese **link** en el servidor',
                                    color= nextcord.Colour.red()
                                
                                )
                                
                                links_embed = await message.channel.send(embed = embed_no_links)
                                
                                await message.delete()
                                
                                await asyncio.sleep(3)
                                
                                return await links_embed.delete()
                        
                    for char in palabras:    
                        
                        if message.content.startswith(char):
                            
                            if message.channel.id == canales:
                                
                                return
                            
                            else:
                        
                                embed_no_words = nextcord.Embed(
                                    
                                    description= 'No esta permitido esa **palabra** en el servidor',
                                    color= nextcord.Colour.red()
                                
                                )
                                
                                palabras_embed = await message.channel.send(embed = embed_no_words)
                                
                                await message.delete()
                                
                                await asyncio.sleep(3)
                                
                                return await palabras_embed.delete()
                        
            else:
                            
                pass  
            
        if os.path.exists('/home/container/Utilidades/data-afk/{}.json'.format(message.author.id)) in [True]:
            
            with open('/home/container/Utilidades/data-afk/{}.json'.format(message.author.id), 'r') as read:
                
                config = json.load(read)
                
                user_id = config['ID']
                
                read.close()
                
                if user_id == message.author.id:
                    
                    user = self.bot.get_user(user_id)
                    
                    if user is not None:
                    
                        embed_afk_term = nextcord.Embed(
                            
                            title= '✅ | AFK',
                            description= '¡{} ya no estas afk!'.format(user.mention),
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()
                            
                        )
                        
                        embed_afk_term.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)
                        
                        embed_afk_term.set_footer(text= 'Creado por DevCheck#4611', icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')
                        
                         
                        try:
                            
                            await message.channel.send(embed = embed_afk_term)
                            
                        except:
                            
                            pass   
                        
                        return os.remove('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-afk/{}.json'.format(message.author.id)) 
                        
                else:
                    
                    pass   
                
        if os.path.exists('/home/container/Utilidades/data-verify/{}.json'.format(message.guild.id)) in [True]:
            
            with open('/home/container/Utilidades/data-verify/{}.json'.format(message.guild.id), 'r') as read:
                
                config = json.load(read)
                
                check_verify = config['STATUS']    
                
                channel = self.bot.get_channel(config['CHANNEL'])
                
                read.close()
                
                if check_verify in [True] and channel is not None:
                  
                    if message.channel.id == channel.id:
                        
                        if message.flags in [nextcord.MessageFlags.ephemeral]:
                            
                            pass
                        
                        else:
                            
                            await message.delete()
    
                            embed_error_verify_chars = nextcord.Embed(
                                
                                title= '❌ | Verify',
                                description= 'No puedes hablar en el canal **{}** es de verificación'.format(channel.name),
                                color= nextcord.Colour.blue(),
                                timestamp= datetime.now()

                            )     
                            
                            embed_error_verify_chars.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                            embed_error_verify_chars.set_footer(text='Creado por DevCheck#4611', icon_url=self.bot.user.avatar)  
                            
                            try:
                        
                                channel_dm = message.author.dm_channel
                                
                                if channel_dm in [None]:
                                    
                                    channel_dm = await message.author.create_dm()

                                await channel_dm.send(embed = embed_error_verify_chars)

                            except:

                                pass
                            
                            if os.path.exists('/home/container/Utilidades/data-user-verify/{}.json'.format(message.author.id)) in [True]:
                                
                                os.remove('/home/container/Utilidades/data-user-verify/{}.json'.format(message.author.id))
                            
                            return await message.author.kick(reason = 'No puede escribir mensajes en el canal {}'.format(channel.mention))
                              
                
def setup(bot : commands.Bot):
    
    bot.add_cog(on_message(bot))                    
                
                
                                       