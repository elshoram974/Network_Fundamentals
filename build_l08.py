import lesson_lib
from lesson_lib import bi, bl, h2, src, extra, img, cli, diagram, Q, build, T

num = 8
pct = round((8 / 11) * 100)
title = "ICMP (Internet Control Message Protocol)"
sub = ("Understanding the diagnostic and error-reporting protocol of IP networks", "فهم بروتوكول التشخيص والإبلاغ عن الأخطاء في شبكات IP")
chip_en = "Unit 2: Network Fundamentals"
chip_ar = "الوحدة الثانية: أساسيات الشبكات"

toc_items = [
    ("what", "What is ICMP?", "ما هو ICMP؟"),
    ("header", "ICMP Header", "ترويسة ICMP"),
    ("types", "ICMP Types & Codes", "أنواع وأكواد ICMP"),
    ("ping", "Ping", "أداة Ping"),
    ("traceroute", "Traceroute", "Traceroute"),
    ("redirect", "ICMP Redirect", "إعادة التوجيه"),
    ("unreachable", "Destination Unreachable", "الوجهة غير قابلة للوصول"),
    ("conclusion", "Conclusion", "الخاتمة"),
]

sec_what = h2("what", "What is ICMP?", "ما هو ICMP؟") + src(
    bl("ICMP (Internet Control Message Protocol) is a network protocol that is used for diagnostics and network management. It is used to send error messages and operational information indicating, for example, that a requested service is not available or that a host or router could not be reached.",
       f"بروتوكول ICMP ({T('Internet Control Message Protocol', 'بروتوكول رسائل التحكم بالإنترنت')}) هو بروتوكول شبكي يُستخدم للتشخيص وإدارة الشبكة. يتم استخدامه لإرسال رسائل الأخطاء والمعلومات التشغيلية، مثلاً أن خدمة مطلوبة غير متوفرة أو أنه لا يمكن الوصول إلى جهاز معين أو راوتر.") +
    bl("ICMP is part of the IP protocol suite and is defined in RFC 792. ICMP messages are encapsulated within IP packets, but ICMP is considered a layer 3 (Network layer) protocol, not a layer 4 protocol. This is because it is an integral part of the IP suite used for reporting errors — it does not transport user data like TCP or UDP.",
       f"بروتوكول ICMP جزء من مجموعة بروتوكولات IP ومُعرَّف في {T('RFC 792', 'وثيقة المعايير الرسمية لبروتوكول ICMP')}. رسائل ICMP تُغلَّف داخل حزم IP، لكن ICMP يُعتبر بروتوكول طبقة 3 (طبقة الشبكة) وليس طبقة 4. وذلك لأنه جزء أساسي من مجموعة IP ويُستخدم للإبلاغ عن الأخطاء — فهو لا ينقل بيانات المستخدم مثل TCP أو UDP.") +
    bl("You might wonder: if ICMP messages are inside IP packets, why isn't it considered a layer 4 protocol? The answer is that ICMP exists to support IP itself — it reports on the health and reachability of the network, not to carry application data.",
       "قد تتساءل: إذا كانت رسائل ICMP داخل حزم IP، لماذا لا يُعتبر بروتوكول طبقة 4؟ الإجابة هي أن ICMP موجود لدعم IP نفسه — فهو يُبلّغ عن صحة الشبكة وإمكانية الوصول، وليس لنقل بيانات التطبيقات.")
) + extra(
    "Think of ICMP as the 'postal service notification system.' If you send a letter (IP packet) and the recipient's address doesn't exist, the postal service sends YOU a notification card back saying 'Address Not Found.' That notification card is ICMP. It doesn't carry your actual letter — it just tells you something went wrong with the delivery.",
    "تخيل ICMP كـ 'نظام إشعارات البريد.' لو بعتت جواب (IP packet) والعنوان اللي بعتله مش موجود، البريد بيبعتلك إشعار يقولك 'العنوان مش موجود.' الإشعار ده هو ICMP. هو مش بينقل الجواب بتاعك — هو بس بيقولك إن في مشكلة في التوصيل."
)

sec_header = h2("header", "ICMP Header", "ترويسة ICMP") + src(
    bl("The ICMP header is relatively simple compared to the TCP header we studied earlier. It consists of the following fields:",
       "ترويسة ICMP بسيطة نسبياً مقارنة بترويسة TCP اللي درسناها قبل كده. وتتكون من الحقول التالية:") +
    img("images/lesson08/img_1.jpg", "ICMP Header Format and Fields",
        "Structure of the ICMP Header (Type, Code, Checksum)", "هيكل ترويسة بروتوكول ICMP (النوع، الكود، فحص الأخطاء)",
        "ICMP Header") +
    diagram(
        '<div class="hdr-grid" style="grid-template-columns:repeat(4,1fr)">'
        '<div class="f span1"><b>Type</b>8 bits</div>'
        '<div class="f span1"><b>Code</b>8 bits</div>'
        '<div class="f span2"><b>Checksum</b>16 bits</div>'
        '<div class="f span4"><b>Rest of Header / Data</b>variable (depends on Type and Code)</div>'
        '</div>',
        "ICMP Header Field Layout", "مخطط حقول ترويسة ICMP"
    ) +
    bl("<b>Type:</b> This 8-bit field identifies the type of ICMP message. For example, Type 8 is an Echo Request (ping), and Type 0 is an Echo Reply.",
       "<b>Type:</b> حقل 8 بت يحدد نوع رسالة ICMP. مثلاً، النوع 8 هو طلب Echo (ping)، والنوع 0 هو رد Echo.") +
    bl("<b>Code:</b> This 8-bit field provides additional context for the Type. For example, if the Type is 3 (Destination Unreachable), the Code tells you exactly WHY it's unreachable — is the network unreachable? The host? The port?",
       "<b>Code:</b> حقل 8 بت يعطي معلومات إضافية عن النوع. مثلاً، لو النوع 3 (الوجهة غير قابلة للوصول)، الكود بيقولك بالظبط ليه — هل الشبكة مش متاحة؟ الجهاز؟ البورت؟") +
    bl("<b>Checksum:</b> A 16-bit field used to check the integrity of the ICMP message. It ensures the header has not been corrupted during transit.",
       "<b>Checksum:</b> حقل 16 بت يُستخدم للتحقق من سلامة رسالة ICMP. يتأكد إن الترويسة ما اتلفتش أثناء النقل.")
) + extra(
    "Compared to the TCP header (20+ bytes with many fields), the ICMP header is tiny — just 8 bytes minimum. This makes sense because ICMP doesn't need port numbers, sequence numbers, or window sizes. It's not transporting data; it's just delivering a short status message.",
    "بالمقارنة مع ترويسة TCP (20+ بايت بحقول كتير)، ترويسة ICMP صغيرة جداً — 8 بايت بس كحد أدنى. وده منطقي لأن ICMP مش محتاج أرقام بورتات أو أرقام تسلسل أو أحجام نوافذ. هو مش بينقل بيانات — هو بس بيوصّل رسالة حالة قصيرة."
)

sec_types = h2("types", "ICMP Types & Codes", "أنواع وأكواد ICMP") + src(
    bl("There are many ICMP types but here are the most important ones you need to know for the CCNA exam:",
       "في أنواع كتير لـ ICMP لكن دي أهم الأنواع اللي محتاج تعرفها لامتحان CCNA:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Type", "النوع") + '</th><th>' + bi("Code", "الكود") + '</th><th>' + bi("Description", "الوصف") + '</th></tr>' +
    '<tr><td class="mono-cell">0</td><td class="mono-cell">0</td><td>' + bi("Echo Reply (response to ping)", "رد Echo (استجابة للـ ping)") + '</td></tr>' +
    '<tr><td class="mono-cell">3</td><td class="mono-cell">0</td><td>' + bi("Destination Network Unreachable", "الشبكة الوجهة غير قابلة للوصول") + '</td></tr>' +
    '<tr><td class="mono-cell">3</td><td class="mono-cell">1</td><td>' + bi("Destination Host Unreachable", "الجهاز الوجهة غير قابل للوصول") + '</td></tr>' +
    '<tr><td class="mono-cell">3</td><td class="mono-cell">3</td><td>' + bi("Destination Port Unreachable", "البورت الوجهة غير قابل للوصول") + '</td></tr>' +
    '<tr><td class="mono-cell">3</td><td class="mono-cell">13</td><td>' + bi("Communication Administratively Prohibited (ACL)", "الاتصال ممنوع إدارياً (بسبب ACL)") + '</td></tr>' +
    '<tr><td class="mono-cell">5</td><td class="mono-cell">0</td><td>' + bi("Redirect for Network", "إعادة توجيه للشبكة") + '</td></tr>' +
    '<tr><td class="mono-cell">5</td><td class="mono-cell">1</td><td>' + bi("Redirect for Host", "إعادة توجيه للجهاز") + '</td></tr>' +
    '<tr><td class="mono-cell">8</td><td class="mono-cell">0</td><td>' + bi("Echo Request (ping)", "طلب Echo (ping)") + '</td></tr>' +
    '<tr><td class="mono-cell">11</td><td class="mono-cell">0</td><td>' + bi("TTL Exceeded in Transit (used by traceroute)", "انتهاء TTL أثناء النقل (يستخدمه traceroute)") + '</td></tr>' +
    '</table></div>' +
    bl("The most common types you will encounter are Type 0 and Type 8 (Echo Reply and Echo Request — used by ping), Type 3 (Destination Unreachable), Type 5 (Redirect), and Type 11 (Time Exceeded — used by traceroute).",
       "أكتر الأنواع اللي هتقابلها هي النوع 0 والنوع 8 (رد وطلب Echo — يستخدمهم ping)، والنوع 3 (الوجهة غير قابلة للوصول)، والنوع 5 (إعادة التوجيه)، والنوع 11 (انتهاء الوقت — يستخدمه traceroute).")
) + extra(
    "For the CCNA exam, the most critical ICMP types to memorize are: Type 0/8 for ping, Type 3 for unreachable, Type 5 for redirect, and Type 11 for TTL exceeded. You should also know that Type 3, Code 13 means an ACL (Access Control List) is blocking the traffic — a very common interview question at telecom companies in Egypt.",
    "لامتحان CCNA، أهم أنواع ICMP اللي لازم تحفظها: النوع 0/8 لـ ping، النوع 3 لـ unreachable، النوع 5 لـ redirect، والنوع 11 لانتهاء TTL. كمان لازم تعرف إن النوع 3 كود 13 معناه إن في ACL (قائمة تحكم بالوصول) بتمنع الترافيك — ده سؤال شائع جداً في المقابلات في شركات الاتصالات في مصر."
)

sec_ping = h2("ping", "Ping (Echo Request / Echo Reply)", "أداة Ping (طلب ورد الـ Echo)") + src(
    bl("The ping command is probably the most well-known use of ICMP. When you ping a device, your computer sends an ICMP Echo Request (Type 8) to the target. If the target is reachable and alive, it responds with an ICMP Echo Reply (Type 0).",
       f"أمر {T('ping', 'أداة تشخيص شبكة تختبر إمكانية الوصول لجهاز معين')} هو أشهر استخدام لـ ICMP. لما بتعمل ping لجهاز، الكمبيوتر بتاعك بيبعت ICMP Echo Request (النوع 8) للهدف. لو الهدف موجود وشغال، بيرد بـ ICMP Echo Reply (النوع 0).") +
    img("images/lesson08/img_2.jpg", "Ping Echo Request and Echo Reply Flow",
        "Ping Diagnostics: Echo Request (Type 8) and Echo Reply (Type 0)", "تشخيص الشبكة بـ Ping: طلب الـ Echo (النوع 8) ورد الـ Echo (النوع 0)",
        "Ping Diagram") +
    diagram(
        '<div style="display:flex; justify-content:space-around; align-items:center; font-family:monospace; margin-bottom:12px;">'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">PC (10.0.0.1)</div>'
        '<div style="text-align:center; color:var(--accent); font-weight:bold;">Echo Request (Type 8) &rarr;<br>&larr; Echo Reply (Type 0)</div>'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Server (10.0.0.2)</div>'
        '</div>',
        "Ping Flow Schematic", "مخطط تدفق رسائل Ping"
    ) +
    img("images/lesson08/img_3.jpg", "Wireshark Capture of ICMP Echo Request and Reply",
        "Wireshark Packet Capture of Ping Exchange", "التقاط حزم تبادل الـ Ping في برنامج Wireshark",
        "Wireshark Ping Capture") +
    bl("Here is an example of a ping on a Cisco IOS device:",
       "ده مثال على ping من جهاز سيسكو:") +
    cli("Router# <b>ping 10.0.0.2</b>\n\nType escape sequence to abort.\nSending 5, 100-byte ICMP Echos to 10.0.0.2, timeout is 2 seconds:\n!!!!!\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms") +
    bl("Each exclamation mark (!) means a successful reply was received. A period (.) means a timeout — no reply was received within the timeout period. A 'U' means an ICMP Destination Unreachable was received.",
       "كل علامة تعجب (!) معناها إن الرد وصل بنجاح. النقطة (.) معناها timeout — مفيش رد وصل في الوقت المحدد. حرف 'U' معناه إن اتبعت رسالة ICMP Destination Unreachable.")
) + extra(
    "Ping is the first tool every network engineer reaches for when troubleshooting. The output tells you a lot: '!!!!!' means everything is working. '.....' means total failure (check cables, IP addresses, routes). 'U.U.U' means a router along the path is telling you 'I don't know how to reach that destination.' In Egyptian telecom interviews, expect questions like: 'You ping a server and get U — what does it mean and where do you troubleshoot?'",
    "Ping هي أول أداة أي مهندس شبكات بيستخدمها في التشخيص. المخرجات بتقولك كتير: '!!!!!' يعني كل حاجة شغالة. '.....' يعني فشل تام (افحص الكابلات، عناوين IP، المسارات). 'U.U.U' يعني في راوتر في الطريق بيقولك 'مش عارف أوصل للوجهة دي.' في مقابلات شركات الاتصالات في مصر، توقع أسئلة زي: 'عملت ping لسيرفر وطلع U — يعني إيه وفين تبدأ تحل المشكلة؟'"
)

sec_traceroute = h2("traceroute", "Traceroute", "أداة Traceroute") + src(
    bl(f"Traceroute is another incredibly useful ICMP-based tool. It traces the path that packets take from your computer to a destination, showing you every {T('hop', 'كل راوتر بتعدي عليه الحزمة في طريقها للوجهة')} (router) along the way.",
       f"Traceroute أداة مفيدة جداً تعتمد على ICMP. بتتبع المسار اللي الحزم بتاخده من جهازك للوجهة، وبتوريك كل {T('hop', 'كل راوتر الحزمة بتعدي عليه')} (راوتر) في الطريق.") +
    bl("Traceroute works by sending packets with an increasing TTL (Time To Live) value. The first packet has TTL=1, so the first router decrements it to 0 and sends back an ICMP Time Exceeded (Type 11) message. The second packet has TTL=2, so it passes the first router but expires at the second. This continues until the packet reaches the final destination.",
       f"Traceroute بتشتغل عن طريق إرسال حزم بقيمة {T('TTL', 'Time To Live — عدد الراوترات اللي الحزمة تقدر تعديها')} متزايدة. أول حزمة TTL=1، فأول راوتر بينقّصه لـ 0 ويبعت رسالة ICMP Time Exceeded (النوع 11). تاني حزمة TTL=2، فبتعدي أول راوتر لكن بتنتهي عند التاني. وهكذا لحد ما الحزمة توصل الوجهة النهائية.") +
    img("images/lesson08/img_5.jpg", "Traceroute TTL Exceeded Process across Routers",
        "How Traceroute Discovers Hops by Incrementing TTL", "كيف تكتشف أداة Traceroute الراوترات بزيادة قيمة TTL",
        "Traceroute Process") +
    diagram(
        '<div style="display:flex; justify-content:space-around; align-items:center; font-family:monospace; flex-wrap:wrap; gap:8px;">'
        '<div style="padding:12px; border:2px solid var(--text); border-radius:8px;">PC</div>'
        '<div style="text-align:center; color:var(--warn); font-weight:bold;">TTL=1<br>&#x1F6D1;</div>'
        '<div style="padding:12px; border:2px solid var(--accent); border-radius:8px;">R1</div>'
        '<div style="text-align:center; color:var(--warn); font-weight:bold;">TTL=2<br>&#x1F6D1;</div>'
        '<div style="padding:12px; border:2px solid var(--accent); border-radius:8px;">R2</div>'
        '<div style="text-align:center; color:var(--good); font-weight:bold;">TTL=3<br>&#x2705;</div>'
        '<div style="padding:12px; border:2px solid var(--text); border-radius:8px;">Server</div>'
        '</div>',
        "Traceroute discovers each hop by incrementing TTL", "Traceroute بتكتشف كل hop عن طريق زيادة TTL"
    ) +
    cli("Router# <b>traceroute 10.0.0.5</b>\n\nType escape sequence to abort.\nTracing the route to 10.0.0.5\n\n  1   10.0.0.1    4 ms    2 ms    1 ms\n  2   10.0.0.3    8 ms    6 ms    5 ms\n  3   10.0.0.5   12 ms   10 ms    9 ms") +
    bl("Important note: Windows tracert uses ICMP Echo Requests by default. However, Cisco IOS traceroute and Linux traceroute use UDP packets by default. They still rely on ICMP Time Exceeded messages coming back from each router.",
       "ملاحظة مهمة: Windows tracert بيستخدم ICMP Echo Requests افتراضياً. لكن traceroute في Cisco IOS و Linux بيستخدم حزم UDP افتراضياً. لكنهم لسه بيعتمدوا على رسائل ICMP Time Exceeded اللي بترجع من كل راوتر.")
) + extra(
    "In Egyptian ISPs like WE, Orange, and Vodafone, traceroute is a daily tool for NOC engineers. When a customer complains about slow internet, the first thing you do is a traceroute to see WHERE the delay is occurring. If hop 3 shows 200ms but hop 2 shows 5ms, you know the problem is between router 2 and router 3.",
    "في شركات الإنترنت المصرية زي WE وأورانج وفودافون، traceroute أداة يومية لمهندسي الـ NOC. لما عميل يشتكي من بطء الإنترنت، أول حاجة تعملها traceroute عشان تشوف فين التأخير. لو الـ hop رقم 3 بيوري 200ms بس الـ hop رقم 2 بيوري 5ms، يبقى المشكلة بين الراوتر 2 و 3."
)

sec_redirect = h2("redirect", "ICMP Redirect", "إعادة التوجيه ICMP Redirect") + src(
    bl(f"An {T('ICMP Redirect', 'رسالة بيبعتها الراوتر لجهاز عشان يقوله استخدم مسار أفضل')} (Type 5) message is sent by a router to tell a host that there is a better first-hop router available for a particular destination.",
       f"رسالة {T('ICMP Redirect', 'رسالة يبعتها الراوتر للجهاز ليستخدم مسار أحسن')} (النوع 5) بيبعتها الراوتر لجهاز عشان يقوله إن في راوتر أول-hop أفضل متاح لوجهة معينة.") +
    img("images/lesson08/img_10.jpg", "ICMP Redirect Message Scenario",
        "Router notifying Host of a more optimal first-hop router via ICMP Redirect (Type 5)", "الراوتر يوجه الجهاز لاستخدام مسار أفضل عبر ICMP Redirect (النوع 5)",
        "ICMP Redirect Topology") +
    bl("For example, imagine a host sends a packet to Router A, but Router A knows that Router B (which is on the same subnet as the host) has a better route to the destination. Router A will forward the packet to Router B, but also send an ICMP Redirect to the host telling it: 'Next time you want to reach this destination, send your packets directly to Router B instead of me.'",
       "مثلاً، تخيل جهاز بيبعت حزمة لـ Router A، لكن Router A يعرف إن Router B (اللي على نفس الشبكة الفرعية للجهاز) عنده مسار أفضل للوجهة. Router A هيوجّه الحزمة لـ Router B، لكن كمان هيبعت ICMP Redirect للجهاز يقوله: 'المرة الجاية لما عايز توصل للوجهة دي، ابعت حزمك مباشرة لـ Router B بدل مني.'")
) + extra(
    "ICMP Redirects can be a security concern. An attacker could send fake ICMP Redirect messages to trick a host into sending traffic through a malicious router (Man-in-the-Middle attack). For this reason, many security-conscious networks disable ICMP Redirects on their routers with the command 'no ip redirects'.",
    "ICMP Redirects ممكن يكون فيها مشكلة أمنية. المهاجم يقدر يبعت رسائل ICMP Redirect مزيفة عشان يخدع الجهاز إنه يبعت الترافيك عبر راوتر خبيث (هجوم Man-in-the-Middle). عشان كده، شبكات كتير واعية أمنياً بتعطّل ICMP Redirects على الراوترات بالأمر 'no ip redirects'."
)

sec_unreachable = h2("unreachable", "Destination Unreachable (Type 3)", "الوجهة غير قابلة للوصول (النوع 3)") + src(
    bl("ICMP Destination Unreachable (Type 3) is one of the most important ICMP message types. When a router or host cannot deliver a packet, it sends this message back to the source. The Code field tells you exactly what went wrong:",
       "رسالة ICMP Destination Unreachable (النوع 3) هي من أهم أنواع رسائل ICMP. لما راوتر أو جهاز ميقدرش يوصّل حزمة، بيبعت الرسالة دي للمصدر. حقل الكود بيقولك بالظبط إيه اللي حصل:") +
    '<div class="table-wrap"><table><tr><th>' + bi("Code", "الكود") + '</th><th>' + bi("Meaning", "المعنى") + '</th><th>' + bi("Common Cause", "السبب الشائع") + '</th></tr>' +
    '<tr><td class="mono-cell">0</td><td>' + bi("Network Unreachable", "الشبكة غير قابلة للوصول") + '</td><td>' + bi("No route in the routing table", "مفيش مسار في جدول التوجيه") + '</td></tr>' +
    '<tr><td class="mono-cell">1</td><td>' + bi("Host Unreachable", "الجهاز غير قابل للوصول") + '</td><td>' + bi("ARP failure (host is down or no ARP reply)", "فشل ARP (الجهاز مطفي أو مفيش رد ARP)") + '</td></tr>' +
    '<tr><td class="mono-cell">3</td><td>' + bi("Port Unreachable", "البورت غير قابل للوصول") + '</td><td>' + bi("No application listening on that port", "مفيش تطبيق شغال على البورت ده") + '</td></tr>' +
    '<tr><td class="mono-cell">4</td><td>' + bi("Fragmentation Needed but DF bit set", "التجزئة مطلوبة لكن بت DF مفعّل") + '</td><td>' + bi("Packet too large and can't be fragmented", "الحزمة كبيرة جداً ومش ممكن تتجزأ") + '</td></tr>' +
    '<tr><td class="mono-cell">13</td><td>' + bi("Administratively Prohibited", "ممنوع إدارياً") + '</td><td>' + bi("Blocked by an ACL on the router", "ممنوع بسبب ACL على الراوتر") + '</td></tr>' +
    '</table></div>' +
    bl("Code 0 vs Code 1 is a very important distinction: Code 0 (Network Unreachable) means the router has no route to the destination network at all. Code 1 (Host Unreachable) means the router found the network but the specific host is not responding (usually an ARP issue).",
       "الفرق بين كود 0 وكود 1 مهم جداً: كود 0 (شبكة غير قابلة للوصول) معناها الراوتر مالوش أي مسار للشبكة دي أصلاً. كود 1 (جهاز غير قابل للوصول) معناها الراوتر لقي الشبكة بس الجهاز المحدد مش بيرد (عادةً مشكلة ARP).")
) + extra(
    "Code 0 vs Code 1 is a classic Cisco interview question. Here's a real-world way to think about it: Code 0 is like calling a phone number with a non-existent area code — the system has no idea where to route your call. Code 1 is like calling a valid area code and number, but the person's phone is turned off — the system knows where they should be, but they're not there.",
    "كود 0 مقابل كود 1 سؤال كلاسيكي في مقابلات سيسكو. طريقة عملية تفكر بيها: كود 0 زي ما تتصل برقم تليفون بكود منطقة مش موجود — النظام مش عارف يوصّل المكالمة خالص. كود 1 زي ما تتصل بكود منطقة ورقم صح، بس التليفون بتاع الشخص مقفول — النظام عارف المفروض يكون فين، بس مش موجود."
)

sec_conclusion = h2("conclusion", "Conclusion", "الخاتمة") + src(
    bl("ICMP is a fundamental protocol of the IP suite used for diagnostics and error reporting. It is a Layer 3 protocol despite being encapsulated in IP packets.",
       "ICMP بروتوكول أساسي في مجموعة IP بيُستخدم للتشخيص والإبلاغ عن الأخطاء. هو بروتوكول طبقة 3 بالرغم من إنه بيتغلف داخل حزم IP.") +
    bl("Key takeaways: Ping uses ICMP Type 8 (Echo Request) and Type 0 (Echo Reply). Traceroute uses ICMP Type 11 (Time Exceeded). Destination Unreachable messages (Type 3) tell you specifically why a packet could not be delivered. ICMP Redirects (Type 5) tell hosts to use a better route.",
       "أهم النقاط: Ping بيستخدم ICMP النوع 8 (طلب Echo) والنوع 0 (رد Echo). Traceroute بيستخدم ICMP النوع 11 (انتهاء الوقت). رسائل الوجهة غير قابلة للوصول (النوع 3) بتقولك بالظبط ليه الحزمة ما وصلتش. ICMP Redirect (النوع 5) بيقول للأجهزة تستخدم مسار أفضل.")
) + extra(
    "For the CCNA exam, remember: ICMP = Layer 3, NOT Layer 4. Know the most common Types (0, 3, 5, 8, 11) and be able to distinguish between Destination Unreachable codes. Understand how ping and traceroute work under the hood. And remember that ICMP can be blocked by firewalls and ACLs — just because ping fails doesn't mean the host is actually down!",
    "لامتحان CCNA، افتكر: ICMP = طبقة 3 مش طبقة 4. اعرف أهم الأنواع (0، 3، 5، 8، 11) واقدر تفرق بين أكواد Destination Unreachable. افهم إزاي ping و traceroute بيشتغلوا من جوا. وافتكر إن ICMP ممكن يتمنع بالفايروول والـ ACL — مش لمجرد إن ping فشل يبقى الجهاز فعلاً مطفي!"
)

recap = [
    Q("In the previous lesson, we learned about TCP Window Size Scaling. What does a TCP Window Size of 0 mean?",
      "في الدرس السابق، اتعلمنا عن TCP Window Size Scaling. إيه معنى TCP Window Size يساوي 0؟",
      [("The connection has been terminated", "تم إنهاء الاتصال"),
       ("The receiver's buffer is full and the sender must pause", "ذاكرة الاستقبال ممتلئة ويجب على المرسل التوقف"),
       ("The sender has nothing left to send", "المرسل مالوش حاجة تانية يبعتها"),
       ("The cable is disconnected", "الكابل مفصول")],
      1,
      "A window size of 0 means the receiver's buffer is completely full. The sender must stop sending until the receiver processes its buffer and sends a new ACK with a non-zero window.",
      "حجم نافذة 0 معناه إن ذاكرة الاستقبال ممتلئة تماماً. المرسل لازم يوقف لحد ما المستقبل يعالج الذاكرة ويبعت ACK جديد بحجم نافذة غير صفري."),

    Q("What mechanism does TCP use to prevent global synchronization?",
      "إيه الآلية اللي TCP بيستخدمها لمنع المزامنة الشاملة (Global Synchronization)؟",
      [("Increase the window size to maximum", "زيادة حجم النافذة للحد الأقصى"),
       ("RED (Random Early Detection)", "RED (الكشف المبكر العشوائي)"),
       ("Switch to UDP", "التحول إلى UDP"),
       ("Disable all TCP connections", "تعطيل كل اتصالات TCP")],
      1,
      "RED drops random packets early before the queue is completely full, preventing all TCP connections from going into slow-start simultaneously.",
      "RED بيسقط حزم عشوائية مبكراً قبل امتلاء الطابور بالكامل، مما يمنع كل اتصالات TCP من الدخول في البداية البطيئة في نفس الوقت."),

    Q("What is the main difference between TCP and UDP regarding congestion?",
      "إيه الفرق الرئيسي بين TCP و UDP فيما يتعلق بالازدحام؟",
      [("TCP slows down during congestion; UDP does not", "TCP بيبطئ أثناء الازدحام؛ UDP لا"),
       ("UDP is more reliable than TCP", "UDP أكتر موثوقية من TCP"),
       ("There is no difference", "مفيش فرق"),
       ("UDP uses window sizing too", "UDP بيستخدم حجم النافذة كمان")],
      0,
      "TCP is 'polite' — it reduces its window size when congestion occurs. UDP is 'impolite' — it keeps sending at the same rate regardless, which can starve TCP traffic.",
      "TCP 'مهذب' — بيقلل حجم نافذته لما يحصل ازدحام. UDP 'مش مهذب' — بيفضل يبعت بنفس المعدل بغض النظر، وده ممكن يحرم ترافيك TCP.")
]

quiz = [
    Q("What layer does ICMP operate at?",
      "ICMP بيشتغل في أنهي طبقة؟",
      [("Layer 1 (Physical)", "طبقة 1 (فيزيائية)"),
       ("Layer 2 (Data Link)", "طبقة 2 (ربط البيانات)"),
       ("Layer 3 (Network)", "طبقة 3 (الشبكة)"),
       ("Layer 4 (Transport)", "طبقة 4 (النقل)")],
      2,
      "ICMP is a Layer 3 (Network layer) protocol. Even though ICMP messages are encapsulated in IP packets, it is considered part of the IP suite at Layer 3.",
      "ICMP بروتوكول طبقة 3 (طبقة الشبكة). بالرغم من إن رسائل ICMP بتتغلف داخل حزم IP، إلا إنه يُعتبر جزء من مجموعة IP في طبقة 3."),

    Q("You ping a server from your router and receive 'UUUUU'. What does the 'U' indicate?",
      "عملت ping لسيرفر من الراوتر وظهرلك 'UUUUU'. الحرف 'U' بيدل على إيه؟",
      [("The host is up and responding", "الجهاز شغال وبيرد"),
       ("Unknown error occurred", "حصل خطأ غير معروف"),
       ("An ICMP Destination Unreachable was received", "اتبعت رسالة ICMP Destination Unreachable"),
       ("The connection is using UDP", "الاتصال بيستخدم UDP")],
      2,
      "'U' in ping output stands for Destination Unreachable — an ICMP Type 3 message was returned by a router along the path.",
      "'U' في مخرجات ping معناها Destination Unreachable — رسالة ICMP نوع 3 رجعت من راوتر في الطريق."),

    Q("Which ICMP Type is used by traceroute to discover intermediate routers?",
      "أنهي نوع ICMP بيستخدمه traceroute لاكتشاف الراوترات الوسيطة؟",
      [("Type 0 — Echo Reply", "النوع 0 — رد Echo"),
       ("Type 3 — Destination Unreachable", "النوع 3 — الوجهة غير قابلة للوصول"),
       ("Type 8 — Echo Request", "النوع 8 — طلب Echo"),
       ("Type 11 — Time Exceeded", "النوع 11 — انتهاء الوقت")],
      3,
      "Traceroute relies on ICMP Type 11 (Time Exceeded) messages. Each router decrements the TTL; when it hits 0, the router sends back a Type 11 message, revealing its IP.",
      "Traceroute بيعتمد على رسائل ICMP النوع 11 (انتهاء الوقت). كل راوتر بينقّص الـ TTL؛ لما يوصل لـ 0، الراوتر بيبعت رسالة نوع 11، وبكده بيكشف عنوان IP بتاعه."),

    Q("What is the difference between ICMP Destination Unreachable Code 0 and Code 1?",
      "إيه الفرق بين ICMP Destination Unreachable كود 0 وكود 1؟",
      [("Code 0 = port closed, Code 1 = host down", "كود 0 = البورت مقفول، كود 1 = الجهاز مطفي"),
       ("Code 0 = no route to network, Code 1 = host on network not responding", "كود 0 = مفيش مسار للشبكة، كود 1 = الجهاز على الشبكة مش بيرد"),
       ("Code 0 = TTL expired, Code 1 = ACL blocking", "كود 0 = انتهاء TTL، كود 1 = ACL بيمنع"),
       ("They mean the same thing", "معناهم واحد")],
      1,
      "Code 0 (Network Unreachable) means no route exists to the destination network. Code 1 (Host Unreachable) means the network was found but the specific host is not responding.",
      "كود 0 (شبكة غير قابلة للوصول) معناها مفيش مسار أصلاً للشبكة. كود 1 (جهاز غير قابل للوصول) معناها الشبكة موجودة بس الجهاز المحدد مش بيرد."),

    Q("A network engineer pings a server successfully, but the web application on port 80 is not responding. Which ICMP Destination Unreachable code would be returned if the port is closed?",
      "مهندس شبكات عمل ping لسيرفر بنجاح، لكن التطبيق على البورت 80 مش بيرد. أنهي كود ICMP Destination Unreachable هيرجع لو البورت مقفول؟",
      [("Code 0 — Network Unreachable", "كود 0 — شبكة غير قابلة للوصول"),
       ("Code 1 — Host Unreachable", "كود 1 — جهاز غير قابل للوصول"),
       ("Code 3 — Port Unreachable", "كود 3 — بورت غير قابل للوصول"),
       ("Code 13 — Administratively Prohibited", "كود 13 — ممنوع إدارياً")],
      2,
      "Code 3 (Port Unreachable) means the host was reached but no application is listening on the requested port.",
      "كود 3 (بورت غير قابل للوصول) معناها إن الجهاز تم الوصول ليه لكن مفيش تطبيق شغال على البورت المطلوب."),

    Q("Why might a successful ping NOT guarantee that a service is actually reachable? (Real interview question)",
      "ليه نجاح الـ ping ممكن ما يضمنش إن الخدمة فعلاً متاحة؟ (سؤال مقابلة حقيقي)",
      [("Ping tests Layer 3 connectivity only, not Layer 4+ services", "Ping بيختبر اتصال طبقة 3 بس، مش خدمات طبقة 4 وما فوقها"),
       ("Ping always fails on firewalled networks", "Ping دايماً بيفشل على الشبكات اللي فيها فايروول"),
       ("Ping uses UDP which is unreliable", "Ping بيستخدم UDP اللي غير موثوق"),
       ("Ping only works on Cisco devices", "Ping بيشتغل على أجهزة سيسكو بس")],
      0,
      "Ping verifies Layer 3 (IP) reachability. A host can respond to ping (ICMP) while having its web server (HTTP, port 80) completely down. Always verify the specific service too.",
      "Ping بيتحقق من إمكانية الوصول على طبقة 3 (IP) بس. الجهاز ممكن يرد على ping (ICMP) بينما سيرفر الويب بتاعه (HTTP، بورت 80) مطفي تماماً. دايماً اتحقق من الخدمة المحددة كمان.")
]

build(
    num=8,
    pct=pct,
    title=title,
    sub=sub,
    chip_en=chip_en,
    chip_ar=chip_ar,
    toc_items=toc_items,
    body_sections=[sec_what, sec_header, sec_types, sec_ping, sec_traceroute, sec_redirect, sec_unreachable, sec_conclusion],
    prev_href="lesson-07-tcp-window-size-scaling.html", prev_label="TCP Window Size Scaling",
    next_href="lesson-09-dns.html", next_label="Introduction to DNS",
    source_pdf="08-icmp (internet control message protocol).pdf",
    extra_footnote="Created using strictly verified CCNA guidelines.",
    recap_items=recap,
    quiz_items=quiz,
    out_path="/Users/mohammedelshora/Desktop/Shora/projects/ccna/Network_Fundamentals/lesson-08-icmp.html"
)

print("✅ Lesson 08 built successfully!")
