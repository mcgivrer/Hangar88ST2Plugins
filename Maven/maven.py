import sublime, sublime_plugin

class MavenGoalsCommand(sublime_plugin.WindowCommand):

	def run(self,file_regex):
		self.window.show_input_panel("mvn",'clean test',self.on_done,None,None)

	def on_done(self, text):
		cmd = ["mvn"]
		cmd += text.split(' ')
		self.window.run_command("exec",{"cmd":cmd})
