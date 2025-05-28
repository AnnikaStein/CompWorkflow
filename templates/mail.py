def firstNewsletterEveryone(compName, shortName, fristStorno, deadlineStorno, zeitBis, timeUntil):
    str = f'''------ English Version Below ------

Liebe Teilnehmende,

in {zeitBis} ist es soweit und {compName} findet statt.

Da das Teilnehmerlimit bereits erreicht wurde, möchten wir dich bitten, uns so bald wie möglich mitzuteilen, falls du doch nicht kommen kannst.
So kann jemand von der Warteliste nachrücken! Wenn deine Anmeldung vor {fristStorno} storniert wird, wirst du eine Rückerstattung von 100 % der Anmeldegebühr erhalten. Antworte in diesem Fall einfach auf diese Email.

Viele Grüße

Euer {shortName} Orgateam

--------

Dear participants,

In {timeUntil}, {compName} will take place.

As the participant limit has already been reached, we would like to ask you to let us know as soon as possible in case you cannot attend the competition.
This way someone from the waiting list can get a competitor spot! If your registration is cancelled before {deadlineStorno}, you will receive a 100% refund of the registration fee. In that case, simply answer this email.

Best regards,

Your {shortName} team

'''
    return str

def secondNewsletterEveryone(compName, shortName, fristStorno, deadlineStorno, zeitBis, timeUntil):
    str = f'''------ English Version Below ------

Liebe Teilnehmende,

in {zeitBis} ist es soweit und {compName} findet statt.

Wenn du deine Anmeldung bis zum {fristStorno} stornierst, wirst du eine Rückerstattung von 100 % der Anmeldegebühr erhalten. Antworte in diesem Fall einfach auf diese Email.

Hier nochmal ein Hinweis auf die Whatsapp-Community, in der ihr euch u.a. zur Anreise bzw. Unterkunft zusammenfinden könnt: https://chat.whatsapp.com/EZmTlmsA8id1Ed9sPHScDY

An dieser Stelle geben wir gerne weiter, dass jemand auf der Suche nach einer Fahrgemeinschaft aus dem Raum Mainz ist. Vielleicht findet sich ja jemand, der sich dazu bereiterklärt. :-)

Viele Grüße

Euer {shortName} Orgateam

--------

Dear participants,

In {timeUntil}, {compName} will take place.

If you cancel your registration until {deadlineStorno}, you will receive a 100% refund of the registration fee. In that case, simply answer this email.

Here we would like to announce the Whatsapp-Community again, where you can for example discuss and plan your arrival and accomodation: https://chat.whatsapp.com/EZmTlmsA8id1Ed9sPHScDY

At this point we also want to pass along that someone is looking for car pooling options from the Mainz area. Perhaps someone is willing to help out. :-)

Best regards,

Your {shortName} team

'''
    return str

def finalNewsletterEveryone(compID, compName, shortName, openingDE, openingEN, systemJRS, systemJRSGerman, tutorialWhenDE = None, tutorialWhenEN = None):
    str = f'''------ English Version Below ------

Liebe Teilnehmende,

am Wochenende ist es soweit und {compName} findet statt. In dieser Rundmail findest du wichtige Informationen, bitte lies alle Abschnitte aufmerksam durch.

Wir gehen davon aus, dass du zum Wettbewerb kommst - falls du doch nicht teilnehmen wirst, sag uns bitte Bescheid und antworte auf diese Mail.


Check-In

'''
    if tutorialWhenDE != None:
        str += f'''Wenn dies dein erster WCA Wettbewerb ist: jeder Neuling muss einen gültigen Lichtbildausweis mitbringen aus welchem Name, Nationalität und Geburtsdatum hervorgehen und diesen während einem der Check-In Zeiträume bei den Organisatoren vorzeigen (z.B. Personalausweis, Reisepass, Führerschein, Krankenkassenkarte o.ä.)!
Ohne diese Überprüfung kannst du nicht offiziell teilnehmen und deine Ergebnisse werden nicht erfasst, also bringe bitte ein solches Ausweisdokument mit.

'''
    str += f'''{openingDE}

Alle, die bereits auf einer WCA Competition waren und eine WCA-Id besitzen, müssen nicht unbedingt schon zum Check-In anreisen.


Namensschilder: Bring-Your-Own-Badge

Falls du noch ein Namensschild von einer unserer vergangenen Competitions hast (z.B. RLP Open 2024, Nationals 2024, Mainzelcubing 2025), bringe es gerne zum Wiederverwenden mit - es gibt vor Ort dann ein neues Blatt zum Einlegen, u.a. mit deinen Einteilungen für die ersten Runden.
Wenn dies dein erster Wettbewerb ist oder du noch kein Standard-Plastiknamensschild von einer früheren Competition in unserer Region erhalten hast, erhältst du ein solches neues Bändel samt Badge zum Umhängen. Bitte beim nächsten Mal wieder mitbringen.

Alle Teilnehmer sollten ihr Namensschild tragen, damit es beim Aufrufen zur Teilnahme nicht zu Verwechslungen kommt.


'''
    if tutorialWhenDE != None:
        str += f'''WCA-Regeln und Tutorial

Wir befolgen die Regeln der WCA in der gültigen Fassung, die man unter diesem Link: https://www.worldcubeassociation.org/regulations findet.
Von Neulingen wird erwartet, dass sie sich die Regeln vor ihrer ersten Competition durchlesen!
Zusätzlich bieten wir für Neulinge ein interaktives Tutorial an, um das Teilnehmen und Schiedsrichter-Sein zu üben.
Dieses sogenannte Competitor- und Judging-Tutorial findet {tutorialWhenDE} statt.
Nimm daran teil und ermutige gerne auch etwaige Begleitpersonen wie z.B. Eltern, denn je mehr Personen das Judgen gelernt haben und später mithelfen, umso besser für den Ablauf!
Das Judgen ist für alle Teilnehmer verpflichtend!

'''
    str += f'''Wichtige Links: Zeitplan, Einteilungen, Live-Ergebnisse und mehr

Den allgemeinen Zeitplan mit allen Runden und Pausen findest du online hier: https://www.worldcubeassociation.org/competitions/{compID}#competition-schedule

Deinen eigenen Zeitplan mit deinen persönlichen Einteilungen für die ersten Runden findest du unter diesem Link: https://www.competitiongroups.com/competitions/{compID}

Wir haben Einteilungen für {systemJRSGerman} vorbereitet. Falls du dein Wissen über die verschiedenen Judging-Systeme auffrischen möchtest, lies den Newcomer-Tab und die dort eingetragenen Links durch.

Tipp: bei competitiongroups.com wirst du auch während des Wettbewerbs fortlaufend alle neuen, jetzt noch nicht bekannten Einteilungen zu den Folgerunden finden!

Während des Wettbewerbs werden alle Ergebnisse (nahezu) live eingetragen und du kannst diese hier betrachten: https://live.worldcubeassociation.org/link/competitions/{compID}

Zusätzlich findest du alle weiteren Infos auf der Website der Competition mit zahlreichen Tabs zu verschiedenen Themenbereichen: https://www.worldcubeassociation.org/competitions/{compID}

Dort findest du auch speziell für Neulinge geeignete Tutorials im Newcomer-Tab, also schau dort gerne rein.


Fragen?

Gerne beantworten wir weitere Fragen, stelle sie dazu einfach als Antwort auf diese Mail.


Viele Grüße und bis bald

Euer {shortName} Orgateam

--------

Dear participants,

this weekend {compName} will take place. In this newsletter you will find important information, please read all paragraphs carefully.

We assume that you will participate - but if you can not come after all, please let us know as early as possible by responding to this email.


Check-In

'''
    if tutorialWhenEN != None:
        str += f'''If this is your first WCA Competition: every newcomer is obliged to bring a valid identity document carrying your name, nationality and date of birth. You will need to show this document matching your registration details to the organization team (e.g. passport, driver's licence, medical insurance card etc.)!
Without this verification you can not compete officially and your results will not be recorded, so make sure to bring some form of ID.
'''
    str += f'''{openingEN}

All returning competitors with a WCA Id do not need to arrive early for the check-in.


Nametags: Bring-Your-Own-Badge

If you already have a nametag from one of our previous competitions (e.g. RLP Open 2024, Nationals 2024, Mainzelcubing 2025), please take it with you for reusing it - you'll receive a new paper inlay covering for example your first round assignments.
If this is your first competition or you do not own a standard nametag as used in our region yet, you'll receive a new lanyard and badge. Next time you can use this one again.

All competitors are asked to wear their nametag visibly to reduce possibilities of mix-ups when called to compete.


'''
    if tutorialWhenDE != None:
        str += f'''WCA Regulations and Tutorial

We follow the WCA Regulations in their current version, which can be found here: https://www.worldcubeassociation.org/regulations .
Newcomers are expected to have already read the regulations before their first competition!
Additionally, there will be an interactive tutorial for newcomers to practice how to compete and how to judge.
This so-called Competitor- and Judging-Tutorial will take place {tutorialWhenDE}.
Join this tutorial and also motivate accompanying people (e.g. parents), the more volunteers available who know how to judge and will help us out, the better for the course of the competition!
For competitors, judging is compulsory!

'''
    str += f'''Important links: schedule, group assignments, live results and more

The general schedule with all rounds and breaks is available online: https://www.worldcubeassociation.org/competitions/{compID}#competition-schedule

Your own schedule with your personal assignments for first rounds can be found here: https://www.competitiongroups.com/competitions/{compID}

We have assigned tasks for {systemJRS}. If you need a refresher on the various judging systems, read through the newcomer tab and links contained therein.

Hint: at competitiongroups.com you will also find all future assignments for next rounds, which are not known in advance!

During the competition we will enter all results in (almost) real time and you can inspect them here: https://live.worldcubeassociation.org/link/competitions/{compID}

Further, you can read more on various topics on our website, where we put additional information into extra tabs: https://www.worldcubeassociation.org/competitions/{compID}

There, you will also find specific instructions for newcomers, so feel free to take a look.


Questions?

We are happy to answer further questions, simply ask them by responding to this email.


Best regards and see you soon,

Your {shortName} team

'''
    return str

def aftercomp(compID, contact, compName, shortName, LaF, LaFGerman, surveyLink, partCertLink, systemJRS, systemJRSGerman):
    str = f'''---- English Version Below ----

Liebe Teilnehmer der {compName},

Der Wettbewerb liegt nun einige Tage hinter uns und wir hoffen, dass ihr Spaß hattet und eure Ziele erreichen konntet.

Die Ergebnisse des Turniers wurden bereits in die WCA-Datenbank übertragen und sind hier zu finden:

https://www.worldcubeassociation.org/competitions/{compID}

Für alle, die am Wochenende teilgenommen haben, wurden zudem Teilnahme-Urkunden erstellt, welche eure persönlichen besten Rankings enthalten:

{partCertLink}

Falls ihr persönliche Gegenstände vermisst, wendet euch doch bitte mit einer möglichst genauen Beschreibung an {contact} und wir werden sehen, ob wir euch helfen können.
'''

    if LaFGerman != None:
        str += f'''
Es wurden gefunden:

'''
        for lost in LaFGerman:
            str += f'''- {lost}\n'''

    str += f'''
An dieser Stelle möchten wir uns auch herzlich bei allen bedanken, die uns während des Wochenendes beim {systemJRSGerman} unterstützt haben! Ihr habt einen großen Beitrag dazu geleistet, dass die Competition so erfolgreich verlaufen ist.
Damit wir zukünftige Wettbewerbe in Deutschland noch besser machen können, sind wir sehr an eurem Feedback interessiert. Wir würden uns freuen, wenn ihr dazu die folgende anonyme Umfrage ausfüllen könntet (dauert nur 5-10 min): {surveyLink}

Weitere Turniere in Deutschland findet ihr immer in der Übersicht der WCA unter https://www.worldcubeassociation.org/competitions?&region=Germany

Viele Grüße und hoffentlich bis zur nächsten Comp,

Euer {shortName} Orgateam

--------

Dear participants of {compName},

A few days have passed since the competition took place and we hope that you had fun and accomplished your goals.

The results have already been added to the WCA database and can be found here:

https://www.worldcubeassociation.org/competitions/{compID}

For all those who competed this weekend certificates of participation have been created. Those contain your personal best rankings:

{partCertLink}

If you’re missing any personal belongings, please contact us at {contact} along with a detailed description of the item; we will try our best to help you.
'''

    if LaF != None:
        str += f'''
We found:

'''
        for lost in LaF:
            str += f'''- {lost}\n'''

    str += f'''
At this point we would like to sincerely thank all who supported us during the weekend in {systemJRS}! You helped a lot to run the competition smoothly.
To improve further competitions in Germany, we are interested in your feedback. Therefore, we appreciate if you could fill out the following anonymous survey (takes just 5-10 min): {surveyLink} (you may use Google Translate or similar to fill it out in your native language).

For finding all future tournaments in Germany, be sure to check out the WCA overview at https://www.worldcubeassociation.org/competitions?&region=Germany

Happy cubing and hopefully until the next competition,

Your {shortName} team

'''
    return str
