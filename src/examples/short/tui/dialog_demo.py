#!/usr/bin/python3

'''
Demonstration program for pythondialog.

This is a simple program demonstrating the possibilities offered by
the pythondialog module (which is itself a Python interface to the
well-known dialog utility, or any other program compatible with
dialog).

Please have a look at the documentation for the `handle_exit_code'
function in order to understand the somewhat relaxed error checking
policy for pythondialog calls in this demo.
'''

import sys
import os
import os.path
import time
import string
import dialog

FAST_DEMO = 0


def handle_exit_code(d, code):
    if code in (d.DIALOG_CANCEL, d.DIALOG_ESC):
        if code == d.DIALOG_CANCEL:
            msg = 'You chose cancel in the last dialog box. Do you want to exit this demo?'
        else:
            msg = 'You pressed ESC in the last dialog box. Do you want to exit this demo?'
        if d.yesno(msg) == d.DIALOG_OK:
            sys.exit(0)
            return 0
        else:
            return 1


def infobox_demo(d):
    d.infobox(
        'One moment, please. Just wasting some time here to show you the infobox...')
    if FAST_DEMO:
        time.sleep(0.5)
    else:
        time.sleep(3)


def gauge_demo(d):
    d.gauge_start('Progress: 0%', title='Still testing your patience...')
    for i in range(1, 101):
        if i < 50:
            d.gauge_update(i, 'Progress: %d%%' % i, update_text=1)
        elif i == 50:
            d.gauge_update(i, 'Over %d%%. Good.' % i, update_text=1)
        elif i == 80:
            d.gauge_update(
                i, 'Yeah, this boring crap will be over Really Soon Now.', update_text=1)
        else:
            d.gauge_update(i)
        if FAST_DEMO:
            time.sleep(0.01)
        else:
            time.sleep(0.1)
    d.gauge_stop()


def yesno_demo(d):
    return d.yesno('Do you like this demo?')


def msgbox_demo(d, answer):
    if answer == d.DIALOG_OK:
        d.msgbox('Excellent! Press OK to see the source code.')
    else:
        d.msgbox('Well, feel free to send your complaints to /dev/null!')


def textbox_demo(d):
    d.textbox('demo.py', width=76)


def inputbox_demo(d):
    while True:
        (code, answer) = d.inputbox('Whats your name?', init='Snow White')
        if handle_exit_code(d, code):
            break
    return answer


def menu_demo(d):
    while True:
        (code, tag) = d.menu(
            'Whats your favorite day of the week?',
                width=60,
                choices=[('Monday', 'Being the first day of the week...'),
                         ('Tuesday', 'Comes after Monday'),
                         ('Wednesday', 'Before Thursday day'),
                         ('Thursday', 'Itself after Wednesday'),
                         ('Friday', 'The best day of all'),
                         ('Saturday', 'Well, Ive had enough, thanks'),
                         ('Sunday', 'Lets rest a little bit')])
        if handle_exit_code(d, code):
            break
    return tag


def checklist_demo(d):
    while True:
        (code, tag) = d.checklist(text='What sandwich toppings do you like?',
                                  height=15, width=54, list_height=7,
                                  choices=[('Catsup', '', 0),
                                           ('Mustard', '', 0),
                                           ('Pesto', '', 0),
                                           ('Mayonaise', '', 1),
                                           ('Horse radish', '', 1),
                                           ('Sun-dried tomatoes', '', 1)],
                                  title='Do you prefer ham or spam?',
                                  backtitle='And now, for something '
                                  'completely different...')
        if handle_exit_code(d, code):
            break
    return tag


def radiolist_demo(d):
    while True:
        (code, tag) = d.radiolist(
            'Whats your favorite kind of sandwich?',
                width=65,
                choices=[('Hamburger', '2 slices of bread, a steak...', 0),
                         ('Hotdog', 'doesnt bite any more', 0),
                         ('Burrito', 'no se lo que es', 0),
                         ('Doener', 'Huh?', 0),
                         ('Falafel', 'Erm...', 0),
                         ('Bagel', 'Of course!', 0),
                         ('Big Mac', 'Ah, thats easy!', 1),
                         ('Whopper', 'Erm, sorry', 0),
                         ('Quarter Pounder',
                          'called \'le Big Mac\' in France', 0),
                         ('Peanut Butter and Jelly', 'Well, thats your own '
                          'business...', 0),
                         ('Grilled cheese', 'And nothing more?', 0)])
        if handle_exit_code(d, code):
            break
    return tag


def calendar_demo(d):
    while True:
        (code, date) = d.calendar(
            'When do you think Debian sarge will be released?', year=0)
        if handle_exit_code(d, code):
            break
    return date


def passwordbox_demo(d):
    while True:
        (code, password) = d.passwordbox(
            'What is your root password, so that I can crack your system right now?')
        if handle_exit_code(d, code):
            break
    return password


def comment_on_sarge_release_date(day, month, year):
    if year < 2004 or (year == 2004 and month <= 3):
        return 'Mmm... what about a little tour on http://www.debian.org/?'
    elif year == 2004 and month <= 4:
        return 'Damn, how optimistic! You dont know much about Debian, do you?'
    elif year == 2004 and month <= 7:
        return 'Well, good guess. But who knows what the future reserves to us? ;-)'
    elif year == 2004:
        return 'Oh, well. Thats plausible. But please, please dont depress other people with your pronostics... ;-)'
    else:
        return 'Hey, youre a troll! (or do you know Debian *so* well? ;-)'


def scrollbox_demo(d, name, favorite_day, toppings, sandwich, date, password):
    day, month, year = date
    msg = 'Here are some vital statistics about you:'
    d.scrollbox(msg, height=20, width=75, title='Great Report of the Year')


def fselect_demo(d):
    while True:
        root_dir = os.sep
        dir = os.getenv('HOME', root_dir)
        if dir and dir[-1] != os.sep:
            dir = dir + os.sep
        (code, path) = d.fselect(dir, 10, 50,
                                 title='Cute little file to show as in a [tail -f]')
        if handle_exit_code(d, code):
            if not os.path.isfile(path):
                d.scrollbox(
                    'Hmm. Didnt I ask you to select a *file*?', width=50, height=10)
        else:
            break
    return path


def tailbox_demo(d, file):
    d.tailbox(
        file, 20, 60, title='You are brave. You deserve the right to rest, now.')


def demo():
    d = dialog.Dialog(dialog='dialog')
    d.add_persistent_args(['--backtitle', 'pythondialog demo'])
    name = inputbox_demo(d)
    favorite_day = menu_demo(d)
    toppings = checklist_demo(d)
    sandwich = radiolist_demo(d)
    date = calendar_demo(d)
    password = passwordbox_demo(d)
    scrollbox_demo(d, name, favorite_day, toppings, sandwich, date, password)
    d.scrollbox(
        'Haha. You thought it was over. Wrong. Even More fun is to come! (well, depending on your definition on fun) Now, please select a file you would like to see growing (or not...).', width=75)
    file = fselect_demo(d)
    tailbox_demo(d, file)
    d.scrollbox(
        'Now, youre done. No, Im not kidding. So, why the hell are you sitting here instead of rushing on that EXIT button? Ah, you did like the demo. Hmm... are you feeling OK? ;-)',
                width=75)


def main():
    try:
        demo()
    except dialog.error as exc_instance:
        sys.stderr.write('Error:\n\n%s\n' % exc_instance.complete_message())
        sys.exit(1)
    sys.exit(0)

main()
