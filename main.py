import discord
from discord.ext import commands
import ovh
import datetime

import config

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = ovh.Client(
    endpoint='ovh-eu',
    application_key=config.APPLICATION_KEY,
    application_secret=config.APPLICATION_SECRET,
    consumer_key=config.CONSUMER_KEY,
)
domaine = config.DOMAINE
destination_mail = config.ADRESSE_MAIL


@bot.command(name='new')
async def _new(ctx, source_mail):
    client.post('/email/domain/{}/redirection'.format(domaine), **{
        'from': source_mail + "@" + domaine,
        'localCopy': False,
        'to': destination_mail,
    })
    await ctx.send(f"L'alias : {source_mail} a bien été créé.")


@bot.command(name="del")
async def _del(ctx, source_mail):
    liste_redirections = client.get(f'/email/domain/{domaine}/redirection')
    for i in liste_redirections:
        redirection = client.get(f'/email/domain/{domaine}/redirection/{i}')
        if redirection['from'] == source_mail + "@" + domaine:
            redirection_id = redirection["id"]
            supprimer = client.delete(f'/email/domain/{domaine}/redirection/{redirection_id}')
            await ctx.send(f"L'alias : {supprimer['account']} a bien été supprimé.")
            break


@bot.command(name="maj")
async def _maj(ctx):
    await bot.get_channel(ctx.channel.id).purge(limit=None)
    await ctx.send(f"Dernière MAJ le {datetime.datetime.now().strftime('%d/%m/%Y')}")
    liste_redirections = client.get(f'/email/domain/{domaine}/redirection')
    for i in liste_redirections:
        redirection = client.get(f'/email/domain/{domaine}/redirection/{i}')
        await ctx.send(redirection["from"])


@bot.command(name="clear")
async def _clear(ctx):
    await bot.get_channel(ctx.channel.id).purge(limit=None)


bot.run(config.DISCORD_TOKEN)
