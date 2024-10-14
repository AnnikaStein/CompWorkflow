def main_info(compID, contact, compName):
    md_str = f'''#### 🇬🇧 English
We're happy to welcome you to {compName}! For the first time in this federal state, we offer all official WCA events. And we're looking forward to unofficial events and the aftercomp, everyone is invited!
The organizing team wishes you all a lot of fun.

We have compiled [Frequently Asked Questions and Answers here.](https://www.worldcubeassociation.org/competitions/RheinlandPfalzOpen2025#49038-faq)

#### 🇩🇪 Deutsch
Willkommen zur {compName}! Erstmals bieten wir in diesem Bundesland alle offiziellen WCA-Disziplinen an. Wir freuen uns außerdem auf inoffizielle Events und die Aftercomp, alle sind herzlich eingeladen!
Das Orga-Team wünscht euch allen viel Spaß.

Wir haben [häufig gestellte Fragen und Antworten hier zusammengestellt.](https://www.worldcubeassociation.org/competitions/RheinlandPfalzOpen2025#49038-faq)

![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY5NTAsInB1ciI6ImJsb2JfaWQifX0=--ba949f872b15afba9ca383b8d6a9bb6aa20d6006/Logo_300.png)
'''
    return md_str

def main_register(compID, contact, ppURL, EUR):
    md_str = f'''*(English version below)*

### 🇩🇪 Deutsch
#### ▶️ Wie melde ich mich an?
1. **[Erstelle einen WCA-Account]**
(Dieser Schritt gilt NUR für Newcomer und Teilnehmer ohne WCA-Account): Erstelle [hier](https://www.worldcubeassociation.org/users/sign_up) einen WCA-Account. Bitte nutze eine E-Mailadresse mit funktionsfähigem Posteingang, welche du regelmäßig liest. Das gilt für jede einzelne Person, die teilnehmen möchte und noch keinen solchen Account besitzt. Eine Nachricht an uns reicht nicht aus! Zuschauer / Gäste benötigen keinen und können einfach vorbeikommen.
2. **Zahle die Anmeldegebühr**
Zahle die Anmeldegebühr in Höhe von {EUR} Euro [*über diesen Link*]({ppURL}{EUR}eur) {ppURL}{EUR}eur via PayPal ("Freunde und Familie"). Dies ist jederzeit möglich. Nutze das Kommentarfeld in Paypal für den Namen des Teilnehmers, so wie er auf der Anmeldeseite erscheinen würde.
3. **Fülle das Anmeldeformular aus**
Fülle das Anmeldeformular aus und schicke es ab: [klicke hier](https://www.worldcubeassociation.org/competitions/{compID}/register) - ganz nach unten ans Ende der Seite scrollen. Das Anmeldeformular ist erst zum Anmeldebeginn freigeschaltet. Nutze das Kommentarfeld auf der Anmeldeseite, um uns den Paypal-Nutzernamen/-Mail oder die Transaktionsnummer mitzuteilen.

⚠️ **Wichtig:**

* Bitte aktiviere **nicht** den optionalen Käuferschutz, da hierfür eine Gebühr vom gezahlten Eintrittspreis abgezogen wird. Solltest du später bei Abmeldung eine Rückerstattung benötigen, wird nur der Betrag erstattet, den das Organisationsteam erhalten hat (nach Abzug der Transaktionsgebühren).

* Falls der Name bei der Zahlung und der Name im Anmeldeformular nicht identisch sind, gib bitte den Namen des Teilnehmers im Anmeldeformular im letzten Schritt der Zahlungsprozedur an oder nenne die Transaktionsnummer im Kommentarfeld der WCA-Anmeldeseite. Im Zweifel kannst du uns kontaktieren. *Eine Zahlung gilt erst dann als geleistet, wenn wir diese eindeutig zuordnen können.*

* **Ohne (eindeutig zugeordnete) Zahlung gilt die Anmeldung als nicht vollständig und wird nicht bestätigt.**

* Teilnehmer werden in der Reihenfolge der vollständigen Anmeldung inkl. Zahlung angenommen.


![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY5MjIsInB1ciI6ImJsb2JfaWQifX0=--78885dfbeffab675e61e73ee078ca283a3b80b7b/signup_register_pay_help.001.png)


ℹ️ **Weitere Informationen:**

* Am Anfang der Anmeldephase ist die öffentliche Teilnehmerliste noch nicht repräsentativ, da wir zur manuellen Zahlungszuordnung Zeit benötigen. Wegen dieser Verzögerung kann es sein, dass das Teilnehmerlimit tatsächlich schon vor deiner Anmeldung erreicht wurde.

* Wenn das Teilnehmerlimit bereits erreicht wurde, erhältst du nach Anmeldung und Zahlung einen Platz auf der Warteliste. Danach erhältst du eine E-Mail, sobald ein Platz für dich frei werden sollte. Falls du keinen freien Teilnehmerplatz mehr erlangen solltest, wird die Anmeldegebühr selbstverständlich erstattet.

* Wenn absehbar ist, dass die Warteliste bereits so lang ist, dass weitere Neuanmeldungen nicht mehr angenommen werden, behalten wir uns vor, die Anmeldung früher als angekündigt zu schließen. Vergiss daher nicht, insbesondere wenn du schon früher zahlst, zum Anmeldebeginn das Anmeldeformular auszufüllen!

* Viele weitere Informationen sind auf der Website in den einzelnen Tabs enthalten. Bitte lese sie aufmerksam, besonders, wenn dies dein erster Wettbewerb ist!

* Wenn du Fragen hast, die auch in keinem der weiteren Tabs beantwortet wurden, oder wenn du dich abmelden möchtest, [kontaktiere uns](mailto:{contact}).


#### 👋 Für Gäste
Gäste haben freien Eintritt.


#### 🌳 Bring-your-own-badge
Auf Competitions wird ganz schön viel Müll produziert und die Plastik-Namensschilder tun ihr Übriges. Wer das Namensschild mit Umhängeband (Lanyard) vom letzten Jahr noch hat, darf es gerne mitbringen und ihr erhaltet dann ein neues Schild mit euren Einteilungen zum Einlegen. Natürlich werden wir auch komplett neue Hüllen/Bänder dabei haben.

### 🇬🇧 English
#### ▶️ How do I register?
1. **[Create a WCA account]**
(This step is ONLY for newcomers and competitors without a WCA account:) Create a WCA account [here](https://www.worldcubeassociation.org/users/sign_up). Please use an email with a working inbox and which you read frequently. This needs to be done for every person willing to compete, for whom there is no such account yet. Just informing us about additional competitors is not enough, every competitor needs their own account. Visitors / guests don't need one, they can just come.
2. **Pay the registration fee**
Pay the registration fee of {EUR} Euro by following [*this link*]({ppURL}{EUR}eur) {ppURL}{EUR}eur and proceed with the payment via Paypal ("Sending to a friend"). This is always possible. Use the comment field in paypal to tell us for which competitor this payment is, with the name as it would show up on the registration page.
3. **Fill in the registration form**
Fill and submit the registration form here: [click here](https://www.worldcubeassociation.org/competitions/{compID}/register) - and scroll all the way down to the bottom of the page. This form will be available as soon as registration starts. Use the comment box on the registration form to tell us the Paypal username / email or the transaction number.

⚠️ **Important:**

* Please do **not** activate the optional buyer protection as this will be deducted as a fee from the amount you pay. If you use this and then later on need a refund, you'll be refunded the amount that the organizers received (after deduction of fees).

* If the name of the payment and the name in the registration form are not identical, please enter the name of the competitor as stated in the registration form in the final step of the payment procedure or put the transaction ID into the commment section on the website. In case of doubt, feel free to contact us. *A payment is only considered to be made once we can clearly match it.*

* **The registration is not considered complete and will not be confirmed until a (clearly matched) payment is made.**

* Competitors are accepted in the order of complete registration including payment.


ℹ️ **Further information:**

* At the beginning of the registration period, the public competitor list is not yet representative, because we need time to match all payments manually. Due to this delay, it can happen that by the time you register, the competitor limit has actually been reached already.

* If you have registered and paid but the competitor limit has been reached, you will receive a spot on the waiting list. You will be notified via email once a spot for you becomes available. If you do not move up from the waiting list until registration closes, you will get a full refund.

* Once the waiting list is long enough for us to anticipate that new registrations will likely not move up to the competitor's list, we may close the registration earlier than announced. Hence, don't forget to fill out the registration form, especially if you paid a while ago.

* Much more information is stated on the website in the different tabs. Please read them carefully, especially if it's your first competition.

* If you have questions for which you didn't find an answer on any tab on the website, or if you want to unregister from the competition, [contact us](mailto:{contact}).

#### 👋 For guests
Guests can attend the competition for free.


#### 🌳 Bring-your-own-badge
Competitions produce a lot of waste and plastic nametags contribute to this issue as well. If you still have your nametag with lanyard from last year, please consider reusing it and bring it with you to this competition. You'll receive a new paper inlay including your assignments. Of course we also have new ones with us just in case.
'''
    return md_str

def dpoa(contact):
    md_str = f'''*(English version below)*

# 🇩🇪

## 📸 Foto- und Videoaufnahmen
Auf der Veranstaltung können eventuell **Foto- und Videoaufnahmen**  gemacht werden. Alle Fotos und Videos werden nach der Veranstaltung den Teilnehmenden zur Verfügung gestellt.

**Einverständnis**: Mit deiner Anmeldung erklärst du dich damit einverstanden, dass Fotos oder Videos von dir später veröffentlicht werden können. Gleiches gilt für Gäste, die Teilnehmende begleiten oder generell zuschauen.
**Unter 18 Jahre alt?** Bitte hol dir das Einverständnis deiner Eltern dazu.

**Bedenken**: Sofern du hierzu Bedenken haben solltest oder nicht einverstanden bist, kontaktiere uns bitte [hier](mailto:{contact}), damit wir das entsprechend berücksichtigen können. Selbstverständlich kannst du dich trotzdem direkt anmelden.

---

# 🇬🇧

## 📸 Photo and video recordings
**Photography and video recordings** may be taken at the event. All photos and videos will be made available to participants after the event. The same applies to guests accompanying participants or watching in general.

**Consent**: With your registration you agree that photos or videos of you may be published later.
**Under 18 years old?** Please get your parents' consent for this.

**Concerns**: If you have any concerns about this or do not agree, please contact us [here](mailto:{contact}) so that we can consider this accordingly. Of course you can still sign up directly.
'''
    return md_str

def faq(compID, contact):
    md_str = f'''*(English version below)*

# 🇩🇪

## Häufig gestellte Fragen
### Thema: Anmeldung, Abmeldung
* *Wie kann ich mich registrieren?*
Zunächst solltest du einen **WCA Account** einrichten, falls du noch keinen besitzt (der WCA Account ist nicht dasselbe wie die *WCA ID*, welche du erst nach deinem ersten Wettbewerb für dein persönliches Profil erhältst). Melde dich dann mit diesem Account auf der WCA Website an, navigiere zu diesem Wettbewerb und klicke auf ["Anmelden"](https://www.worldcubeassociation.org/competitions/{compID}/register). Alle weiteren Schritte, auch zur Bezahlung, sind dort erläutert. Die wichtigsten Punkte wiederholen wir gerne hier erneut: erst, wenn du dich angemeldet und die Teilnahmegebühr gezahlt hast, kann deine Anmeldung weiter berücksichtigt werden. Je nachdem, wann du dich anmeldest, gelangst du dann auf die Teilnehmerliste, oder, wenn das Teilnehmerlimit bereits erreicht wurde, auf die Warteliste. Ein Platz auf der Warteliste begründet keinen Anspruch auf Teilnahme am Wettbewerb, und erst, wenn sich jemand anderes abmeldet, können Personen von der Warteliste auf die Teilnehmerliste nachrücken. Welcher Fall für dich zutrifft, erfährst du a) über die Website b) persönliche E-Mails. Stelle daher sicher, dass die angegebene Mailadresse aktuell ist, oder ändere sie bei Bedarf.

* *Ich habe kein PayPal, wie kann ich mich trotzdem anmelden und die Zahlung vornehmen?*
Kontaktiere uns [per Mail](mailto:{contact}), sodass wir dir alternative Zahlungsmethoden zukommen lassen können.

* *Gibt es ein Mindestalter? Gibt es verschiedene Alterskategorien?*
Nein! Zur Sicherheit solltest du allerdings immer deine Erziehungsberechtigten fragen. Alle Teilnehmer treten auf dem gleichen Niveau an, und alle Altersgruppen sind willkommen. In der Regel sind die meisten zwischen 10 und 20 Jahre alt, aber wir haben auch viele Teilnehmer, die älter oder jünger sind!

* *Wie schnell muss ich den Würfel lösen, um teilnehmen zu können?*
Wir empfehlen, dass du dir die Tabs ["Disziplinen"](https://www.worldcubeassociation.org/competitions/{compID}#competition-events) und ["Zeitplan"](https://www.worldcubeassociation.org/competitions/{compID}#competition-schedule) ansiehst - wenn du das Zeitlimit für eine Disziplin, an der du gerne teilnehmen möchtest, normalerweise einhältst, dann bist du schnell genug! Viele Leute kommen nur zu den Wettbewerben, um ihre persönlichen Bestzeiten zu schlagen und Gleichgesinnte zu treffen, ohne die Absicht zu gewinnen oder auch nur die erste Runde zu überstehen.

* *Kann ich Gäste mitbringen?*
Ja! Du hilfst uns bei der Organisation, wenn du bereits bei der Anmeldung die erwartete Anzahl Gäste angibst. Danke!

* *Warum bin ich noch nicht auf der Anmeldeliste?*
Bitte überprüfe ob du die Anweisungen auf der Seite ["Anmelden"](https://www.worldcubeassociation.org/competitions/{compID}/register) komplett befolgt hast. Du könntest auch auf der Warteliste stehen. Das Teilnehmerlimit findest du auf der Seite ["Allgemeine Info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info), und die Anzahl der bereits angemeldeten Teilnehmer kannst du auf der Seite "Teilnehmer" sehen. Wenn du alles richtig gemacht hast und das Teilnehmerlimit noch nicht erreicht wurde, habe bitte etwas Geduld. Wir müssen die Anmeldungen manuell genehmigen und die ehrenamtlichen Organisatoren sind nicht immer ununterbrochen erreichbar. Wenn du der Meinung bist, dass du die Schritte richtig befolgt hast, aber nach einigen Stunden immer noch nicht auf der Anmeldeliste stehst, dann schreib uns bitte eine E-Mail über den Kontaktlink auf dem ["Allgemeine Info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info)-Tab.

* *Ich kann nicht mehr teilnehmen, was muss ich tun?*
Du solltest uns so schnell wie möglich über den Kontaktlink auf der Seite ["Allgemeine Info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info) darüber informieren. Die Wettbewerbe sind in der Regel recht schnell ausgebucht, und wenn du uns mitteilst, dass du nicht mehr teilnehmen kannst, können wir jemanden von der Warteliste nachrücken lassen.

* *Bekomme ich eine Rückerstattung, wenn ich nicht teilnehme?*
Wenn du uns mitteilst, dass du nicht mehr teilnehmen kannst bevor die Frist für die Rückerstattung auf der Seite ["Allgemeine Info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info) vorbei ist, dann erhältst du eine Rückerstattung. Wenn diese Frist verstrichen ist, erhältst du keine Rückerstattung mehr.

### Thema: Wettbewerb
* *Kann ich meine eigenen Würfel für den Wettbewerb verwenden?*
Ja! Auf Wettkämpfen werden keine Würfel zur Verfügung gestellt. Bring also für alle Disziplinen an denen du teilnimmst deine eigene Würfel mit und achte darauf, dass sie den Bedingungen im Regelwerk entsprechen.

* *Kann ich nur zum Zuschauen kommen?*
Ja! Allerdings ist der Veranstaltungsort in der Regel insbesondere morgens ziemlich voll.

* *Ich bin ein Elternteil, was kann ich tun, um mitzuhelfen?*
Wenn du etwas zu tun haben möchtest, dann kannst du beim Judging (schiedsrichtern der Teilnehmer) helfen! Dafür empfehlen wir zuvor das Tutorial für Neulinge gehört zu haben, wann dieses stattfindet steht im Tab ["Zeitplan"](https://www.worldcubeassociation.org/competitions/{compID}#competition-schedule). Wir brauchen so gut wie immer Hilfe und die Abläufe sind wirklich einfach zu befolgen.

* *Wann muss ich beim Wettbewerb ankommen?*
Wenn du ein neuer Teilnehmer bist empfehlen wir dir dringend zum "Tutorial for new competitors" zu kommen, das an beiden Tagen stattfindet. Andernfalls empfehlen wir dir, mindestens 20 Minuten vor deiner ersten Disziplin zu erscheinen (siehe Zeitplan). So hast du genug Zeit, um anzukommen, einen Platz zu finden und dich aufzuwärmen.

* *Was muss ich tun, wenn ich ankomme?*
Wenn du ankommst, finde zuerst den Anmeldungs-Tisch auf, sofern die Anmeldung geöffnet ist. Normalerweise ist dieser direkt am Eingang, und erkannbar durch Namensschilder verteilt über den Tisch. Wenn du ankommst, bevor die Anmeldung geöffnet ist, warte bitte vor dem Raum bis wir die Türen öffnen. Wenn niemand am Anmeldeschalter ist, wende dich bitte an einen Organisator oder Delegate, und wir werden dafür sorgen, dass du dich anmelden kannst.

* *Wann kann ich den Wettbewerb verlassen?*
Du kannst jederzeit gehen, wann immer du willst. Wenn du keine weiteren Disziplinen mehr hast musst du nicht bleiben. Natürlich solltest du aber dann anwesend sein, wenn du zu Aufgaben wie z.B. Scrambling eingeteilt bist. 😉

### Thema: Ergebnisse und Preise
* *Wie kann ich die Ergebnisse einsehen?*
Alle Ergebnisse werden einige Tage nach dem Wettbewerb auf dieser Seite zu finden sein, sobald sie überprüft und hochgeladen wurden. Wenn du nach Live-Ergebnissen suchst, gehe zu [WCA Live](https://live.worldcubeassociation.org/link/competition/{compID}).

* *Gibt es Preise zu gewinnen?*
Üblicherweise erhalten die Podiumsplätze Urkunden, sollten wir darüber hinaus noch Preise überreichen, werden wir dies auf der Website kommunizieren (schaue nach dem 🏆 Auszeichnungen-Tab).

---

# 🇬🇧

## Frequently asked questions
### Topic: Registration, cancellation
* *How can I register?*
First, make sure you have a valid **WCA account** (don't confuse this term with the *WCA-ID* and profile, which, if this is your first competition, you don't have yet). Login with your account, navigate to the competition page and click ["Register"](https://www.worldcubeassociation.org/competitions/{compID}/register). All further steps, including payment, are explained there. The most important points we still want to emphasize here as well: your registration is only complete after you filled the online form and payed the entry fee. Depending on when you registered completely, you can either obtain a spot on the competitor's list directly, or you will be placed on the waiting list if the maximum number of competitors has already been reached earlier. Only if someone cancels their registration, people on the waiting list can move up to the competitor's list. Which variant is the case for you, will be visible on a) the website and b) via personalized emails. Make sure your address is valid / a recent one to receive all information, update your address if necessary.

* *I don't have a PayPal account, how can I pay the registration fee?*
Please reach out us [via email](mailto:{contact}), and we will send you alternative ways to pay the fee.

* *Is there a minimum age? Are there age categories?*
No! But if you are underage, make sure you have asked your parents who give permission for your participation. Everyone competes under the same regulations and there are no age categories, the majority of competitors is aged 10 to 20 years, but we often also have a lot of people younger or older than this age!

* *How fast do I need to be?*
We suggest you take a look at ["Events"](https://www.worldcubeassociation.org/competitions/{compID}#competition-events) and ["Schedule"](https://www.worldcubeassociation.org/competitions/{compID}#competition-schedule) - if you usually make the specified timelimits for the respective categories, you are fast enough! Many people simply come to break their own personal records or meet likeminded cubers, without aiming for the win or proceeding to the next round.

* *Can I bring guests?*
Yes! We'd appreciate if you can inform us about the anticipated number of guests in advance by filling out the respective field in the registration form. Thanks!

* *Why am I not on the competitor's list yet?*
Make sure you followed all steps on the ["Register"](https://www.worldcubeassociation.org/competitions/{compID}/register) page. You might also be on the waiting list. The competitor limit is mentioned on the ["General info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info) tab, and the number of currently registered people can be seen on the "Competitors" page. If you did everything correctly and the competitor limit has not been reached yet, be a little patient. We need to accept all registrations manually and organizers are not available 24/7. If you think that you did all required steps correctly, but even after several hours you can not find yourself on the competitor's list, please contact us via the contact email mentioned at the ["General info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info) tab.

* *I can not participate anymore, what do I need to do?*
First you need to inform us as quickly as possible via the contact email mentioned at the ["General info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info) tab. Usually, competitions fill very quickly, such that we would very much appreciate it if you tell us that you can not participate anymore. Someone else will be happy to move up from the waiting list.

* *Do I get a refund if I can not participate anymore?*
If you inform us about this before the deadline for refunds (see ["General info"](https://www.worldcubeassociation.org/competitions/{compID}#general-info)), you will get a refund. Otherwise, after that deadline, no more refunds are possible.

### Topic: Competition
* *Can I use my own puzzles at the competition?*
Yes! At competitions, we do not provide the puzzles, instead make sure to bring puzzles for the events you are registered for and make sure they fulfil the criteria outlined in the regulations.

* *Can I also just come as a spectator?*
Yes! However, the venue might be crowded at times, especially in the mornings.

* *I am not participating myself, can I still help out with something?*
If you want to do something yourself to help out at the competition, you are welcome to help with judging the competitors' attempts! For this we recommend you join the competitor and judging tutorial in the morning (have a look at the ["Schedule"](https://www.worldcubeassociation.org/competitions/{compID}#competition-schedule)). Usually, we will be happy to receive any help during the day and this task can be learned quite quickly.

* *When do I need to arrive for the competition?*
If you are a new competitor, please already arrive for the "Tutorial for new competitors", which will be held on both days. Otherwise, arriving 20 minutes before your first event (see schedule) is usually sufficient to grab a seat and warm up.

* *What do I need to do when I arrive?*
Once you enter the venue, first stop by the registration desk, if the registration is open. Usually you will find a clearly visible table close to the entrance with several nametags distributed over the whole table. If you arrive before registration opens, please wait outside the building until we open the doors. If you don't arrive during the usual registration times in the morning and no one is currently at the registration desk, contact an organizer or delegate and we make sure you can properly register and receive your nametag.

* *When can I leave the competition?*
You can leave at any time, if you don't participate in any further rounds you don't need to stay until the end. Just don't leave when you're assigned with any task like scrambling. 😉

### Topic: Results and Awards
* *How can I view the results?*
All results will be available right here a couple days after the competition, after they have been checked and uploaded. While the competition is still running, you can view live results via [WCA Live](https://live.worldcubeassociation.org/link/competition/{compID}).

* *Can I win any prizes?*
Usually, podium spots receive certificates. If there will be any prizes on top of that, we will communicate this clearly on the website (look for the 🏆 Awards tab).
'''
    return md_str

def food():
    md_str = f'''*(English version below)*

# 🇩🇪

## Verpflegung
### 🛒 Supermärkte und 🥐 Bäckereien
- Ihr habt die Qual der Wahl, ob ihr mit 5 Minuten Fußweg lieber zu Wasgau, Lidl, Rewe oder Aldi gehen möchtet. Nebenan ist auch eine Rossmann-Filiale.
- Ähnlich sieht es bei den Bäckereien aus: hier gibt es Filialen von z.B. Die Lohners, Wildbadmühle, Wasgau Bäckerei; Aldi und Lidl haben ihre eigenen Backwaren-Selbstbedienungstheken; im Ortskern findet man noch weitere Bäckereien.


### 🍔 Restaurants und ☕️ Cafés
- In Morbach und Umgebung gibt es verschiedene Restaurants, die warme Gerichte anbieten: mit einem Fußweg von etwa 10 - 15 Minuten von der Venue erreicht man sowohl ein Bistro, mehrere Dönerläden (die aber auch andere schnelle Gerichte anbieten), ein Asia-Restaurant, oder Speisegaststätten, die sich auf regionale Küche oder Klassiker spezialisiert haben. Über Lieferando findet man Betriebe, die Essen liefern.
- Wer Lust auf Kaffee, Kuchen oder ein leckeres Eis hat, wird ebenfalls im Ortskern fündig (10 Minuten Fußweg). Persönliche Empfehlungen: Eiscafé Rizzardini, Café Risch und Bäckerei Wildbadmühle (beim Lidl).


### 🥤 Getränke und 🍬 Snacks
- Es wird während des Turniers eine Auswahl an Softdrinks und kleinen Snacks geben.

---

# 🇬🇧

## Food
### 🛒 Supermarkets and 🥐 bakeries
- You are spoilt for choice, whether you prefer to go to Wasgau, Lidl, Rewe or Aldi, all just a 5-minute walk away. There is also a Rossmann shop next door.
- The situation is similar with the bakeries: there are branches of Die Lohners, Wildbadmühle, Wasgau Bäckerei; Aldi and Lidl have their own self-service bakery counters; there are other bakeries in the town centre.


### 🍔 Restaurants and ☕️ cafés
- In Morbach and close-by there are various restaurants offering hot food: within walking distance of 10 - 15 minutes from the venue, you can reach a bistro, several kebap places (they also have other fast food), an asian restaurant, or restaurants specializing in offering regional dishes or typical German classics. With Lieferando (the German "Just Eat") you can find places offering food for delivery.
- If you are a fan of coffee, pastries or some gelato (italian ice cream), you will find some options in the central area of Morbach (walking distance about 10 minutes). Personal recommendations: Eiscafé Rizzardini, Café Risch und Bäckerei Wildbadmühle (next to Lidl market).


### 🥤 Drinks and 🍬 snacks
- At the competition, there will be a selection of soft drinks and small snacks.
'''
    return md_str

def gca():
    md_str = f'''[![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcGNqIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--3f93d32973ed5f3ad112f6e04ddc042b289f871c/Ohne%20Titel.jpg)](https://www.germancubeassociation.de/)

🇩🇪 Alle Wettkämpfe in Deutschland werden von Mitgliedern der [German Cube Association](https://www.germancubeassociation.de/) und weiteren freiwilligen Organisator:innen aus dem ganzen Land durchgeführt. Bitte kommt auf uns zu, wenn auch ihr Interesse am Organisieren eines Turniers habt. Ihr könnt der German Cube Association e.V. auch als Mitglied beitreten! Weitere Informationen erhaltet ihr auf unserer Website.
🇬🇧 All competitions in Germany are run by members of the [German Cube Association](https://www.germancubeassociation.de/) and further voluntary organisers from all over the country. Please approach us if you are interested in hosting a competition. You can also join the German Cube Association e.V. as a member! Further information is available on our website.

🇩🇪 Folge uns auf unseren Social-Media-Seiten, um über die neuesten Inhalte und Ankündigungen auf dem Laufenden zu bleiben!
🇬🇧 Follow us on social media to stay up to date with new information and announcements!

[![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcEVqIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--c465d8deba5509ea829e38813e375c7a7b846b3f/fFmmADt.png)](https://www.instagram.com/germancubeassociation/) [![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBcFVqIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--500c3d9550cb8161085be58845afbf73b50190e7/Bildschirmfoto%202022-09-25%20um%2012.08.41.png)](https://www.twitch.tv/germanonlinecubing2020/)
'''
    return md_str

def important(contact, compID):
    md_str = f'''*(English version below)*

# 🇩🇪

## Informationen für alle
### 🗞️ Länger nicht mehr bei einer Comp gewesen oder nur Zuschauer?
- Dann schau in den 🐣 Newcomer-Tab - dort gibt es aktuelles Informationsmaterial.

### ⚖️📖 Wichtiger Auszug aus den Regeln für ein faires Turnier
- Wir erwarten, dass ihr die [offiziellen Regeln der WCA](https://www.worldcubeassociation.org/regulations/translations/german/) kennt.
- Das Helfen und Judgen während der Competition ist verpflichtend. Im besten Fall hilfst du in den Events, in denen du teilnimmst, jeweils in der anderen Gruppe aus. Das hilft den Zeitplan einzuhalten und den Wettbewerb am Laufen zu behalten.
- Während aller "Blindfolded" Events muss absolute Ruhe im Raum herrschen, da viel Konzentration benötigt wird. Wer sich unterhalten will, verlässt für die Zeit des Events den Raum. Für FMC gilt dies entsprechend.
- Bitte keine Fotos mit Blitz machen, weil dies die Teilnehmer ablenkt. Fotos ohne Blitz sind erlaubt.
- Du darfst deine Versuche filmen, allerdings muss der Kamerabildschirm außer Sicht sein.
- Alle Zuschauer halten mindestens 1,5 Meter Abstand zu den Stationen.
- Wenn eine Runde läuft, warten alle Teilnehmer der Gruppe in dem Wartebereich, bis sie zum Versuch von einem Judge aufgerufen werden.
- Wer während einer Runde über die Scrambles spricht, kann disqualifiziert werden!

### ⚠️ Mögliche Änderung von Runden, Zeitlimits, Cutoffs und Bedingungen zum Weiterkommen
- Die Anzahl Runden, die wir pro Event anbieten können, hängt von der Anzahl der Teilnehmer der ersten Runde ab (siehe [Regel 9m](https://www.worldcubeassociation.org/regulations/#9m), z.B. 100 Teilnehmer um vier Runden durchzuführen). Sollten wir daher die Anzahl geplanter Runden in einer Disziplin tagesaktuell reduzieren müssen, wird die freigewordene Zeit nach Abstimmung unter allen betroffenen Teilnehmern während des Wettbewerbs entweder mit einer anderen Runde, einer Pause, oder einem inoffiziellem Event ersetzt, oder die nachfolgenden Disziplinen verschieben sich entsprechend nach vorne (der Tag endet früher).
- Bei Abweichungen vom Zeitplan (z.B. bei mehr Anmeldungen oder umgekehrt mehr No-Shows als geplant) sind Änderung an Zeitlimits, Cutoffs und Bedingungen zum Weiterkommen möglich, darüber werden wir aber aktuell informieren.

### 📲 (Live-)Ergebnisse und Einteilungen
- Live Ergebnisse sind über [WCA Live](https://live.worldcubeassociation.org/link/competitions/{compID}) verfügbar. Nach dem Wettkampf werden alle Ergebnisse in die Datenbank der WCA hochgeladen, und auf dieser Seite einzusehen sein.
- Einteilungen in Gruppen findet man immer aktuell bei [competitiongroups](https://www.competitiongroups.com/competitions/{compID}). Deine Einteilungen zum Scramblen/Runnen/Judgen sind unbedingt einzuhalten!

### ⏰📌 Mehr zum Ablauf
- Wie für Turniere dieser Größe üblich, werden wir mit mehreren Stages arbeiten. Das sind Bereiche in der Halle, um die gleichzeitig teilnehmenden Personen räumlich aufzuteilen. Achte im Zeitplan auf die Farben. Wenn mehrere Farben zur selben Zeit angezeigt werden, findet die Disziplin auf mehreren Stages statt. Schaue dann online in deinen [Einteilungen](https://www.competitiongroups.com/competitions/{compID}) nach, wohin du gehen musst.
- Du musst nur zu den Events da sein, für die du dich angemeldet hast. Wir empfehlen, mindestens eine halbe Stunde vor deinem ersten Event da zu sein. Wenn du nur an einem Tag kannst, kannst du auch nur an den entsprechenden Events des Tages teilnehmen.
- Bei Unklarheiten oder wichtigen Fragen vor dem Turnier kannst du dich gerne [an das Organisationsteam wenden](mailto:{contact}).

---

# 🇬🇧

## Information for everyone
### 🗞️ Been a while since your last competition or just coming as a spectator?
- Have a look at the 🐣 Newcomer-Tab - there you find up-to-date informative material.

### ⚖️📖 Important excerpt of the regulations for a fair competition
- We expect you to know the [official WCA regulations](https://www.worldcubeassociation.org/regulations/full).
- You are expected to help during the competition. For each event you participate in, you will then need to help out for at least one other group in the same event. If you see a lack of judges or we call your name, please step in and help! This helps the competition run a lot smoother!
- Every time there is any blindfolded event, there has to be complete silence! It requires a lot of concentration, so please be silent. If you need to talk or make noise, please leave the venue room where people are solving to do so.
- No flash photography in the entire venue! Flash is distracting to the competitors. Only pictures without the use of flash are allowed.
- You are also allowed to film your official attempts, as long as the camera's screen is out of sight.
- All spectators must remain at least 1.5 meters away from every solving station.
- When a round is in progress, then all competitors in the current group must wait in the competitor waiting area, until they get called up to solve.
- You are not allowed to talk about the scrambles until the round is done! Otherwise, you might get disqualified.

### ⚠️ Possible change of rounds, time limits, cutoffs and proceeds to next rounds
- The number of rounds we are allowed to offer per event depends on the number of competitors in the first round of each event (see [Regulation 9m](https://www.worldcubeassociation.org/regulations/#9m), e.g. 100 competitors to do four rounds). Should we have to cut a planned round on the day of the competition, we hold a vote among the competitors on how we use the free time slot. There could be another round of a different event, a break, an unofficial event, or just moving all upcoming rounds earlier (then the day would end earlier).
- If we deviate from the planned schedule (e.g. significantly more registrations than anticipated or large number of no-shows), we may change time limits, cutoffs and proceeding conditions for next rounds, but we will inform you about this.

### 📲 (Live) results und assignments
- Live results are available via [WCA Live](https://live.worldcubeassociation.org/link/competitions/{compID}). All results will be uploaded to the WCA database after the competition, and will be available right here.
- Group assignments are updated on [competitiongroups](https://www.competitiongroups.com/competitions/{compID}). Your assignments for scrambling/running/judging absolutely need to be followed!

### ⏰📌 More on the procedures
- As is common for tournaments of this size, we use multiple stages. Those are specific areas in the venue that help us efficiently distribute the competitors who are competing at the same time. Look at the colours on the schedule. If there are multiple colours shown for the same time frame, the event takes place at multiple stages. Have a look at your [assignments online](https://www.competitiongroups.com/competitions/{compID}) to find out to which one you need to go.
- You only need to be present, when you have to compete, in the events that you're registered for! We recommend that you are present half an hour up to one hour before your first event, since the schedule might change. If you can only be present one of the days, then you can only compete in the events on the given date.
- Feel free to [contact the organizers](mailto:{contact}) if you have any uncertainties.
'''
    return md_str

def logo():
    md_str = f'''*(English version below)*

# 🇩🇪

## 🏷️ Logo und T-Shirt-Bestellung
Im Vorfeld versenden wir ein Formular, um ein T-Shirt mit dem Logo des Turniers zu bestellen (optional). Prüfe regelmäßig deine E-Mails!

---

# 🇬🇧

## 🏷️ Logo and t-shirt ordering
Leading up to the tournament we will distribute a form to order a t-shirt with the logo of the competition (non mandatory). Check your email frequently!

![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MzY5NTAsInB1ciI6ImJsb2JfaWQifX0=--ba949f872b15afba9ca383b8d6a9bb6aa20d6006/Logo_300.png)
'''
    return md_str

def news(compID, contact):
    md_str = f'''|  | News |
|------|------|
| XY.10.2024 | 🇬🇧 Website is public! We will keep you up-to-date with all news here, on [Instagram](https://www.instagram.com/speedcubingrlpsaar/) and with the [Whatsapp-Community](https://chat.whatsapp.com/EZmTlmsA8id1Ed9sPHScDY).|
| | 🇩🇪 Die Website wurde veröffentlicht! Wir halten euch hier, bei [Instagram](https://www.instagram.com/speedcubingrlpsaar/) und in der [Whatsapp-Community](https://chat.whatsapp.com/EZmTlmsA8id1Ed9sPHScDY) mit allen Neuigkeiten auf dem Laufenden.|
'''
    return md_str

def newcomer(compID, contact):
    md_str = f'''*(English version below)*

# 🇩🇪

## Informationen für Neulinge
Falls dies dein erstes WCA Turnier sein sollte, beachte bitte die folgenden Punkte:

- Alle Neulinge sind dazu verpflichtet, ein **Ausweisdokument** an der Anmeldung vorzuzeigen (Regulation [2e](https://www.worldcubeassociation.org/regulations/#2e))). Aus dem Dokument müssen Name, Nationalität und Geburtsdatum hervorgehen.
- Alle Neulinge sind eindringlich gebeten, am **Tutorial** (siehe Zeitplan) teilzunehmen. Wir werden euch zur Unterstützung außerdem [diesen Flyer](https://drive.google.com/file/d/1NVO-icO_VEObBvKCGAN-gZo-HXHXEMqY/view?usp=sharing) austeilen.
- Jeder sollte bereits vor dem Turnier mindestens einmal die **[offiziellen Regeln der WCA](https://www.worldcubeassociation.org/regulations/translations/german/)** gelesen haben. Zusätzlich empfehlen wir euch einen Blick in das [WCA Competition Tutorial](https://documents.worldcubeassociation.org/edudoc/competitor-tutorial/tutorial.pdf) bzw. unsere deutschsprachige [Teilnehmer-Anleitung](https://www.germancubeassociation.de/anleitungen/). Dort findet ihr wichtige Infos zum Ablauf und zur Teilnahme am Wettbewerb. Weiterhin bietet zum Beispiel auch [dieses Video-Tutorial](https://www.youtube.com/watch?v=dPL3eV-A0ww) einen guten unterstützenden Einblick.
- Keine Angst: während des Turniers besteht die Möglichkeit, sich mit dem offiziellen Equipment (Stackmat-Timer) vertraut zu machen und Fragen zu stellen.

---

# 🇬🇧

## Newcomer information
If this is your first WCA competition, please pay attention to the following:

- According to Regulation [2e)](https://www.worldcubeassociation.org/regulations/#2e), all newcomers are required to bring some form of **identification document** that shows name, citizenship and date of birth.
- All newcomers are urgently asked to attend the **Tutorial** (see schedule).
- Every competitor should have read the **[official WCA regulations](https://www.worldcubeassociation.org/regulations/full)** at least once before attending the competition! A more condensed version of the important regulations can be found at the [WCA Competition Tutorial](https://documents.worldcubeassociation.org/edudoc/competitor-tutorial/tutorial.pdf). We also recommend [this video guide](https://www.youtube.com/watch?v=dPL3eV-A0ww) for a more visual impression.
- Don't be afraid: there will also be time to test the equipment (for example the official timing device, the Stackmat timer) and discuss the rules if you have questions at the competition.
'''
    return md_str

def travel():
    md_str = f'''*(English version below)*

# 🇩🇪

## Anreise
### 🚙 Mit dem Auto
- Aus dem Rhein-Main-Gebiet: A61 in Richtung Köln. Von der A61 bei Rheinböllen auf die B50/B327 in Richtung Flughafen Frankfurt/Hahn. Dieser Bundesstraße folgen bis nach Morbach, am Kreisel zweite Ausfahrt, nach 200m entweder zur Halle rechts abbiegen oder auf den wesentlich größeren Parkplatz links einbiegen. Reine Fahrzeit Mainz — Morbach: ~1h.
- 🇱🇺 Aus Luxemburg: A64 (E44) in Richtung Trier, A602 in Richtung Köln/Saarbrücken, A1 in Richtung Hermeskeil, an der Ausfahrt Mehring auf die B327 in Richtung Flughafen Frankfurt/Hahn. Reine Fahrzeit Luxemburg (Stadt) — Morbach: ~1h.
- 🇧🇪 Aus Belgien: A60 (E42) in Richtung Frankfurt/Hahn, später wird die Autobahn zur B50. Am Kreisel Ausfahrt zur B327 in Richtung Morbach/Hermeskeil nehmen. Reine Fahrzeit Spa — Morbach: ~1,5h.
- Aus Köln / von Norden: A61 in Richtung Ludwigshafen. Von der A61 bei Rheinböllen auf die B50/B327 in Richtung Flughafen Frankfurt/Hahn. Reine Fahrzeit Köln — Morbach: ~2h.
- Von Süden: via A65 und A61 dann weiter wie im ersten Beispiel, oder via A65 und B10 nach Pirmasens, oder auf A6 Richtung Kaiserslautern, bei Landstuhl auf A62 Richtung Norden, bei Neubrücke/Birkenfeld abfahren und B269 nach Morbach nehmen. Reine Fahrzeit Karlsruhe — Morbach: ~2h.
- 🅿️ **Parkplätze** stehen *kostenlos* zur Verfügung. Einige sind direkt dem Gebäude gegenüber. Am Sportzentrum (der Kreuzung gegenüber) ist ein größerer Parkplatz.


### 🚆🚌 Mit öffentlichen Verkehrsmitteln / andere Möglichkeiten
- Nach Morbach fahren **Busse** von den beiden nächsten Bahnhöfen Idar-Oberstein oder Wittlich (Wengerohr). Gegenüber letztem Jahr sind weitere frühe Verbindungen von / nach Morbach vorhanden:
    - Beachtet die [Fahrpläne des VRT](https://www.vrt-info.de/fahrplanauskunft) und schaut nach [aktuellen Ankündigungen](https://www.vrt-info.de/aktuelles). Die relevanten Linien sind hier zusammengefasst:
      - Bus 840 (Eifel-Hunsrück-Bus) / 845 von Idar-Oberstein (in Idar-Oberstein u.a. Anschluss an RE3 Saarbrücken - **Idar-Oberstein** - Mainz - Frankfurt am Main)
      - Bus 840 (Eifel-Hunsrück-Bus) von Wittlich Wengerohr (in Wittlich Hbf (= Wengerohr) u.a. Anschluss an Züge zwischen Köln / Koblenz - Cochem - **Wengerohr** - Trier - Saarbrücken - Mannheim oder Trier - Luxemburg)
      - Bus 300 von Wittlich nach Bernkastel-Kues, weiter mit Bus 311 von Bernkastel-Kues nach Morbach.
      - Bus 340 von Wittlich nach Morbach, evtl. in Bernkastel-Kues in Bus 341 umsteigen.
    - In Morbach am besten an der Haltestelle "Morbach ZOB" aussteigen, von dort sind es 500m zur Venue.
- Fahrgemeinschaften sind für dieses Turnier auch eine gute Option. Wir haben eine [Community auf Whatsapp](https://chat.whatsapp.com/EZmTlmsA8id1Ed9sPHScDY) für Competitions in der Region gegründet, dort könnt ihr euch z.B. zu Fahrgemeinschaften zusammentun!
- ✈️ Der nächste Flughafen, Frankfurt/Hahn, ist etwa 18km entfernt, es gibt Flughafen-Taxis nach Morbach.


## Unterkunft
Unterkünfte in Morbach und Umgebung findet man z.B. bei [der Tourist-Info](https://www.morbach.de/uebernachten-geniessen/). Auch ein Blick auf z.B. Google Maps, booking.com oder airbnb.de lohnt sich. Neben den Angeboten in und um Morbach hält die Moselregion auch zahlreiche Unterkünfte bereit. Sofern man mit dem Auto anreist, ist dies eine gute Ausweichmöglichkeit.

---

# 🇬🇧

## Getting there

### 🚙 By car
- From the Rhine-Main-Area: A61 in direction Cologne. Exit A61 at Rheinböllen to follow B50/B327 in direction airport Frankfurt/Hahn. Follow this main road to Morbach, take the second exit at the roundabout. After 200m you either head right towards the venue directly, or left, where you will find a large parking lot. Time from Mainz — Morbach: ~1h.
- 🇱🇺 From Luxembourg: E44 (A64 in Germany) in direction Trier, A602 in direction Cologne/Saarbrücken, A1 in direction Hermeskeil, at the exit Mehring change to B327 in direction airport Frankfurt/Hahn, take Morbach's second exit from the B327. Time from Luxembourg (city) — Morbach: ~1h.
- 🇧🇪 From Belgium: take the E42 (A60 in Germany) in direction Frankfurt/Hahn, which changes its name to B50 later on. At the roundabout, take the exit to B327 in direction Morbach/Hermeskeil. Time from Spa — Morbach: ~1,5h.
- From Cologne / from the north: take the A61 in direction Ludwigshafen. Exit A61 at Rheinböllen to follow B50/B327 in direction airport Frankfurt/Hahn. Time from Köln — Morbach: ~2h.
- From the south: via A65 and B10 to Pirmasens or via A6 headed to Kaiserslautern, change at Landstuhl to the A62 in northern direction, exit the freeway at Neubrücke/Birkenfeld and take the B269 to Morbach. Time from Karlsruhe — Morbach: ~2h.
- 🅿️ **Parking spots** are *free of charge*. Some are close to the building across the street. At the sports center (cross the main road at the junction), there are many more spots available.


### 🚆🚌 By public transport
- There are **busses** to Morbach from the closest train stations Idar-Oberstein or Wittlich (Wengerohr). Compared to last year, additional early connections have been added:
    - Please note the [timetable information from the "VRT"](https://www.vrt-info.de/fahrplanauskunft/XSLT_TRIP_REQUEST2?language=en&itdLPxx_contractor=vrt) and [check for announcements here](https://www.vrt-info.de/aktuelles). Relevant bus routes are summarized below:
      - Bus 840 (Eifel-Hunsrück-Bus) / 845 from Idar-Oberstein (in Idar-Oberstein among others connections to RE3 Saarbrücken - **Idar-Oberstein** - Mainz - Frankfurt am Main)
      - Bus 840 (Eifel-Hunsrück-Bus) from Wittlich Wengerohr (in Wittlich Hbf (= Wengerohr) among others connections to Köln / Koblenz - Cochem - **Wengerohr** - Trier - Saarbrücken - Mannheim oder Trier - Luxemburg)
      - Bus 300 from Wittlich to Bernkastel-Kues and Bus 311 from Bernkastel-Kues to Morbach.
      - Bus 340 from Wittlich to Morbach, potentially change to Bus 341 in Bernkastel-Kues.
    - In Morbach you exit at the stop "Morbach ZOB", from where you walk 500m to the venue.
- Carpooling is also a suitable option for this competition. We have created a [Community on Whatsapp](https://chat.whatsapp.com/EZmTlmsA8id1Ed9sPHScDY) for competitions in the area, there you can look for carpooling options and more!
- ✈️ The closest airport, Frankfurt/Hahn, is 18km from the venue, you can book a taxi to Morbach.


## Accomodation
You can find accomodation on the pages of the [local tourist information](https://www.morbach.de/uebernachten-geniessen/). Other places to search for accomodation are for example Google Maps, booking.com or airbnb.de. We can recommend looking for accomodation in the holiday region at the river Mosel, which is a good alternative if you arrive by car.
'''
    return md_str

def waitlist(compID):
    md_str = f'''*(English version below)*

# 🇩🇪

## 📜 Warteliste
Das Teilnehmerlimit wurde erreicht und du hast alle Schritte auf der [Anmeldeseite](https://www.worldcubeassociation.org/competitions/{compID}/register) befolgt, aber stehst nicht auf der Teilnehmerliste? Dann befindest du dich auf der Warteliste.

Im Falle der Abmeldung eines anderen Teilnehmers rücken die Personen auf der Warteliste in der Reihenfolge ihrer **vollständigen Anmeldung** nach. Es entsteht Dir kein Nachteil, solltest Du keinen Platz im Nachrückverfahren erhalten, denn in diesem Fall erhältst Du die Anmeldegebühr selbstverständlich zurück. Wenn die Warteliste zu lang werden sollte, kann die Anmeldung vorzeitig geschlossen werden.

Unten siehst du die aktuelle Warteliste.

---

# 🇬🇧

## 📜 Waiting List
The competitor limit has been reached and you did all required steps outlined on the [registration page](https://www.worldcubeassociation.org/competitions/{compID}/register), but didn't make it onto the competitor list? Then you are on the waiting list.

Moving up from the waiting list will be done in the order of **complete registration** if someone cancels their registration. If you can not obtain a spot through the waiting list procedure, you will of course get a full refund of the registration fee. Should the waiting list become too long, we may close the registration early.


### 📝 Names and positions on the waiting list
(In order of complete registration):

Waiting list is currently empty
1.
'''
    return md_str

def tba():
    md_str = f'''*(English version below)*

# 🇩🇪

Mehr Informationen in Kürze.

---

# 🇬🇧

More Information coming soon.
'''
    return md_str

def aftercomp():
    md_str = f'''*(English version below)*

# 🇩🇪

## 🌅 Aftercomp

Am Freitag- und Samstag-Abend können wir gemeinsam Abendessen bestellen und noch ein paar Stunden mit inoffiziellen Fun-Events verbringen. Ihr seid eingeladen, bis 21:30 Uhr zu bleiben.

---

# 🇬🇧

## 🌅 Aftercomp

Friday and Saturday evening, we can order dinner together and enjoy a couple more hours of unofficial fun events. Feel free to stay until 9:30 pm.
'''
    return md_str

def awards():
    md_str = f''' *(English version below)*

# 🇩🇪

## 🏆 Auszeichnungen
Alle Podiumsplätze erhalten Medaillen und Urkunden.

Außerdem erhalten bestimmte Podiumsplätze zusätzlich Cuboss - Gutscheine, deren Verteilung in der folgenden Tabelle zusammengefasst ist:

| 3x3x3 (Main event) | Alle anderen Disziplinen |
| -------- | -------- |
| 1. 25 € |  1. 20 € |
| 2. 20 € |   |
| 3. 15 € |   |

Ebenfalls ausgezeichnet werden die besten Neulinge des Turniers, wobei der oder die schnellste aus 3x3x3 Runde 1 ebenfalls einen Gutschein erhält (20 €).

---

# 🇬🇧

## 🏆 Awards
All podium finishers receive medals as well as certificates.

Additionally, for selected podium finishers we also hand out cuboss gift cards, their distribution is summarized in the following table:

| 3x3x3 (Main event) | All other events |
| -------- | -------- |
| 1. EUR 25 |  1. EUR 20 |
| 2. EUR 20 |   |
| 3. EUR 15 |   |

Furthermore, the best newcomers will be awarded at the competition, out of those, the fastest in 3x3x3 round 1 will receive a gift card valued EUR 20.
'''
    return md_str

def sponsor(compName):
    md_str = f'''[![](https://cuboss.se/wp-content/uploads/2022/10/logo_400.png)](https://cuboss.com/?r=wca)
### Sponsor - Cuboss

#### ENGLISH

“{compName}” is sponsored by the cube store [Cuboss.com](https://cuboss.com/?r=wca)! Cuboss is an online cube store based in Sweden, specializing in speedcubes and other types of puzzles, with worldwide delivery available from 4,99 €. Cuboss is sponsoring the competition with gift cards for the medalists in the various event as outlined below:

Podium finishers in 3x3x3 are awarded gift cards from Cuboss as below:
1st place: EUR 25
2nd place: EUR 20
3rd place: EUR 15

Medalists in the other events (including FTO and Kilominx!) are awarded gift cards from Cuboss as follows:
1st place: EUR 20

Furthermore, the best newcomer according to 3x3x3 average in round 1 will be awarded a gift card (EUR 20) and each day, we hold a raffle of another gift card before lunch (each valued EUR 20).

#### DEUTSCH

“{compName}” wird vom Cubeshop [Cuboss.com](https://cuboss.com/?r=wca) gesponsort! Cuboss ist ein in Schweden ansässiger Onlineshop, welcher auf Speedcubes und andere Puzzles spezialisiert ist, mit weltweitem Versand bereits ab 4,99€. Cuboss unterstützt den Wettbewerb wie folgt mit Gutscheinen für die Podiumsplätze der jeweiligen Disziplinen:

Das 3x3x3-Podium erhält Cuboss-Gutscheine:
1. Platz: 25 €
2. Platz: 20 €
3. Platz: 15 €

Sieger der anderen Disziplinen (inklusive FTO und Kilominx!) erhalten ebenfalls Gutscheine von Cuboss:
1. Platz: 20 €

Weiterhin geht ein 20 € Gutschein an den schnellsten Neuling im 3x3x3 (Durchschnitt aus Runde 1) und es wird an jedem Tag vor der Mittagspause je ein Gutschein verlost, jeweils im Wert von 20€.
'''
    return md_str

def unofficial(compID):
    md_str = f'''*(English version below)*

# 🇩🇪

## 🎲 Inoffizielle Events

Freitag- und Samstag-Abend (im Rahmen der Aftercomp) wird es Gelegenheit zur Teilnahme an inoffiziellen Events geben.

Wir werden hier in Kürze mehr dazu kommunizieren und auf dem Wettbewerb erklären, wie ihr daran teilnehmen könnt.

Events 🎲
1. Face-Turning Octahedron (FTO)
2. Kilominx

| FTO | Kilominx |
| -------- | -------- |
| Zeitlimit: 5:00.00 | Zeitlimit: 2:30.00 |
| Cutoff: 2:00.00 | Cutoff: 1:20.00 |

Die Ergebnisse werden auf [Cubing Contests](https://cubingcontests.com/) hochgeladen und in die dortigen Rankings aufgenommen. [Results](https://cubingcontests.com/competitions/{compID})

---

# 🇬🇧

## 🎲 Unofficial events

Friday and Saturday evening (during the aftercomp), there will be the option to participate in unofficial events.

Soon we will communicate more on this topic here and let you know during the competition how to compete in those events.

Events 🎲
1. Face-Turning Octahedron (FTO)
2. Kilominx

| FTO | Kilominx |
| -------- | -------- |
| Time Limit: 5:00.00 | Time Limit: 2:30.00 |
| Cutoff: 2:00.00 | Cutoff: 1:20.00 |

The results will be uploaded to [Cubing Contests](https://cubingcontests.com/) and included in the rankings there. [Results](https://cubingcontests.com/competitions/{compID})
'''
    return md_str
