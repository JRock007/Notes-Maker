#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from ext import find
from ext import abbreviations
from ext import datetime
from ext import table
from ext import wordcount


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.filename = ""

        self.changesSaved = True

        self.initUI()

    def initToolbar(self):

        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"), "New", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"), "Open file", self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"), "Save", self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.convertAction = QtGui.QAction(QtGui.QIcon("icons/abbreviations.png"), "Replace abbreviations", self)
        self.convertAction.setStatusTip("Replace abbreviations")
        self.convertAction.setShortcut("Ctrl+I")
        self.convertAction.triggered.connect(abbreviations.Abbreviations(self).show)

        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"), "Print document", self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"), "Page view", self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"), "Find and replace", self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"), "Undo last action", self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"), "Redo last undone thing", self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        tableAction = QtGui.QAction(QtGui.QIcon("icons/table.png"), "Insert table", self)
        tableAction.setStatusTip("Insert table")
        tableAction.setShortcut("Ctrl+T")
        tableAction.triggered.connect(table.Table(self).show)

        imageAction = QtGui.QAction(QtGui.QIcon("icons/image.png"), "Insert image", self)
        imageAction.setStatusTip("Insert image")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)

        bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"), "Insert bullet List", self)
        bulletAction.setStatusTip("Insert bullet list")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"), "Insert numbered List", self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        fontBox = QtGui.QFontComboBox(self)
        fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

        fontSize = QtGui.QSpinBox(self)

        # Will display " pt" after each value
        fontSize.setSuffix(" pt")

        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

        fontSize.setValue(14)

        fontColor = QtGui.QAction(QtGui.QIcon("icons/font-color.png"), "Change font color", self)
        fontColor.triggered.connect(self.fontColorChanged)

        boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"), "Bold", self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"), "Italic", self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"), "Underline", self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QtGui.QAction(QtGui.QIcon("icons/strike.png"), "Strike-out", self)
        strikeAction.triggered.connect(self.strike)

        superAction = QtGui.QAction(QtGui.QIcon("icons/superscript.png"), "Superscript", self)
        superAction.triggered.connect(self.superScript)

        subAction = QtGui.QAction(QtGui.QIcon("icons/subscript.png"), "Subscript", self)
        subAction.triggered.connect(self.subScript)

        alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png"), "Align left", self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"), "Align center", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"), "Align right", self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"), "Align justify", self)
        alignJustify.triggered.connect(self.alignJustify)

        backColor = QtGui.QAction(QtGui.QIcon("icons/highlight.png"), "Change background color", self)
        backColor.triggered.connect(self.highlight)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addWidget(fontBox)
        self.toolbar.addWidget(fontSize)

        self.toolbar.addSeparator()

        self.toolbar.addAction(boldAction)
        self.toolbar.addAction(italicAction)
        self.toolbar.addAction(underlAction)
        self.toolbar.addAction(strikeAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(fontColor)
        self.toolbar.addAction(backColor)

        self.toolbar.addSeparator()

        self.toolbar.addAction(alignLeft)
        self.toolbar.addAction(alignCenter)
        self.toolbar.addAction(alignRight)
        self.toolbar.addAction(alignJustify)

        self.toolbar.addSeparator()

        self.toolbar.addAction(superAction)
        self.toolbar.addAction(subAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.findAction)
        self.toolbar.addAction(self.convertAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(tableAction)
        self.toolbar.addAction(imageAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)

    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        indentAction = QtGui.QAction(QtGui.QIcon("icons/indent.png"), "Indent Area", self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.indentAction)

        dedentAction = QtGui.QAction(QtGui.QIcon("icons/dedent.png"), "Dedent Area", self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.dedentAction)

        dateTimeAction = QtGui.QAction(QtGui.QIcon("icons/calender.png"), "Insert current date/time", self)
        dateTimeAction.setStatusTip("Insert current date/time")
        dateTimeAction.setShortcut("Ctrl+D")
        dateTimeAction.triggered.connect(datetime.DateTime(self).show)

        rightArrowAction = QtGui.QAction(QtGui.QIcon("icons/number.png"), "Insert right arrow", self)
        rightArrowAction.setShortcut(Qt.CTRL + Qt.Key_Right)
        rightArrowAction.triggered.connect(self.rightArrowAction)

        leftArrowAction = QtGui.QAction(QtGui.QIcon("icons/number.png"), "Insert left arrow", self)
        leftArrowAction.setShortcut(Qt.CTRL + Qt.Key_Left)
        leftArrowAction.triggered.connect(self.leftArrowAction)

        wordCountAction = QtGui.QAction(QtGui.QIcon("icons/count.png"), "See word/symbol count", self)
        wordCountAction.setStatusTip("See word/symbol count")
        wordCountAction.setShortcut("Ctrl+Shift+W")
        wordCountAction.triggered.connect(self.wordCount)

        # Add the most important actions to the menubar

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addSeparator()
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addSeparator()
        edit.addAction(self.findAction)
        edit.addAction(self.convertAction)
        edit.addSeparator()
        edit.addAction(indentAction)
        edit.addAction(dedentAction)
        edit.addAction(dateTimeAction)
        edit.addAction(rightArrowAction)
        edit.addAction(leftArrowAction)
        edit.addAction(wordCountAction)

        # Toggling actions for the various bars
        toolbarAction = QtGui.QAction("Toggle Toolbar", self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        view.addAction(toolbarAction)

    def initUI(self):

        self.text = QtGui.QTextEdit(self)

        # Set the tab stop width to around 33 pixels which is
        # more or less 8 spaces
        self.text.setTabStopWidth(33)

        self.initToolbar()
        self.initMenubar()

        self.setCentralWidget(self.text)

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # If the cursor position changes, call the function that displays
        # the line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)

        # We need our own context menu for tables
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)

        self.text.textChanged.connect(self.changed)

        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("Notes Maker")
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.show()
        self.raise_()

    def changed(self):
        self.changesSaved = False

    def closeEvent(self, event):

        if self.changesSaved:

            event.accept()

        else:

            popup = QtGui.QMessageBox(self)

            popup.setIcon(QtGui.QMessageBox.Warning)

            popup.setText("The document has been modified")

            popup.setInformativeText("Do you want to save your changes?")

            saveButton = QtGui.QPushButton("Save")
            discardButton = QtGui.QPushButton("Discard")
            cancelButton = QtGui.QPushButton("Cancel")

            popup.addButton(saveButton, QtGui.QMessageBox.YesRole)
            popup.addButton(discardButton, QtGui.QMessageBox.NoRole)
            popup.addButton(cancelButton, QtGui.QMessageBox.RejectRole)

            popup.setDefaultButton(saveButton)

            answer = popup.exec_()

            if answer == 0:  # Save button
                self.save()

            elif answer == 1:  # Discard button
                event.accept()

            else:  # Cancel button
                event.ignore()

    def rightArrowAction(self):

        # Grab the text cursor
        cursor = self.text.textCursor()

        # Security
        if cursor:

            # We insert the arrow
            cursor.insertText(" -> ")

    def leftArrowAction(self):

        # Grab the text cursor
        cursor = self.text.textCursor()

        # Security
        if cursor:

            # We insert the arrow
            cursor.insertText(" <- ")

    def context(self, pos):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table, if there is one
        table = cursor.currentTable()

        # Above will return 0 if there is no current table, in which case
        # we call the normal context menu. If there is a table, we create
        # our own context menu specific to table interaction
        if table:

            menu = QtGui.QMenu(self)

            appendRowAction = QtGui.QAction("Append row", self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))

            appendColAction = QtGui.QAction("Append column", self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))

            removeRowAction = QtGui.QAction("Remove row", self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtGui.QAction("Remove column", self)
            removeColAction.triggered.connect(self.removeCol)

            insertRowAction = QtGui.QAction("Insert row", self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtGui.QAction("Insert column", self)
            insertColAction.triggered.connect(self.insertCol)

            mergeAction = QtGui.QAction("Merge cells", self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            # Only allow merging if there is a selection
            if not cursor.hasSelection():
                mergeAction.setEnabled(False)

            splitAction = QtGui.QAction("Split cells", self)

            cell = table.cellAt(cursor)

            # Only allow splitting if the current cell is larger
            # than a normal cell
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(), cell.column(), 1, 1))

            else:
                splitAction.setEnabled(False)

            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)

            # Convert the widget coordinates into global coordinates
            pos = self.mapToGlobal(pos)

            # Add pixels for the tool and formatbars, which are not included
            # in mapToGlobal(), but only if the two are currently visible and
            # not toggled by the user

            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            # Move the menu to the new position
            menu.move(pos)

            menu.show()

        else:

            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse, QtCore.QPoint())

            self.text.contextMenuEvent(event)

    def removeRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's row
        table.removeRows(cell.row(), 1)

    def removeCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's column
        table.removeColumns(cell.column(), 1)

    def insertRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertRows(cell.row(), 1)

    def insertCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertColumns(cell.column(), 1)

    def toggleToolbar(self):

        state = self.toolbar.isVisible()

        # Set the visibility to its inverse
        self.toolbar.setVisible(not state)

    def toggleStatusbar(self):

        state = self.statusbar.isVisible()

        # Set the visibility to its inverse
        self.statusbar.setVisible(not state)

    def new(self):

        spawn = Main()

        spawn.show()

    def open(self):

        # Get filename and show only .nmkr files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open File", ".", "(*.nmkr)")

        if self.filename:
            with open(self.filename, "r") as file:
                self.text.setText(file.read())

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save File")

        if self.filename:

            # Append extension if not there yet
            if not self.filename.endsWith(".nmkr"):
                self.filename += ".nmkr"

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename, "w") as file:
                file.write(self.text.toHtml())

            self.changesSaved = True

    def preview(self):

        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def printHandler(self):

        # Open printing dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def cursorPosition(self):

        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line, col))

    def wordCount(self):

        wc = wordcount.WordCount(self)

        wc.getText()

        wc.show()

    def insertImage(self):

        # Get image file name
        filename = QtGui.QFileDialog.getOpenFileName(self, "Insert image", ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")

        if filename:

            # Create image object
            image = QtGui.QImage(filename)

            # Error if unloadable
            if image.isNull():

                popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                          "Image load error",
                                          "Could not load image file!",
                                          QtGui.QMessageBox.Ok,
                                          self)
                popup.show()

            else:

                cursor = self.text.textCursor()

                cursor.insertImage(image, filename)

    def fontColorChanged(self):

        # Get a color from the text dialog
        color = QtGui.QColorDialog.getColor()

        # Set it as the new text color
        self.text.setTextColor(color)

    def highlight(self):

        color = QtGui.QColorDialog.getColor()

        self.text.setTextBackgroundColor(color)

    def bold(self):

        if self.text.fontWeight() == QtGui.QFont.Bold:

            self.text.setFontWeight(QtGui.QFont.Normal)

        else:

            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):

        state = self.text.fontItalic()

        self.text.setFontItalic(not state)

    def underline(self):

        state = self.text.fontUnderline()

        self.text.setFontUnderline(not state)

    def strike(self):

        # Grab the text's format
        fmt = self.text.currentCharFormat()

        # Set the fontStrikeOut property to its opposite
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        # And set the next char format
        self.text.setCurrentCharFormat(fmt)

    def superScript(self):

        # Grab the current format
        fmt = self.text.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.text.setCurrentCharFormat(fmt)

    def subScript(self):

        # Grab the current format
        fmt = self.text.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.text.setCurrentCharFormat(fmt)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def indentAction(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        if cursor.hasSelection():

            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's end
            cursor.setPosition(cursor.anchor())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            # Iterate over lines (diff absolute value)
            for n in range(abs(diff) + 1):

                # Move to start of each line
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)

                # Insert tabbing
                cursor.insertText("\t")

                # And move back up
                cursor.movePosition(direction)

        # If there is no selection, just insert a tab
        else:

            cursor.insertText("\t")

    def handleDedent(self, cursor):

        cursor.movePosition(QtGui.QTextCursor.StartOfLine)

        # Grab the current line
        line = cursor.block().text()

        # If the line starts with a tab character, delete it
        if line.startsWith("\t"):

            # Delete next character
            cursor.deleteChar()

        # Otherwise, delete all spaces until a non-space character is met
        else:
            for char in line[:8]:

                if char != " ":
                    break

                cursor.deleteChar()

    def dedentAction(self):

        cursor = self.text.textCursor()

        if cursor.hasSelection():

            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's last line
            cursor.setPosition(cursor.anchor())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            # Iterate over lines
            for n in range(abs(diff) + 1):

                self.handleDedent(cursor)

                # Move up
                cursor.movePosition(direction)

        else:
            self.handleDedent(cursor)

    def bulletList(self):

        cursor = self.text.textCursor()

        # Insert bulleted list
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()

        # Insert list with numbers
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)


def main():
    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    # Remove line to keep default style from platform
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("cleanlooks"))

    if QtGui.QApplication.style():
        QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

    main()
