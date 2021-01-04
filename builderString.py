builderString = """
<MenuScreen>:
	BoxLayout:
		Button:
			text: 'Goto settings'
			on_press: root.manager.current = 'settings'
		Button:
			text: 'Quit'

<StartScreen>:
	
	canvas:
		Color:
			rgba: 0.94, 0.94, 0.94, 1
		Rectangle:
			size: self.size
			pos: self.pos

	BoxLayout:
		padding: 25,25,25,500

		spacing: 50
		orientation: 'vertical'



	BoxLayout:
		orientation: 'vertical'
		padding: 50
		width: 50

		Image:
			source: 'assets/salt_72_2.png'
			allow_stretch: True

		Widget:
		Widget:

		Label:
			id: loading_text
			text:"LOADING"
			color: 0.34,0.33,0.33,1

		ProgressBar:
			id: loading_progress
			value: 0.2
			max: 1

"""
