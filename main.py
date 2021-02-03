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
            await ctx.send(f'Found and deleted {deleted_channels} channels')
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
            await ctx.send(f'Found and deleted {deleted_channels} channels')


@client.command()
@commands.has_permissions(manage_roles=True, administrator=True)
async def delete_roles(ctx, role_name, *, exceptions='None'):
    deleted_roles = 0
    if exceptions == 'None':
        guild = client.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == role_name:
                await role.delete()
                deleted_roles += 1
        if deleted_roles == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} channels')
    else:
        exceptions_cont = exceptions.split(', ')
        guild = client.get_guild(ctx.guild.id)
        for role in ctx.guild.roles:
            is_exception = False
            if role.name == role_name:

                for exception in exceptions_cont:
                    if int(role.id) == int(exception):
                        is_exception = True

                if is_exception:
                    pass
                else:
                    await role.delete()
                    deleted_roles += 1

        if deleted_roles == 0:
            await ctx.send("Couldn't find any channels with that name")
        else:
            await ctx.send(f'Found and deleted {deleted_roles} channels')


client.run(TOKEN)
