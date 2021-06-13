import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='ac!')


@client.event
async def on_ready():
    print('bot is ready')


@client.command()
@commands.has_permissions(manage_channels=True, administrator=True)
async def delete_channels(ctx, channel_name, *, exceptions='None'):
    deleted_channels = 0
    if exceptions == 'None':
        guild = client.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:
                await channel.delete()
                deleted_channels += 1
        if deleted_channels == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass
    else:

        exceptions_cont = exceptions.split(', ')
        guild = client.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:

                for exception in exceptions_cont:
                    if int(channel.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await channel.delete()
                    deleted_channels += 1

        if deleted_channels == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            try:
                await ctx.send(f'Found and deleted {deleted_channels} channels')
            except Exception:  # If the channel you typed the message is deleted some errors occure
                pass


@client.command()
@commands.has_guild_permissions(manage_roles=True, administrator=True)
async def delete_roles(ctx, role_name, *, exceptions=None):
    deleted_roles = 0
    if exceptions == None:
        guild = client.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == role_name:
                await role.delete()
                deleted_roles += 1
        if deleted_roles == 0:
            await ctx.send("Couldn't find any roles with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} roles')
    else:
        try:
            exceptions_cont = exceptions.split(' --exc ')
            print(len(exceptions_cont))
            print(exceptions_cont)
            if len(exceptions_cont) > 1:
                role_name = role_name + ' ' + exceptions_cont[0]
                if not exceptions_cont[1] == '':
                    exceptions = exceptions_cont[1].split(', ')
            else:
                exceptions = exceptions.split(', ')
            
        except Exception as e:
            exceptions = exceptions.split(', ')
        print(role_name)
        print(exceptions)
        guild = client.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == '@everyone':
                continue
            if role.name == role_name:

                for exception in exceptions:
                    if int(role.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await role.delete()
                    deleted_roles += 1

        if deleted_roles == 0:
            await ctx.send("Couldn't find any roles with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} roles')


@client.command()
@commands.has_guild_permissions(manage_guild=True)
async def delete_messages(ctx, for_, *, message_):
    guild = int(ctx.guild.id)
    if str(for_).endswith('m'):
        for_ = for_[:-1]
        for_ = int(for_) * 60
    elif str(for_).endswith('s'):
        for_ = for_[:-1]
        for_ = int(for_)
    elif str(for_).endswith('h'):
        for_ = for_[:-1]
        for_ = int(for_)
    else:
        for_ = for_[:-1]
        for_ = int(for_)

    @client.listen()
    async def on_message(message):
        if message.guild.id == ctx.guild.id:
            if message.content == message_:
                await message.delete()

    await asyncio.sleep(for_)
    client.remove_listener(func=on_message)


client.run(TOKEN)
