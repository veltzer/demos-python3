#!/usr/bin/python3

'''
References:
The basic code I stole from and modified:
	https://gist.github.com/evoL/1650115
How to write a custom pygtk widget:
	http://www.pygtk.org/articles/writing-a-custom-widget-using-pygtk/writing-a-custom-widget-using-pygtk.htm
'''

import gobject
import gtk


class EntryMultiCompletion(gtk.Entry):

    def __init__(self):
        gtk.Entry.__init__(self)
        self.completion = gtk.EntryCompletion()
        # customize the matching function to match multiple space
        # separated words
        self.completion.set_match_func(self.match_func, None)
        # handle the match-selected signal, raised when a completion
        # is selected from the popup
        self.completion.connect('match-selected', self.on_completion_match)
        self.set_completion(self.completion)

    def match_func(self, completion, key_string, iter, data):
        model = self.completion.get_model()
        # get the completion strings
        modelstr = model[iter][0]
        # check if the user has typed in a space char,
        # get the last word and check if it matches something
        if ' ' in key_string:
            last_word = key_string.split()[-1]
            return modelstr.startswith(last_word)
        # we have only one word typed
        return modelstr.startswith(key_string)

    def on_completion_match(self, completion, model, iter):
        current_text = self.get_text()
        # if more than a word has been typed, we throw away the
        # last one because we want to replace it with the matching word
        # note: the user may have typed only a part of the entire word
        # and so this step is necessary
        if ' ' in current_text:
            current_text = ' '.join(current_text.split()[:-1])
            # current_text='%s %s'%(current_text, model[iter][0])
        else:
            current_text = model[iter][0]
        # add the matching word
        # current_text='%s %s'%(current_text, model[iter][0])
        # set back the whole text
        self.set_text(current_text)
        # move the cursor at the end
        self.set_position(-1)
        # stop the event propagation
        return True

win = gtk.Window()
win.connect('delete-event', gtk.main_quit)
entrycompl = EntryMultiCompletion()
liststore = gtk.ListStore(gobject.TYPE_STRING)
entrycompl.completion.set_model(liststore)
entrycompl.completion.set_text_column(0)
for word in ['python', 'perl', 'scala', 'c++', 'ruby', 'c#', 'java', 'assembly', 'PHP']:
    liststore.append([word])
win.add(entrycompl)
win.show_all()
'''
The try/except is needed so that if you CTRL+C the application you will not get an exception
with stack trace
'''
try:
    gtk.main()
except:
    pass
