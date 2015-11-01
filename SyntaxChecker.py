import sublime, sublime_plugin

def has_ext(name, exts):
    if not isinstance(exts, list):
        exts = [exts]
    return any(name.endswith(ext) for ext in exts)

class SyntaxChecker(sublime_plugin.EventListener):
    def on_post_save(self, view):
        global_settings = sublime.load_settings(__name__ + '.sublime-settings')
        exts = view.settings().get('checker_extensions', global_settings.get('checker_extensions', {}))
        exts['ruby'] = exts['ruby'] or ['.rb']
        exts['xml'] = exts['xml'] or ['.xml']
        exts['perl'] = exts['perl'] or ['.pl']
        exts['php'] = exts['php'] or ['.php', '.php.inc']
        print exts

        name = view.file_name()
        print name
        for key in ['ruby', 'perl', 'php', 'xml']:
            if has_ext(name, exts[key]):
                print "got it"
                view.window().run_command(key + "_checker", {"saving": True})
                break

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

class XmlCheckerCommand(sublime_plugin.TextCommand):
    def run(self, edit, saving=False):
        view = self.view
        global_settings = sublime.load_settings(__name__ + '.sublime-settings')
        cmd_setting = 'xml_syntax_checker_cmd'
        xml = view.settings().get(cmd_setting, global_settings.get(cmd_setting))
        view.window().run_command("exec", {"cmd": [xml, "--noout", view.file_name()]})
