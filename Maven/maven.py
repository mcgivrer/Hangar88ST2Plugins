import sublime, sublime_plugin

class MavenGoalsCommand(sublime_plugin.WindowCommand):
	wrkDir = None

	def run(self,working_dir):
		
		self.wrkDir = working_dir
		print self.wrkDir
		self.window.show_input_panel("mvn",'clean test',self.on_done,None,None)

	def on_done(self, text):
		cmd = [u'mvn',u'-B']
		cmd += text.split(' ')
		print cmd
		self.window.run_command("exec",{"cmd":cmd, 'working_dir':self.wrkDir})
