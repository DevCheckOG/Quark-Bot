import asyncio
import random
import re
import string
import nextcord
import os
import time
import json
from nextcord.utils import get 
from nextcord.ext import commands
from datetime import datetime



class on_member_join(commands.Cog):
    
    def __init__ (self, bot : commands.Bot):
        
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_member_join(self, member):
        
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(member.guild.id)) in [True]:
            
            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-autorole/{}.json'.format(member.guild.id), 'r') as read:
                
                config = json.load(read)
                
                check_autorole = config['ACTIVATE']
                rol_bot = config['BOT_ROLE']
                rol_user = config['USER_ROLE']
                
                rol_bot_get =  get(member.guild.roles, id= config['BOT_ROLE'])
                rol_user_get = get(member.guild.roles, id= config['USER_ROLE'])
                
                read.close() 
                
                if check_autorole == True:
                    
                    if rol_bot != False:
                        
                        if member.bot != False:
                         
                            try:
                                
                                await member.add_roles(rol_bot_get)
                                
                            except:
                                
                                pass
                    
                    elif rol_user != False:
                        
                        if member.bot != True:
                            
                            try:
                                
                                member.add_roles(rol_user_get)
                                
                            except:
                                
                                pass
                
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(member.guild.id)) in [True]:
            
            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-antibot/{}.json'.format(member.guild.id), 'r') as read:
                
                config = json.load(read)
                
                check_antibot = config['ESTADO'] 
                
                read.close() 
                
                if check_antibot == True:
                    
                    if member.bot == True:

                        await member.kick(reason = 'Antibot Activado ~ Arqui#9588')
                        
                    else:
                        
                        pass
                
        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(member.guild.id)) in [True]:
            
            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-welcome/{}.json'.format(member.guild.id), 'r') as read:
                
                config = json.load(read)
                
                check_welcome = config['STATUS'] 
                canal_welcome = await self.bot.fetch_channel(config['CANAL'])
                titulo = config['Titulo']
                desc = config['desc']  
                color = config['color']
                img = config['img']
                
                read.close() 
                
                if check_welcome in [True]:
                    
                    if canal_welcome is not None:

                        new_title = titulo.replace('{name}', '{}'.format(member))
                        desc_new = desc.replace('{mention}', '{}'.format(member.mention))
                        desc_new_final = desc_new.replace('{name}', '**{}**'.format(member.name))

                        try:
                            
                            channel = re.search(r'\d+', desc_new_final).group()
                            channel_id = await self.bot.fetch_channel(int(channel))
                            desc_new_final = desc_new_final.replace('{channel.' + str(channel_id.id) + '}', channel_id.mention)
                            
                        except:
                            
                            pass    
                        
                        match color:
                            
                            case 'Azul':
                                
                        
                                embed_welcome = nextcord.Embed(
                                    
                                    title= '{}'.format(new_title),
                                    description= desc_new_final,
                                    color= nextcord.Colour.blue(),
                                    timestamp= datetime.now()
                                    
                                )
                    
                            case 'Verde':
                                
                                embed_welcome = nextcord.Embed(
                                    
                                    title= '{}'.format(new_title),
                                    description= desc_new_final,
                                    color= nextcord.Colour.green(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                            case 'Rojo':
                                
                                embed_welcome = nextcord.Embed(
                                    
                                    title= '{}'.format(new_title),
                                    description= desc_new_final,
                                    color= nextcord.Colour.red(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                            case 'Oro':
                                
                                embed_welcome = nextcord.Embed(
                                    
                                    title= '{}'.format(new_title),
                                    description= desc_new_final,
                                    color= nextcord.Colour.gold(),
                                    timestamp= datetime.now()
                                    
                                )
                                
                            case 'Random':
                                
                                embed_welcome = nextcord.Embed(
                                    
                                    title= '{}'.format(new_title),
                                    description= desc_new_final,
                                    color= nextcord.Colour.random(),
                                    timestamp= datetime.now()
                                    
                                )  
                            
                            
                        if member.avatar is not None and member.guild.icon is not None:
                            
                            embed_welcome.set_thumbnail(url= member.avatar)
                            embed_welcome.set_footer(text= '¡Bienvenido {}!'.format(member.name), icon_url= member.guild.icon)
                            
                        else:
                            
                            embed_welcome.set_thumbnail(url= member.default_avatar)
                            embed_welcome.set_footer(text= '¡Bienvenido {}!'.format(member.name), icon_url= 'https://cdn.discordapp.com/avatars/1079159577473462312/705e0b7b6b1f445e1cd71d4e796f5830.png?size=1024')

                        if img is not None:

                            try:

                                embed_welcome.set_image(url= img)
                                await canal_welcome.send(embed= embed_welcome)

                            except:

                                embed_welcome.set_image(url= None)
                                await canal_welcome.send(embed= embed_welcome)

                        else:

                            await  canal_welcome.send(embed= embed_welcome)


        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(member.guild.id)) in [True]:

            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-verify/{}.json'.format(member.guild.id), 'r') as read:

                config = json.load(read)

                check_verify = config['STATUS']
                size_verify = config['SIZE']
                server = await self.bot.fetch_guild(config['SERVER'])
                role_verify = config['ROL']
                role_get_verify = server.get_role(role_verify)

                read.close()
                if check_verify in [True]:

                    if member.bot != True:

                        contra = ''.join(random.choice(string.digits + string.ascii_letters) for z in range(size_verify))

                        embed_verify = nextcord.Embed(

                            title= '✅ | Verify',
                            description= 'Use /code para verificarte en el servidor **{}**, solo tienes 2 Minutos'.format(server.name),
                            color= nextcord.Colour.blue(),
                            timestamp= datetime.now()

                        )

                        embed_verify.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                        embed_verify.set_footer(text='Creado por DevCheck#4611', icon_url=self.bot.user.avatar)

                        if os.path.exists('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-user-verify/{}.json'.format(member.id)) in [True]:

                            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-user-verify/{}.json'.format(member.id), 'r') as read:

                                config_user = json.load(read)

                                config_user['USER-ID'] = member.id
                                config_user['PASS'] = contra
                                config_user['ROL'] = role_verify

                            with open('C:/Users/WIndows USER/Documents/Quark Bot/Utilidades/data-user-verify/{}.json'.format(member.id), 'w') as write:

                                json.dump(config_user, write, indent= 4)

                            write.close()

                        else:

                            ruta = os.path.join('C:/Users/WIndows USER/Documents\Quark Bot/Utilidades/data-user-verify/', '{}.json'.format(member.id))

                            with open(ruta, 'w') as write:

                                dic_user = {

                                    'USER-ID' : member.id,
                                    'PASS' : contra,
                                    'ROL' : role_verify

                                }

                                json.dump(dic_user, write, indent= 4)

                            write.close()

                        try:
                            
                            channel_dm = member.dm_channel
                            
                            if channel_dm in [None]:
                                
                                channel_dm = await member.create_dm()

                            await channel_dm.send(embed = embed_verify)

                        except:

                            return

                        await asyncio.sleep(2)

                        await member.send(content = 'Código: `{}`'.format(contra))

                        await asyncio.sleep(60 * 2)
                        
                        if get(member.roles, name = role_get_verify.name):
                            
                            os.remove('C:/Users/WIndows USER/Documents\Quark Bot/Utilidades/data-user-verify/{}.json'.format(member.id))
                                
                        else:
                                
                            embed_no_verify = nextcord.Embed(
                                
                                title= '❌ | Verify',
                                description= 'Debes verificarte en el tiempo de 3 Minutos en el servidor `{}`'.format(server.name),
                                color= nextcord.Colour.red(),
                                timestamp= datetime.now()
                                    
                            )
                            
                            embed_no_verify.set_author(name='{}'.format(self.bot.user), icon_url=self.bot.user.avatar)

                            embed_no_verify.set_footer(text='Creado por DevCheck#4611', icon_url=self.bot.user.avatar)
                            
                            channel_dm = member.dm_channel
                        
                            if channel_dm in [None]:
                                    
                                channel_dm = await member.create_dm()

                            await channel_dm.send(embed = embed_no_verify)
                            
                            await member.kick(reason = 'No se verifico en el canal de verificación')  

                            os.remove('C:/Users/WIndows USER/Documents\Quark Bot/Utilidades/data-user-verify/{}.json'.format(member.id))    
                                
                                  

                            
                            
def setup(bot : commands.Bot):
    
    bot.add_cog(on_member_join(bot))                             
                
                
             