from discord.ext import commands

client = commands.Bot(command_prefix='ac!')


@client.event
async def on_ready():
    print('bot is ready')


@client.command()
@commands.has_permissions(manage_channels=True, administrator=True)
async def delete_channels(ctx, channel_name, *, exception=None):
    deleted_channels = 0
    has_exceptions = False
    if exception is None:
        guild = client.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            if channel.name == channel_name:
                await channel.delete()
                deleted_channels += 1
    else:
        guild = client.get_guild(ctx.guild.id)
        for channel in ctx.guild.text_channels:
            is_exception = False
            if channel.name == channel_name:

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


client.run(TOKEN)
