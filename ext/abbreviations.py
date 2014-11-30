from PyQt4 import QtGui
import json
import ast


class Abbreviations(QtGui.QDialog):

    def __init__(self, parent=None):

        QtGui.QDialog.__init__(self, parent)

        self.parent = parent

        self.lastStart = 0
        self.data = {}

        self.createJson()
        self.initUI()

    def createJson(self):

        try:

            open("abbreviations.json")

        except:

            with open("abbreviations.json", "a") as jsonfile:

                json.dump({"txt": ["text"], "lol": ["laughing out loud"]}, jsonfile)

    def loadJson(self):
        try:

            with open('abbreviations.json') as data_file:

                self.data = json.load(data_file)

        except ValueError:

            popup = QtGui.QMessageBox(self)

            popup.setIcon(QtGui.QMessageBox.Warning)

            popup.setText("Invalid Json file")

            popup.setInformativeText("The abbreviation Json file is not valid.")

            answer = popup.exec_()

            if answer == QtGui.QMessageBox.Warning:
                pass

    def initUI(self):

        # Button to replace the last finding
        replaceButton = QtGui.QPushButton("Replace", self)
        replaceButton.clicked.connect(self.replaceAll)

        # Button to edit the abbreviation list
        editButton = QtGui.QPushButton("Edit abbreviation list", self)
        editButton.clicked.connect(self.test)

        layout = QtGui.QGridLayout()

        layout.addWidget(replaceButton, 1, 0, 1, 2)
        layout.addWidget(editButton, 2, 0, 1, 2)

        replaceButton.setDefault(True)

        self.setGeometry(300, 300, 360, 150)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

    def test(self):
        self.listEditor = ListEditor()
        self.listEditor.show()

    def find(self, query, replaceSize=0):

        reachedEnd = 0

        # Grab the parent's text
        text = str(self.parent.text.toPlainText())

        if text == "" or query == "":
            reachedEnd = 1
            return reachedEnd

        if not replaceSize:
            replaceSize = len(query)

        self.lastStart = text.find(query, self.lastStart)

        # If the find() method didn't return -1 (not found)
        if self.lastStart >= 0:

            end = self.lastStart + replaceSize

            self.moveCursor(self.lastStart, end)

            self.lastStart = self.lastStart + replaceSize

        else:

            # Make the next search start from the begining again
            self.lastStart = 0

            reachedEnd = 1

            self.parent.text.moveCursor(QtGui.QTextCursor.End)

        return reachedEnd

    def replace(self, replaceText):

        # Grab the text cursor
        cursor = self.parent.text.textCursor()

        # Security
        if cursor.hasSelection():

            # We insert the new text, which will override the selected
            # text
            cursor.insertText(replaceText)

            # And set the new cursor
            self.parent.text.setTextCursor(cursor)

    def replaceAll(self):

        self.loadJson()

        for i in self.data:

            self.lastStart = 0
            founds = 0
            replaced = 0
            reachedEnd = 0

            print i, "->", self.data[i]

            if (not self.find(str(i))) or (len(str(self.parent.text.toPlainText())) == len(str(i))):

                self.lastStart = 0

                while not reachedEnd:
                    reachedEnd = self.find(str(i))
                    founds += 1

                print founds
                self.lastStart = 0

                # Replace and find until self.lastStart is 0 again and all of them haven't been replaced
                while founds > replaced:

                    if self.find(str(i)):

                        self.lastStart = 0
                        self.find(str(i))

                    self.replace(self.data[i][0])
                    replaced += 1

    def moveCursor(self, start, end):

        # We retrieve the QTextCursor object from the parent's QTextEdit
        cursor = self.parent.text.textCursor()

        # Then we set the position to the beginning of the last match
        cursor.setPosition(start)

        # Next we move the Cursor by over the match and pass the KeepAnchor parameter
        # which will make the cursor select the the match's text
        cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, end - start)

        # And finally we set this new cursor as the parent's
        self.parent.text.setTextCursor(cursor)


class ListEditor(QtGui.QWidget):

    def __init__(self, parent=None):

        print "init"

        QtGui.QDialog.__init__(self, parent)

        self.parent = parent

        self.initUI()

        self.createJson()
        self.loadJson()

    def initUI(self):

        # The field into which to type the query
        self.abbreviationField = QtGui.QTextEdit(self)
        self.abbreviationField.resize(250, 50)

        # Button to edit the abbreviation list
        doneButton = QtGui.QPushButton("done", self)
        doneButton.clicked.connect(self.save)

        # Button to edit the abbreviation list
        cancelButton = QtGui.QPushButton("cancel", self)
        cancelButton.clicked.connect(self.cancel)

        layout = QtGui.QGridLayout()

        layout.addWidget(self.abbreviationField, 1, 0, 1, 4)
        layout.addWidget(cancelButton, 2, 0, 1, 2)
        layout.addWidget(doneButton, 2, 2, 1, 2)

        doneButton.setDefault(True)

        self.setGeometry(300, 300, 360, 250)
        self.setWindowTitle("Find and Replace")
        self.setLayout(layout)

    def createJson(self):

        try:

            open("abbreviations.json")

        except:

            with open("abbreviations.json", "a") as jsonfile:

                json.dump({"slt": ["salut"], "cmd": ["command"]}, jsonfile)

    def loadJson(self):

        try:

            with open('abbreviations.json') as data_file:

                self.data = json.load(data_file)

            self.abbreviationField.append(str(json.dumps(self.data)))

        except ValueError:
            self.displayJsonError()

    def displayFieldError(self):

        popup = QtGui.QMessageBox(self)

        popup.setIcon(QtGui.QMessageBox.Warning)

        popup.setText("Invalid text field content")

        popup.setInformativeText("The abbreviation text field is not a valid json content.")

        answer = popup.exec_()

        if answer == QtGui.QMessageBox.Warning:
            pass

    def displayJsonError(self):

        popup = QtGui.QMessageBox(self)

        popup.setIcon(QtGui.QMessageBox.Warning)

        popup.setText("Invalid json file")

        popup.setInformativeText("The abbreviation file is not a valid json file.")

        answer = popup.exec_()

        if answer == QtGui.QMessageBox.Warning:
            pass

    def save(self):

        data = []

        try:

            data = ast.literal_eval(str(self.abbreviationField.toPlainText()))
            print data
            self.close()

        except:

            self.displayJsonError()

        jsonData = json.dumps(data, indent=4)

        try:

            jsonFile = open('abbreviations.json', 'w')
            print >> jsonFile, jsonData
            jsonFile.close()

        except:
            pass

    def cancel(self):

        self.close()
