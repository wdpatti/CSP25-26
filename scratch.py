from scratchcloud import CloudClient, CloudChange

client = CloudClient(username='wdp09CloudServer', project_id='622084628')

@client.event
async def on_connect():
  await client.set_cloud("test", '200')
  
client.run('')