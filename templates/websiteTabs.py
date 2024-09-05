def main_info(compID, contact):
    md_str = f'''#### 🇬🇧 English
We're happy to welcome you to Rheinland-Pfalz Open 2025! For the first time in this federal state, we offer all official WCA events. And we're looking forward to unoffical events and the aftercomp, everyone is invited!
​
#### 🇩🇪 Deutsch
Willkommen zur Rheinland-Pfalz Open 2025! Erstmals bieten wir in diesem Bundesland alle offiziellen WCA-Disziplinen an. Wir freuen uns außerdem auf inoffizielle Events und die Aftercomp, alle sind herzlich eingeladen!
​
![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBajFwIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--0f34339ce61c10eae598ba2f23976a7f3bc8543a/LogoTShirt300dpi.png)
'''
    return md_str

def main_register(compID, contact, ppURL, EUR):
    md_str = f'''*(English version below)*
​
### 🇩🇪 Deutsch
#### Wie melde ich mich an?
1. **[Erstelle einen WCA-Account]**
(Dieser Schritt gilt NUR für Newcomer und Teilnehmer ohne WCA-Account): Erstelle [hier](https://www.worldcubeassociation.org/users/sign_up) einen WCA-Account. Bitte nutze eine E-Mailadresse mit funktionsfähigem Posteingang, welche du regelmäßig liest. Das gilt für jede einzelne Person, die teilnehmen möchte und noch keinen solchen Account besitzt. Eine Nachricht an uns reicht nicht aus! Zuschauer / Gäste benötigen keinen und können einfach vorbeikommen.
2. **Zahle die Anmeldegebühr**
Zahle die Anmeldegebühr in Höhe von {EUR} Euro via PayPal [*über diesen Link*]({ppURL}{EUR}eur) ({ppURL}{EUR}eur). Dies ist jederzeit möglich. Nutze das Kommentarfeld in Paypal für den Namen des Teilnehmers, so wie er auf der Anmeldeseite erscheinen würde.
3. **Fülle das Anmeldeformular aus**
Fülle das Anmeldeformular aus und schicke es ab: [klicke hier](https://www.worldcubeassociation.org/competitions/{compID}/register) - ganz nach unten ans Ende der Seite scrollen. Das Anmeldeformular ist erst zum Anmeldebeginn freigeschaltet. Nutze das Kommentarfeld auf der Anmeldeseite, um uns den Paypal-Nutzernamen/-Mail oder die Transaktionsnummer mitzuteilen.
​
**Wichtig:**
* Bitte aktiviere **nicht** den optionalen Käuferschutz, da hierfür eine Gebühr vom gezahlten Eintrittspreis abgezogen wird.
* Falls der Name bei der Zahlung und der Name im Anmeldeformular nicht identisch sind, gib bitte den Namen des Teilnehmers im Anmeldeformular im letzten Schritt der Zahlungsprozedur an oder nenne die Transaktionsnummer im Kommentarfeld der WCA-Anmeldeseite. Im Zweifel kannst du uns kontaktieren. *Eine Zahlung gilt erst dann als geleistet, wenn wir diese eindeutig zuordnen können.*
* **Ohne (eindeutig zugeordnete) Zahlung gilt die Anmeldung als nicht vollständig und wird nicht bestätigt.**
* Teilnehmer werden in der Reihenfolge der vollständigen Anmeldung inkl. Zahlung angenommen.
​

![](https://www.worldcubeassociation.org/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBajVwIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--15151a06f1845351622ff18884f7a991a951f45c/signup_register_pay_help.001.png)
​

**Weitere Informationen:**
* Am Anfang der Anmeldephase ist die öffentliche Teilnehmerliste noch nicht repräsentativ, da wir zur manuellen Zahlungszuordnung Zeit benötigen. Wegen dieser Verzögerung kann es sein, dass das Teilnehmerlimit tatsächlich schon vor deiner Anmeldung erreicht wurde.

* Wenn das Teilnehmerlimit bereits erreicht wurde, erhältst du nach Anmeldung und Zahlung einen Platz auf der Warteliste. Danach erhältst du eine E-Mail, sobald ein Platz für dich frei werden sollte. Falls du keinen freien Teilnehmerplatz mehr erlangen solltest, wird die Anmeldegebühr selbstverständlich erstattet.
​
* Wenn absehbar ist, dass die Warteliste bereits so lang ist, dass weitere Neuanmeldungen nicht mehr angenommen werden, behalten wir uns vor, die Anmeldung früher als angekündigt zu schließen. Vergiss daher nicht, insbesondere wenn du schon früher zahlst, zum Anmeldebeginn das Anmeldeformular auszufüllen!

* Viele weitere Informationen sind auf der Website in den einzelnen Tabs enthalten. Bitte lese sie aufmerksam, besonders, wenn dies dein erster Wettbewerb ist!
​
* Wenn du Fragen hast, die auch in keinem der weiteren Tabs beantwortet wurden, oder wenn du dich abmelden möchtest, [kontaktiere uns](mailto:{contact}).


#### Für Gäste
Gäste haben freien Eintritt.
​
### 🇬🇧 English
#### How do I register?
1. **[Create a WCA account]**
(This step is ONLY for newcomers and competitors without a WCA account:) Create a WCA account [here](https://www.worldcubeassociation.org/users/sign_up). Please use an email with a working inbox and which you read frequently. This needs to be done for every person willing to compete, for whom there is no such account yet. Just informing us about additional competitors is not enough, every competitor needs their own account. Visitors / guests don't need one, they can just come.
2. **Pay the registration fee**
Pay the registration fee of {EUR} Euro by following [*this link*]({ppURL}{EUR}eur) ({ppURL}{EUR}eur) and proceed with the payment via Paypal.
3. **Fill in the registration form**
Fill and submit the registration form here: [click here](https://www.worldcubeassociation.org/competitions/{compID}/register) - and scroll all the way down to the bottom of the page.
​
**Important:**
* Please do **not** activate the optional buyer protection as this will be deducted as a fee from the amount you pay.
* If the name of the payment and the name in the registration form are not identical, please enter the name of the competitor as stated in the registration form in the final step of the payment procedure or put the transaction ID into the commment section on the website. In case of doubt, feel free to contact us. *A payment is only considered to be made once we can clearly match it.*
* **The registration is not considered complete and will not be confirmed until a (clearly matched) payment is made.**
* Competitors are accepted in the order of complete registration including payment. ​


**Further information:**
* At the beginning of the registration period, the public competitor list is not yet representative, because we need time to match all payments manually. Due to this delay, it can happen that by the time you register, the competitor limit has actually been reached already.

* If you have registered and paid but the competitor limit has been reached, you will receive a spot on the waiting list. You will be notified via email once a spot for you becomes available. If you do not move up from the waiting list until registration closes, you will get a full refund.
​
* Once the waiting list is long enough for us to anticipate that new registrations will likely not move up to the competitor's list, we may close the registration earlier than announced. Hence, don't forget to fill out the registration form, especially if you paid a while ago.
​
* Much more information is stated on the website in the different tabs. Please read them carefully, especially if it's your first competition.
​
* If you have questions for which you didn't find an answer on any tabs on the website, or if you want to unregister from the competition, [contact us](mailto:{contact}).


#### For guests
Guests can attend the competition for free.
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

def faq(compID):
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
'''
    return md_str

def food():
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
'''
    return md_str

def gca():
    md_str = f'''GCA
'''
    return md_str

def important(contact):
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
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
'''
    return md_str

def news(compID, contact):
    md_str = f'''#### 🇬🇧 News
September 12th, 2024: Website is public!
​
#### 🇩🇪 Neuigkeiten
12.09.2024: Die Website wurde veröffentlicht!
'''
    return md_str

def newcomer(compID, contact):
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
'''
    return md_str

def travel():
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
'''
    return md_str

def waitlist():
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
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

---

# 🇬🇧
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
| 1. 30 € |  1. 25 € |
| 2. 25 € |   |
| 3. 20 € |   |

Ebenfalls ausgezeichnet werden die besten Neulinge des Turniers, wobei der oder die schnellste aus 3x3x3 Runde 1 ebenfalls einen Gutschein erhält (25 €).

---

# 🇬🇧

## 🏆 Awards
All podium finishers receive medals as well as certificates.

Additionally, for selected podium finishers we also hand out cuboss gift cards, their distribution is summarized in the following table:

| 3x3x3 (Main event) | All other events |
| -------- | -------- |
| 1. EUR 30 |  1. EUR 30 |
| 2. EUR 25 |   |
| 3. EUR 20 |   |

Furthermore, the best newcomers will be awarded at the competition, out of those, the fastest in 3x3x3 round 1 will receive a gift card valued EUR 25.
'''
    return md_str

def sponsor(compName):
    md_str = f'''[![](https://cuboss.se/wp-content/uploads/2022/10/logo_400.png)](https://cuboss.com/?r=wca)
### Sponsor - Cuboss

#### ENGLISH

“{compName}” is sponsored by the cube store [Cuboss.com](https://cuboss.com/?r=wca)! Cuboss is an online cube store based in Sweden, specializing in speedcubes and other types of puzzles, with worldwide delivery available from 4,99 €. Cuboss is sponsoring the competition with gift cards for the medalists in the various event as outlined below:

Podium finishers in 3x3x3 are awarded gift cards from Cuboss as below:
1st place: EUR 30
2nd place: EUR 25
3rd place: EUR 20

Medalists in the other events are awarded gift cards from Cuboss as follows:
1st place: EUR 25

Furthermore, the best newcomer according to 3x3x3 average in round 1 will be awarded a gift card (EUR 25) and we hold a raffle of further gift cards Sunday before lunch (each valued EUR 25).

#### DEUTSCH

“{compName}” wird vom Cubeshop [Cuboss.com](https://cuboss.com/?r=wca) gesponsort! Cuboss ist ein in Schweden ansässiger Onlineshop, welcher auf Speedcubes und andere Puzzles spezialisiert ist, mit weltweitem Versand bereits ab 4,99€. Cuboss unterstützt den Wettbewerb wie folgt mit Gutscheinen für die Podiumsplätze der jeweiligen Disziplinen:

Das 3x3x3-Podium erhält Cuboss-Gutscheine:
1. Platz: 30 €
2. Platz: 25 €
3. Platz: 20 €

Sieger der anderen Disziplinen erhalten ebenfalls Gutscheine von Cuboss:
1. Platz: 25 €

Weiterhin geht ein 25 € Gutschein an den schnellsten Neuling im 3x3x3 (Durchschnitt aus Runde 1) und es gibt am Sonntag vor der Mittagspause eine Verlosung der restlichen Gutscheine, jeweils im Wert von 25€.
'''
    return md_str

def unofficial():
    md_str = f'''*(English version below)*

# 🇩🇪

---

# 🇬🇧
'''
    return md_str
