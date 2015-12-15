import digitalocean
droplet = digitalocean.Droplet(token="2257cd137a617460f07a6dd72a7a38ff6e1a389d17fc3588ac641585110b45c9")
actions = droplet.get_actions()
for action in actions:
	action.load()
	print action.status
