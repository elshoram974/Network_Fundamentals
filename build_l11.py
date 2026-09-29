import lesson_lib
from lesson_lib import bi, bl, h2, src, extra, img, cli, diagram, Q, build, T

num = 11
pct = 100 # Unit 2 Completed (11/11)
title = "User Mode and Privileged Mode Security"
sub = ("Securing Cisco console, enable mode, password encryption types, secrets, and AAA", "تأمين أوضاع سيسكو: حماية الكونسول، كلمات مرور التمكين، أنواع التشفير، وخوادم AAA")
chip_en = "Unit 2: Network Fundamentals — Lesson 11 / 11 (Completed)"
chip_ar = "الوحدة الثانية: أساسيات الشبكات — الدرس 11 من 11 (مكتمل)"

toc_items = [
    ("user-mode", "User Mode Security (Console)", "أمان وضع المستخدم (User EXEC)"),
    ("enable-mode", "Enable Mode Security", "أمان وضع التمكين (Privileged EXEC)"),
    ("password-encryption", "Service Password-Encryption", "تشفير كلمات المرور (Type 7)"),
    ("secrets", "Strong Secrets & Hashing Types", "حماية Secret وأنواع التجزئة (Type 5/8/9)"),
    ("vty-lines", "Remote Access (VTY Lines & SSH)", "تأمين الاتصال عن بعد (VTY و SSH)"),
    ("aaa-servers", "External Authentication Servers (AAA)", "خوادم المصادقة المركزية (AAA / RADIUS / TACACS+)"),
    ("matrix", "Cisco Password Types Matrix", "جدول مقارنة أنواع كلمات المرور في سيسكو"),
    ("conclusion", "Conclusion & Hardening Checklist", "الخاتمة وقائمة التحصين الأمني"),
]

# Section 1: User Mode Security
sec_user_mode = h2("user-mode", "User Mode Security (Protecting the Console)", "أمان وضع المستخدم (حماية منفذ الكونسول)") + src(
    bl("In this lesson, we examine how to secure <b>User Mode (User EXEC)</b> and <b>Privileged Mode (Enable Mode)</b> on Cisco switches and routers. By default, out of the box, Cisco IOS devices have <b>no authentication required</b>. When you plug a console cable into a brand-new device, here is what happens:",
       "في هذا الدرس، سنتعلم كيفية تأمين <b>وضع المستخدم (User EXEC)</b> و<b>وضع التمكين (Enable Mode)</b> على أجهزة سيسكو. بشكل افتراضي، عند تشغيل جهاز سيسكو جديد من المصنع، <b>لا توجد أي مصادقة مطلوبة</b>. بمجرد توصيل كابل الكونسول بالجهاز، هذا ما يحدث مباشرة:") +
    cli("Switch con0 is now available\n\nPress RETURN to get started.\n\nSwitch>") +
    bl("Once you press the Enter (RETURN) key, you end up directly in User EXEC mode (<code>Switch&gt;</code>) without any password. Anyone with physical access can immediately view basic switch data and interfaces. To prevent unauthorized physical access, we must configure authentication on the console port.",
       "بمجرد الضغط على زر Enter، تدخل مباشرة إلى وضع المستخدم (<code>Switch&gt;</code>) دون طلب أي كلمة مرور. هذا يعني أن أي شخص يصل فيزيائياً للجهاز يمكنه رؤية معلومات الشبكة. لمنع هذا الوصول غير المصرح به، يجب تفعيل المصادقة على منفذ الكونسول.") +
    img("images/web/cisco_console_cable.jpg", "Official Cisco Console Cable Rollover RJ45 to DB9",
        "Physical Cisco Console Rollover Cable connecting terminal PC to Console Port", "كابل الكونسول الأزرق (Rollover Cable) المستخدم للاتصال المباشر بمنفذ الكونسول",
        "Cisco Console Cable") +
    bl("<h3>1. Simple Shared Password</h3>The simplest option to protect the console is to configure a single shared password under the console line settings:",
       "<h3>1. كلمة مرور مشتركة بسيطة (Simple Password)</h3>أبسط طريقة لحماية الكونسول هي تعيين كلمة مرور واحدة مشتركة تحت إعدادات خط الكونسول:") +
    cli("Switch# <b>configure terminal</b>\nSwitch(config)# <b>line console 0</b>\nSwitch(config-line)# <b>password cisco</b>\nSwitch(config-line)# <b>login</b>\nSwitch(config-line)# <b>exit</b>") +
    bl("<b>The Critical 'login' Command:</b> Notice the <code>login</code> command above! In Cisco IOS, simply typing <code>password cisco</code> is <b>not enough</b>. The <code>login</code> command explicitly instructs Cisco IOS to prompt users for this password when establishing a session. If you forget <code>login</code>, IOS will not ask for any password!",
       "<b>أهمية أمر login الحاسم:</b> لاحظ وجود أمر <code>login</code>! في نظام سيسكو، كتابة <code>password cisco</code> وحدها <b>لا تكفي</b>. أمر <code>login</code> هو الذي يأمر الجهاز صراحة بطلب كلمة المرور عند بدء الجلسة. إذا نسيت كتابة <code>login</code>، فلن يطلب الجهاز كلمة المرور إطلاقاً!") +
    bl("Next time you connect your console cable and press Enter, Cisco IOS prompts you for access verification:",
       "في المرة القادمة التي تتصل فيها بالكونسول وتضغط Enter، سيطلب منك النظام التحقق:") +
    cli("Switch con0 is now available\n\nPress RETURN to get started.\n\nUser Access Verification\nPassword: <b>******</b>\nSwitch>") +
    bl("<h3>2. Local Username and Password Database</h3>A single shared password provides basic protection, but it lacks accountability (you cannot tell which engineer logged in). A superior approach is configuring individual <b>usernames and passwords</b> stored in the router's local database:",
       "<h3>2. قاعدة بيانات المستخدمين المحلية (Username & Password)</h3>كلمة المرور المشتركة تفتقر إلى مبدأ المحاسبة (لا يمكنك معرفة من قام بتسجيل الدخول). الحل الاحترافي هو إنشاء <b>حسابات مستخدمين فردية</b> بكلمات مرور خاصة مخزنة في قاعدة البيانات المحلية للجهاز:") +
    cli("Switch(config)# <b>line console 0</b>\nSwitch(config-line)# <b>login local</b>\nSwitch(config-line)# <b>exit</b>\nSwitch(config)# <b>username admin password cisco</b>") +
    bl("<b>login vs login local:</b> Under <code>line console 0</code>, we used <code>login local</code> instead of <code>login</code>. This instructs the switch to check credentials against its <b>local database</b> (the <code>username</code> commands). When connecting now, the console requests both username and password:",
       "<b>الفرق بين login و login local:</b> استخدمنا أمر <code>login local</code> بدلاً من <code>login</code>. هذا يخبر السويتش بالتحقق من الحسابات المسجلة في <b>قاعدة البيانات المحلية</b> (أوامر <code>username</code>). عند الاتصال الآن، سيطلب الكونسول كلاً من اسم المستخدم وكلمة المرور:") +
    cli("Switch con0 is now available\n\nPress RETURN to get started.\n\nUser Access Verification\nUsername: <b>admin</b>\nPassword: <b>******</b>\nSwitch>")
) + extra(
    "Exam Trick Alert (login vs login local): Cisco CCNA exam questions frequently test this distinction! 'login' expects a single password configured directly under that line ('password xyz'). 'login local' tells IOS to look up user accounts configured globally with 'username <user> password/secret <pass>'. If you configure 'login local' without creating any username in global configuration, you will be LOCKED OUT of the switch!",
    "تنبيه امتحاني هام جداً (login مقابل login local): أسئلة امتحان CCNA تركز بشدة على هذا الفرق! أمر 'login' يتطلب كلمة مرور موضوعة على الخط نفسه ('password xyz'). أما 'login local' فيأمر الجهاز بالبحث في الحسابات المنشأة عالمياً بأمر 'username'. لو كتبت 'login local' ونسيت تنشئ مستخدم بأمر 'username'، فسيتم قفل الجهاز ولن تتمكن من الدخول نهائياً!"
)

# Section 2: Enable Mode Security
sec_enable_mode = h2("enable-mode", "Privileged Mode (Enable Mode) Security", "أمان وضع التمكين (Privileged EXEC Mode)") + src(
    bl("What happens when someone types <code>enable</code> from User Mode on a default, unsecured switch? They gain <b>unrestricted administrative control</b> instantly:",
       "ماذا يحدث عندما يكتب شخص ما أمر <code>enable</code> من وضع المستخدم على سويتش افتراضي غير مؤمن؟ يحصل فوراً على <b>صلاحيات إدارية كاملة</b> دون أي قيود:") +
    cli("Switch> <b>enable</b>\nSwitch#") +
    bl("In Privileged EXEC mode (<code>Switch#</code>), anyone can view running configurations, clear routing tables, inspect passwords, or issue <code>reload</code> to bring down the network. To protect this mode, we configure an enable password from Global Configuration mode:",
       "في وضع الـ Privileged EXEC (<code>Switch#</code>)، يستطيع أي شخص عرض ملفات الإعدادات، مسح جداول التوجيه، أو كتابة <code>reload</code> لإيقاف الشبكة بالكامل. لحماية هذا الوضع، نضبط كلمة مرور التمكين من وضع الإعداد العام:") +
    cli("Switch# <b>configure terminal</b>\nSwitch(config)# <b>enable password cisco</b>\nSwitch(config)# <b>exit</b>") +
    bl("Let's test our configuration by leaving privileged mode with <code>disable</code> and attempting to re-enter:",
       "دعنا نختبر الإعداد بالخروج من وضع التمكين بأمر <code>disable</code> ثم محاولة الدخول مجدداً:") +
    cli("Switch# <b>disable</b>\nSwitch>\nSwitch> <b>enable</b>\nPassword: <b>******</b>\nSwitch#") +
    bl("The switch now prompts for the enable password before granting privileged access. However, there is a severe security vulnerability with this command...",
       "السويتش الآن يطلب كلمة المرور قبل منح الصلاحيات الإدارية. ومع ذلك، هناك ثغرة أمنية خطيرة للغاية في هذا الأمر...")
) + extra(
    "User Mode (>) vs Privileged Mode (#): Think of User Mode like being a visitor in a museum — you can look at the exhibits, but you cannot touch anything. Privileged Mode is having the master keys to the building, security cameras, and electrical vault. Protecting Privileged Mode with strong authentication is the single most important security step on any Cisco router or switch.",
    "مقارنة بين وضع المستخدم (>) ووضع التمكين (#): تخيل وضع المستخدم كأنك زائر في متحف — يمكنك النظر ولكن لا تستطيع تغيير أي شيء. أما وضع التمكين فهو امتلاك المفاتيح الرئيسية للمبنى وغرفة المراقبة والكهرباء. حماية وضع التمكين بمصادقة قوية هي أهم خطوة أمنية على الإطلاق في أي راوتر أو سويتش سيسكو."
)

# Section 3: Password Encryption
sec_password_encryption = h2("password-encryption", "Password Encryption (Type 7 Weakness)", "تشفير كلمات المرور وضعف تشفير Type 7") + src(
    bl("In our previous examples, we configured passwords using <code>enable password cisco</code> and <code>username admin password cisco</code>. Let's see how they appear inside the running configuration:",
       "في الأمثلة السابقة، قمنا بضبط كلمات المرور باستخدام <code>enable password cisco</code> و <code>username admin password cisco</code>. دعنا نرى كيف تظهر هذه الكلمات داخل ملف الإعدادات الجاري:") +
    cli("Switch# <b>show running-config | include password</b>\nno service password-encryption\nenable password cisco\nusername admin password 0 cisco") +
    bl("<b>The Cleartext Disaster:</b> They are displayed in 100% plain text! The <code>0</code> before 'cisco' indicates <b>Type 0 (unencrypted cleartext)</b>. Anyone looking over your shoulder, inspecting a saved configuration backup, or stealing an archived config file instantly knows your network's master passwords.",
       "<b>كارثة النصوص الصريحة (Cleartext):</b> تظهر كلمات المرور بنص صريح وواضح تماماً! الرقم <code>0</code> قبل كلمة المرور يشير إلى <b>Type 0 (غير مشفر / نص صريح)</b>. أي شخص يمر بجانبك، أو يفتح نسخة احتياطية من الإعدادات، يكتشف كلمات مرور الشبكة فوراً.") +
    bl("Cisco IOS provides a built-in command to obfuscate all cleartext passwords:",
       "يوفر نظام Cisco IOS أمراً مدمجاً لتمويه وتشفير جميع كلمات المرور الصريحة:") +
    cli("Switch(config)# <b>service password-encryption</b>") +
    bl("Once enabled, Cisco IOS automatically converts all existing and future plain text passwords into encrypted strings:",
       "بمجرد تفعيل هذا الأمر، يقوم النظام فوراً بتحويل جميع كلمات المرور الصريحة الحالية والجديدة إلى نصوص مشفرة:") +
    cli("Switch# <b>show running-config | include password</b>\nservice password-encryption\nenable password 7 13061E010803\nusername admin password 7 110A1016141D") +
    bl("Notice the number <b>7</b> before each password. This indicates <b>Cisco Type 7 encryption</b>.",
       "لاحظ ظهور الرقم <b>7</b> قبل كلمة المرور. هذا يشير إلى <b>تشفير سيسكو Type 7</b>.") +
    bl("<b>Why Type 7 is Dangerously Weak:</b> While seeing scrambled characters like <code>13061E010803</code> might give you a feeling of security, in reality <b>Type 7 is not real encryption</b>. It is an extremely weak, reversible Vigenère-style XOR algorithm using a static key published back in 1995. Dozens of websites and mobile apps can decrypt Type 7 strings back into clear text in under <b>1 millisecond</b>! It only protects against casual shoulder surfing, never against a serious attacker.",
       "<b>لماذا يعتبر تشفير Type 7 خطيراً وضعيفاً للغاية:</b> على الرغم من أن رؤية حروف مشفرة مثل <code>13061E010803</code> قد تعطيك شعوراً بالأمان، إلا أن <b>Type 7 ليس تشفيراً حقيقياً</b>. هو مجرد خوارزمية تمويه بسيطة (Vigenère XOR) بمفتاح ثابت معروف منذ عام 1995. توجد عشرات المواقع التي تفك هذا التشفير وتكشف كلمة المرور في أقل من <b>جزء من الألف من الثانية</b>! تشفير Type 7 يحمي فقط من نظرات الفضوليين العابرة (Shoulder Surfing)، ولا يقدم أي حماية حقيقية.")
) + extra(
    "How to Decrypt Type 7 in Practice: You can copy any Type 7 hash (like '13061E010803') into any free online tool or Python script: chr(int(hex_byte, 16) ^ static_cisco_key). In 0.001 seconds, it outputs 'cisco'. Cisco created Type 7 in the early 1990s purely to hide passwords from someone standing right behind the network admin. Never rely on 'service password-encryption' alone for enterprise security!",
    "كيفية فك تشفير Type 7 عملياً: يمكنك نسخ أي كود Type 7 ووضعه في أي موقع أو كود بايثون بسيط يعتمد على XOR، وفي جزء من الثانية تظهر لك كلمة 'cisco'. أنشأت سيسكو هذا التشفير في أوائل التسعينيات فقط لمنع زميلك الواقف خلفك من قراءة الشاشة. لذلك، لا تعتمد أبداً على 'service password-encryption' وحده لحماية شبكتك!"
)

# Section 4: Strong Secrets & Hashing Types
sec_secrets = h2("secrets", "Cisco Secrets & Hashing Algorithms (Type 5, 8, 9)", "حماية Secret وخوارزميات التجزئة القوية (Type 5, 8, 9)") + src(
    bl("Because <code>enable password</code> and Type 7 encryption are so vulnerable, Cisco IOS introduced the <b><code>secret</code></b> command. Unlike passwords which use reversible encryption, secrets use <b>one-way cryptographic hash functions</b>.",
       "نظراً للضعف الشديد في أمر <code>enable password</code> وتشفير Type 7، أضافت سيسكو أمر <b><code>secret</code></b>. على عكس كلمات المرور التي تستخدم تشفيراً قابلاً للعكس، تستخدم الـ secrets <b>دوال تجزئة رياضية أحادية الاتجاه (One-Way Hash)</b> لا يمكن عكسها حسابياً.") +
    bl("Let's look at the available options when configuring <code>enable secret</code> in Cisco IOS:",
       "دعنا نستعرض الخيارات المتاحة عند كتابة أمر <code>enable secret ?</code> في سيسكو:") +
    cli("Switch(config)# <b>enable secret ?</b>\n  0      Specifies an UNENCRYPTED password will follow\n  5      Specifies a MD5 HASHED secret will follow\n  8      Specifies a PBKDF2 HASHED secret will follow\n  9      Specifies a SCRYPT HASHED secret will follow\n  LINE   The UNENCRYPTED (cleartext) 'enable' secret\n  level  Set exec level password") +
    bl("Notice the hash types supported by modern Cisco IOS:<br>• <b>Type 5:</b> MD5 hash (supported across all legacy and modern IOS devices).<br>• <b>Type 8:</b> PBKDF2 with SHA-256 hash (strong enterprise-grade protection).<br>• <b>Type 9:</b> Scrypt hash (memory-hard modern hashing, virtually immune to ASIC brute-force).",
       "لاحظ أنواع التجزئة المدعومة في نظام سيسكو الحديث:<br>• <b>Type 5:</b> تجزئة MD5 (مدعومة في كل أجهزة سيسكو القديمة والحديثة).<br>• <b>Type 8:</b> تجزئة PBKDF2 بخوارزمية SHA-256 (حماية قوية وموصى بها).<br>• <b>Type 9:</b> تجزئة Scrypt (خوارزمية حديثة تستهلك الذاكرة وتمنع هجمات المعالجات المتخصصة ASIC).") +
    bl("<h3>1. Default Secret (Type 5 MD5)</h3>When you simply configure <code>enable secret cisco</code>, Cisco IOS defaults to Type 5 (MD5):",
       "<h3>1. التجزئة الافتراضية (Type 5 MD5)</h3>عندما تكتب أمر <code>enable secret cisco</code> مباشرة، يستخدم السويتش خوارزمية MD5 افتراضياً:") +
    cli("Switch(config)# <b>enable secret cisco</b>\nSwitch(config)# <b>do show running-config | include secret</b>\nenable secret 5 $1$CANW$U9Y8O6KeFhrFR4l1Qo07h/") +
    bl("The <b>5</b> indicates an <b>MD5 hash</b> with salt. While significantly better than Type 7, modern GPU clusters can crack simple MD5 passwords using rainbow tables and brute-force in minutes. For robust protection, we must utilize Type 8 or 9.",
       "الرقم <b>5</b> يشير إلى <b>تجزئة MD5</b> مع قيمة عشوائية (Salt). على الرغم من تفوقها بمراحل على Type 7، إلا أن معالجات كروت الشاشة الحديثة قادرة على كسر كلمات مرور MD5 البسيطة عبر جداول Rainbow Table وهجمات التخمين. لذلك يفضل استخدام Type 8 أو 9.") +
    bl("<h3>2. Modern Enterprise Secret (Type 8 SHA-256)</h3>On modern Cisco IOS (15.x and IOS XE), you can select the modern hashing algorithm using <code>algorithm-type</code>:",
       "<h3>2. التجزئة الحديثة للمؤسسات (Type 8 SHA-256)</h3>في أنظمة سيسكو الحديثة، يمكنك تحديد خوارزمية التجزئة عبر أمر <code>algorithm-type</code>:") +
    cli("Switch(config)# <b>enable algorithm-type sha256 secret cisco</b>\nSwitch(config)# <b>do show running-config | include secret</b>\nenable secret 8 $8$dvX/fx/FJ0Snk2$HhqrOUaEtBgk4zJvG2IQuAJNUicZmmELelC/L6.Fcl2") +
    bl("The <b>8</b> indicates <b>PBKDF2 SHA-256</b>. You can also configure user accounts with SHA-256 secrets:",
       "الرقم <b>8</b> يشير إلى <b>PBKDF2 SHA-256</b>. ويمكنك كذلك تطبيق نفس الخوارزمية على حسابات المستخدمين:") +
    cli("Switch(config)# <b>username rene algorithm-type sha256 secret cisco</b>\nSwitch(config)# <b>do show running-config | include rene</b>\nusername rene secret 8 $8$dyzsAmZjA3w.aY$YBZn8LBI6CK04ij5ZmqQ/88OrFdc3jzGb6v7SSQI0cw")
) + extra(
    "Critical Rule of Precedence ('enable secret' vs 'enable password'): What happens if both 'enable secret' AND 'enable password' are configured on the same Cisco device? Cisco IOS ALWAYS prioritizes 'enable secret'! The 'enable password' is completely ignored. Cisco keeps 'enable password' only for backward compatibility with ancient software that cannot interpret hashes.",
    "قاعدة الأسبقية الحاسمة (enable secret مقابل enable password): ماذا يحدث إذا قمت بضبط الاثنين معاً على نفس الجهاز؟ نظام Cisco IOS يعطي الأولوية القصوى دائماً لـ 'enable secret'! ويتم تجاهل 'enable password' تماماً. سيسكو تحتفظ بأمر enable password فقط للتوافق مع البرمجيات القديمة جداً التي لا تفهم التجزئة."
)

# Section 5: Remote Access Security (VTY Lines & SSH)
sec_vty_lines = h2("vty-lines", "Remote Management Security (VTY Lines & SSH)", "تأمين الاتصال عن بعد (خطوط VTY وبروتوكول SSH)") + src(
    bl("So far, we secured the physical console port (<code>line console 0</code>). However, in production networks, engineers rarely sit in front of the rack with a console cable. They manage switches and routers across the network using <b>VTY (Virtual Terminal)</b> lines.",
       "حتى الآن، قمنا بحماية منفذ الكونسول الفيزيائي (<code>line console 0</code>). ولكن في بيئات العمل الحقيقية، نادراً ما يجلس المهندس في غرفة السيرفرات بكابل الكونسول. بدلاً من ذلك، يدير الأجهزة عن بعد عبر الشبكة باستخدام <b>خطوط VTY (Virtual Terminal)</b>.") +
    bl("<b>VTY Lines Security:</b> Switches support multiple simultaneous remote sessions (typically 16 lines: <code>0 to 15</code>). By default, if no password or authentication is configured on VTY lines, Cisco IOS <b>rejects all remote connection attempts</b> for security.",
       "<b>أمان خطوط VTY:</b> تدعم السويتشات عدة جلسات اتصال عن بعد في نفس الوقت (عادة 16 خطاً: <code>من 0 إلى 15</code>). افتراضياً، إذا لم تقم بضبط كلمة مرور أو مصادقة على خطوط VTY، فإن سيسكو <b>ترفض أي محاولة اتصال عن بعد</b> لحماية الجهاز.") +
    bl("To configure secure remote management with <b>SSH (Secure Shell)</b> and local accounts:",
       "لضبط إدارة آمنة عن بعد باستخدام بروتوكول <b>SSH المشفر</b> والحسابات المحلية:") +
    cli("Switch(config)# <b>ip domain-name mynetwork.com</b>\nSwitch(config)# <b>crypto key generate rsa modulus 2048</b>\nSwitch(config)# <b>ip ssh version 2</b>\nSwitch(config)# <b>line vty 0 15</b>\nSwitch(config-line)# <b>transport input ssh</b>\nSwitch(config-line)# <b>login local</b>\nSwitch(config-line)# <b>exit</b>") +
    bl("<b>Why 'transport input ssh' matters:</b> By default, VTY lines allow <b>Telnet (TCP port 23)</b>, which transmits all credentials, show outputs, and passwords in <b>unencrypted plain text</b> across the network! By configuring <code>transport input ssh</code>, you completely disable Telnet and force all management traffic to use <b>encrypted SSH (TCP port 22)</b>.",
       "<b>لماذا يعتبر 'transport input ssh' أمراً حيوياً:</b> افتراضياً، تسمح خطوط VTY ببروتوكول <b>Telnet (منفذ 23)</b>، وهو بروتوكول ينقل كل كلمات المرور والأوامر <b>بنص صريح غير مشفر</b> عبر أسلاك الشبكة! بتحديد <code>transport input ssh</code>، فإنك تمنع الـ Telnet تماماً وتجبر الجميع على استخدام <b>SSH المشفر (منفذ 22)</b>.")
) + extra(
    "Telnet vs SSH on Wireshark: If someone sniffs traffic while you log in via Telnet, they can right-click the packet in Wireshark and choose 'Follow TCP Stream' to see your username and enable password in clear readable text. With SSH, the entire TCP payload is encrypted with AES/RSA, appearing as pure random entropy.",
    "الفرق بين Telnet و SSH على Wireshark: لو قام متطفل باعتراض حركة البيانات أثناء دخولك بـ Telnet، يمكنه بالضغط على 'Follow TCP Stream' في Wireshark قراءة اسم المستخدم وباسورد الـ enable بوضوح تام. أما مع SSH، فكل حزم البيانات تكون مشفرة بخوارزميات قوية مثل AES، ولا يستطيع أحد رؤية أي شيء مفيد."
)

# Section 6: External Authentication Servers (AAA)
sec_aaa_servers = h2("aaa-servers", "External Authentication Servers (AAA, RADIUS & TACACS+)", "خوادم المصادقة المركزية (AAA و RADIUS و TACACS+)") + src(
    bl("Configuring usernames and secrets in the local database works fine for a small test lab with 2 or 3 switches. However, in an enterprise network with <b>500 switches and routers</b>, local accounts fail due to <b>lack of scalability</b>:<br>• If an engineer joins or leaves the company, you must manually update 500 devices.<br>• If an admin changes their password, they must reconfigure 500 devices.<br>• There is no centralized audit trail of who typed which command on which device.",
       "إنشاء المستخدمين في قاعدة البيانات المحلية مناسب لمعمل تجارب صغير به سويتشين أو ثلاثة. ولكن في شبكة مؤسسة كبرى تضم <b>500 راوتر وسويتش</b>، تفشل الحسابات المحلية بسبب <b>انعدام قابلية التوسع (Scalability)</b>:<br>• إذا انضم مهندس جديد أو استقال، يجب تعديل 500 جهاز يدوياً.<br>• إذا غير موظف كلمة مروره، يجب تحديث 500 جهاز.<br>• لا يوجد سجل تدقيق مركزي يوضح من نفذ أي أمر وعلى أي جهاز.") +
    bl("To solve this, enterprise networks implement <b>AAA (Authentication, Authorization, and Accounting)</b> connected to centralized authentication servers:",
       "لحل هذه المعضلة، تطبق الشركات نظام <b>AAA (المصادقة، والتخويل، والمحاسبة)</b> المتصل بخوادم مصادقة مركزية:") +
    diagram(
        '<div style="font-family:var(--font-body);display:flex;justify-content:space-around;align-items:center;flex-wrap:wrap;gap:16px;">'
        '<div style="padding:16px;border:2px solid var(--accent);background:var(--panel2);border-radius:8px;text-align:center;">'
        '<b>Administrator PC</b><br><span style="font-size:0.85rem;color:var(--muted);">Initiates SSH connection</span></div>'
        '<div style="text-align:center;color:var(--accent);font-weight:bold;font-size:0.9rem;">'
        '&larr; 1. Enter Credentials &rarr;<br><span style="font-size:0.8rem;color:var(--text);font-family:monospace;">User: mohamed / Pass: ***</span></div>'
        '<div style="padding:16px;border:2px solid var(--line);background:var(--panel2);border-radius:8px;text-align:center;">'
        '<b>Cisco Router / Switch</b><br><span style="font-size:0.85rem;color:var(--good);font-weight:bold;">[AAA Client]</span></div>'
        '<div style="text-align:center;color:var(--good);font-weight:bold;font-size:0.9rem;">'
        '&larr; 2. Forward to AAA &rarr;<br><span style="font-size:0.8rem;color:var(--text);font-family:monospace;">TACACS+ / RADIUS</span></div>'
        '<div style="padding:16px;border:2px solid var(--good);background:var(--panel2);border-radius:8px;text-align:center;">'
        '<b>Central AAA Server</b><br><span style="font-size:0.85rem;color:var(--good);font-weight:bold;">Cisco ISE / FreeRADIUS</span></div>'
        '</div>',
        "AAA Centralized Authentication Flow", "مخطط تدفق المصادقة المركزية عبر نظام AAA"
    ) +
    img("images/web/radius_authentication.png", "RADIUS authentication and authorization flow diagram",
        "RADIUS Protocol Authentication and Authorization Packet Exchange Flow", "تبادل حزم المصادقة والتخويل في بروتوكول RADIUS القياسي",
        "RADIUS Authentication Flow") +
    bl("<b>TACACS+ vs RADIUS Comparison:</b> Two primary protocols communicate between network devices and AAA servers:",
       "<b>مقارنة بين بروتوكولي TACACS+ و RADIUS:</b> هناك بروتوكولان رئيسيان يربطان أجهزة الشبكة بخوادم المصادقة المركزية:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Feature", "الميزة / المعيار") + '</th><th>' + bi("TACACS+ (Terminal Access Controller)", "بروتوكول TACACS+") + '</th><th>' + bi("RADIUS (Remote Authentication Dial-In)", "بروتوكول RADIUS") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>Developer & Standard</b></td><td>' + bi("Cisco proprietary (open RFC)", "مطور بواسطة سيسكو") + '</td><td>' + bi("Open IETF Industry Standard", "معيار عالمي مفتوح (IETF)") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Transport Protocol</b></td><td class="mono-cell"><b>TCP port 49</b> (reliable)</td><td class="mono-cell"><b>UDP ports 1812 & 1813</b> (or 1645/1646)</td></tr>' +
    '<tr><td class="mono-cell"><b>AAA Separation</b></td><td>' + bi("<b>Separates</b> Authentication, Authorization, Accounting", "يفصل المصادقة عن التخويل عن المحاسبة تماماً") + '</td><td>' + bi("<b>Combines</b> Authentication & Authorization together", "يدمج المصادقة والتخويل معاً في خطوة واحدة") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Packet Encryption</b></td><td>' + bi("<b>Encrypts entire payload</b> (100% confidential)", "يشفر محتوى الحزمة بالكامل") + '</td><td>' + bi("<b>Only encrypts password</b> (headers & usernames clear)", "يشفر كلمة المرور فقط ويبقى اسم المستخدم صريحاً") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Primary Use Case</b></td><td>' + bi("Device Administration (router/switch CLI control)", "إدارة أجهزة الشبكة والتحكم في أوامر الـ CLI") + '</td><td>' + bi("Network Access (802.1X, VPN, Wi-Fi authentication)", "التحكم في وصول المستخدمين للشبكة والـ Wi-Fi") + '</td></tr>' +
    '</table></div>' +
    bl("<b>Enabling AAA on Cisco IOS:</b> To activate modern AAA on Cisco switches, use <code>aaa new-model</code>:",
       "<b>تفعيل AAA على أجهزة سيسكو:</b> لتفعيل نظام المصادقة المتقدم، نستخدم الأمر العام <code>aaa new-model</code>:") +
    cli("Switch(config)# <b>aaa new-model</b>\nSwitch(config)# <b>tacacs server ISE_SERVER</b>\nSwitch(config-server-tacacs)# <b>address ipv4 10.1.1.50</b>\nSwitch(config-server-tacacs)# <b>key MySecretKey123</b>")
) + extra(
    "Exam Favorite (TACACS+ vs RADIUS): This exact comparison table appears in almost every CCNA exam! Remember the mnemonics: TACACS+ uses TCP (both start with T!), encrypts the Total packet, and separates each A. RADIUS uses UDP, combines Auth+Auth, and only hides the password.",
    "سؤال امتحاني متكرر جداً (TACACS+ مقابل RADIUS): هذا الجدول يظهر في جميع امتحانات CCNA تقريباً! احفظ هذه العلامة الذكية: TACACS+ يبدأ بحرف T ويستخدم TCP، ويشفر كامل الحزمة (Total encryption)، ويفصل بين عناصر AAA. بينما RADIUS يستخدم UDP ويدمج المصادقة مع التخويل ويشفر كلمة المرور فقط."
)

# Section 7: Cisco Password Types Matrix
sec_matrix = h2("matrix", "Complete Cisco Password & Hash Types Matrix", "جدول مقارنة شامل لأنواع كلمات المرور والتجزئة في سيسكو") + src(
    bl("When configuring or inspecting a Cisco device with <code>show running-config</code>, you will encounter different numbers indicating how each password is stored. Here is the authoritative summary every network engineer must know:",
       "عند ضبط أجهزة سيسكو أو فحصها بأمر <code>show running-config</code>، ستجد أرقاماً مختلفة تدل على كيفية تخزين كل كلمة مرور. هذا هو الجدول المرجعي الشامل الذي يحتاجه كل مهندس شبكات:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Type Number", "رقم النوع") + '</th><th>' + bi("Algorithm / Method", "الخوارزمية وطريقة المعالجة") + '</th><th>' + bi("Configuration Command", "أمر التفعيل المستخدم") + '</th><th>' + bi("Security Rating", "مستوى الأمان") + '</th><th>' + bi("Vulnerability / Evaluation", "التقييم الأمني ونقاط الضعف") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>Type 0</b></td><td>' + bi("Clear text (no encryption)", "نص صريح بدون تشفير") + '</td><td class="mono-cell">password &lt;pass&gt;</td><td><span style="color:var(--err);font-weight:bold;">⛔ Insecure</span></td><td>' + bi("Readable by anyone in show running-config", "مكشوف تماماً في ملف الإعدادات") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Type 7</b></td><td>' + bi("Cisco Vigenère / XOR cipher", "تمويه خفيف Vigenère XOR") + '</td><td class="mono-cell">service password-encryption</td><td><span style="color:var(--warn);font-weight:bold;">⚠️ Very Weak</span></td><td>' + bi("Easily decrypted in milliseconds with online tools", "يمكن فكه في جزء من الثانية بأدوات مجانية") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Type 5</b></td><td>' + bi("MD5 cryptographic hash", "تجزئة تشفيرية MD5") + '</td><td class="mono-cell">enable secret &lt;pass&gt;</td><td><span style="color:var(--accent);font-weight:bold;">🟡 Moderate / Legacy</span></td><td>' + bi("One-way hash, but vulnerable to GPU brute-force", "أحادي الاتجاه لكنه عرضة لهجمات التخمين الحديثة") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Type 8</b></td><td>' + bi("PBKDF2 with SHA-256", "تجزئة قوية PBKDF2 SHA-256") + '</td><td class="mono-cell">enable algorithm-type sha256 secret</td><td><span style="color:var(--good);font-weight:bold;">✅ Strong (Recommended)</span></td><td>' + bi("Cisco recommended standard for modern networks", "المعيار الموصى به رسمياً في شبكات سيسكو") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Type 9</b></td><td>' + bi("Scrypt hash (memory-hard)", "تجزئة Scrypt المحصنة") + '</td><td class="mono-cell">enable algorithm-type scrypt secret</td><td><span style="color:var(--good);font-weight:bold;">🔒 Strongest</span></td><td>' + bi("Memory-hard design prevents ASIC & GPU cracking", "محصن ضد الأجهزة المتخصصة لاستهلاكه العالي للذاكرة") + '</td></tr>' +
    '</table></div>'
)

# Section 8: Conclusion & Hardening Checklist
sec_conclusion = h2("conclusion", "Conclusion & Production Hardening Checklist", "الخاتمة وقائمة أفضل الممارسات لتحصين الأجهزة") + src(
    bl("Securing device access is the baseline requirement before connecting any router or switch to a corporate network. Here is the 5-point hardening checklist you should apply to every fresh Cisco device:",
       "تأمين الوصول للأجهزة هو حجر الأساس قبل توصيل أي راوتر أو سويتش بشبكة المؤسسة. إليك قائمة التحصين الأمني المكونة من 5 خطوات أساسية يجب تطبيقها على كل جهاز سيسكو:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Step", "الخطوة") + '</th><th>' + bi("Recommended Command", "الأمر الموصى به") + '</th><th>' + bi("Security Purpose", "الهدف الأمني المباشر") + '</th></tr>' +
    '<tr><td><b>1. Secure Privileged Mode</b></td><td class="mono-cell">enable algorithm-type sha256 secret &lt;pass&gt;</td><td>' + bi("Protects enable mode with uncrackable Type 8 SHA-256 hash", "حماية وضع التمكين بتجزئة Type 8 المشفرة بـ SHA-256") + '</td></tr>' +
    '<tr><td><b>2. Individual User Accounts</b></td><td class="mono-cell">username &lt;user&gt; algorithm-type sha256 secret &lt;pass&gt;</td><td>' + bi("Eliminates shared passwords; ensures administrative accountability", "إلغاء كلمات المرور المشتركة وتطبيق مبدأ المحاسبة الفردية") + '</td></tr>' +
    '<tr><td><b>3. Secure Console Port</b></td><td class="mono-cell">line con 0 -> login local</td><td>' + bi("Enforces local username/password verification on physical console", "إجبار التحقق من المستخدمين عند التوصيل بالكونسول") + '</td></tr>' +
    '<tr><td><b>4. Disable Plaintext Telnet</b></td><td class="mono-cell">line vty 0 15 -> transport input ssh -> login local</td><td>' + bi("Forces remote sessions over encrypted SSH (TCP 22) only", "إجبار الاتصال عن بعد عبر بروتوكول SSH المشفر فقط ومنع Telnet") + '</td></tr>' +
    '<tr><td><b>5. Obfuscate Config Passwords</b></td><td class="mono-cell">service password-encryption</td><td>' + bi("Prevents cleartext passwords from showing in configuration backups", "منع ظهور كلمات المرور بنصوص صريحة في ملفات النسخ الاحتياطي") + '</td></tr>' +
    '</table></div>' +
    bl("Remember that no cryptographic hash can protect a weak password! Always use strong, complex passphrases containing letters, numbers, and symbols.",
       "تذكر دائماً أن أقوى خوارزميات التشفير لن تحميك إذا كانت كلمة المرور سهلة! استخدم دائماً كلمات مرور معقدة تحتوي على مزيج من الحروف الكبيرة والصغيرة والأرقام والرموز.")
)

# Recap quiz items (Testing Lesson 10 concepts)
recap_items = [
    Q("What are the standard serial communication parameters for connecting PuTTY to a Cisco console port?",
      "ما هي الإعدادات القياسية للاتصال التسلسلي (Serial) ببرنامج PuTTY لمنفذ كونسول سيسكو؟",
      [
        ("9600 baud, 8 data bits, no parity, 1 stop bit, no flow control (9600-8-N-1)", "9600 باود، 8 بت بيانات، بدون تطابق، 1 بت توقف، بدون تحكم في التدفق (9600-8-N-1)"),
        ("115200 baud, 7 data bits, even parity, 2 stop bits", "115200 باود، 7 بت بيانات، تطابق زوجي، 2 بت توقف"),
        ("9600 baud, 8 data bits, odd parity, 1 stop bit, XON/XOFF", "9600 باود، 8 بت بيانات، تطابق فردي، تحكم XON/XOFF"),
        ("38400 baud, 8 data bits, no parity, 1 stop bit", "38400 باود، 8 بت بيانات، بدون تطابق، 1 بت توقف")
      ], 0,
      "Cisco console ports use the universal standard: 9600 baud, 8 data bits, no parity, 1 stop bit, and no flow control (9600-8-N-1).",
      "منافذ الكونسول في سيسكو تعتمد المعيار القياسي: 9600 سرعة نقل، 8 بت بيانات، بدون تطابق (None)، 1 بت توقف، وبدون تحكم في التدفق."),

    Q("Which Cisco IOS prompt indicates that you are in Privileged EXEC (Enable) mode?",
      "أي علامة (Prompt) في سيسكو تدل على أنك في وضع الـ Privileged EXEC (Enable Mode)؟",
      [
        ("Switch>", "Switch>"),
        ("Switch#", "Switch#"),
        ("Switch(config)#", "Switch(config)#"),
        ("Switch(config-if)#", "Switch(config-if)#")
      ], 1,
      "The pound sign (Switch#) denotes Privileged EXEC mode. Switch> is User EXEC, and Switch(config)# is Global Configuration mode.",
      "علامة الشباك (Switch#) تميز وضع Privileged EXEC. بينما Switch> لوضع المستخدم، و Switch(config)# لوضع الإعداد العام."),

    Q("Where is the 'running-config' stored, and what happens to it when the device is rebooted?",
      "أين يتم تخزين ملف 'running-config'، وماذا يحدث له إذا أعيد تشغيل الجهاز؟",
      [
        ("Stored in NVRAM; preserved permanently across reboots", "يخزن في NVRAM؛ ويظل محفوظاً بعد إعادة التشغيل"),
        ("Stored in Flash memory; automatically updated every 60 seconds", "يخزن في ذاكرة Flash؛ ويتم تحديثه كل 60 ثانية"),
        ("Stored in RAM; completely erased if the device reboots without saving", "يخزن في ذاكرة RAM؛ ويمحى بالكامل إذا أعيد التشغيل دون حفظ"),
        ("Stored on the Boot ROM chip; read-only and unmodifiable", "يخزن على شريحة ROM؛ وهو للقراءة فقط")
      ], 2,
      "The running-config resides in volatile RAM. All changes are lost on power loss or reload unless saved to startup-config in NVRAM via 'copy run start'.",
      "ملف running-config موجود في ذاكرة RAM المؤقتة. كل التعديلات تضيع فوراً عند انقطاع الكهرباء أو إعادة التشغيل ما لم تحفظ إلى NVRAM بأمر 'copy run start'."),

    Q("How can you run the privileged command 'show ip interface brief' while working inside interface configuration mode without exiting?",
      "كيف يمكنك تنفيذ أمر 'show ip interface brief' وأنت داخل وضع إعداد المنفذ دون الخروج منه؟",
      [
        ("Prepend the command with 'do' (e.g. 'do show ip interface brief')", "إضافة كلمة 'do' قبل الأمر (مثل 'do show ip interface brief')"),
        ("Type 'run show ip interface brief'", "كتابة 'run show ip interface brief'"),
        ("Press Ctrl+Shift+6 to bypass mode restrictions", "الضغط على Ctrl+Shift+6 لتجاوز قيود الوضع"),
        ("It is impossible; you must type 'exit' first", "مستحيل؛ يجب كتابة exit أولاً")
      ], 0,
      "The 'do' command allows engineers to execute any Privileged EXEC command directly from within configuration modes.",
      "أمر 'do' يسمح للمهندس بتنفيذ أي أمر من أوامر Privileged EXEC مباشرة أثناء وجوده داخل أي وضع إعداد فرعي."),

    Q("Which piping modifier filters output to show ONLY lines that contain a specific keyword?",
      "أي أداة فلترة (Pipe) تعرض فقط السطور التي تحتوي على كلمة مفتاحية معينة؟",
      [
        ("| begin", "| begin"),
        ("| include", "| include"),
        ("| exclude", "| exclude"),
        ("| section", "| section")
      ], 1,
      "The '| include' filter displays only lines matching the specified regex/string, exactly like grep.",
      "الأداة '| include' تقوم بفلترة المخرجات وعرض السطور التي تتضمن الكلمة المطلوبة فقط تماماً مثل أمر grep.")
]

# Lesson quiz items (Testing Lesson 11 concepts)
quiz_items = [
    Q("An engineer configured 'password cisco' under 'line console 0', but the switch still does not prompt for a password. What is missing?",
      "قام مهندس بكتابة 'password cisco' داخل 'line console 0' ولكن السويتش لا يطلب كلمة المرور عند الاتصال. ما الذي ينقصه؟",
      [
        ("The 'login' command was not entered under line console 0", "لم يكتب أمر 'login' تحت إعدادات line console 0"),
        ("The 'enable secret' command was not configured globally", "لم يقم بضبط أمر 'enable secret' في الإعداد العام"),
        ("The baud rate of the console cable must be reset to 115200", "يجب تغيير سرعة كابل الكونسول إلى 115200"),
        ("Console passwords only take effect after typing 'copy run start'", "كلمات مرور الكونسول لا تعمل إلا بعد حفظ الإعدادات")
      ], 0,
      "Without the 'login' command, Cisco IOS does not activate password verification for the line, even if a password string is defined.",
      "بدون كتابة أمر 'login'، لا يقوم نظام سيسكو بتفعيل طلب كلمة المرور على المنفذ حتى لو كانت كلمة المرور مكتوبة."),

    Q("What is the primary difference between 'login' and 'login local' on Cisco management lines?",
      "ما هو الفرق الأساسي بين أمر 'login' وأمر 'login local' على خطوط إدارة سيسكو؟",
      [
        ("'login' uses a single shared password on the line; 'login local' checks usernames/passwords in the device's local database", "'login' يطلب كلمة مرور واحدة مشتركة؛ بينما 'login local' يتحقق من الحسابات المسجلة بقاعدة بيانات الجهاز"),
        ("'login' is for Telnet; 'login local' is only for console connections", "'login' مخصص لـ Telnet؛ بينما 'login local' للكونسول فقط"),
        ("'login local' encrypts traffic with AES; 'login' leaves traffic cleartext", "'login local' يشفر البيانات بـ AES؛ بينما 'login' بدون تشفير"),
        ("There is no functional difference; they are interchangeable aliases", "لا يوجد فرق وظيفي؛ هما اسمان لنفس الأمر")
      ], 0,
      "'login' prompts for the line password configured with 'password <pass>'. 'login local' instructs IOS to authenticate using locally defined 'username' accounts.",
      "أمر 'login' يطلب كلمة المرور المشتركة للخط. أما 'login local' فيأمر الجهاز بمطابقة اسم المستخدم وكلمة المرور مع الحسابات المنشأة بأمر 'username'."),

    Q("If BOTH 'enable secret' and 'enable password' are configured on the same switch, what happens when entering privileged mode?",
      "إذا تم ضبط كلاً من 'enable secret' و 'enable password' معاً على نفس السويتش، فماذا يحدث عند الدخول لوضع التمكين؟",
      [
        ("The switch prompts for BOTH passwords sequentially", "يطلب السويتش الكلمتين معاً بالتتابع"),
        ("The switch prioritizes and prompts ONLY for the 'enable secret'", "يعطي السويتش الأولوية لـ 'enable secret' ويطلبها وحدها"),
        ("The switch falls back to 'enable password' because it was created first", "يستخدم السويتش 'enable password' لأنها الأقدم"),
        ("A configuration conflict error occurs and disables access", "يحدث تعارض برمجي ويتم قفل الوصول للجهاز")
      ], 1,
      "Cisco IOS always gives precedence to 'enable secret' because it uses cryptographic hashing; 'enable password' is completely ignored.",
      "نظام سيسكو يعطي الأسبقية دائماً لـ 'enable secret' لأنها تعتمد على التجزئة التشفيرية، ويتم تجاهل 'enable password' بالكامل."),

    Q("What type of encryption does 'service password-encryption' apply to cleartext passwords, and why is it considered weak?",
      "ما هو نوع التشفير الذي يطبقه أمر 'service password-encryption'، ولماذا يعتبر ضعيفاً وغير آمن؟",
      [
        ("Type 7; it uses a weak, easily reversible XOR algorithm that can be cracked in milliseconds", "تشفير Type 7؛ وهو تمويه بسيط بخوارزمية XOR يمكن فكه في أجزاء من الثانية"),
        ("Type 5; it uses SHA-1 which is subject to mathematical collisions", "تشفير Type 5؛ وهو يستخدم خوارزمية SHA-1 المعرضة للتصادم"),
        ("Type 0; it leaves passwords in pure clear text without any alteration", "تشفير Type 0؛ وهو يترك النصوص صريحة دون تغيير"),
        ("Type 8; it requires excessive CPU resources to decrypt", "تشفير Type 8؛ وهو يستهلك موارد المعالج بشكل مفرط")
      ], 0,
      "Service password-encryption applies Type 7 encoding. Type 7 uses a static key and simple XOR cipher, making it trivial to reverse using widely available tools.",
      "أمر service password-encryption يطبق تشفير Type 7. وهو مجرد تمويه بمفتاح ثابت وخوارزمية XOR يسهل فكها فوراً بأدوات مجانية على الإنترنت."),

    Q("Which Cisco secret hashing algorithm is represented by 'Type 8' in the running configuration?",
      "أي خوارزمية تجزئة في سيسكو يشار إليها بالرقم 'Type 8' في ملف الإعدادات؟",
      [
        ("MD5 (Message Digest 5)", "خوارزمية MD5"),
        ("PBKDF2 with SHA-256", "خوارزمية PBKDF2 باستخدام SHA-256"),
        ("Scrypt memory-hard hash", "خوارزمية Scrypt"),
        ("Vigenère stream cipher", "خوارزمية Vigenère")
      ], 1,
      "Type 8 corresponds to PBKDF2 with HMAC-SHA-256. Type 5 is MD5, Type 9 is Scrypt, and Type 7 is Cisco's weak reversible cipher.",
      "النوع 8 يمثل خوارزمية PBKDF2 المعتمدة على SHA-256. بينما النوع 5 هو MD5، والنوع 9 هو Scrypt، والنوع 7 هو تشفير سيسكو الضعيف."),

    Q("Why is TACACS+ typically preferred over RADIUS for administrative management of routers and switches?",
      "لماذا يفضل استخدام بروتوكول TACACS+ بدلاً من RADIUS لإدارة أجهزة الراوتر والسويتش في الشبكات الكبيرة؟",
      [
        ("TACACS+ uses reliable TCP (port 49), separates Authorization from Authentication, and encrypts the entire packet", "لأن TACACS+ يستخدم TCP (منفذ 49)، ويفصل التخويل عن المصادقة، ويشفر كامل الحزمة"),
        ("TACACS+ is an open standard supported by all vendors, while RADIUS is Cisco proprietary", "لأن TACACS+ معيار مفتوح لكل الشركات، بينما RADIUS خاص بسيسكو فقط"),
        ("RADIUS does not support passwords longer than 8 characters", "لأن RADIUS لا يدعم كلمات مرور أطول من 8 أحرف"),
        ("TACACS+ uses UDP for faster command execution across WAN links", "لأن TACACS+ يستخدم UDP لسرعة تنفيذ الأوامر عبر شبكات WAN")
      ], 0,
      "TACACS+ runs over TCP port 49, encrypts the complete packet payload, and strictly separates Authentication, Authorization, and Accounting, allowing granular per-command authorization.",
      "بروتوكول TACACS+ يعمل عبر TCP منفذ 49، ويشفر كامل محتوى الحزمة، ويفصل تماماً بين المصادقة والتخويل مما يسمح بتحديد الصلاحيات بدقة لكل أمر على حدة.")
]

body_sections = [
    sec_user_mode,
    sec_enable_mode,
    sec_password_encryption,
    sec_secrets,
    sec_vty_lines,
    sec_aaa_servers,
    sec_matrix,
    sec_conclusion,
]

build(
    num=num,
    pct=pct,
    title=title,
    sub=sub,
    chip_en=chip_en,
    chip_ar=chip_ar,
    toc_items=toc_items,
    body_sections=body_sections,
    prev_href="lesson-10-cisco-ios-cli.html",
    prev_label="Introduction to Cisco IOS CLI",
    next_href="exam-unit-02-network-fundamentals.html",
    next_label="Unit 2 Comprehensive Exam & Question Bank",
    source_pdf="011-user mode and privileged mode security.pdf",
    extra_footnote="",
    recap_items=recap_items,
    quiz_items=quiz_items,
    out_path="lesson-11-user-mode-privileged-mode-security.html"
)
print("Successfully generated lesson-11-user-mode-privileged-mode-security.html!")
