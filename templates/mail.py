def firstNewsletterEveryone(compName, shortName, fristStorno, deadlineStorno, zeitBis, timeUntil):
    str = f'''---- English Version Below ------

Liebe Teilnehmende,

in {zeitBis} ist es soweit und die {compName} finden statt.

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

def finalNewsletterEveryone(compID, contact, compName, shortName, fristStorno, deadlineStorno, zeitBis, timeUntil):
    str = f'''---- English Version Below ------

Liebe Teilnehmende,

in {XX} ist es soweit und die {compName} finden statt.

Da das Teilnehmerlimit bereits erreicht wurde, möchten wir dich bitten, uns so bald wie möglich mitzuteilen, falls du doch nicht kommen kannst.
So kann jemand von der Warteliste nachrücken! Wenn deine Anmeldung vor {fristStorno} storniert wird, wirst du eine Rückerstattung von 100 % der Anmeldegebühr erhalten.

Viele Grüße

Euer {shortName} Orgateam

--------

Dear participants,

In {XX}, the {compName} will take place.

As the participant limit has already been reached, we would like to ask you to let us know as soon as possible in case you cannot attend the competition.
This way someone from the waiting list can get a competitor spot! If your registration is cancelled before {deadlineStorno}, you will receive a 100% refund of the registration fee.

Best regards,

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

For all those who competed this weekend participant certificates have been created. Those contain your personal best rankings:

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
