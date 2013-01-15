import sublime, sublime_plugin

class SyntaxChecker(sublime_plugin.EventListener):
	def on_post_save(self, view):
		if view.file_name()[-3:] == '.rb':
			view.window().run_command("ruby_checker", {"saving": True})
		elif view.file_name()[-3:] == '.pl':
			view.window().run_command("perl_checker", {"saving": True})
		elif view.file_name()[-4:] == '.php' or view.file_name()[-8:] == '.php.inc':
			view.window().run_command("php_checker", {"saving": True})

class RubyCheckerCommand(sublime_plugin.TextCommand):
	def run(self, edit, saving=False):
		view = self.view
		global_settings = sublime.load_settings(__name__ + '.sublime-settings')
		cmd_setting = 'ruby_syntax_checker_cmd'
		ruby = view.settings().get(cmd_setting, global_settings.get(cmd_setting))
		view.window().run_command("exec", {"cmd": [ruby, "-cw", view.file_name()]})

class PerlCheckerCommand(sublime_plugin.TextCommand):
	def run(self, edit, saving=False):
		view = self.view
		global_settings = sublime.load_settings(__name__ + '.sublime-settings')
		cmd_setting = 'perl_syntax_checker_cmd'
		perl = view.settings().get(cmd_setting, global_settings.get(cmd_setting))
		view.window().run_command("exec", {"cmd": [perl, "-cw", view.file_name()]})

class PhpCheckerCommand(sublime_plugin.TextCommand):
	def run(self, edit, saving=False):
		view = self.view
		global_settings = sublime.load_settings(__name__ + '.sublime-settings')
		cmd_setting = 'php_syntax_checker_cmd'
		php = view.settings().get(cmd_setting, global_settings.get(cmd_setting))
		view.window().run_command("exec", {"cmd": [php, "-l", view.file_name()]})
