import lesson_lib
from lesson_lib import bi, bl, h2, src, extra, img, cli, diagram, Q, build, T

num = 9
pct = round((9 / 11) * 100) # 82%
title = "Introduction to DNS (Domain Name System)"
sub = ("How domain names are translated into IP addresses across the global network", "كيفية تحويل أسماء النطاقات إلى عناوين IP عبر الشبكة العالمية")
chip_en = "Unit 2: Network Fundamentals"
chip_ar = "الوحدة الثانية: أساسيات الشبكات"

toc_items = [
    ("what", "What is DNS?", "ما هو نظام DNS؟"),
    ("hierarchy", "DNS Hierarchy", "الهيكل الهرمي لـ DNS"),
    ("fqdn", "FQDN & Root Dot", "الاسم الكامل FQDN ونقطة الجذر"),
    ("resolution", "How Resolution Works", "كيف تعمل عملية الاستعلام والترجمة؟"),
    ("transport", "UDP vs TCP Port 53", "بروتوكول النقل: UDP أم TCP 53؟"),
    ("wireshark", "Wireshark Packet Analysis", "تحليل حزم DNS في Wireshark"),
    ("records", "Common DNS Record Types", "أهم أنواع سجلات DNS"),
    ("cisco", "Cisco IOS & Troubleshooting", "أوامر سيسكو والتشخيص العملي"),
    ("conclusion", "Conclusion", "الخاتمة"),
]

# Section: What is DNS?
sec_what = h2("what", "What is DNS?", "ما هو نظام DNS؟") + src(
    bl("DNS (Domain Name System) is a network protocol that we use to find the IP addresses of hostnames. Computers use IP addresses to communicate, but for us humans, it is far more convenient to use domain names and hostnames instead of memorizing long strings of numbers.",
       f"نظام {T('DNS', 'Domain Name System — نظام أسماء النطاقات')} هو بروتوكول شبكة نستخدمه للبحث عن عناوين IP لأسماء الأجهزة والمواقع. أجهزة الكمبيوتر بتتعامل مع عناوين IP، لكن بالنسبة لينا كبشر، الأسهل بكتير نستخدم أسماء النطاقات بدلاً من حفظ أرقام طويلة ومعقدة.") +
    bl("If you want, you could visit networklessons.com by going directly to its IP address (for example, 95.85.36.216), but typing in the domain name networklessons.com is much easier and more intuitive.",
       "لو تحب، تقدر تزور موقع networklessons.com بكتابة عنوان الـ IP المباشر بتاعه (مثلاً 95.85.36.216)، لكن كتابة اسم الموقع networklessons.com أسهل بكتير وبديهية أكتر لأي مستخدم.") +
    bl("DNS is distributed and hierarchical. There are thousands of DNS servers worldwide, but none of them has a complete database containing all hostnames and IP addresses in the world. A DNS server might have information for certain domains, but it queries other DNS servers when it does not know the answer.",
       "نظام DNS نظام موزّع وهرمي (Distributed & Hierarchical). في آلاف السيرفرات حول العالم، لكن مفيش سيرفر واحد عنده قاعدة بيانات كاملة لكل الأسماء والـ IPs اللي في كوكب الأرض. سيرفر الـ DNS ممكن يكون عنده معلومات نطاقات معينة، وبيسأل سيرفرات تانية لما يجيله استفسار عن نطاق مش عنده.")
) + extra(
    "Think of DNS as the 'Contacts App' on your smartphone. You don't memorize the 11-digit phone numbers of all your friends; you simply click on 'Ahmed' or 'Sarah', and your phone automatically dials the underlying number. DNS does the exact same thing for the entire Internet: it maps friendly names to numeric IP addresses.",
    "تخيل الـ DNS زي تطبيق 'جهات الاتصال' (Contacts) في موبايلك. أنت مش حافظ أرقام تليفونات صحابك المكونة من 11 رقم؛ أنت بتضغط على اسم 'أحمد' أو 'سارة'، والموبايل هو اللي بيتصل بالرقم الفعلي. الـ DNS بيعمل نفس الوظيفة دي بالظبط لكل أجهزة الإنترنت: بيربط الأسماء السهلة بعناوين IP الرقمية."
)

# Section: DNS Hierarchy
sec_hierarchy = h2("hierarchy", "The DNS Hierarchy", "الهيكل الهرمي لنظام DNS") + src(
    bl("DNS is organized into an inverted tree structure, starting at the root and branching downward into Top-Level Domains, Second-Level Domains, and Subdomains:",
       "شجرة الـ DNS بتترتب بشكل هرمي مقلوب، بتبدأ من الجذر (Root) في القمة وتتفرع للأسفل:") +
    diagram(
        '<div style="font-family:var(--font-body);display:flex;flex-direction:column;align-items:center;gap:16px;">'
        '<div style="padding:10px 24px;border:2px solid var(--accent);background:var(--panel2);border-radius:8px;font-weight:bold;text-align:center;">'
        '. (Root Level — 13 Logical Root Server Clusters: a.root-servers.net to m.root-servers.net)</div>'
        '<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">'
        '<div style="padding:8px 16px;border:1px solid var(--text);background:var(--panel);border-radius:6px;font-weight:600;">.com (gTLD)</div>'
        '<div style="padding:8px 16px;border:1px solid var(--text);background:var(--panel);border-radius:6px;font-weight:600;">.net (gTLD)</div>'
        '<div style="padding:8px 16px;border:1px solid var(--text);background:var(--panel);border-radius:6px;font-weight:600;">.org (gTLD)</div>'
        '<div style="padding:8px 16px;border:1px solid var(--text);background:var(--panel);border-radius:6px;font-weight:600;">.edu (gTLD)</div>'
        '<div style="padding:8px 16px;border:1px solid var(--accent2);background:var(--panel);border-radius:6px;font-weight:600;">.eg / .uk (ccTLD)</div>'
        '</div>'
        '<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">'
        '<div style="padding:8px 16px;border:1px dashed var(--line);background:var(--panel2);border-radius:6px;">networklessons.com</div>'
        '<div style="padding:8px 16px;border:1px dashed var(--line);background:var(--panel2);border-radius:6px;">cisco.com</div>'
        '<div style="padding:8px 16px;border:1px dashed var(--line);background:var(--panel2);border-radius:6px;">google.com</div>'
        '</div>'
        '<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">'
        '<div style="padding:6px 14px;border:1px solid var(--good);border-radius:6px;font-family:monospace;">vps.networklessons.com</div>'
        '<div style="padding:6px 14px;border:1px solid var(--good);border-radius:6px;font-family:monospace;">tools.cisco.com</div>'
        '</div>'
        '</div>',
        "The Inverted Tree Structure of DNS Hierarchy", "الهيكل الهرمي المقلوب لنظام أسماء النطاقات"
    ) +
    img("images/lesson09/img_1.jpg", "DNS Hierarchy Inverted Tree Structure",
        "The Hierarchical Inverted Tree of DNS (Root, TLDs, Domains, Hostnames)", "الهيكل الهرمي المقلوب لنظام أسماء النطاقات (الجذر، النطاقات العليا، النطاقات الفرعية)",
        "DNS Hierarchy Diagram") +
    img("images/web/dns_domain_names.svg", "Global Domain Name System Tree Structure Vector",
        "Global DNS Domain Name Space and Tree Organization (RFC 1034)", "المخطط الشجري القياسي لمساحة أسماء نطاقات الإنترنت العالمية (RFC 1034)",
        "DNS Domain Namespace Vector") +
    bl("<b>1. Root Name Servers:</b> At the very top are 13 logical root server authorities (named from a.root-servers.net to m.root-servers.net). These contain pointer information for all Top-Level Domain (TLD) extensions.",
       "<b>1. سيرفرات الجذر (Root Name Servers):</b> في قمة الهرم يوجد 13 عنوان منطقي لسيرفرات الجذر (من a.root-servers.net إلى m.root-servers.net). دي بتعرف أماكن السيرفرات المسؤولة عن كل امتدادات النطاقات العليا.") +
    bl("<b>2. Top-Level Domains (TLDs):</b> Divided into generic TLDs (gTLD) like .com, .org, .net, .biz, .edu, and country-code TLDs (ccTLD) like .eg (Egypt), .uk (United Kingdom), .de (Germany), and .ca (Canada).",
       "<b>2. نطاقات المستوى الأعلى (TLD):</b> بتنقسم لنطاقات عامة (gTLD) زي .com و .org و .net، ونطاقات دولية جغرافية (ccTLD) زي .eg (مصر)، .uk (بريطانيا)، و .de (ألمانيا).") +
    bl("<b>3. Second-Level Domains:</b> This is where organization domain names live, such as networklessons, cisco, or google, under a specific TLD.",
       "<b>3. نطاقات المستوى الثاني (Second-Level Domains):</b> هنا بيعيش اسم الشركة أو المؤسسة اللي بيتم حجزها وتسجيلها، زي networklessons أو cisco تحت نطاق .com.") +
    bl("<b>4. Subdomains and Hostnames:</b> Further down the tree, you find specific machines or services. For example, <code>vps.networklessons.com</code> is the hostname of the VPS running the site, and <code>tools.cisco.com</code> is a subdomain for Cisco tools.",
       "<b>4. النطاقات الفرعية وأسماء الأجهزة (Subdomains & Hostnames):</b> أعمق في الشجرة بنلاقي أجهزة أو خدمات معينة. مثلاً <code>vps.networklessons.com</code> هو اسم خادم الـ VPS، و <code>tools.cisco.com</code> نطاق فرعي لأدوات سيسكو.")
) + extra(
    "Common Cisco Exam / Interview Fact: People often say 'there are only 13 DNS root servers in the world.' In reality, there are 13 logical IP addresses managed by 12 distinct organizations (ICANN, NASA, Verisign, etc.), but each address is backed by hundreds of physical Anycast servers worldwide! Today there are over 1,500+ physical root server instances globally for maximum resilience and redundancy.",
    "معلومة امتحانات ومقابلات سيسكو الشهيرة: كتير بيقولوا 'في 13 سيرفر جذر بس في العالم كله'. الحقيقة إنهم 13 عنوان IP منطقي بتديرهم 12 مؤسسة دولية (زي ICANN و NASA و Verisign)، لكن كل عنوان وراه مئات السيرفرات الفيزيائية الموزعة حول العالم بتقنية Anycast! حالياً في أكتر من 1,500 سيرفر فيزيائي شغالين في نفس اللحظة عشان يضمنوا إن خدمة الإنترنت ما تقعش أبداً."
)

# Section: FQDN & Root Dot
sec_fqdn = h2("fqdn", "FQDN & The Trailing Root Dot", "الاسم المؤهل الكامل FQDN ونقطة الجذر") + src(
    bl("Between each DNS label in a name we use a period character (.). Officially, a complete domain name must also end with a trailing dot representing the root, although web browsers hide it automatically for convenience.",
       "بين كل مقطع والتاني في اسم النطاق بنستخدم علامة النقطة (.). ورسمياً وفقاً لمعايير الإنترنت، الاسم الكامل لازم ينتهي بنقطة في آخره بتمثل الجذر (Root)، مع إن متصفحات الويب بتخفيها تلقائياً لتسهيل الاستخدام.") +
    bl("Take a close look at these two examples:<br><code>vps.networklessons.com.</code> (with trailing dot)<br><code>vps.networklessons.com</code> (without trailing dot)",
       "دقق في المثالين دول:<br><code>vps.networklessons.com.</code> (بنقطة في النهاية)<br><code>vps.networklessons.com</code> (بدون نقطة)") +
    bl("Writing down a hostname with its complete domain structure all the way back to the root is called an <b>FQDN (Fully Qualified Domain Name)</b>.",
       f"كتابة اسم الجهاز مع تسلسل نطاقاته بالكامل وصولاً للجذر يُسمى {T('FQDN', 'Fully Qualified Domain Name — اسم النطاق المؤهل بالكامل')}.") +
    '<div class="table-wrap"><table><tr><th>' + bi("Component", "المكوّن") + '</th><th>' + bi("Example Label", "المثال") + '</th><th>' + bi("Role in DNS", "الدور في شجرة DNS") + '</th></tr>' +
    '<tr><td class="mono-cell">.</td><td class="mono-cell">. (trailing)</td><td>' + bi("Root of the entire DNS hierarchy", "جذر شجرة الـ DNS بالكامل") + '</td></tr>' +
    '<tr><td class="mono-cell">com</td><td class="mono-cell">.com</td><td>' + bi("Top-Level Domain (TLD)", "نطاق المستوى الأعلى") + '</td></tr>' +
    '<tr><td class="mono-cell">networklessons</td><td class="mono-cell">networklessons</td><td>' + bi("Second-Level Domain registered to owner", "نطاق المستوى الثاني المسجل للمالك") + '</td></tr>' +
    '<tr><td class="mono-cell">vps</td><td class="mono-cell">vps</td><td>' + bi("Specific hostname / server within that domain", "اسم الجهاز أو السيرفر المحدد داخل النطاق") + '</td></tr>' +
    '</table></div>'
) + extra(
    "In BIND DNS zone configuration files and Cisco domain setups, forgetting the trailing dot (.) on a domain name is a classic engineer error! If you write 'mail.example.com' without the trailing dot inside a zone record, the server will append the origin domain again, creating 'mail.example.com.example.com.' Always remember the trailing dot in raw DNS configurations.",
    "في إعدادات ملفات مناطق الـ DNS (Zone Files) وإعدادات سيسكو، نسيان النقطة الأخيرة (.) خطأ شائع جداً بيقع فيه المهندسون! لو كتبت 'mail.example.com' من غير نقطة في آخرها داخل إعدادات الـ Zone، السيرفر تلقائياً هيضيف اسم الدومين مرة تانية وتبقى 'mail.example.com.example.com.' افتكر دايماً إن النقطة الأخيرة هي اللي بتوقف التكرار وبتعلن الوصول للجذر."
)

# Section: How Resolution Works
sec_resolution = h2("resolution", "How DNS Resolution Works", "كيف تعمل عملية استعلام وترجمة DNS؟") + src(
    bl("When a client needs to communicate with a hostname, it goes through a resolution process. First, let's examine what a client has configured on Windows using <code>ipconfig /all</code>:",
       "لما جهاز يحتاج يكلم موقع أو جهاز باسمه، بيمر بعملية ترجمة (Resolution). الأول، خلينا نشوف إعدادات الجهاز على ويندوز بأمر <code>ipconfig /all</code>:") +
    cli("C:\\Users\\Vmware> <b>ipconfig /all | more</b>\n\nWindows IP Configuration\n   Host Name . . . . . . . . . . . . : vmware\n   DNS Suffix Search List. . . . . . : networklessons.local\n   IPv4 Address. . . . . . . . . . . : 10.56.100.1\n   Subnet Mask . . . . . . . . . . . : 255.255.255.0\n   Default Gateway . . . . . . . . . : 10.56.100.254\n   <b>DNS Servers . . . . . . . . . . . : 10.56.100.253</b>") +
    bl("The host is configured to use <b>10.56.100.253</b> as its local DNS server. When the user opens a browser to visit <code>networklessons.com</code>, the host sends a DNS query to this server.",
       "الجهاز مضبوط إنه يستخدم <b>10.56.100.253</b> كسيرفر DNS محلي. لما المستخدم يفتح المتصفح ويدخل <code>networklessons.com</code>، الجهاز بيبعت طلب استعلام (DNS Query) للسيرفر ده.") +
    img("images/lesson09/img_2.jpg", "DNS Request and Reply Process",
        "Host Sending DNS Request and Receiving Resolved Reply from Local Server", "إرسال طلب استعلام DNS من الجهاز واستلام الرد بالعنوان من السيرفر المحلي",
        "DNS Resolution Flow") +
    diagram(
        '<div style="font-family:monospace;display:flex;flex-direction:column;gap:12px;">'
        '<div style="display:flex;justify-content:space-between;align-items:center;background:var(--panel2);padding:12px;border:1px solid var(--line);border-radius:6px;">'
        '<span>1. PC (10.56.100.1)</span><span style="color:var(--accent);font-weight:bold;">Query: "Where is networklessons.com?" &rarr;</span><span>Local DNS (10.56.100.253)</span></div>'
        '<div style="display:flex;justify-content:space-between;align-items:center;background:var(--panel);padding:12px;border:1px dashed var(--line);border-radius:6px;">'
        '<span>Local DNS Resolver</span><span style="color:var(--warn);font-weight:bold;">&rarr; Queries Root Servers (.) &rarr; TLD Servers (.com) &rarr; Authoritative NS</span></div>'
        '<div style="display:flex;justify-content:space-between;align-items:center;background:var(--panel2);padding:12px;border:1px solid var(--good);border-radius:6px;">'
        '<span>Local DNS (10.56.100.253)</span><span style="color:var(--good);font-weight:bold;">&larr; Reply: "networklessons.com is at 95.85.36.216"</span><span>PC (10.56.100.1)</span></div>'
        '</div>',
        "Step-by-Step DNS Resolution Flow", "مخطط خطوات استعلام وترجمة اسم النطاق"
    ) +
    bl("A local DNS server typically only has authority over local network hostnames. When it needs to resolve an Internet address, it performs a lookup using the Internet root servers, TLD servers, or forwards the query to the ISP's recursive DNS server.",
       "سيرفر الـ DNS المحلي عادةً بيكون مسؤول عن أسماء أجهزة الشبكة الداخلية بس. ولما يحتاج يترجم عنوان على الإنترنت، بيستعلم من سيرفرات الجذر و TLD أو يوجّه الطلب لسيرفر الـ DNS الخاص بشركة الإنترنت (ISP).")
) + extra(
    "Crucial Interview Concept: Recursive vs Iterative Queries.<br>• <b>Recursive Query:</b> The client tells the local DNS server: 'Find me the IP address, and don't come back until you have the final answer.' The server does all the legwork on the client's behalf.<br>• <b>Iterative Query:</b> The DNS server queries upstream servers (Root, TLD, Authoritative). Each upstream server says: 'I don't have the final IP, but here is the referral to the next server down the chain who might know.'",
    "سؤال مقابلات شركات الاتصالات الشهير: الفرق بين الاستعلام التكراري والاستعلام المتكرر (Recursive vs Iterative):<br>• <b>الاستعلام التكراري (Recursive):</b> العميل (الـ PC) بيقول للـ DNS المحلي: 'هاتلي الـ IP النهائي، ومتترجعليش إلا بالحل الكامل.' السيرفر بيتولى كل خطوات البحث نيابة عن الجهاز.<br>• <b>الاستعلام التتابعي (Iterative):</b> سيرفر الـ DNS بيكلم سيرفرات الإنترنت؛ كل سيرفر يقوله: 'أنا معنديش الـ IP النهائي، بس اتفضل عنوان السيرفر اللي بعدي في الشجرة هو اللي هيفيدك'."
)

# Section: UDP vs TCP Port 53
sec_transport = h2("transport", "Transport Layer: UDP vs TCP Port 53", "بروتوكول النقل: UDP أم TCP على المنفذ 53؟") + src(
    bl("DNS operates using port number 53, but an important question is: does DNS use TCP or UDP? The answer is that DNS uses <b>both</b>, depending on the scenario:",
       "نظام DNS بيشتغل على البورت رقم 53، لكن السؤال الأهم: هل بيستخدم TCP ولا UDP؟ الإجابة إنه بيستخدم <b>الاثنين</b>، حسب طبيعة العملية:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Protocol", "البروتوكول") + '</th><th>' + bi("Port", "المنفذ") + '</th><th>' + bi("When is it Used?", "متى يُستخدم؟") + '</th><th>' + bi("Reason", "السبب") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>UDP</b></td><td class="mono-cell">53</td><td>' + bi("Standard client queries & lookup requests", "استعلامات الأجهزة العادية والتصفح اليومي") + '</td><td>' + bi("Fast, lightweight, minimal overhead (no 3-way handshake needed for quick requests)", "سريع وخفيف جداً، مفيش استهلاك للشبكة بمصافحة ثلاثية لسؤال وإجابة سريعة") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>TCP</b></td><td class="mono-cell">53</td><td>' + bi("Zone Transfers (AXFR/IXFR), responses > 512 bytes, DNSSEC", "نقل المناطق بين السيرفرات، والردود الأكبر من 512 بايت، وتأمين DNSSEC") + '</td><td>' + bi("Reliability is mandatory to avoid database corruption; packet size exceeds standard UDP payload", "الموثوقية ضرورية لمنع تلف قاعدة البيانات، وحجم البيانات كبير ميستحملش فقدان حزم") + '</td></tr>' +
    '</table></div>' +
    bl("For regular web browsing, almost 100% of DNS traffic between endpoints and resolvers is UDP port 53. If a UDP reply is too large (traditionally over 512 bytes), the DNS server sets the <b>Truncation bit (TC)</b> in the header, signalling the client to retry using TCP port 53.",
       "في التصفح العادي، تقريباً 100% من ترافيك الـ DNS بين جهازك والسيرفر بيكون UDP بورت 53. لكن لو حجم الرد كبير زيادة عن 512 بايت، السيرفر بيفعّل بت الاقتطاع (TC Bit) عشان يقول للجهاز: البيانات أكبر من الـ UDP، أعد الطلب باستخدام TCP بورت 53.")
) + extra(
    "Top Exam & Interview Trap Question: 'Does DNS use UDP or TCP?' — Never just say 'UDP'! The correct, professional answer that impresses interviewers is: 'DNS uses UDP port 53 for standard host queries because of speed and low overhead, but uses TCP port 53 for Zone Transfers between primary and secondary servers, or when DNS responses exceed 512 bytes or utilize DNSSEC.'",
    "أشهر فخ في امتحانات ومقابلات سيسكو: 'الـ DNS بيستخدم UDP ولا TCP؟' — إياك تجاوب بكلمة واحدة زي 'UDP بس'! الإجابة الهندسية الاحترافية هي: 'الـ DNS بيستخدم UDP بورت 53 لطلبات الاستعلام السريعة لتقليل الحمل، وبيستخدم TCP بورت 53 في نقل المناطق (Zone Transfers) بين السيرفرات وللبيانات اللي حجمها بيتعدى 512 بايت أو عند تفعيل DNSSEC.'")

# Section: Wireshark Analysis
sec_wireshark = h2("wireshark", "Wireshark Packet Analysis", "تحليل حزم DNS في برنامج Wireshark") + src(
    bl("Let's look at the actual packet capture when the host opens a web browser to visit <code>networklessons.com</code>:",
       "تعالوا نشوف حزم البيانات الحقيقية من برنامج Wireshark لما الجهاز بيفتح المتصفح ويزور <code>networklessons.com</code>:") +
    img("images/lesson09/img_3.jpg", "Wireshark DNS Query capture on UDP port 53",
        "Wireshark Capture: Standard DNS Query for networklessons.com over UDP Port 53", "التقاط حزمة استعلام DNS في برنامج Wireshark عبر منفذ UDP 53",
        "Wireshark DNS Query Capture") +
    diagram(
        '<div style="font-family:monospace;background:var(--panel2);border:1px solid var(--line);padding:16px;border-radius:6px;font-size:0.85rem;line-height:1.6;">'
        '<span style="color:var(--muted)">Frame 1: 76 bytes on wire</span><br>'
        'Ethernet II, Src: Intel_7d:22:8c, Dst: Router_10:00:fe<br>'
        'Internet Protocol Version 4, Src: <b>10.56.100.1</b>, Dst: <b>10.56.100.253</b><br>'
        'User Datagram Protocol, Src Port: 54821, <b>Dst Port: 53 (DNS)</b><br>'
        'Domain Name System (query)<br>'
        '&nbsp;&nbsp;Transaction ID: 0x2b4c<br>'
        '&nbsp;&nbsp;Flags: 0x0100 Standard query<br>'
        '&nbsp;&nbsp;<b>Queries: networklessons.com: type A, class IN</b>'
        '</div>',
        "Wireshark Capture Details: DNS Query", "تفاصيل التقاط Wireshark: حزمة استعلام DNS"
    ) +
    bl("The host sends a UDP packet to destination port 53 on the DNS server (10.56.100.253). The query specifically asks for an <b>A record</b> (IPv4 address) for <code>networklessons.com</code>.",
       "الجهاز بيبعت حزمة UDP للبورت 53 على سيرفر الـ DNS (10.56.100.253). الطلب بيسأل تحديداً عن سجل من النوع <b>A record</b> (عنوان IPv4) لموقع <code>networklessons.com</code>.") +
    img("images/lesson09/img_4.jpg", "Wireshark DNS Answer packet with resolved IP",
        "Wireshark Capture: DNS Response with Resolved IP Address 95.85.36.216", "التقاط حزمة رد DNS في Wireshark متضمنة عنوان IP المحلول",
        "Wireshark DNS Answer Capture") +
    diagram(
        '<div style="font-family:monospace;background:var(--panel2);border:1px solid var(--good);padding:16px;border-radius:6px;font-size:0.85rem;line-height:1.6;">'
        '<span style="color:var(--muted)">Frame 2: 92 bytes on wire</span><br>'
        'Internet Protocol Version 4, Src: <b>10.56.100.253</b>, Dst: <b>10.56.100.1</b><br>'
        'User Datagram Protocol, Src Port: 53, Dst Port: 54821<br>'
        'Domain Name System (response)<br>'
        '&nbsp;&nbsp;Transaction ID: 0x2b4c<br>'
        '&nbsp;&nbsp;Flags: 0x8180 Standard query response, No error<br>'
        '&nbsp;&nbsp;Queries: networklessons.com: type A, class IN<br>'
        '&nbsp;&nbsp;<b>Answers:</b><br>'
        '&nbsp;&nbsp;&nbsp;&nbsp;<b>networklessons.com: type A, class IN, addr 95.85.36.216</b>'
        '</div>',
        "Wireshark Capture Details: DNS Response", "تفاصيل التقاط Wireshark: حزمة رد DNS"
    ) +
    bl("The DNS server responds with IP address <b>95.85.36.216</b>. Once the client receives this response, it can immediately begin the TCP 3-way handshake to establish a web session on port 80/443.",
       "سيرفر الـ DNS بيرد بعنوان الـ IP وهو <b>95.85.36.216</b>. بمجرد ما الجهاز يستلم الرد، يقدر فوراً يبدأ مصافحة TCP الثلاثية (3-way handshake) لفتح جلسة الويب على بورت 80 أو 443.")
) + extra(
    "Notice the Transaction ID (0x2b4c in the capture). Because UDP is connectionless and stateless, DNS uses this 16-bit Transaction ID to match the incoming response with the exact query that was sent. If the transaction ID in the reply doesn't match the query, the client discards it.",
    "لاحظ وجود معرّف المعاملة (Transaction ID بقيمة 0x2b4c في الصورة). بما إن UDP بروتوكول بدون اتصال وبدون حالات (Stateless)، الـ DNS بيستخدم رقم المعاملة ده المكون من 16 بت عشان يطابق الرد اللي راجع مع نفس السؤال اللي اتبعت بالضبط. لو الرقمين مش متطابقين، الجهاز بيرمي الحزمة فوراً لحماية نفسه من الهجمات."
)

# Section: Common DNS Records
sec_records = h2("records", "Common DNS Record Types", "أهم أنواع سجلات DNS التي يحتاجها مهندس الشبكات") + src(
    bl("DNS servers store various types of Resource Records (RR). For the CCNA exam and real enterprise networking, you must recognize these core records:",
       "سيرفرات الـ DNS بتخزن سجلات الموارد (Resource Records). لامتحان CCNA وبيئة العمل الواقعية، لازم تكون عارف السجلات الأساسية دي:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Record Type", "نوع السجل") + '</th><th>' + bi("Full Name", "الاسم الكامل") + '</th><th>' + bi("Purpose & Description", "الوظيفة والاستخدام") + '</th></tr>' +
    '<tr><td class="mono-cell"><b>A</b></td><td>Address Record</td><td>' + bi("Maps a hostname to an <b>IPv4 address</b> (e.g. example.com &rarr; 192.0.2.1)", "يربط اسم النطاق بعنوان <b>IPv4</b>") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>AAAA</b></td><td>IPv6 Address (Quad-A)</td><td>' + bi("Maps a hostname to a 128-bit <b>IPv6 address</b> (e.g. example.com &rarr; 2001:db8::1)", "يربط اسم النطاق بعنوان <b>IPv6</b> مكون من 128 بت") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>CNAME</b></td><td>Canonical Name</td><td>' + bi("An alias for another domain name (e.g. www.example.com points to example.com)", "اسم مستعار يشير إلى اسم نطاق رئيسي آخر") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>MX</b></td><td>Mail Exchanger</td><td>' + bi("Specifies mail servers responsible for receiving emails for the domain with a priority score", "يحدد خوادم البريد الإلكتروني المسؤولة عن استقبال الإيميلات مع رقم أولوية") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>PTR</b></td><td>Pointer Record</td><td>' + bi("Used in <b>Reverse DNS (rDNS)</b>: maps an IP address back to its hostname", "يُستخدم في البحث العكسي: تحويل عنوان IP إلى اسم النطاق المقابل له") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>NS</b></td><td>Name Server</td><td>' + bi("Identifies the authoritative nameservers for a given DNS zone", "يحدد أسماء السيرفرات الرسمية المعتمدة للمنطقة") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>SOA</b></td><td>Start of Authority</td><td>' + bi("Contains administrative info about the zone: primary master server, admin email, serial number, refresh timers", "يحتوي على البيانات الإدارية الأساسية للمنطقة ورقم الإصدار ومؤقتات التحديث") + '</td></tr>' +
    '<tr><td class="mono-cell"><b>TXT</b></td><td>Text Record</td><td>' + bi("Holds human/machine-readable text; commonly used for email security (SPF, DKIM, DMARC)", "يخزن نصوص متنوعة؛ يُستخدم حالياً بكثرة في تأمين البريد وحمايته من التزوير") + '</td></tr>' +
    '</table></div>'
) + extra(
    "Why is IPv6 record called 'AAAA'? Because IPv4 addresses are 32 bits (1 A), while IPv6 addresses are 128 bits — exactly 4 times longer than IPv4! Hence, four A's: 'Quad-A'.",
    "ليه سجل الـ IPv6 اتسمى 'AAAA'؟ لأن عنوان الـ IPv4 حجمه 32 بت (ويرمز له بحرف A واحد)، بينما الـ IPv6 حجمه 128 بت — يعني 4 أضعاف حجم IPv4 بالضبط! عشان كده اتسمى 'Quad-A' بأربعة حروف A."
)

# Section: Cisco IOS & Troubleshooting
sec_cisco = h2("cisco", "DNS on Cisco IOS & Diagnostic Tools", "إعدادات DNS على أجهزة سيسكو وأدوات التشخيص") + src(
    bl("On Cisco IOS routers and switches, DNS is enabled by default. However, there is one command every Cisco engineer learns immediately:",
       "على روترات وسويتشات سيسكو (Cisco IOS)، خدمة DNS مفعلة افتراضياً. ولكن في أمر مشهور جداً كل مهندس سيسكو لازم يعرفه:") +
    cli("Router(config)# <b>no ip domain-lookup</b>\n\n! Disables DNS translation for mistyped commands.\n! Prevents the router from freezing and broadcasting 'Translating ... domain server (255.255.255.255)'") +
    bl("If you make a typo on a router prompt without this command (for example typing <code>shwo</code> instead of <code>show</code>), the router assumes you want to Telnet to a host named 'shwo' and tries to resolve it via DNS broadcast, freezing your console for up to 30 seconds!",
       "لو غلطت في كتابة أمر في سيسكو (مثلاً كتبت <code>shwo</code> بدل <code>show</code>)، الراوتر بيفترض إنك عايز تعمل اتصال Telnet بجهاز اسمه 'shwo' وبيحاول يترجمه عبر DNS، وده بيجمد الشاشة لمدة نص دقيقة مزعجة جداً!") +
    bl("To configure a Cisco router to use real DNS servers for lookups, use these commands:",
       "عشان تضبط راوتر سيسكو إنه يستخدم سيرفرات DNS حقيقية لترجمة العناوين، بتستخدم الأوامر دي:") +
    cli("Router(config)# <b>ip domain-lookup</b>\nRouter(config)# <b>ip name-server 8.8.8.8 1.1.1.1</b>\nRouter(config)# <b>ip domain-name mycompany.local</b>") +
    bl("Essential PC Troubleshooting Commands:",
       "أهم أوامر التشخيص على أجهزة الكمبيوتر:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Command", "الأمر") + '</th><th>' + bi("Operating System", "نظام التشغيل") + '</th><th>' + bi("What it Does", "ما يفعله الأمر") + '</th></tr>' +
    '<tr><td class="mono-cell"><code>nslookup domain.com</code></td><td>Windows / Linux</td><td>' + bi("Queries DNS server directly to test resolution", "يرسل استعلاماً مباشراً لسيرفر DNS لاختبار الترجمة") + '</td></tr>' +
    '<tr><td class="mono-cell"><code>ipconfig /displaydns</code></td><td>Windows</td><td>' + bi("Shows local DNS cache stored on the PC", "يعرض الذاكرة المؤقتة (Cache) للـ DNS على الجهاز") + '</td></tr>' +
    '<tr><td class="mono-cell"><code>ipconfig /flushdns</code></td><td>Windows</td><td>' + bi("Clears local DNS resolver cache to fix stale records", "يمسح الذاكرة المؤقتة للـ DNS لحل مشاكل السجلات القديمة") + '</td></tr>' +
    '<tr><td class="mono-cell"><code>dig domain.com</code></td><td>Linux / macOS</td><td>' + bi("Detailed, powerful DNS diagnostic tool", "أداة تشخيص متقدمة وتفصيلية لنظام DNS") + '</td></tr>' +
    '</table></div>'
) + extra(
    "Classic NOC / Telecom Egypt Interview Scenario: A customer says 'My internet is down! I cannot open google.com or any website.' What are your systematic diagnostic steps?<br>1. Ask the customer to ping 8.8.8.8. If the ping succeeds, IP routing and physical connectivity are 100% fine!<br>2. Now ask them to ping google.com. If it fails with 'Ping request could not find host', the issue is strictly DNS.<br>3. Check DNS settings: run <code>ipconfig /all</code>, check DNS IP, try <code>ipconfig /flushdns</code> or assign public DNS (8.8.8.8 or 1.1.1.1).",
    "سيناريو مقابلات الدعم الفني وشركات الاتصالات (NOC / Tech Support) الشهير: عميل بيتصل يقولك 'النت قاطع ومفيش أي موقع بيفتح.' إزاي تشخص المشكلة بخطوات هندسية مرتبة؟<br>1. اطلب منه يعمل <code>ping 8.8.8.8</code>. لو الـ ping رد بنجاح، يبقى كابل النت والراوتر والتوجيه (IP Routing) شغالين 100% سليم!<br>2. اطلب منه يعمل <code>ping google.com</code>. لو ظهرله 'could not find host'، يبقى المشكلة بنسبة 100% هي DNS بحتة!<br>3. ابدأ في حل مشكلة الـ DNS: افحص سيرفرات الـ DNS في <code>ipconfig /all</code>، جرب مسح الكاش بـ <code>ipconfig /flushdns</code> أو غيّر الـ DNS لـ 8.8.8.8 أو 1.1.1.1."
)

# Section: Conclusion
sec_conclusion = h2("conclusion", "Conclusion", "خلاصة الدرس") + src(
    bl("DNS is the unsung hero of the Internet, quietly mapping human-friendly names to machine-readable IP addresses in milliseconds.",
       "نظام DNS هو الجندي المجهول في الإنترنت، بيحول الأسماء السهلة لعناوين IP رقمية في أجزاء من الثانية دون أن نشعر.") +
    bl("Key Takeaways for CCNA:<br>• DNS operates on <b>Port 53</b> (UDP for client queries, TCP for zone transfers and packets > 512 bytes).<br>• The DNS hierarchy is an inverted tree starting at the <b>Root (.)</b>, branching into <b>TLDs (.com, .eg)</b>, <b>Second-Level Domains</b>, and <b>Hostnames</b>.<br>• <b>A record</b> = IPv4, <b>AAAA record</b> = IPv6, <b>CNAME</b> = alias, <b>MX</b> = mail, <b>PTR</b> = reverse lookup.<br>• On Cisco routers, configure <code>no ip domain-lookup</code> to stop mistyped commands from freezing your CLI terminal.",
       "أهم نقاط امتحان سيسكو CCNA:<br>• الـ DNS بيشتغل على <b>البورت 53</b> (UDP لطلبات الأجهزة، و TCP لنقل المناطق والبيانات الأكبر من 512 بايت).<br>• هيكل الـ DNS شجرة مقلوبة بتبدأ من <b>الجذر (.)</b> ثم <b>النطاقات العليا TLD (.com, .eg)</b> ثم <b>نطاقات المستوى الثاني</b> ثم <b>أسماء الأجهزة</b>.<br>• <b>سجل A</b> = لـ IPv4، <b>سجل AAAA</b> = لـ IPv6، <b>سجل CNAME</b> = اسم مستعار، <b>سجل MX</b> = للبريد، <b>سجل PTR</b> = للبحث العكسي.<br>• على روترات سيسكو، اكتب أمر <code>no ip domain-lookup</code> لمنع تهنيج الشاشة عند كتابة أمر غلط.")
) + extra(
    "DNS Security Note: Standard DNS traffic is sent in cleartext, meaning anyone on your local network or ISP can see what domains you are visiting. Modern protocols like DoH (DNS over HTTPS) and DoT (DNS over TLS) encrypt DNS queries over TCP port 443 or 853 to ensure privacy and security.",
    "ملاحظة أمنية متقدمة: طلبات الـ DNS العادية بتتبعت كنص واضح غير مشفر (Cleartext)، يعني أي حد على شبكتك أو مزود الخدمة يقدر يعرف أسماء المواقع اللي بتزورها. التقنيات الحديثة زي DoH (DNS over HTTPS) و DoT (DNS over TLS) بتشفر الاستعلامات دي عبر بورت 443 أو 853 لضمان الخصوصية التامة."
)

# Recap Quiz (Testing Lesson 8: ICMP)
recap = [
    Q("In the previous lesson on ICMP, what does an ICMP Type 3, Code 13 message indicate?",
      "في الدرس السابق الخاص بـ ICMP، رسالة ICMP النوع 3، الكود 13 بتدل على إيه؟",
      [("Host is offline due to ARP failure", "الجهاز مطفأ بسبب فشل ARP"),
       ("Communication is Administratively Prohibited (e.g., blocked by an ACL)", "الاتصال ممنوع إدارياً (محظور بواسطة Access Control List)"),
       ("Echo Reply was received successfully", "تم استلام رد الـ Echo بنجاح"),
       ("The packet TTL expired in transit", "انتهت صلاحية الـ TTL للحزمة أثناء النقل")],
      1,
      "ICMP Type 3 is Destination Unreachable. Code 13 specifically means 'Communication Administratively Prohibited', which occurs when a router's ACL filters or blocks the packet.",
      "النوع 3 في ICMP هو الوجهة غير قابلة للوصول. الكود 13 تحديداً معناه ممنوع إدارياً، وده بيحصل لما ACL على الراوتر يحظر مرور الحزمة."),

    Q("How does the traceroute tool discover intermediate routers along a network path?",
      "إزاي أداة traceroute بتكتشف الراوترات الوسيطة على طول مسار الشبكة؟",
      [("By sending packets with an increasing TTL, causing each router to return ICMP Type 11 (Time Exceeded)", "بإرسال حزم بقيمة TTL متزايدة، مما يجعل كل راوتر يرجع رسالة ICMP النوع 11 (Time Exceeded)"),
       ("By sending TCP SYN packets to port 80 of every router", "بإرسال حزم TCP SYN للمنفذ 80 في كل راوتر"),
       ("By using ICMP Redirect (Type 5) messages", "باستخدام رسائل إعادة التوجيه ICMP Redirect (النوع 5)"),
       ("By examining the router's ARP table directly", "بفحص جدول ARP الخاص بالراوتر مباشرة")],
      0,
      "Traceroute starts with TTL=1. The first router decrements TTL to 0, drops the packet, and returns an ICMP Type 11 (Time Exceeded) message revealing its IP address. It repeats this with TTL=2, 3, etc.",
      "أداة traceroute بتبدأ بحزمة TTL=1. أول راوتر بينقص الـ TTL لـ 0، ويرمي الحزمة، ويرجع رسالة ICMP النوع 11 (انتهاء الوقت) كاشفاً عنوان الـ IP بتاعه. وتكرر العملية بـ TTL=2 ثم 3 وهكذا."),

    Q("A network engineer can successfully ping a web server (10.0.0.5), but users cannot open the website hosted on it. Why?",
      "مهندس شبكات عمل ping لسيرفر ويب (10.0.0.5) بنجاح، لكن المستخدمين مش قادرين يفتحوا الموقع عليه. ما السبب؟",
      [("Ping operates at Layer 3 verifying IP reachability, but the web service at Layer 7 / TCP port 80 could still be down", "الـ Ping بيشتغل في الطبقة 3 ويتأكد من اتصال IP فقط، لكن خدمة الويب في الطبقة 7 / منفذ TCP 80 ممكن تكون متوقفة"),
       ("Ping only works if the web server is using UDP", "الـ Ping مش بيشتغل إلا لو سيرفر الويب كان شغال بـ UDP"),
       ("The router has corrupted the MAC address", "الراوتر قام بإتلاف عنوان الـ MAC"),
       ("Successful ping automatically guarantees web server functionality", "نجاح الـ ping بيضمن تلقائياً أن سيرفر الويب شغال")],
      0,
      "Ping verifies Network layer (Layer 3) connectivity using ICMP. A successful ping does NOT guarantee that the transport layer (TCP port 80/443) or the application service itself is running properly.",
      "الـ Ping بيتحقق من اتصال طبقة الشبكة (الطبقة 3) باستخدام ICMP. نجاح الـ ping لا يضمن أبداً أن طبقة النقل (منفذ TCP 80/443) أو خدمة التطبيق نفسه شغالة بشكل صحيح.")
]

# Lesson Quiz (Testing Lesson 9: DNS)
quiz = [
    Q("What transport layer protocol and destination port are used by default for standard client DNS queries?",
      "ما هو بروتوكول طبقة النقل ومنفذ الوجهة المستخدم افتراضياً لاستعلامات DNS العادية من الأجهزة؟",
      [("TCP port 80", "منفذ TCP 80"),
       ("UDP port 53", "منفذ UDP 53"),
       ("TCP port 53", "منفذ TCP 53"),
       ("UDP port 67", "منفذ UDP 67")],
      1,
      "Standard client DNS lookups use UDP port 53 because it is fast, lightweight, and does not require the overhead of a 3-way handshake.",
      "استعلامات DNS العادية للأجهزة بتستخدم UDP منفذ 53 لأنه سريع وخفيف ولا يتطلب استهلاك موارد الشبكة بمصافحة ثلاثية."),

    Q("Under which of the following circumstances does DNS switch to using TCP port 53?",
      "في أي من الحالات التالية يتحول نظام DNS إلى استخدام منفذ TCP 53؟",
      [("When pinging a domain name", "عند عمل ping لاسم نطاق"),
       ("During DNS Zone Transfers (AXFR/IXFR) or when responses exceed 512 bytes", "أثناء نقل المناطق (Zone Transfers) أو عندما يتجاوز حجم الرد 512 بايت"),
       ("Only when IPv6 is disabled", "فقط عند تعطيل IPv6"),
       ("Whenever an Android phone connects to Wi-Fi", "كلما اتصل هاتف أندرويد بالواي فاي")],
      1,
      "DNS uses TCP port 53 when reliability is required, such as Zone Transfers between DNS servers, or when DNS response packets exceed the traditional 512-byte limit.",
      "الـ DNS بيستخدم TCP منفذ 53 لما تكون الموثوقية إجبارية زي نقل المناطق (Zone Transfers) بين السيرفرات، أو لو رد الـ DNS زاد حجمه عن 512 بايت."),

    Q("In the Fully Qualified Domain Name (FQDN) 'server.cisco.com.', what does the trailing period (.) represent?",
      "في اسم النطاق المؤهل بالكامل (FQDN) 'server.cisco.com.'، النقطة الأخيرة (.) تمثل ماذا؟",
      [("A typing error that invalidates the name", "خطأ إملائي يبطل صحة الاسم"),
       ("The root of the DNS namespace hierarchy", "جذر الهيكل الهرمي لنظام أسماء النطاقات (DNS Root)"),
       ("The top-level domain .com", "نطاق المستوى الأعلى .com"),
       ("The host itself", "الجهاز نفسه")],
      1,
      "The trailing dot explicitly represents the DNS root level at the top of the hierarchy. Although browsers hide it, it is officially present in an FQDN.",
      "النقطة الأخيرة في نهاية الاسم بتمثل رسمياً مستوى الجذر (Root) في قمة شجرة الـ DNS. ورغم أن المتصفحات بتخفيها، إلا إنها جزء أساسي من الـ FQDN."),

    Q("Why is the command 'no ip domain-lookup' commonly entered in Cisco IOS configuration?",
      "لماذا يُستخدم الأمر 'no ip domain-lookup' بكثرة في إعدادات روترات وسويتشات سيسكو؟",
      [("To disable internet access entirely", "لتعطيل الوصول للإنترنت بالكامل"),
       ("To stop the CLI from hanging when an unrecognized command is mistyped", "لمنع تجميد شاشة الأوامر عند كتابة أمر خاطئ بشكل غير مقصود"),
       ("To prevent users from opening websites", "لمنع المستخدمين من فتح المواقع"),
       ("To delete the router's IP routing table", "لحذف جدول التوجيه من الراوتر")],
      1,
      "Without 'no ip domain-lookup', any mistyped command is treated by Cisco IOS as a hostname, causing the router to freeze while broadcasting DNS queries to 255.255.255.255.",
      "بدون هذا الأمر، أي كلمة تتكتب غلط في سيسكو بيفترض الراوتر إنها اسم جهاز، ويحاول يترجمها عبر DNS فتهنج الشاشة وتفضل معلقة لمدة تصل إلى 30 ثانية."),

    Q("In an interview, you are asked: A customer can ping 8.8.8.8, but cannot open 'google.com' in any browser. What is the root cause?",
      "في مقابلة عمل سُئلت: عميل يقدر يعمل ping على 8.8.8.8، لكن مش قادر يفتح 'google.com' في المتصفح. ما هو السبب الجذري؟",
      [("The customer's network cable is broken", "كابل شبكة العميل تالف ومفصول"),
       ("DNS resolution failure — the computer cannot resolve domain names to IP addresses", "فشل في خدمة DNS — الجهاز غير قادر على ترجمة أسماء المواقع إلى عناوين IP"),
       ("The ISP has blocked all IP routing", "مزود الخدمة حظر التوجيه بالكامل"),
       ("The computer lacks an Ethernet NIC", "الكمبيوتر لا يحتوي على كارت شبكة")],
      1,
      "Since the customer can ping a public IP (8.8.8.8), Layer 1 through Layer 3 connectivity is intact. The inability to resolve 'google.com' points squarely to a DNS issue.",
      "بما أن العميل يقدر يعمل ping على IP عام (8.8.8.8)، يبقى الاتصال الفيزيائي وعناوين الـ IP والتوجيه سليمين 100%. العجز عن فتح الموقع بالاسم يؤكد أن العطل في خدمة الـ DNS فقط."),

    Q("Which DNS Resource Record is specifically used to map a domain name to an IPv6 address?",
      "أي سجل من سجلات DNS التالية يُستخدم تحديداً لربط اسم النطاق بعنوان IPv6؟",
      [("A record", "سجل A"),
       ("CNAME record", "سجل CNAME"),
       ("AAAA record", "سجل AAAA"),
       ("PTR record", "سجل PTR")],
      2,
      "The 'AAAA' (Quad-A) record maps a hostname to a 128-bit IPv6 address, whereas the 'A' record maps to a 32-bit IPv4 address.",
      "سجل 'AAAA' (أو Quad-A) مخصص لعناوين IPv6 المكونة من 128 بت، بينما سجل 'A' مخصص لعناوين IPv4 المكونة من 32 بت.")
]

build(
    num=9,
    pct=pct,
    title=title,
    sub=sub,
    chip_en=chip_en,
    chip_ar=chip_ar,
    toc_items=toc_items,
    body_sections=[sec_what, sec_hierarchy, sec_fqdn, sec_resolution, sec_transport, sec_wireshark, sec_records, sec_cisco, sec_conclusion],
    prev_href="lesson-08-icmp.html", prev_label="ICMP (Internet Control Message Protocol)",
    next_href="lesson-10-cisco-ios-cli.html", next_label="Introduction to Cisco IOS CLI",
    source_pdf="09-introduction to dns.pdf",
    extra_footnote="Created using strictly verified CCNA guidelines and real-world networking practices.",
    recap_items=recap,
    quiz_items=quiz,
    out_path="/Users/mohammedelshora/Desktop/Shora/projects/ccna/Network_Fundamentals/lesson-09-dns.html"
)

print("✅ Lesson 09 built successfully!")
