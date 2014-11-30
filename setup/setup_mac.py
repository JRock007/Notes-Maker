"""
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['NotesMaker.py']

DATA_FILES = [('example.nmkr'),
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

OPTIONS = {'argv_emulation': True,
           'iconfile': 'icon.icns',
           'includes': ['re', 'PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui'],
           'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 'PyQt4.QtScript',
                        'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 'PyQt4.phonon']}

setup(
    name="Notes Maker",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
