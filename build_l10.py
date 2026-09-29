import lesson_lib
from lesson_lib import bi, bl, h2, src, extra, img, cli, diagram, Q, build, T

num = 10
pct = round((10 / 11) * 100) # 91%
title = "Introduction to Cisco IOS CLI (Command-Line Interface)"
sub = ("Mastering terminal emulation, console connections, CLI modes, and navigation shortcuts", "احتراف الاتصال بالكونسول، أوضاع الـ CLI، وإدارة إعدادات أجهزة سيسكو")
chip_en = "Unit 2: Network Fundamentals"
chip_ar = "الوحدة الثانية: أساسيات الشبكات"

toc_items = [
    ("connecting", "Connecting via Console", "الاتصال عبر منفذ الكونسول"),
    ("modes", "Cisco IOS Modes", "أوضاع ومستويات أوامر سيسكو"),
    ("config", "Running vs Startup Config", "ملفات الإعدادات والذاكرة"),
    ("help", "Help, Completion & Errors", "المساعدة والإكمال واكتشاف الأخطاء"),
    ("shortcuts", "Navigation Shortcuts", "اختصارات لوحة المفاتيح وسجل الأوامر"),
    ("do", "The 'do' Command", "أمر do للتنفيذ السريع"),
    ("pipe", "Piping Output Modifiers", "فلترة مخرجات الأوامر (Piping)"),
    ("conclusion", "Conclusion", "الخاتمة"),
]

# Section 1: Connecting via Console & Terminal Emulator
sec_connecting = h2("connecting", "Connecting via Console & Terminal Emulator", "الاتصال بجهاز سيسكو عبر منفذ الكونسول وبرامج المحاكاة") + src(
    bl("Most Cisco network devices (including routers and switches) use a <b>CLI (Command-Line Interface)</b> for configuration and management. The CLI is a text-based interface where you type commands to configure features or use <code>show</code> commands to verify and troubleshoot device operations.",
       f"أغلب أجهزة سيسكو (الروترات والسويتشات) بتعتمد على {T('CLI', 'Command-Line Interface — واجهة السطر البرمجي')} للضبط والإدارة. الـ CLI هي واجهة نصية بتكتب فيها الأوامر لإعداد وتفعيل الخصائص، أو بتستخدم أوامر <code>show</code> لفحص واستكشاف أخطاء الشبكة.") +
    bl("<b>Console Cabling:</b> When a device is fresh out of the box with no IP configuration, you cannot connect over the network (SSH/Telnet). You must establish an out-of-band physical connection using the <b>Console Port</b> (colored in light cyan/blue). Older devices use an RJ-45 console port paired with a light blue rollover cable (RJ-45 to DB9 serial or USB adapter). Modern Cisco switches also feature a mini-USB or micro-USB console port.",
       "<b>كابل الكونسول (Console Cabling):</b> لما الجهاز يكون جديد وخارج من كرتونته بدون أي إعدادات IP، مش هتقدر تتصل بيه عبر الشبكة (بـ SSH أو Telnet). لازم تعمل اتصال فيزيائي مباشر عبر <b>منفذ الكونسول (Console Port)</b> اللي لونه أزرق سماوي. الأجهزة بتستخدم منفذ RJ-45 مع كابل كونسول أزرق (Rollover Cable) بينتهي بـ DB9 serial أو USB، والأجهزة الحديثة فيها كمان منفذ mini-USB أو micro-USB.") +
    diagram(
        '<div style="font-family:var(--font-body);display:flex;justify-content:space-around;align-items:center;flex-wrap:wrap;gap:16px;">'
        '<div style="padding:16px;border:2px solid var(--accent);background:var(--panel2);border-radius:8px;text-align:center;">'
        '<b>Engineer Laptop</b><br><span style="font-size:0.85rem;color:var(--muted);">Running PuTTY / Tera Term</span></div>'
        '<div style="text-align:center;color:var(--accent);font-weight:bold;font-size:0.9rem;">'
        '&larr; Light Blue Rollover / USB Cable &rarr;<br><span style="font-size:0.8rem;color:var(--text);font-family:monospace;">Serial: 9600-8-N-1</span></div>'
        '<div style="padding:16px;border:2px solid var(--line);background:var(--panel2);border-radius:8px;text-align:center;">'
        '<b>Cisco Switch / Router</b><br><span style="font-size:0.85rem;color:var(--good);font-weight:bold;">[Console Port (RJ45 / USB)]</span></div>'
        '</div>',
        "Out-of-Band Management via Console Cable", "الاتصال المباشر لإدارة الأجهزة عبر كابل الكونسول"
    ) +
    img("images/lesson10/img_1.jpg", "Cisco Catalyst 2960 switch console ports RJ-45 and micro-USB",
        "Physical Console Connectors on Cisco Catalyst Switch (RJ-45 and micro-USB)", "منافذ الكونسول الفيزيائية على سويتش سيسكو كاتاليست (RJ-45 و micro-USB)",
        "Cisco Switch Console Connectors") +
    img("images/lesson10/img_2.png", "Cisco light blue console rollover cable",
        "Official Cisco Rollover Console Cable", "كابل الكونسول الأزرق (Rollover Cable) من سيسكو",
        "Cisco Rollover Cable") +
    bl("<b>Terminal Emulator Settings:</b> To connect via serial port using tools like <b>PuTTY</b>, <b>Tera Term</b>, or <b>SecureCRT</b>, you must configure the exact serial parameters required by Cisco IOS:",
       "<b>إعدادات برامج المحاكاة (Terminal Emulator):</b> عشان تفتح شاشة الكونسول ببرامج زي <b>PuTTY</b> أو <b>SecureCRT</b>، لازم تضبط إعدادات الاتصال التسلسلي (Serial) القياسية لأجهزة سيسكو:") +
    img("images/lesson10/img_5.jpg", "PuTTY Serial configuration for Cisco console",
        "Configuring PuTTY for Serial Connection (9600-8-N-1)", "إعداد برنامج PuTTY للاتصال بالكونسول (9600-8-N-1)",
        "PuTTY Serial Settings") +
    '<div class="table-wrap"><table><tr><th>' + bi("Serial Parameter", "خاصية الاتصال") + '</th><th>' + bi("Standard Cisco Value", "القيمة القياسية في سيسكو") + '</th><th>' + bi("Description", "الوصف والوظيفة") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>Baud Rate (Speed)</b></td><td class="mono-cell">9600 bps</td><td>' + bi("Speed of data transmission over serial line", "سرعة نقل البيانات عبر الكابل التسلسلي") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Data Bits</b></td><td class="mono-cell">8</td><td>' + bi("Number of data bits in each character", "عدد بتات البيانات لكل حرف") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Parity</b></td><td class="mono-cell">None (N)</td><td>' + bi("No parity bit used for error checking", "عدم استخدام بت تطابق") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Stop Bits</b></td><td class="mono-cell">1</td><td>' + bi("Single stop bit marking character end", "بت توقف واحد يشير لنهاية الحرف") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>Flow Control</b></td><td class="mono-cell">None</td><td>' + bi("No hardware/software flow control", "بدون تحكم في تدفق الإشارة") + '</td></tr>' +
    '</table></div>' +
    bl("<b>First Boot & POST:</b> When a switch or router powers on, it executes the <b>POST (Power-On Self-Test)</b> to verify CPU, DRAM, flash memory, and interface ASICs. Once POST passes successfully, the bootloader loads the Cisco IOS software image into RAM, presents licensing information, and initiates the CLI prompt.",
       "<b>بدء التشغيل واختبار POST:</b> لما تشغل الراوتر أو السويتش، بيبدأ باختبار الفحص الذاتي {T('POST', 'Power-On Self-Test — فحص عتاد الجهاز عند التشغيل')} للتحقق من المعالج والذاكرة والمنافذ. بعد نجاح الاختبار، بيتم تحميل نظام تشغيل سيسكو (IOS) من الفلاش إلى ذاكرة الـ RAM، وتظهر شاشة البداية.")
) + extra(
    "Crucial Exam & Practical Tip (9600 8-N-1): Always memorize '9600, 8, None, 1, None'. If you connect to a Cisco switch and see weird unreadable gibberish characters (like #@), the baud rate on your terminal emulator doesn't match the switch! Change the baud rate in PuTTY until clear English text appears.",
    "نصيحة عملية هامة جداً (9600 8-N-1): احفظ المعادلة دي صم. لو وصلت كابل الكونسول وفتحت PuTTY ولقيت طالعلك رموز غريبة وغير مفهومة (زي #@)، ده معناه فوراً إن سرعة الـ Baud Rate في البرنامج مش متطابقة مع سرعة السويتش! غير السرعة في PuTTY لحد ما الكلام يظهر إنجليزي سليم ومقروء."
)

# Section 2: Cisco IOS Modes
sec_modes = h2("modes", "Cisco IOS Modes & Navigation Hierarchy", "أوضاع ومستويات أوامر سيسكو والتنقل بينها") + src(
    bl("Cisco IOS is organized into a hierarchical structure of command modes. Each mode has its own distinct prompt, access privileges, and set of available commands:",
       "أوامر سيسكو متقسمة لهيكل هرمي من الأوضاع (Modes). كل وضع ليه علامة مميزة (Prompt)، وصلاحيات معينة، ومجموعة أوامر خاصة بيه:") +
    diagram(
        '<div style="font-family:monospace;display:flex;flex-direction:column;gap:12px;">'
        '<div style="padding:12px;border:1px solid var(--line);background:var(--panel2);border-radius:6px;">'
        '<b style="color:var(--muted);">1. User EXEC Mode:</b> <code>Switch&gt;</code><br>'
        '<span style="font-size:0.85rem;color:var(--text);">Basic view-only monitoring (ping, traceroute, limited show). No config changes allowed.</span></div>'
        '<div style="text-align:center;color:var(--accent);font-weight:bold;">&darr; type: enable &nbsp;|&nbsp; type: disable &uarr;</div>'
        '<div style="padding:12px;border:1px solid var(--accent);background:var(--panel2);border-radius:6px;">'
        '<b style="color:var(--accent);">2. Privileged EXEC Mode (Enable Mode):</b> <code>Switch#</code><br>'
        '<span style="font-size:0.85rem;color:var(--text);">Full viewing and maintenance (all show commands, debug, copy, erase, reload).</span></div>'
        '<div style="text-align:center;color:var(--accent);font-weight:bold;">&darr; type: configure terminal &nbsp;|&nbsp; type: exit / end &uarr;</div>'
        '<div style="padding:12px;border:1px solid var(--accent2);background:var(--panel2);border-radius:6px;">'
        '<b style="color:var(--accent2);">3. Global Configuration Mode:</b> <code>Switch(config)#</code><br>'
        '<span style="font-size:0.85rem;color:var(--text);">System-wide changes (hostname, banner, domain name, routing protocols).</span></div>'
        '<div style="text-align:center;color:var(--warn);font-weight:bold;">&darr; enter specific sub-modes &darr;</div>'
        '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;">'
        '<div style="padding:8px;border:1px dashed var(--line);border-radius:4px;background:var(--panel);font-size:0.85rem;"><b>Interface Mode:</b><br><code>Switch(config-if)#</code></div>'
        '<div style="padding:8px;border:1px dashed var(--line);border-radius:4px;background:var(--panel);font-size:0.85rem;"><b>Line Mode:</b><br><code>Switch(config-line)#</code></div>'
        '<div style="padding:8px;border:1px dashed var(--line);border-radius:4px;background:var(--panel);font-size:0.85rem;"><b>Router Mode:</b><br><code>Switch(config-router)#</code></div>'
        '</div>'
        '</div>',
        "Hierarchical Navigation of Cisco IOS Modes", "الهيكل الهرمي للتنقل بين أوضاع تشغيل سيسكو"
    ) +
    bl("<b>Navigating Between Modes:</b> Here is how you move up and down through the hierarchy in practice:",
       "<b>طريقة التنقل عملياً بين الأوضاع:</b> ده مثال حي للتنقل بين المستويات المختلفة:") +
    cli("Switch> <b>enable</b>\nSwitch# <b>configure terminal</b>\nEnter configuration commands, one per line.  End with CNTL/Z.\nSwitch(config)# <b>interface FastEthernet 0/1</b>\nSwitch(config-if)# <b>description LAN_UPLINK</b>\nSwitch(config-if)# <b>exit</b>\nSwitch(config)# <b>exit</b>\nSwitch# <b>disable</b>\nSwitch>") +
    bl("<b>Exit vs End vs Ctrl+Z:</b><br>• <code>exit</code> moves you back <b>one level up</b> the hierarchy (e.g. from <code>(config-if)#</code> to <code>(config)#</code>).<br>• <code>end</code> or pressing <b>Ctrl+Z</b> jumps directly from <b>any configuration sub-mode</b> all the way back to Privileged EXEC mode (<code>Switch#</code>).",
       "<b>الفرق بين exit و end و Ctrl+Z:</b><br>• أمر <code>exit</code> بيرجعك <b>خطوة واحدة للخلف</b> للمستوى اللي قبله (مثلاً من <code>(config-if)#</code> إلى <code>(config)#</code>).<br>• أمر <code>end</code> أو الضغط على <b>Ctrl+Z</b> بيخرجك فوراً من <b>أي وضع فرعي</b> ويرجعك مباشرة لوضع الـ Privileged EXEC الرئيسي (<code>Switch#</code>).")
) + extra(
    "Why does Cisco separate User Mode (>) from Privileged Mode (#)? For Security! In User Mode, a guest or junior technician can view basic interface status and run ping tests without being able to see sensitive configurations, passwords, or reload the router. Privileged Mode is password-protected (via 'enable secret') to ensure only authorized admins can view configs or make modifications.",
    "ليه سيسكو فصلت بين User Mode (>) و Privileged Mode (#)؟ عشان الأمان! في الـ User Mode، أي فني مبتدئ يقدر يشوف حاجات بسيطة ويعمل ping للتأكد من الشبكة، لكن ميقدرش يشوف الإعدادات الحساسة ولا الباسوردات ولا يطفي الجهاز. وضع الـ Privileged بيكون محمي بباسورد قوية (عبر أمر 'enable secret') عشان الأدمن المعتمد بس هو اللي يقدر يغير حاجة."
)

# Section 3: Running vs Startup Config
sec_config = h2("config", "Running-Config vs Startup-Config & Memory Types", "ملفات الإعدادات وأنواع الذاكرة في أجهزة سيسكو") + src(
    bl("Cisco routers and switches use multiple types of memory to store their operating system, active configuration, and persistent boot configuration:",
       "روترات وسويتشات سيسكو بتستخدم كذا نوع من الذاكرة لتخزين نظام التشغيل والإعدادات الحالية وإعدادات الإقلاع الدائمة:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Memory Type", "نوع الذاكرة") + '</th><th>' + bi("Volatility", "طبيعة الذاكرة") + '</th><th>' + bi("Stores What?", "ماذا تخزن؟") + '</th><th>' + bi("Command to View", "أمر العرض") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>RAM (DRAM)</b></td><td>Volatile (Lost on power off)</td><td><b>running-config</b>, routing tables, ARP cache, packet buffers</td><td class="mono-cell"><code>show running-config</code></td></tr>' +
    '<tr><td class="mono-cell"><b>NVRAM</b></td><td>Non-Volatile (Permanent)</td><td><b>startup-config</b>, software configuration register</td><td class="mono-cell"><code>show startup-config</code></td></tr>' +
    '<tr><td class="mono-cell"><b>Flash Memory</b></td><td>Non-Volatile (Permanent)</td><td>Cisco IOS Software images (.bin files), backup files</td><td class="mono-cell"><code>show flash:</code></td></tr>' +
    '<tr><td class="mono-cell"><b>ROM</b></td><td>Permanent (Read-Only)</td><td>Bootstrap program, POST diagnostics, ROMMON recovery mode</td><td class="mono-cell"><code>show version</code></td></tr>' +
    '</table></div>' +
    bl("<b>Saving Configurations:</b> Any command you type in configuration mode takes effect <b>immediately</b> in RAM (running-config). However, if the power drops or the switch reboots, all unsaved changes are lost! To save changes permanently to NVRAM:",
       "<b>حفظ الإعدادات:</b> أي أمر بتكتبه بيتطبق <b>في نفس اللحظة</b> في ذاكرة الـ RAM (الـ running-config). لكن لو الكهرباء قطعت أو الجهاز اتعمله ريستارت، كل اللي كتبته هيروح! عشان تحفظ الإعدادات بشكل دائم في الـ NVRAM:") +
    img("images/lesson10/img_9.jpg", "RAM running-config vs NVRAM startup-config memory diagram",
        "Visualizing Memory: Volatile RAM (running-config) vs Persistent NVRAM (startup-config)", "مخطط توضيحي للذاكرة: ذاكرة RAM المؤقتة (running-config) مقابل NVRAM الدائمة (startup-config)",
        "RAM vs NVRAM Diagram") +
    cli("Switch# <b>copy running-config startup-config</b>\nDestination filename [startup-config]? \nBuilding configuration...\n[OK]\n\n! Shorthand legacy command (widely used in real life):\nSwitch# <b>write memory</b>  ! or simply: <b>wr</b>") +
    bl("<b>Erasing and Resetting to Factory Defaults:</b> To completely wipe a switch or router configuration back to clean factory state:",
       "<b>مسح الإعدادات والعودة لضبط المصنع:</b> عشان تمسح كل الإعدادات القديمة وترجع الجهاز جديد تماماً:") +
    cli("Switch# <b>write erase</b>   ! or: <b>erase startup-config</b>\nErasing the nvram filesystem will remove all configuration files! Continue? [confirm]\n[OK]\nErase of nvram: complete\nSwitch# <b>reload</b>\nProceed with reload? [confirm]")
) + extra(
    "Golden Rule in Telecom & Enterprise Networks: Always do 'copy run start' (or 'wr') after finishing your work! In Egyptian ISPs and enterprise NOCs, engineers who forget to save configs before a maintenance window reboots the router can cause major service outages. Also note: On Catalyst switches, erasing startup-config does NOT delete the VLAN database (`vlan.dat` in flash)! You must also run `delete flash:vlan.dat` to completely factory reset a switch.",
    "القاعدة الذهبية في كل شركات الاتصالات وشبكات الشركات: دايماً اكتب 'wr' أو 'copy run start' أول ما تخلص شغلك! في شركات الـ NOC، لو مهندس نسي يحفظ والراوتر اتعمله ريستارت فجأة، الإعدادات بتضيع والخدمة بتقف. ملحوظة هامة جداً للامتحانات: مسح الـ startup-config في السويتش مش بيمسح الـ VLANs! لأن الـ VLANs بتتخزن في ملف اسمه `vlan.dat` في الفلاش، ولازم تمسحه بأمر `delete flash:vlan.dat` عشان تصفر السويتش بالكامل."
)

# Section 4: Help, Completion & Errors
sec_help = h2("help", "Context Help, Autocompletion & Error Messages", "المساعدة الذكية، الإكمال التلقائي، واكتشاف الأخطاء") + src(
    bl("Cisco IOS features powerful built-in help and diagnostic tools to assist you without needing to memorize every complex command syntax:",
       "نظام سيسكو مزود بأدوات مساعدة ذكية متطورة بتساعدك توصل لأي أمر ومعاملاته بسهولة من غير ما تحفظ كل التفاصيل:") +
    bl("<b>1. Context-Sensitive Help with Question Mark (?):</b><br>• <code>?</code> alone at prompt: lists all available commands in current mode.<br>• <code>c?</code> (no space): lists all commands that start with the letter 'c' (e.g., clear, clock, configure).<br>• <code>clock ?</code> (with a space): shows the next keyword or argument required by the command.",
       "<b>1. المساعدة السياقية بعلامة الاستفهام (?):</b><br>• كتابة <code>?</code> لوحدها: بتعرض كل الأوامر المتاحة في الوضع الحالي.<br>• كتابة <code>c?</code> (بدون مسافة): بتعرض كل الأوامر اللي بتبدأ بحرف c (زي clear و clock و configure).<br>• كتابة <code>clock ?</code> (بمسافة): بتوريك الكلمة أو المعامل التالي المطلوب إدخاله بعد clock.") +
    cli("Switch# <b>clock ?</b>\n  set  Set the time and date\n\nSwitch# <b>clock set ?</b>\n  hh:mm:ss  Current Time\n\nSwitch# <b>clock set 15:30:00 ?</b>\n  <1-31>  Day of the month\n  MONTH   Month of the year") +
    bl("<b>2. Tab Key (Autocompletion):</b> Pressing <b>Tab</b> automatically completes the remainder of a command word, provided you have typed enough characters to make it unique (e.g. typing <code>conf</code> and pressing Tab expands to <code>configure</code>).",
       "<b>2. زر الـ Tab للإكمال التلقائي:</b> الضغط على زر <b>Tab</b> بيكمل باقي الكلمة تلقائياً طالما كتبت حروف كافية تميزها عن غيرها (مثلاً لو كتبت <code>conf</code> وضغطت Tab هتتكمل تلقائياً إلى <code>configure</code>).") +
    bl("<b>3. Understanding CLI Error Messages:</b> When an error occurs, Cisco IOS tells you exactly what went wrong:",
       "<b>3. فهم رسائل الأخطاء في سيسكو:</b> لما يحصل خطأ، الـ CLI بيوضحلك نوع المشكلة بدقة:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Error Message", "رسالة الخطأ") + '</th><th>' + bi("What it Means", "المعنى وسبب الخطأ") + '</th><th>' + bi("Example & Fix", "مثال وطريقة الحل") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>% Ambiguous command</b></td><td>Not enough characters were typed to distinguish between multiple matching commands</td><td>Typing <code>c</code> in enable mode (could be <code>clear</code>, <code>clock</code>, or <code>configure</code>). Type more letters like <code>conf</code>.</td></tr>' +
    '<tr><td class="mono-cell"><b>% Incomplete command</b></td><td>The command is valid so far, but requires additional mandatory parameters</td><td>Typing <code>clock set 14:00:00</code> without specifying day/month. Use <code>?</code> to see missing arguments.</td></tr>' +
    '<tr><td class="mono-cell"><b>% Invalid input detected at \'^\' marker</b></td><td>A syntax error was detected. The caret symbol (<code>^</code>) points directly to the first unrecognized character</td><td>Typing <code>shwo version</code>. The <code>^</code> points under &apos;w&apos; showing where the typo began.</td></tr>' +
    '</table></div>'
) + extra(
    "Exam Trick on Caret (^) Marker: In the CCNA exam simulations, if you see the caret symbol `^`, look directly above it! The error is ALWAYS at or immediately following that specific character. It saves you from re-reading a 50-character command when only one letter is wrong.",
    "خدعة امتحانات CCNA بخصوص علامة السهم (^): في أسئلة الامتحان العملي والمحاكاة، لو طلعلك رمز `^`، بص فوقه مباشرة! الخطأ دايماً بيكون في الحرف اللي فوق السهم بالضبط. الحركة دي بتوفر عليك وقت قراءة الأمر الطويل وتعرفك الحرف الغلط فوراً."
)

# Section 5: Navigation Shortcuts
sec_shortcuts = h2("shortcuts", "CLI Shortcuts & Command History", "اختصارات لوحة المفاتيح وسجل الأوامر (History)") + src(
    bl("Professional network engineers work rapidly in the CLI using built-in keyboard shortcuts and command recall history:",
       "مهندسو الشبكات المحترفون بيتحركوا بسرعة كبيرة في الـ CLI باستخدام اختصارات لوحة المفاتيح وسجل استرجاع الأوامر:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Keyboard Shortcut", "الاختصار") + '</th><th>' + bi("Action Performed", "الوظيفة") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>Ctrl + A</b></td><td>Moves the cursor to the <b>beginning</b> of the current line</td></tr>' +
    '<tr><td class="mono-cell"><b>Ctrl + E</b></td><td>Moves the cursor to the <b>end</b> of the current line</td></tr>' +
    '<tr><td class="mono-cell"><b>Ctrl + Z</b> (or <code>end</code>)</td><td>Instantly returns to Privileged EXEC mode (<code>#</code>) from any configuration sub-mode</td></tr>' +
    '<tr><td class="mono-cell"><b>Ctrl + C</b></td><td>Aborts the current command execution or exits Setup Mode</td></tr>' +
    '<tr><td class="mono-cell"><b>Up / Down Arrows</b></td><td>Recalls previously entered commands from the history buffer</td></tr>' +
    '<tr><td class="mono-cell"><b>Ctrl + Shift + 6</b></td><td>Breaks/aborts an ongoing ping, traceroute, or unwanted DNS broadcast hang</td></tr>' +
    '</table></div>' +
    bl("<b>Command History Buffer:</b> Cisco IOS automatically remembers the last <b>10 commands</b> you typed by default. You can view them using <code>show history</code> or increase the buffer size with <code>terminal history size &lt;number&gt;</code>.",
       "<b>سجل الأوامر (History Buffer):</b> سيسكو تلقائياً بيحفظ آخر <b>10 أوامر</b> كتبتها افتراضياً. تقدر تعرضهم بأمر <code>show history</code> أو تكبر حجم السجل لغاية 256 بأمر <code>terminal history size 50</code>.")
) + extra(
    "Life-Saving Shortcut: Ctrl + Shift + 6! If you accidentally type an invalid command and forgot to configure 'no ip domain-lookup', the router begins broadcasting to 255.255.255.255 and freezes your terminal. Pressing Ctrl+Shift+6 immediately breaks and terminates the lookup loop!",
    "اختصار الإنقاذ السريع: Ctrl + Shift + 6! لو كتبت كلمة غلط بالغلط وكنت ناسي تحط أمر 'no ip domain-lookup'، الراوتر هيبدأ يعمل broadcast ويهنج الشاشة. دوس مع بعض على Ctrl + Shift + 6 وهيوقف المحاولة ويرجعلك شاشة التحكم فوراً!"
)

# Section 6: The "do" Command
sec_do = h2("do", "The 'do' Command", "أمر do للتنفيذ المباشر من أوضاع الإعدادات") + src(
    bl("Normally, <code>show</code> and <code>debug</code> commands can only be executed in Privileged EXEC mode (<code>Switch#</code>). If you are deep inside configuration mode, typing a show command generates an error:",
       "في العادة، أوامر <code>show</code> و <code>debug</code> بتشتغل بس في وضع الـ Privileged EXEC (<code>Switch#</code>). لو أنت جوا وضع الإعدادات وكتبت أمر show، بيطلعلك خطأ:") +
    cli("Switch(config-if)# <b>show ip interface brief</b>\n                    ^\n% Invalid input detected at '^' marker.") +
    bl("Without the <code>do</code> command, you would have to type <code>exit</code> or <code>end</code>, run the show command, and then navigate all the way back into the interface sub-mode. To avoid this frustration, Cisco introduced the <b>do</b> prefix:",
       "من غير أمر <code>do</code>، كنت هتضطر تخرج بـ <code>exit</code>، وتشغل أمر الـ show، وبعدين ترجع تدخل تاني لكل المستويات الفرعية. عشان يحلوا المشكلة دي، سيسكو أضافت بادئة <b>do</b>:") +
    cli("Switch(config-if)# <b>do show ip interface brief</b>\nInterface              IP-Address      OK? Method Status                Protocol\nFastEthernet0/1        unassigned      YES unset  up                    up      \nFastEthernet0/2        unassigned      YES unset  down                  down\n\nSwitch(config)# <b>do ping 10.1.1.1</b>\nType escape sequence to abort.\nSending 5, 100-byte ICMP Echos to 10.1.1.1, timeout is 2 seconds:\n!!!!!\nSuccess rate is 100 percent (5/5)") +
    bl("The <code>do</code> command allows you to run ANY privileged mode command (like <code>show</code>, <code>ping</code>, <code>traceroute</code>, or <code>write memory</code>) from within configuration mode!",
       "أمر <code>do</code> بيسمحلك تشغل أي أمر من أوامر وضع الـ Privileged (زي <code>show</code> أو <code>ping</code> أو <code>traceroute</code> أو حتى <code>write memory</code>) وأنت في مكانك جوا وضع الإعدادات!")
) + extra(
    "Historical Limitation to Remember: In older Cisco IOS versions, context-sensitive help (`?`) does not work after the `do` command (typing `do show ?` would output an error or show nothing). You had to know the exact syntax of the command. Modern Cisco IOS versions have resolved this, but it remains a famous interview trivia question!",
    "معلومة امتحانات تاريخية: في إصدارات سيسكو IOS القديمة، علامة الاستفهام (`?`) مكنتش بتشتغل بعد كلمة `do` (يعني لو كتبت `do show ?` مكنش بيطلعلك مساعدة). كنت لازم تكون حافظ صيغة الأمر بالضبط. الإصدارات الحديثة حلت الموضوع ده، بس لسه سؤال شهير في المقابلات!"
)

# Section 7: Piping Output Modifiers
sec_pipe = h2("pipe", "Filtering Output with Pipe (|) Modifiers", "فلترة مخرجات الأوامر باستخدام الـ Pipe (|)") + src(
    bl("On complex production devices, commands like <code>show running-config</code> produce hundreds of lines of output. Scrolling through all of them is slow and inefficient. Cisco IOS allows you to pipe the output through filters using the vertical bar (<b>|</b>):",
       "في بيئات العمل الحقيقية، أمر زي <code>show running-config</code> بيطلع مئات الأسطر. إنك تقعد تقلب فيهم كلهم مضيعة كبيرة للوقت. سيسكو بتوفرلك إمكانية فلترة النتائج باستخدام علامة الـ Pipe (<b>|</b>):") +
    cli("Switch# <b>show running-config | ?</b>\n  append    Append redirected output to URL\n  begin     Begin with the line that matches\n  exclude   Exclude lines that match\n  include   Include lines that match\n  section   Filter a section of the output") +
    '<div class="table-wrap"><table><tr><th>' + bi("Filter Modifier", "نوع الفلتر") + '</th><th>' + bi("How it Works", "طريقة عمله") + '</th><th>' + bi("Practical Command Example", "مثال عملي شهير") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>| include &lt;regex&gt;</b></td><td>Shows <b>only</b> the lines that contain the matching pattern (like grep)</td><td class="mono-cell"><code>show ip int br | include up</code></td></tr>' +
    '<tr><td class="mono-cell"><b>| exclude &lt;regex&gt;</b></td><td>Displays all lines <b>except</b> those matching the pattern</td><td class="mono-cell"><code>show ip int br | exclude unassigned</code></td></tr>' +
    '<tr><td class="mono-cell"><b>| begin &lt;regex&gt;</b></td><td>Starts displaying output from the first line that matches the pattern onward</td><td class="mono-cell"><code>show run | begin line vty</code></td></tr>' +
    '<tr><td class="mono-cell"><b>| section &lt;regex&gt;</b></td><td>Displays the entire configuration block/paragraph associated with that keyword</td><td class="mono-cell"><code>show run | section router ospf</code></td></tr>' +
    '</table></div>' +
    bl("Example of <code>| section</code> in action:",
       "مثال عملي على استخدام <code>| section</code>:") +
    cli("Switch# <b>show running-config | section line</b>\nline con 0\n logging synchronous\nline vty 0 4\n login\n transport input ssh")
) + extra(
    "NOC & Exam Time-Saver: `show ip int br | ex unassigned` is universally the favorite command of NOC engineers. Instead of scrolling through 48 FastEthernet switchports with 'unassigned', this command instantly displays only the ports that actually have configured IP addresses and active connections!",
    "أسرع أمر في غرف الـ NOC والامتحانات: أمر `show ip int br | ex unassigned` هو السحر لكل مهندسي الشبكات. بدل ما تشوف جدول عملاق فيه 48 بورت مكتوب عليهم unassigned، الأمر ده بيخفيهم كلهم في ثانية ويعرضلك بس البورتات اللي عليها IPs وروترات شغالة!"
)

# Section 8: Conclusion
sec_conclusion = h2("conclusion", "Conclusion", "خلاصة الدرس") + src(
    bl("The Cisco IOS Command-Line Interface is the primary tool of every network engineer. Mastering navigation, configuration saving, shortcuts, and output filters transforms configuration and troubleshooting from a tedious task into an efficient process.",
       "واجهة السطر البرمجي لسيسكو (IOS CLI) هي السلاح الأساسي لكل مهندس شبكات. إتقان التنقل بين الأوضاع، وحفظ الإعدادات، واستخدام الاختصارات وفلاتر البحث بيحول عملية الإدارة واستكشاف الأعطال لمهمة سريعة واحترافية.") +
    bl("Key Takeaways for CCNA:<br>• <b>Serial Settings:</b> 9600 baud, 8 data bits, no parity, 1 stop bit, no flow control (9600-8-N-1).<br>• <b>Modes:</b> User Mode (<code>&gt;</code>), Privileged Mode (<code>#</code>), Global Config (<code>(config)#</code>).<br>• <b>Memory:</b> RAM = running-config (volatile), NVRAM = startup-config (persistent). Save with <code>copy run start</code> or <code>wr</code>.<br>• <b>do command:</b> Executes privileged commands from within configuration sub-modes.<br>• <b>Piping:</b> Use <code>| include</code>, <code>| exclude</code>, <code>| begin</code>, and <code>| section</code> to instantly pinpoint information.",
       "أهم نقاط CCNA المستفادة:<br>• <b>إعدادات الكونسول:</b> 9600 سرعة، 8 بت، بدون تطابق، 1 بت توقف، بدون تحكم في التدفق (9600-8-N-1).<br>• <b>الأوضاع:</b> وضع المستخدم (<code>&gt;</code>)، وضع الصلاحيات (<code>#</code>)، وضع الإعدادات العامة (<code>(config)#</code>).<br>• <b>الذاكرة:</b> RAM = running-config (مؤقتة)، NVRAM = startup-config (دائمة). احفظ بـ <code>copy run start</code> أو <code>wr</code>.<br>• <b>أمر do:</b> بيشغل أوامر الـ show والـ ping وأنت داخل أوضاع الإعدادات.<br>• <b>الفلترة:</b> استخدم <code>| include</code> و <code>| section</code> للوصول الفوري للمعلومة المطلوبة.")
) + extra(
    "Looking Ahead to Lesson 11: In the next lesson, we will build directly upon this foundation to learn how to secure the Cisco CLI: setting up console passwords, securing privileged mode with `enable secret`, configuring vty lines for remote management, and encrypting stored passwords with service password-encryption.",
    "تمهيد للدرس القادم (الدرس 11): في الدرس الجاي هنبني مباشرة على اللي اتعلمناه هنا عشان نعرف إزاي نأمّن أجهزة سيسكو: باسورد الكونسول، وحماية وضع الـ enable بأمر `enable secret`، وتأمين خطوط الـ vty، وتشفير كلمات المرور المخزنة."
)

# Recap Quiz (Testing Lesson 9: DNS)
recap = [
    Q("In the previous lesson on DNS, what transport layer protocol and destination port are used for standard host queries?",
      "في الدرس السابق الخاص بـ DNS، ما هو بروتوكول طبقة النقل ومنفذ الوجهة المستخدم لاستعلامات الأجهزة العادية؟",
      [("TCP port 80", "منفذ TCP 80"),
       ("UDP port 53", "منفذ UDP 53"),
       ("TCP port 53", "منفذ TCP 53"),
       ("UDP port 67", "منفذ UDP 67")],
      1,
      "Standard client DNS queries use UDP port 53 for speed, low overhead, and absence of connection setup delay.",
      "استعلامات DNS العادية للأجهزة بتستخدم UDP منفذ 53 لسرعته وخفة وزنه وعدم وجود تأخير لفتح الاتصال."),

    Q("In the FQDN 'server.cisco.com.', what does the trailing period (.) at the very end represent?",
      "في اسم النطاق المؤهل بالكامل 'server.cisco.com.'، ماذا تمثل النقطة الأخيرة (.) في النهاية؟",
      [("The root of the DNS namespace hierarchy", "جذر الهيكل الهرمي لنظام أسماء النطاقات (DNS Root)"),
       ("A syntax error that prevents resolution", "خطأ إملائي يمنع الترجمة"),
       ("The top-level domain extension", "امتداد نطاق المستوى الأعلى"),
       ("An alias pointer to the IP address", "مؤشر مستعار لعنوان الـ IP")],
      0,
      "The trailing dot explicitly signifies the root of the DNS hierarchy. While web browsers hide it, it is officially present in a Fully Qualified Domain Name.",
      "النقطة الأخيرة بتمثل رسمياً جذر شجرة الـ DNS بالكامل. ورغم أن المتصفحات بتخفيها، إلا إنها جزء أساسي من الاسم الكامل FQDN."),

    Q("Why do network engineers commonly enter 'no ip domain-lookup' on Cisco routers?",
      "لماذا يحرص مهندسو الشبكات على إدخال أمر 'no ip domain-lookup' على أجهزة سيسكو؟",
      [("To disable the Ethernet interfaces", "لتعطيل منافذ الإيثرنت"),
       ("To stop the router from freezing and broadcasting DNS queries when a command is mistyped", "لمنع الراوتر من تجميد الشاشة وعمل بث DNS عند كتابة أمر خاطئ دون قصد"),
       ("To turn off IP routing", "لتعطيل توجيه حزم الـ IP"),
       ("To allow Telnet access without a password", "للسماح بالدخول عبر Telnet بدون كلمة مرور")],
      1,
      "Without 'no ip domain-lookup', any mistyped command causes Cisco IOS to treat the input as a hostname and broadcast DNS queries, freezing the console for up to 30 seconds.",
      "بدون هذا الأمر، أي كلمة تتكتب غلط في سيسكو بيعتبرها الراوتر اسم جهاز وبيعمل بث DNS لمحاولة ترجمته، فتهنج الشاشة لمدة تصل لـ 30 ثانية.")
]

# Lesson Quiz (Testing Lesson 10: Cisco IOS CLI)
quiz = [
    Q("What are the standard serial communication parameters required to connect a console cable to a Cisco device?",
      "ما هي إعدادات الاتصال التسلسلي (Serial) القياسية المطلوبة للاتصال بجهاز سيسكو عبر كابل الكونسول؟",
      [("9600 baud, 8 data bits, no parity, 1 stop bit, no flow control (9600-8-N-1)", "سرعة 9600، 8 بت بيانات، بدون تطابق، 1 بت توقف، بدون تحكم بالتدفق (9600-8-N-1)"),
       ("115200 baud, 7 data bits, even parity, 2 stop bits", "سرعة 115200، 7 بت بيانات، تطابق زوجي، 2 بت توقف"),
       ("4800 baud, 8 data bits, odd parity, 1 stop bit", "سرعة 4800، 8 بت بيانات، تطابق فردي، 1 بت توقف"),
       ("9600 baud, 8 data bits, mark parity, flow control hardware", "سرعة 9600، 8 بت بيانات، تطابق علامة، تحكم تدفق بالعتاد")],
      0,
      "The universal standard settings for connecting to a Cisco console port are: 9600 baud, 8 data bits, no parity, 1 stop bit, and no flow control (9600-8-N-1).",
      "الإعدادات القياسية الثابتة للاتصال بمنفذ الكونسول في سيسكو هي: 9600 baud و 8 بت و None و 1 بت و None (9600-8-N-1)."),

    Q("When you configure a command in 'Switch(config)#', where is the change immediately stored?",
      "عند إدخال وتطبيق أمر في وضع الإعدادات 'Switch(config)#'، أين يتم تخزين التعديل فوراً؟",
      [("In NVRAM as part of the startup-config", "في ذاكرة NVRAM كجزء من startup-config"),
       ("In RAM as part of the running-config", "في ذاكرة RAM كجزء من running-config"),
       ("In Flash memory alongside the IOS image", "في ذاكرة الفلاش بجانب نظام التشغيل"),
       ("In ROM permanently", "في ذاكرة ROM بشكل دائم")],
      1,
      "Configuration changes take effect immediately in volatile RAM as part of the running-config. They are not stored in persistent NVRAM until you run 'copy running-config startup-config' or 'write memory'.",
      "التعديلات بتدخل حيز التنفيذ فوراً في ذاكرة RAM المؤقتة ضمن الـ running-config. ومش بتتحفظ في NVRAM إلا بعد كتابة أمر الحفظ `copy run start` أو `wr`."),

    Q("You enter 'clock set 14:00:00' in Privileged EXEC mode and the CLI returns '% Incomplete command'. What does this mean?",
      "قمت بكتابة 'clock set 14:00:00' في وضع الصلاحيات وظهرت الرسالة '% Incomplete command'. ماذا تعني هذه الرسالة؟",
      [("The command is misspelled and does not exist", "الأمر مكتوب بشكل خاطئ وغير موجود في النظام"),
       ("The command syntax is valid so far, but requires additional mandatory arguments (e.g. month, day, year)", "صيغة الأمر صحيحة حتى الآن، لكن ينقصها معاملات إجبارية إضافية (مثل الشهر واليوم والسنة)"),
       ("You lack administrative privileges to run this command", "ليس لديك الصلاحيات الكافية لتشغيل هذا الأمر"),
       ("The switch clock hardware has failed", "ساعة السويتش الداخلية معطلة فيزيائياً")],
      1,
      "'% Incomplete command' means you haven't provided all required arguments for the command. Using '?' shows what parameters are still needed to complete the command.",
      "رسالة '% Incomplete command' معناها إن الأمر صح لحد دلوقتي، لكن لسه ناقصه معاملات إجبارية عشان يتنفذ. استخدام علامة `?` بيوريك إيه اللي ناقص."),

    Q("From deep within sub-interface configuration mode 'Router(config-subif)#', what shortcut takes you directly back to Privileged EXEC mode 'Router#'?",
      "وأنت داخل وضع إعدادات المنفذ الفرعي 'Router(config-subif)#'، ما الاختصار الذي يعيدك فوراً إلى وضع 'Router#' الرئيسي؟",
      [("Ctrl + C", "Ctrl + C"),
       ("Ctrl + Z (or typing 'end')", "Ctrl + Z (أو كتابة أمر 'end')"),
       ("Ctrl + Shift + 6", "Ctrl + Shift + 6"),
       ("Ctrl + A", "Ctrl + A")],
      1,
      "Pressing Ctrl+Z or typing 'end' jumps directly from any configuration sub-mode back to Privileged EXEC mode (#), unlike 'exit' which only moves up one level.",
      "الضغط على Ctrl+Z أو كتابة أمر 'end' بينقلك فوراً من أي وضع إعدادات فرعي إلى وضع الـ Privileged EXEC (#) مباشرة، بعكس أمر exit اللي بيرجعك خطوة واحدة بس."),

    Q("An engineer is configuring an interface 'SW1(config-if)#' and wants to check IP interface statuses without exiting to privileged mode. Which command does this?",
      "مهندس يقوم بضبط منفذ 'SW1(config-if)#' ويريد فحص حالة عناوين IP للمنافذ دون الخروج لوضع الـ privileged. أي أمر يحقق ذلك؟",
      [("show ip interface brief", "show ip interface brief"),
       ("do show ip interface brief", "do show ip interface brief"),
       ("run show ip interface brief", "run show ip interface brief"),
       ("exec show ip interface brief", "exec show ip interface brief")],
      1,
      "The 'do' prefix allows executing any Privileged EXEC command (such as show, ping, traceroute, or write) directly from within configuration mode.",
      "بادئة 'do' بتسمح بتشغيل أي أمر من أوامر وضع الصلاحيات (زي show و ping و wr) وأنت في مكانك داخل أوضاع الإعدادات دون الحاجة للخروج."),

    Q("Which output modifier command displays only the configuration block corresponding to 'line vty' inside the running configuration?",
      "أي أمر فلترة باستخدام الـ Pipe يعرض فقرة الإعدادات الخاصة بـ 'line vty' فقط من ملف الـ running-config؟",
      [("show running-config | include line vty", "show running-config | include line vty"),
       ("show running-config | section line vty", "show running-config | section line vty"),
       ("show running-config | begin line vty", "show running-config | begin line vty"),
       ("show running-config | exclude line vty", "show running-config | exclude line vty")],
      1,
      "The '| section' modifier displays the matching line along with all its indented sub-configuration lines belonging to that section.",
      "فلتر '| section' بيعرض السطر المطابق وكل الأسطر والخصائص التابعة ليه في نفس الفقرة، مما يوفر وقتاً كبيراً في استعراض الإعدادات.")
]

build(
    num=10,
    pct=pct,
    title=title,
    sub=sub,
    chip_en=chip_en,
    chip_ar=chip_ar,
    toc_items=toc_items,
    body_sections=[sec_connecting, sec_modes, sec_config, sec_help, sec_shortcuts, sec_do, sec_pipe, sec_conclusion],
    prev_href="lesson-09-dns.html", prev_label="Introduction to DNS",
    next_href="lesson-11-user-mode-privileged-mode-security.html", next_label="User Mode & Privileged Mode Security",
    source_pdf="010-introduction to cisco ios cli (command-line interface).pdf",
    extra_footnote="Created using strictly verified CCNA guidelines and real-world networking practices.",
    recap_items=recap,
    quiz_items=quiz,
    out_path="/Users/mohammedelshora/Desktop/Shora/projects/ccna/Network_Fundamentals/lesson-10-cisco-ios-cli.html"
)

print("✅ Lesson 10 built successfully!")
