def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
W, H = 1440, 1080
HW, HH = W / 2, H / 2
AREA = W * H