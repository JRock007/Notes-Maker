from distutils.core import setup
import py2exe
import glob
import fnmatch
import sys
import os
import shutil
import operator

#hack which fixes font
origIsSystemDLL = py2exe.build_exe.isSystemDLL  # save the orginal before we edit it


def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):  # "sdl_ttf.dll" added by arit.
            return 0
    return origIsSystemDLL(pathname)  # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL  # override the default function with this one


class BuildExe:
    def __init__(self):
        #Name of starting .py
        self.script = "NotesMaker.py"

        #Name of program
        self.project_name = "Notes Maker"

        #Project url
        self.project_url = "about:none"

        #Version of program
        self.project_version = "1.0"

        #Auhor of program
        self.author_name = "Jean-Romain Garnier"
        self.copyright = "Copyright (c) 2014 Jean-Romain Garnier."

        #Description
        self.project_description = "A quick notes maker"

        #Icon file (None will use pygame default icon)
        self.icon_file = "icon.ico"

        #Extra files/dirs copied to game
        self.extra_datas = [('example.nmkr'),
                            ('LICENSE'),
                            ('README.md'),

                            ('ext', ['ext/__init__.py']),
                            ('ext', ['ext/datetime.py']),
                            ('ext', ['ext/find.py']),
                            ('ext', ['ext/table.py']),
                            ('ext', ['ext/wordcount.py']),

                            ('icons', ['icons/align-center.png']),
                            ('icons', ['icons/align-center.png']),
                            ('icons', ['icons/align-justify.png']),
                            ('icons', ['icons/align-left.png']),
                            ('icons', ['icons/align-right.png']),
                            ('icons', ['icons/bold.png']),
                            ('icons', ['icons/bullet.png']),
                            ('icons', ['icons/calender.png']),
                            ('icons', ['icons/copy.png']),
                            ('icons', ['icons/count.png']),
                            ('icons', ['icons/cut.png']),
                            ('icons', ['icons/dedent.png']),
                            ('icons', ['icons/find.png']),
                            ('icons', ['icons/font-color.png']),
                            ('icons', ['icons/font-size.png']),
                            ('icons', ['icons/font.png']),
                            ('icons', ['icons/highlight.png']),
                            ('icons', ['icons/icon.png']),
                            ('icons', ['icons/image.png']),
                            ('icons', ['icons/indent.png']),
                            ('icons', ['icons/italic.png']),
                            ('icons', ['icons/new.png']),
                            ('icons', ['icons/number.png']),
                            ('icons', ['icons/open.png']),
                            ('icons', ['icons/open2.png']),
                            ('icons', ['icons/open3.png']),
                            ('icons', ['icons/paste.png']),
                            ('icons', ['icons/preview.png']),
                            ('icons', ['icons/print.png']),
                            ('icons', ['icons/redo.png']),
                            ('icons', ['icons/save.png']),
                            ('icons', ['icons/strike.png']),
                            ('icons', ['icons/subscript.png']),
                            ('icons', ['icons/superscript.png']),
                            ('icons', ['icons/table.png']),
                            ('icons', ['icons/underline.png']),
                            ('icons', ['icons/undo.png']),
                            ('icons', ['icons/time.png']),
                            ('icons', ['icons/iconmonstr-license.pdf'])]

        #Extra/excludes python modules
        self.exclude_modules = ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript',
                                'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon']

        #DLL Excludes
        self.exclude_dll = ['']
        #python scripts (strings) to be included, seperated by a comma
        self.extra_scripts = []

        #Zip file name (None will bundle files in exe instead of zip file)
        self.zipfile_name = None

        #Dist directory
        self.dist_dir = 'dist'

    ## Code from DistUtils tutorial at http://wiki.python.org/moin/Distutils/Tutorial
    ## Originally borrowed from wxPython's setup and config files
    def opj(self, *args):
        path = os.path.join(*args)
        return os.path.normpath(path)

    def find_data_files(self, srcdir, *wildcards, **kw):
        # get a list of all files under the srcdir matching wildcards,
        # returned in a format to be used for install_data
        def walk_helper(arg, dirname, files):
            if '.svn' in dirname:
                return
            names = []
            lst, wildcards = arg
            for wc in wildcards:
                wc_name = self.opj(dirname, wc)
                for f in files:
                    filename = self.opj(dirname, f)

                    if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                        names.append(filename)
            if names:
                lst.append((dirname, names))

        file_list = []
        recursive = kw.get('recursive', True)
        if recursive:
            os.path.walk(srcdir, walk_helper, (file_list, wildcards))
        else:
            walk_helper((file_list, wildcards),
                        srcdir,
                        [os.path.basename(f) for f in glob.glob(self.opj(srcdir, '*'))])
        return file_list

    def run(self):
        if os.path.isdir(self.dist_dir):  # Erase previous destination dir
            shutil.rmtree(self.dist_dir)

        setup(
            version=self.project_version,
            description=self.project_description,
            name=self.project_name,
            url=self.project_url,
            author=self.author_name,

            # targets to build
            windows=[{
                'script': self.script,
                'icon_resources': [(0, self.icon_file)],
                'copyright': self.copyright
            }],
            options={'py2exe': {'optimize': 2, 'bundle_files': 1, 'compressed': True,
                                'excludes': self.exclude_modules,
                                'dll_excludes': self.exclude_dll,
                                'includes': self.extra_scripts}},
            zipfile=self.zipfile_name,
            data_files=self.extra_datas
            )

        if os.path.isdir('build'):  # Clean up build dir
            shutil.rmtree('build')

if __name__ == '__main__':
    if operator.lt(len(sys.argv), 2):
        sys.argv.append('py2exe')
    BuildExe().run()  # Run generation
    raw_input("Press any key to continue")  # Pause to let user see that things ends
