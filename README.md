# HTML2MD
To convert Html files to Github Readme File

Run python3 sample.py

Output Readme File

ms word - html to .doc converter in Python? - Stack Overflow

[ Stack Overflow ](https://stackoverflow.com)

  1. Products 
  2. [Customers](/teams/customers)
  3. [Use cases](/teams/use-cases)

  1. [ Stack Overflow Public questions and answers ](/questions)
  2. [ Teams Private questions and answers for your team ](/teams)
  3. [ Enterprise Private self-hosted questions and answers for your enterprise ](/enterprise)
  4. [ Talent Hire technical talent ](https://stackoverflow.com/talent)
  5. [ Advertising Reach developers worldwide ](https://stackoverflow.com/advertising)

Loading…

  1.   2. [Log in](https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f4226095%2fhtml-to-doc-converter-in-python%2f4227062) [Sign up](https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent)
  3. ### [current community](https://stackoverflow.com)

    * [ Stack Overflow  ](https://stackoverflow.com)

[help](https://stackoverflow.com/help) [chat](https://chat.stackoverflow.com)

    * [ Meta Stack Overflow  ](https://meta.stackoverflow.com)

###  your communities

[Sign
up](https://stackoverflow.com/users/signup?ssrc=site_switcher&returnurl=%2fusers%2fstory%2fcurrent)
or [log
in](https://stackoverflow.com/users/login?ssrc=site_switcher&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f4226095%2fhtml-
to-doc-converter-in-python%2f4227062) to customize your list.

### [more stack exchange communities](https://stackexchange.com/sites)

[company blog](https://stackoverflow.blog)

By using our site, you acknowledge that you have read and understand our
[Cookie Policy](https://stackoverflow.com/legal/cookie-policy), [Privacy
Policy](https://stackoverflow.com/legal/privacy-policy), and our [Terms of
Service](https://stackoverflow.com/legal/terms-of-service/public).

  1. [ Home ](/)
  2.     1. Public
    2. [ Stack Overflow ](/questions)
    3. [ Tags ](/tags)
    4. [ Users ](/users)
    5. [ Jobs ](/jobs?so_medium=StackOverflow&so_source=SiteNav)
  3.     1. Teams

[ What’s this? ](javascript:void\(0\))

    2. [ First 25 Users Free  ](https://stackoverflow.com/teams "Stack Overflow for Teams is a private, secure spot for your organization's questions and answers.")

**Teams**

Q&A for Work

Stack Overflow for Teams is a private, secure spot for you and your coworkers
to find and share information.

[ Learn more ](https://stackoverflow.com/teams)

# [html to .doc converter in Python?](/questions/4226095/html-to-doc-
converter-in-python)

[ Ask Question ](/questions/ask)

Asked 9 years, 1 month ago

Active [5 years, 3 months ago](?lastactivity "2014-10-05 03:18:19Z")

Viewed 12k times

9

3

I am using pisa, which is an HTML to PDF conversion library for Python.

Does there exist the same thing for a Word document: an HTML to .doc
conversion library for Python?

[python](/questions/tagged/python "show questions tagged 'python'") [ms-
word](/questions/tagged/ms-word "show questions tagged 'ms-word'")
[pisa](/questions/tagged/pisa "show questions tagged 'pisa'")

[share](/q/4226095 "short permalink to this question")|[improve this
question](/posts/4226095/edit)

[edited Oct 5 '14 at 3:18](/posts/4226095/revisions "show all edits to this
post")

[![](https://i.stack.imgur.com/z5AzI.png?s=32&g=1)](/users/1402846/pang)

[Pang](/users/1402846/pang)

7,9141616 gold badges6868 silver badges108108 bronze badges

asked Nov 19 '10 at 14:48

[![](https://www.gravatar.com/avatar/f51fc6fe520b9802e519b4e170255daf?s=32&d=identicon&r=PG)](/users/243483/eric)

[Eric](/users/243483/eric)Eric

4,22199 gold badges3232 silver badges4242 bronze badges

  * Why would you want this? MS Word can read HTML. - [MSalters](/users/15416/msalters "147,195 reputation") Nov 19 '10 at 15:08

  * I have the same problem: I have a html that uses pisa to convert to pdf and I want to do the same thing with word. its a big document, ~20 pages, using the same piece of code to generate the html and then export thru pisa or something else would be great. - [Rafael Barros](/users/629187/rafael-barros "2,008 reputation") Jun 12 '12 at 17:24

  * @Eric: Recently, I had the same problem. Just wondering, did you find a solution to convert HTML to Word .docx? Thanks. - [TH339](/users/1231509/th339 "3,424 reputation") Apr 8 '13 at 21:42

  * @tao.hong : Did you manage to solve your problem? I am looking for a suitable open source solution too. Thanks - [sudshekhar](/users/1819007/sudshekhar "1,236 reputation") Sep 4 '15 at 15:10

add a comment  |

##  3 Answers 3

[ active](/questions/4226095/html-to-doc-converter-in-
python?answertab=active#tab-top "Answers with the latest activity first") [
oldest](/questions/4226095/html-to-doc-converter-in-
python?answertab=oldest#tab-top "Answers in the order they were provided") [
votes](/questions/4226095/html-to-doc-converter-in-python?answertab=votes#tab-
top "Answers with the highest score first")

9

You could use win32com from the [pywin32](http://pypi.python.org/pypi/pywin32)
python extensions for windows, to let MS Word convert it for you. A simple
example:

    
    
    import win32com.client
    
    word = win32com.client.Dispatch('Word.Application')
    
    doc = word.Documents.Add('example.html')
    doc.SaveAs('example.doc', FileFormat=0)
    doc.Close()
    
    word.Quit()
    

[share](/a/4227062 "short permalink to this answer")|[improve this
answer](/posts/4227062/edit)

answered Nov 19 '10 at 16:26

[![](https://www.gravatar.com/avatar/87945c64969674b52fd9412edde91885?s=32&d=identicon&r=PG)](/users/601581/steven)

[Steven](/users/601581/steven)Steven

21.9k55 gold badges4747 silver badges4545 bronze badges

add a comment  |

3

Though I am not aware of a direct module that can allow you to convert this,
however:

  1. You can convert ^^HTML^^ to ^^plain text^^ first using the [html2text](http://www.aaronsw.com/2002/html2text/) module.
  2. After that, you can use this the [python-docx](https://github.com/mikemaccana/python-docx) module to convert the text to a ^^doc^^ or a ^^docx^^ file.

[share](/a/4226314 "short permalink to this answer")|[improve this
answer](/posts/4226314/edit)

answered Nov 19 '10 at 15:12

[![](https://www.gravatar.com/avatar/98be1fca8529611a09e77da800faa817?s=32&d=identicon&r=PG)](/users/225312/user225312)

[user225312](/users/225312/user225312)user225312

91.2k5959 gold badges154154 silver badges176176 bronze badges

add a comment  |

2

In case anybody else lands here attempting to convert the other way around,
the above code works, but you need to modify the FileFormat value.

<http://msdn.microsoft.com/en-us/library/ff839952.aspx>

Example: Filtered html is 10, instead of 0.

[share](/a/10755880 "short permalink to this answer")|[improve this
answer](/posts/10755880/edit)

answered May 25 '12 at 14:08

[![](https://www.gravatar.com/avatar/4fc1b3b206b326ecfa77c779d9099e33?s=32&d=identicon&r=PG)](/users/1417571/cooldox)

[Cooldox](/users/1417571/cooldox)Cooldox

2111 bronze badge

add a comment  |

##  Your Answer

Thanks for contributing an answer to Stack Overflow!

  * Please be sure to ^^answer the question^^. Provide details and share your research!

But ^^avoid^^ …

  * Asking for help, clarification, or responding to other answers.
  * Making statements based on opinion; back them up with references or personal experience.

To learn more, see our [tips on writing great answers](/help/how-to-answer).

draft saved

draft discarded

### Sign up or [log
in](/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f4226095%2fhtml-
to-doc-converter-in-python%23new-answer)

Sign up using Google

Sign up using Facebook

Sign up using Email and Password

### Post as a guest

Name

Email

Required, but never shown

### Post as a guest

Name

Email

Required, but never shown

Post Your Answer  Discard

By clicking “Post Your Answer”, you agree to our [terms of
service](https://stackoverflow.com/legal/terms-of-service/public), [privacy
policy](https://stackoverflow.com/legal/privacy-policy) and [cookie
policy](https://stackoverflow.com/legal/cookie-policy)

##  Not the answer you're looking for? Browse other questions tagged
[python](/questions/tagged/python "show questions tagged 'python'") [ms-
word](/questions/tagged/ms-word "show questions tagged 'ms-word'")
[pisa](/questions/tagged/pisa "show questions tagged 'pisa'") or [ask your own
question](/questions/ask).

Blog

  * [ ](https://stackoverflow.blog/2020/01/03/this-week-stackoverflowknows-parties-with-introverts-perfect-cookie-ratio-and-harmless-habits/)

[This Week #StackOverflowKnows Parties With Introverts, Perfect Cookie
Ratio,…](https://stackoverflow.blog/2020/01/03/this-week-stackoverflowknows-
parties-with-introverts-perfect-cookie-ratio-and-harmless-habits/ "This Week
#StackOverflowKnows Parties With Introverts, Perfect Cookie Ratio, and
Harmless !-Habits")

  * [ ](https://stackoverflow.blog/2020/01/07/podcast-matt-cutts-usds-google/)

[Podcast: The Director’s Cutts](https://stackoverflow.blog/2020/01/07/podcast-
matt-cutts-usds-google/)

Featured on Meta

  * [ ](https://meta.stackexchange.com/questions/340906/update-an-agreement-with-monica-cellio)

[Update: an agreement with Monica
Cellio](https://meta.stackexchange.com/questions/340906/update-an-agreement-
with-monica-cellio)

  * [ ](https://meta.stackoverflow.com/questions/392550/2019-a-year-in-moderation)

[2019: a year in
moderation](https://meta.stackoverflow.com/questions/392550/2019-a-year-in-
moderation)

#### Linked

[ 2 ](/q/42779184 "Vote score \(upvotes - downvotes\)") [How can i convert
html to word docx in python?](/questions/42779184/how-can-i-convert-html-to-
word-docx-in-python?noredirect=1)

[ 0 ](/q/48884755 "Vote score \(upvotes - downvotes\)") [Is it possible to
edit MS word doc files with Python?](/questions/48884755/is-it-possible-to-
edit-ms-word-doc-files-with-python?noredirect=1)

[ 0 ](/q/25290041 "Vote score \(upvotes - downvotes\)") [Converting HTML to
DOC with look and feel](/questions/25290041/converting-html-to-doc-with-look-
and-feel?noredirect=1)

[ -1 ](/q/56448985 "Vote score \(upvotes - downvotes\)") [How to generate word
document from html in Django?](/questions/56448985/how-to-generate-word-
document-from-html-in-django?noredirect=1)

[ 0 ](/q/45879736 "Vote score \(upvotes - downvotes\)") [Python: convert
json+html string to .doc](/questions/45879736/python-convert-jsonhtml-string-
to-doc?noredirect=1)

[ 0 ](/q/50524692 "Vote score \(upvotes - downvotes\)") [TinyMCE, Django and
python-docx](/questions/50524692/tinymce-django-and-python-docx?noredirect=1)

#### Related

[4625](/q/89228 "Vote score \(upvotes - downvotes\)")[Calling an external
command from Python](/questions/89228/calling-an-external-command-from-python)

[5474](/q/100003 "Vote score \(upvotes - downvotes\)")[What are metaclasses in
Python?](/questions/100003/what-are-metaclasses-in-python)

[2941](/q/176918 "Vote score \(upvotes - downvotes\)")[Finding the index of an
item given a list containing it in Python](/questions/176918/finding-the-
index-of-an-item-given-a-list-containing-it-in-python)

[1906](/q/387453 "Vote score \(upvotes - downvotes\)")[How do you display code
snippets in MS Word preserving format and syntax
highlighting?](/questions/387453/how-do-you-display-code-snippets-in-ms-word-
preserving-format-and-syntax-highlig)

[5675](/q/394809 "Vote score \(upvotes - downvotes\)")[Does Python have a
ternary conditional operator?](/questions/394809/does-python-have-a-ternary-
conditional-operator)

[2675](/q/415511 "Vote score \(upvotes - downvotes\)")[How to get the current
time in Python](/questions/415511/how-to-get-the-current-time-in-python)

[2058](/q/466345 "Vote score \(upvotes - downvotes\)")[Converting string into
datetime](/questions/466345/converting-string-into-datetime)

[3601](/q/3437059 "Vote score \(upvotes - downvotes\)")[Does Python have a
string 'contains' substring method?](/questions/3437059/does-python-have-a-
string-contains-substring-method)

[1329](/q/5082452 "Vote score \(upvotes - downvotes\)")[String formatting: %
vs. .format](/questions/5082452/string-formatting-vs-format)

[1944](/q/30081275 "Vote score \(upvotes - downvotes\)")[Why is
"1000000000000000 in range(1000000000000001)" so fast in Python
3?](/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-
fast-in-python-3)

####  [ Hot Network Questions ](https://stackexchange.com/questions?tab=hot)

  * [ Is this quadrilateral tangential? ](https://codegolf.stackexchange.com/questions/197713/is-this-quadrilateral-tangential)
  * [ Is this box bonded properly to the ground? ](https://diy.stackexchange.com/questions/181839/is-this-box-bonded-properly-to-the-ground)
  * [ Can you please show me a final atomic model which demonstrates movement of electrons inside it? ](https://physics.stackexchange.com/questions/523349/can-you-please-show-me-a-final-atomic-model-which-demonstrates-movement-of-elect)
  * [ What set are these large quarter circle curved bricks from? ](https://bricks.stackexchange.com/questions/13125/what-set-are-these-large-quarter-circle-curved-bricks-from)
  * [ Can a server certificate expire after its issuer? ](https://serverfault.com/questions/997788/can-a-server-certificate-expire-after-its-issuer)
  * [ What can we do to make UX Stack Exchange Badges Accessible? ](https://ux.stackexchange.com/questions/130881/what-can-we-do-to-make-ux-stack-exchange-badges-accessible)
  * [ Will doing a chargeback on tuition hurt my chances at getting into the same university for grad school? ](https://academia.stackexchange.com/questions/142445/will-doing-a-chargeback-on-tuition-hurt-my-chances-at-getting-into-the-same-univ)
  * [ Integer points of one Mordell equation ](https://mathoverflow.net/questions/349819/integer-points-of-one-mordell-equation)
  * [ My email address is being used to enroll for online services. Should I be concerned? ](https://security.stackexchange.com/questions/223737/my-email-address-is-being-used-to-enroll-for-online-services-should-i-be-concer)
  * [ Is stealing the moon actually possible? ](https://worldbuilding.stackexchange.com/questions/164879/is-stealing-the-moon-actually-possible)
  * [ Dealing with a cheapskate employer ](https://workplace.stackexchange.com/questions/150828/dealing-with-a-cheapskate-employer)
  * [ What should a low-level employee do when contacted by a salesman? ](https://workplace.stackexchange.com/questions/150734/what-should-a-low-level-employee-do-when-contacted-by-a-salesman)
  * [ Why should 'boneheaded' exceptions not be caught, especially in server code? ](https://softwareengineering.stackexchange.com/questions/403318/why-should-boneheaded-exceptions-not-be-caught-especially-in-server-code)
  * [ Company wants me to apply for my own corporate credit card - is this normal? ](https://workplace.stackexchange.com/questions/150770/company-wants-me-to-apply-for-my-own-corporate-credit-card-is-this-normal)
  * [ Handle bar rotates on its own. Can’t screw the screw all the way down ](https://bicycles.stackexchange.com/questions/65755/handle-bar-rotates-on-its-own-can-t-screw-the-screw-all-the-way-down)
  * [ Generate a Nine-Ball Pool rack ](https://codegolf.stackexchange.com/questions/197677/generate-a-nine-ball-pool-rack)
  * [ What are the advantages of an electron-electron collider vs. An elec./positron one? Has one ever been built? ](https://physics.stackexchange.com/questions/523557/what-are-the-advantages-of-an-electron-electron-collider-vs-an-elec-positron-o)
  * [ 8080 vs. 8086 - Are 16 Bit CPUs bloaty by nature? ](https://retrocomputing.stackexchange.com/questions/13290/8080-vs-8086-are-16-bit-cpus-bloaty-by-nature)
  * [ Habitable Planet with Highly Eliptical Orbit ](https://worldbuilding.stackexchange.com/questions/164919/habitable-planet-with-highly-eliptical-orbit)
  * [ Drum fill generator ](https://codegolf.stackexchange.com/questions/197743/drum-fill-generator)
  * [ How to generate random integers between 1 and 4 that have a specific mean? ](https://stats.stackexchange.com/questions/443445/how-to-generate-random-integers-between-1-and-4-that-have-a-specific-mean)
  * [ Good way to remove something from a bathroom sink overflow drain? ](https://diy.stackexchange.com/questions/181694/good-way-to-remove-something-from-a-bathroom-sink-overflow-drain)
  * [ Avoiding zeros in ArrayReshape ](https://mathematica.stackexchange.com/questions/212466/avoiding-zeros-in-arrayreshape)
  * [ Whether 16 schools are too many for a professor to provider rec letter? ](https://academia.stackexchange.com/questions/142502/whether-16-schools-are-too-many-for-a-professor-to-provider-rec-letter)

more hot questions

[ Question feed ](/feeds/question/4226095 "Feed of this question and its
answers")

#  Subscribe to RSS

Question feed

To subscribe to this RSS feed, copy and paste this URL into your RSS reader.

![](/posts/4226095/ivc/ba7d)

lang-py

[](https://stackoverflow.com)

##### [Stack Overflow](https://stackoverflow.com)

  * [Questions](/questions)
  * [Jobs](https://stackoverflow.com/jobs)
  * [Developer Jobs Directory](https://stackoverflow.com/jobs/directory/developer-jobs)
  * [Salary Calculator](https://stackoverflow.com/jobs/salary)
  * [Help](/help)
  * Mobile

##### [Products](https://stackoverflowbusiness.com)

  * [Teams](https://stackoverflow.com/teams)
  * [Talent](https://stackoverflow.com/talent)
  * [Advertising](https://stackoverflow.com/advertising)
  * [Enterprise](https://stackoverflow.com/enterprise)

##### [Company](https://stackoverflow.com/company/about)

  * [About](https://stackoverflow.com/company/about)
  * [Press](https://stackoverflow.com/company/press)
  * [Work Here](https://stackoverflow.com/company/work-here)
  * [Legal](https://stackoverflow.com/legal)
  * [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
  * [Contact Us](https://stackoverflow.com/company/contact)

##### [Stack Exchange  
Network](https://stackexchange.com)

  * Technology
  * Life / Arts
  * Culture / Recreation
  * Science
  * Other

  * [Stack Overflow](https://stackoverflow.com "professional and enthusiast programmers")
  * [Server Fault](https://serverfault.com "system and network administrators")
  * [Super User](https://superuser.com "computer enthusiasts and power users")
  * [Web Applications](https://webapps.stackexchange.com "power users of web applications")
  * [Ask Ubuntu](https://askubuntu.com "Ubuntu users and developers")
  * [Webmasters](https://webmasters.stackexchange.com "pro webmasters")
  * [Game Development](https://gamedev.stackexchange.com "professional and independent game developers")

  * [TeX - LaTeX](https://tex.stackexchange.com "users of TeX, LaTeX, ConTeXt, and related typesetting systems")
  * [Software Engineering](https://softwareengineering.stackexchange.com "professionals, academics, and students working within the systems development life cycle")
  * [Unix & Linux](https://unix.stackexchange.com "users of Linux, FreeBSD and other Un*x-like operating systems")
  * [Ask Different (Apple)](https://apple.stackexchange.com "power users of Apple hardware and software")
  * [WordPress Development](https://wordpress.stackexchange.com "WordPress developers and administrators")
  * [Geographic Information Systems](https://gis.stackexchange.com "cartographers, geographers and GIS professionals")
  * [Electrical Engineering](https://electronics.stackexchange.com "electronics and electrical engineering professionals, students, and enthusiasts")

  * [Android Enthusiasts](https://android.stackexchange.com "enthusiasts and power users of the Android operating system")
  * [Information Security](https://security.stackexchange.com "information security professionals")
  * [Database Administrators](https://dba.stackexchange.com "database professionals who wish to improve their database skills and learn from others in the community")
  * [Drupal Answers](https://drupal.stackexchange.com "Drupal developers and administrators")
  * [SharePoint](https://sharepoint.stackexchange.com "SharePoint enthusiasts")
  * [User Experience](https://ux.stackexchange.com "user experience researchers and experts")
  * [Mathematica](https://mathematica.stackexchange.com "users of Wolfram Mathematica")

  * [Salesforce](https://salesforce.stackexchange.com "Salesforce administrators, implementation experts, developers and anybody in-between")
  * [ExpressionEngine® Answers](https://expressionengine.stackexchange.com "administrators, end users, developers and designers for ExpressionEngine® CMS")
  * [Stack Overflow em Portugues](https://pt.stackoverflow.com "programadores profissionais e entusiastas")
  * [Blender](https://blender.stackexchange.com "people who use Blender to create 3D graphics, animations, or games")
  * [Network Engineering](https://networkengineering.stackexchange.com "network engineers")
  * [Cryptography](https://crypto.stackexchange.com "software developers, mathematicians and others interested in cryptography")
  * [Code Review](https://codereview.stackexchange.com "peer programmer code reviews")

  * [Magento](https://magento.stackexchange.com "users of the Magento e-Commerce platform")
  * [Software Recommendations](https://softwarerecs.stackexchange.com "people seeking specific software recommendations")
  * [Signal Processing](https://dsp.stackexchange.com "practitioners of the art and science of signal, image and video processing")
  * [Emacs](https://emacs.stackexchange.com "those using, extending or developing Emacs")
  * [Raspberry Pi](https://raspberrypi.stackexchange.com "users and developers of hardware and software for Raspberry Pi")
  * [Stack Overflow на русском](https://ru.stackoverflow.com "программистов")
  * [Code Golf](https://codegolf.stackexchange.com "programming puzzle enthusiasts and code golfers")

  * [Stack Overflow en español](https://es.stackoverflow.com "programadores y profesionales de la informática")
  * [Ethereum](https://ethereum.stackexchange.com "users of Ethereum, the decentralized application platform and smart contract enabled blockchain")
  * [Data Science](https://datascience.stackexchange.com "Data science professionals, Machine Learning specialists, and those interested in learning more about the field")
  * [Arduino](https://arduino.stackexchange.com "developers of open-source hardware and software that is compatible with Arduino")
  * [Bitcoin](https://bitcoin.stackexchange.com "Bitcoin crypto-currency enthusiasts")
  * [Software Quality Assurance & Testing](https://sqa.stackexchange.com "software quality control experts, automation engineers, and software testers")
  * [Sound Design](https://sound.stackexchange.com "sound engineers, producers, editors, and enthusiasts")

  * [Windows Phone](https://windowsphone.stackexchange.com "enthusiasts and power users of Windows Phone OS")
  * [ **more (27)** ](https://stackexchange.com/sites#technology)

  * [Photography](https://photo.stackexchange.com "professional, enthusiast and amateur photographers")
  * [Science Fiction & Fantasy](https://scifi.stackexchange.com "science fiction and fantasy enthusiasts")
  * [Graphic Design](https://graphicdesign.stackexchange.com "Graphic Design professionals, students, and enthusiasts")
  * [Movies & TV](https://movies.stackexchange.com "movie and tv enthusiasts")
  * [Music: Practice & Theory](https://music.stackexchange.com "musicians, students, and enthusiasts")
  * [Worldbuilding](https://worldbuilding.stackexchange.com "writers/artists using science, geography and culture to construct imaginary worlds and settings")
  * [Video Production](https://video.stackexchange.com "engineers, producers, editors, and enthusiasts spanning the fields of video, and media creation")

  * [Seasoned Advice (cooking)](https://cooking.stackexchange.com "professional and amateur chefs")
  * [Home Improvement](https://diy.stackexchange.com "contractors and serious DIYers")
  * [Personal Finance & Money](https://money.stackexchange.com "people who want to be financially literate")
  * [Academia](https://academia.stackexchange.com "academics and those enrolled in higher education")
  * [Law](https://law.stackexchange.com "legal professionals, students, and others with experience or interest in law")
  * [Physical Fitness](https://fitness.stackexchange.com "physical fitness professionals, athletes, trainers, and those providing health-related needs")
  * [Gardening & Landscaping](https://gardening.stackexchange.com "gardeners and landscapers")

  * [Parenting](https://parenting.stackexchange.com "parents, grandparents, nannies and others with a parenting role")
  * [ **more (11)** ](https://stackexchange.com/sites#lifearts)

  * [English Language & Usage](https://english.stackexchange.com "linguists, etymologists, and serious English language enthusiasts")
  * [Skeptics](https://skeptics.stackexchange.com "scientific skepticism")
  * [Mi Yodeya (Judaism)](https://judaism.stackexchange.com "those who base their lives on Jewish law and tradition and anyone interested in learning more")
  * [Travel](https://travel.stackexchange.com "road warriors and seasoned travelers")
  * [Christianity](https://christianity.stackexchange.com "committed Christians, experts in Christianity and those interested in learning more")
  * [English Language Learners](https://ell.stackexchange.com "speakers of other languages learning English")
  * [Japanese Language](https://japanese.stackexchange.com "students, teachers, and linguists wanting to discuss the finer points of the Japanese language")

  * [Chinese Language](https://chinese.stackexchange.com "students, teachers, and linguists wanting to discuss the finer points of the Chinese language")
  * [French Language](https://french.stackexchange.com "students, teachers, and linguists wanting to discuss the finer points of the French language")
  * [German Language](https://german.stackexchange.com "speakers of German wanting to discuss the finer points of the language and translation")
  * [Biblical Hermeneutics](https://hermeneutics.stackexchange.com "professors, theologians, and those interested in exegetical analysis of biblical texts")
  * [History](https://history.stackexchange.com "historians and history buffs")
  * [Spanish Language](https://spanish.stackexchange.com "linguists, teachers, students and Spanish language enthusiasts in general wanting to discuss the finer points of the language")
  * [Islam](https://islam.stackexchange.com "Muslims, experts in Islam, and those interested in learning more about Islam")

  * [Русский язык](https://rus.stackexchange.com "лингвистов и энтузиастов русского языка")
  * [Russian Language](https://russian.stackexchange.com "students, teachers, and linguists wanting to discuss the finer points of the Russian language")
  * [Arqade (gaming)](https://gaming.stackexchange.com "passionate videogamers on all platforms")
  * [Bicycles](https://bicycles.stackexchange.com "people who build and repair bicycles, people who train cycling, or commute on bicycles")
  * [Role-playing Games](https://rpg.stackexchange.com "gamemasters and players of tabletop, paper-and-pencil role-playing games")
  * [Anime & Manga](https://anime.stackexchange.com "anime and manga fans")
  * [Puzzling](https://puzzling.stackexchange.com "those who create, solve, and study puzzles")

  * [Motor Vehicle Maintenance & Repair](https://mechanics.stackexchange.com "mechanics and DIY enthusiast owners of cars, trucks, and motorcycles")
  * [Board & Card Games](https://boardgames.stackexchange.com "people who like playing board games, designing board games or modifying the rules of existing board games")
  * [Bricks](https://bricks.stackexchange.com "LEGO® and building block enthusiasts")
  * [Homebrewing](https://homebrew.stackexchange.com "dedicated home brewers and serious enthusiasts")
  * [Martial Arts](https://martialarts.stackexchange.com "students and teachers of all martial arts")
  * [The Great Outdoors](https://outdoors.stackexchange.com "people who love being outdoors enjoying nature and wilderness, and learning about the required skills and equipment")
  * [Poker](https://poker.stackexchange.com "serious players and enthusiasts of poker")

  * [Chess](https://chess.stackexchange.com "serious players and enthusiasts of chess")
  * [Sports](https://sports.stackexchange.com "participants in team and individual sport activities")
  * [ **more (16)** ](https://stackexchange.com/sites#culturerecreation)

  * [MathOverflow](https://mathoverflow.net "professional mathematicians")
  * [Mathematics](https://math.stackexchange.com "people studying math at any level and professionals in related fields")
  * [Cross Validated (stats)](https://stats.stackexchange.com "people interested in statistics, machine learning, data analysis, data mining, and data visualization")
  * [Theoretical Computer Science](https://cstheory.stackexchange.com "theoretical computer scientists and researchers in related fields")
  * [Physics](https://physics.stackexchange.com "active researchers, academics and students of physics")
  * [Chemistry](https://chemistry.stackexchange.com "scientists, academics, teachers, and students in the field of chemistry")
  * [Biology](https://biology.stackexchange.com "biology researchers, academics, and students")

  * [Computer Science](https://cs.stackexchange.com "students, researchers and practitioners of computer science")
  * [Philosophy](https://philosophy.stackexchange.com "those interested in the study of the fundamental nature of knowledge, reality, and existence")
  * [Linguistics](https://linguistics.stackexchange.com "professional linguists and others with an interest in linguistic research and theory")
  * [Psychology & Neuroscience](https://psychology.stackexchange.com "practitioners, researchers, and students in cognitive science, psychology, neuroscience, and psychiatry")
  * [Computational Science](https://scicomp.stackexchange.com "scientists using computers to solve scientific problems")
  * [ **more (8)** ](https://stackexchange.com/sites#science)

  * [Meta Stack Exchange](https://meta.stackexchange.com "meta-discussion of the Stack Exchange family of Q&A websites")
  * [Stack Apps](https://stackapps.com "apps, scripts, and development with the Stack Exchange API")
  * [API](https://api.stackexchange.com "programmatic interaction with Stack Exchange sites")
  * [Data](https://data.stackexchange.com "querying Stack Exchange data using SQL")

  * [Blog](https://stackoverflow.blog?blb=1)
  * [Facebook](https://www.facebook.com/officialstackoverflow/)
  * [Twitter](https://twitter.com/stackoverflow)
  * [LinkedIn](https://linkedin.com/company/stack-overflow)

site design / logo (C) 2020 Stack Exchange Inc; user contributions licensed
under [cc by-sa 4.0](https://creativecommons.org/licenses/by-sa/4.0/) with
[attribution required](https://stackoverflow.blog/2009/06/25/attribution-
required/). rev 2020.1.3.35708

Stack Overflow works best with JavaScript enabled
![](https://pixel.quantserve.com/pixel/p-c1rF4kxgLUzNc.gif)
