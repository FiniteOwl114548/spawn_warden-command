def on_on_chat():
    mobs.spawn(mobs.monster(WARDEN), player.position())
player.on_chat("/spawn_warden", on_on_chat)
