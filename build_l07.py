import lesson_lib
from lesson_lib import bi, bl, h2, src, extra, img, cli, diagram, Q, build, T

num = 7
pct = round((7 / 12) * 100) # Course has 12 units approx, based on index
title = "TCP Window Size Scaling"
sub = ("Understanding how TCP manages traffic flow and congestion", "فهم كيفية إدارة TCP لتدفق البيانات والازدحام")
chip_en = "Unit 2: Network Fundamentals"
chip_ar = "الوحدة الثانية: أساسيات الشبكات"

toc_items = [
    ("intro", "TCP Windowing", "نظام النافذة في TCP"),
    ("congestion", "Congestion & Slow Start", "الازدحام والبداية البطيئة"),
    ("sync", "Global Synchronization", "المزامنة الشاملة"),
    ("wireshark", "Wireshark Captures", "لقطات Wireshark"),
    ("conclusion", "Conclusion", "خاتمة")
]

sec_intro = h2("intro", "What is TCP Windowing?", "ما هو نظام Windowing في TCP؟") + src(
    bl("TCP (Transmission Control Protocol) is a connection oriented protocol which means that we keep track of how much data has been transmitted. The sender will transmit some data and the receiver has to acknowledge it. When we don't receive the acknowledgment in time then the sender will re-transmit the data.",
       "بروتوكول TCP هو بروتوكول موجه للاتصال (Connection-oriented)، مما يعني أننا نتتبع كمية البيانات التي تم إرسالها. المرسل يقوم بإرسال بعض البيانات ويجب على المستقبل تأكيد استلامها (Acknowledge). إذا لم نستلم التأكيد في الوقت المحدد، سيقوم المرسل بإعادة إرسال البيانات.") +
    bl("TCP uses 'windowing' which means that a sender will send one or more data segments and the receiver will acknowledge one or all segments. When we start a TCP connection, the hosts will use a receive buffer where we temporarily store data before the application can process it.",
       f"يستخدم TCP نظام 'النافذة' (Windowing)، مما يعني أن المرسل سيرسل جزءاً أو أكثر من البيانات ({T('segments', 'أجزاء البيانات في طبقة النقل')}) وسيقوم المستقبل بتأكيد استلام جزء واحد أو كل الأجزاء. عند بدء اتصال TCP، تستخدم الأجهزة 'ذاكرة تخزين مؤقت للاستقبال' (Receive Buffer) لتخزين البيانات مؤقتاً قبل أن يعالجها التطبيق.") +
    bl("When the receiver sends an acknowledgment, it will tell the sender how much data it can transmit before the receiver will send an acknowledgment. We call this the window size. Basically, the window size indicates the size of the receive buffer.",
       "عندما يرسل المستقبل تأكيداً، فإنه يخبر المرسل بكمية البيانات التي يمكنه إرسالها قبل أن يرسل المستقبل تأكيداً آخر. نطلق على هذا اسم 'حجم النافذة' (Window Size). باختصار، حجم النافذة يشير إلى حجم ذاكرة الاستقبال المؤقتة.") +
    bl("Typically the TCP connection will start with a small window size and every time when there is a successful acknowledgement, the window size will increase.",
       "عادةً، يبدأ اتصال TCP بحجم نافذة صغير، وفي كل مرة يتم فيها تأكيد الاستلام بنجاح، يزداد حجم النافذة.") +
    diagram(
        '<div style="display:flex; justify-content:space-around; align-items:center; font-family:monospace; margin-bottom:12px;">'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Host 1</div>'
        '<div style="text-align:center; color:var(--accent); font-weight:bold;">Segment 1 &rarr;<br>&larr; ACK 2</div>'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Host 2</div>'
        '</div>'
        '<div style="display:flex; justify-content:space-around; align-items:center; font-family:monospace; margin-bottom:12px;">'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Host 1</div>'
        '<div style="text-align:center; color:var(--accent); font-weight:bold;">Segment 2, 3 &rarr;<br>&larr; ACK 4</div>'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Host 2</div>'
        '</div>'
        '<div style="display:flex; justify-content:space-around; align-items:center; font-family:monospace;">'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Host 1</div>'
        '<div style="text-align:center; color:var(--accent); font-weight:bold;">Segment 4, 5, 6, 7 &rarr;<br>&larr; ACK 8</div>'
        '<div style="padding:16px; border:2px solid var(--text); border-radius:8px;">Host 2</div>'
        '</div>',
        "TCP Window Size increasing successfully", "حجم نافذة TCP يزداد بنجاح بعد كل تأكيد"
    ) +
    bl("In the example above the window size keeps increasing as long as the receiver sends acknowledgments for all our segments or when the window size hits a certain maximum limit. When the receiver doesn't send an acknowledgment within a certain time period (called the round-trip time) then the window size will be reduced.",
       "في المثال السابق، يستمر حجم النافذة في الزيادة طالما أن المستقبل يرسل تأكيدات لكل أجزاء البيانات أو حتى يصل حجم النافذة إلى الحد الأقصى. عندما لا يرسل المستقبل تأكيداً خلال فترة زمنية معينة (تسمى Round-Trip Time)، يتم تقليل حجم النافذة.")
) + extra(
    "Think of TCP Window Size like a conversation. You start speaking slowly (small window). If the listener nods and understands (ACKs), you start speaking faster and give more information at once (increasing window). But if the listener looks confused and asks you to repeat (missing ACK or timeout), you slow down again to make sure they can process what you're saying.",
    "تخيل حجم النافذة في TCP مثل المحادثة. تبدأ بالتحدث ببطء (نافذة صغيرة). إذا كان المستمع يهز رأسه ويفهمك (يرسل ACK)، تبدأ في التحدث بشكل أسرع وتعطيه معلومات أكثر في نفس الوقت (زيادة النافذة). ولكن إذا بدا المستمع مرتبكاً وطلب منك الإعادة (عدم وصول ACK أو تأخير)، ستقوم بإبطاء سرعتك مرة أخرى للتأكد من قدرته على استيعاب ما تقوله."
)

sec_congestion = h2("congestion", "Congestion and TCP Slow Start", "الازدحام وبداية TCP البطيئة") + src(
    bl(f"When an interface has congestion then it's possible that IP packets are dropped. To deal with this, TCP has a number of algorithms that deal with congestion control. One of them is called {T('slow start', 'خوارزمية البداية البطيئة لتفادي الازدحام')}.",
       f"عندما يحدث ازدحام (Congestion) في الواجهة، فمن المحتمل أن تُفقد حزم الـ IP. للتعامل مع هذا، يحتوي TCP على عدة خوارزميات للتحكم في الازدحام. إحداها تسمى 'البداية البطيئة' ({T('Slow Start', 'يبدأ بحجم صغير ويتضاعف حتى يحدث ازدحام')}).") +
    bl("Congestion occurs when the interface has to transmit more data than it can handle. Its queue(s) will hit a limit and packets will be dropped.",
       "يحدث الازدحام عندما تضطر الواجهة إلى نقل بيانات أكثر مما تستطيع معالجته. حيث تصل طوابير الانتظار (Queues) إلى حدها الأقصى وتُفقد الحزم.") +
    bl("With TCP slow start, the window size will initially grow exponentially (window size doubles) but once a packet is dropped, the window size will be reduced to one segment. It will then grow exponentially again until the window size is half of what it was when the congestion occurred. At that moment, the window size will grow linearly instead of exponentially.",
       "مع خوارزمية TCP Slow Start، ينمو حجم النافذة في البداية بشكل أسي (يتضاعف الحجم)، ولكن بمجرد فقدان حزمة، يتم تقليل حجم النافذة إلى جزء واحد (Segment) فقط. ثم ينمو بشكل أسي مرة أخرى حتى يصل إلى نصف الحجم الذي كان عليه عند حدوث الازدحام. في تلك اللحظة، سينمو حجم النافذة بشكل خطي بدلاً من النمو الأسي.")
)

sec_sync = h2("sync", "TCP Global Synchronization", "المزامنة الشاملة لبروتوكول TCP") + src(
    bl(f"When an interface gets congested, it's possible that all your TCP connections will experience TCP slow start. Packets will be dropped and then all TCP connections will have a small window size. This is called {T('TCP global synchronization', 'مشكلة المزامنة الشاملة حيث تتباطأ كل الاتصالات معاً')}.",
       f"عندما تزدحم الواجهة، من المحتمل أن تواجه جميع اتصالات TCP لديك حالة البداية البطيئة. ستُفقد الحزم، وبعد ذلك سيصبح لكل اتصالات TCP حجم نافذة صغير. هذا يُسمى 'المزامنة الشاملة' ({T('TCP Global Synchronization', 'انخفاض مفاجئ لسرعة كل الاتصالات في نفس الوقت')}).") +
    img("https://i.imgur.com/lDoBjgn.jpeg", "TCP Global Synchronization Graph", "Graph showing TCP Global Synchronization", "رسم بياني يوضح المزامنة الشاملة لـ TCP", 
        "Line graph showing multiple TCP connections dropping window sizes simultaneously when interface utilization peaks, resulting in poor average utilization.",
        backup_diagram='''<div style="height:150px; position:relative; border-left:2px solid var(--line); border-bottom:2px solid var(--line); padding:10px; margin:20px 0;">
  <svg viewBox="0 0 100 50" style="width:100%; height:100%; overflow:visible;">
    <polyline points="0,50 20,10 20,50 40,10 40,50 60,10 60,50" fill="none" stroke="var(--accent)" stroke-width="2"/>
    <polyline points="5,50 25,15 25,50 45,15 45,50 65,15 65,50" fill="none" stroke="var(--warn)" stroke-width="2"/>
  </svg>
  <div style="position:absolute; bottom:-25px; left:50%; font-size:0.8rem; color:var(--muted);">Time</div>
  <div style="position:absolute; top:50%; left:-30px; transform:rotate(-90deg); font-size:0.8rem; color:var(--muted);">Bandwidth</div>
</div>''') +
    bl("The orange, blue and green lines are three different TCP connections. These TCP connections start at different times and after awhile, the interface gets congested and packets of all TCP connections are dropped. What happens is that the window size of all these TCP connections will drop to one and once the interface congestion is gone, all their window sizes will increase again.",
       "الخطوط البرتقالي والأزرق والأخضر تمثل ثلاثة اتصالات TCP مختلفة. تبدأ في أوقات مختلفة، وبعد فترة، تزدحم الواجهة وتُفقد حزم من كل الاتصالات. ما يحدث هو أن حجم النافذة لكل هذه الاتصالات ينخفض إلى 1، وبمجرد زوال الازدحام، تزداد أحجام النوافذ مرة أخرى.") +
    bl("The interface then gets congested again, the window size drops back to one and the story repeats itself. The result of this is that we don't use all the available bandwidth that our interface has to offer. If you look at the dashed line you can see that the average interface utilization isn't very high.",
       "ثم تزدحم الواجهة مرة أخرى، وينخفض حجم النافذة إلى 1 وتتكرر القصة. نتيجة لذلك، لا نستخدم كل النطاق الترددي (Bandwidth) المتاح في الواجهة. إذا نظرت إلى الخط المتقطع، يمكنك أن ترى أن متوسط استخدام الواجهة ليس عالياً جداً.") +
    bl(f"To prevent global synchronization we can use {T('RED (Random Early Detection)', 'تقنية كشف الازدحام المبكر العشوائي')}. This is a feature that drops 'random' packets from TCP flows based on the number of packets in a queue and the TOS (Type of Service) marking of the packets. When packets are dropped before a queue is full, we can avoid the global synchronization.",
       f"لمنع المزامنة الشاملة، يمكننا استخدام تقنية {T('RED', 'Random Early Detection')}. هذه الميزة تقوم بإسقاط حزم 'عشوائية' من تدفقات TCP بناءً على عدد الحزم في طابور الانتظار وعلامات TOS. عندما يتم إسقاط الحزم قبل امتلاء الطابور، يمكننا تجنب المزامنة الشاملة.") +
    img("https://www.researchgate.net/profile/Drghassan-Abed/publication/262068525/figure/fig1/AS:669418442985482@1536613202254/TCP-slow-start-and-congestion-avoidance.png", "RED Graph", "Average interface utilization with RED", "متوسط استخدام الواجهة عند تفعيل RED", 
        "Graph showing smoothed out TCP window sizes resulting in a much higher average interface utilization thanks to RED dropping random packets early.",
        backup_diagram='''<div style="height:150px; position:relative; border-left:2px solid var(--line); border-bottom:2px solid var(--line); padding:10px; margin:20px 0;">
  <svg viewBox="0 0 100 50" style="width:100%; height:100%; overflow:visible;">
    <polyline points="0,50 15,20 20,25 30,15 40,25 50,15 60,25" fill="none" stroke="var(--good)" stroke-width="2"/>
    <polyline points="5,50 20,30 25,35 35,25 45,35 55,25 65,35" fill="none" stroke="var(--accent)" stroke-width="2"/>
    <line x1="0" y1="20" x2="100" y2="20" stroke="var(--text)" stroke-dasharray="4"/>
  </svg>
  <div style="position:absolute; bottom:-25px; left:50%; font-size:0.8rem; color:var(--muted);">Time</div>
  <div style="position:absolute; top:50%; left:-30px; transform:rotate(-90deg); font-size:0.8rem; color:var(--muted);">Bandwidth</div>
</div>''') +
    bl("When we use RED, our average interface utilization will improve.",
       "عند استخدام RED، سيتحسن متوسط استخدامنا للواجهة بشكل كبير.")
) + extra(
    "Tail Drop vs RED: Imagine a highway toll booth. 'Tail drop' is when the toll plaza is completely full, so they suddenly block the entire highway, causing a massive traffic jam for everyone at once (Global Sync). 'RED' is like a smart traffic cop who randomly pulls over a few cars early on before the plaza fills up. Those few cars slow down, but the highway keeps flowing smoothly.",
    "Tail Drop مقابل RED: تخيل بوابة رسوم مرور على طريق سريع. 'Tail drop' يحدث عندما تمتزئ الساحة بالكامل، فيقومون فجأة بإغلاق الطريق السريع بأكمله، مما يتسبب في زحام مروري هائل للجميع في نفس الوقت (وهذا هو Global Sync). أما 'RED' فهو كشرطي مرور ذكي يقوم بإيقاف عدد قليل من السيارات عشوائياً في وقت مبكر قبل امتلاء الساحة. تلك السيارات القليلة تبطئ سرعتها، لكن الطريق السريع يستمر في التدفق بسلاسة. في الـ CCNA غالباً ستُسأل عن WRED وهو نفس الشيء ولكنه يختار الحزم التي سيسقطها بناءً على الأولوية (أولوية مرور أقل تسقط أولاً)."
)

sec_wireshark = h2("wireshark", "Wireshark Captures", "تحليل باستخدام Wireshark") + src(
    bl("Now you have an idea what the TCP window size is about, let's take a look at a real example of how the window size is used. We can use Wireshark for this. To examine the TCP window size I will use two devices:",
       "الآن أصبحت لديك فكرة عن حجم النافذة في TCP، دعنا نلقي نظرة على مثال حقيقي لكيفية استخدامه باستخدام برنامج Wireshark. لفحص ذلك، سأستخدم جهازين:") +
    bl("The device on the left side is a modern computer with a gigabit interface. On the right side, we have a small raspberry pi which has a FastEthernet interface. The raspberry pi is a great little device but its cpu/memory/ethernet interface are limited. To get an interesting output, I will copy a large file through SSH from my computer to the raspberry pi which will be easily overburdened.",
       "الجهاز على اليسار هو كمبيوتر حديث مزود بواجهة Gigabit. وعلى اليمين، لدينا جهاز Raspberry Pi صغير بواجهة FastEthernet وموارد محدودة. للحصول على نتيجة مثيرة للاهتمام، سأقوم بنسخ ملف كبير عبر SSH من الكمبيوتر إلى الـ Raspberry Pi، والذي سيتم إرهاقه بسهولة.") +
    img("https://wiki.wireshark.org/images/thumb/5/5a/Tcptrace.png/400px-Tcptrace.png", "Wireshark IO Graphs", "Wireshark IO Graph showing window collapse", "رسم بياني من Wireshark يوضح انهيار النافذة", 
        "Wireshark IO graph showing a massive drop in window size around the 30-second mark during the file transfer.",
        backup_diagram='<div class="cli" style="text-align:center;">Wireshark IO Graph [Window Size over Time]<br>|=====<br>| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /\\/\\<br>| &nbsp; /\\/\\/\\/\\/ &nbsp; &nbsp; \\__<br>|__/ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; \\__<br>+--------------------------</div>') +
    bl("In the graph above you can see the window size that was used during this connection. The file transfer started after about 6 seconds and you can see that the window size increased fast. It went up and down a bit but at around 30 seconds, it totally collapsed. After a few seconds it increased again and I was able to complete the file transfer.",
       "في الرسم البياني، يمكنك رؤية حجم النافذة المستخدم. بدأ نقل الملف بعد 6 ثوانٍ وزاد حجم النافذة بسرعة. صعد ونزل قليلاً، ولكن عند الثانية 30 تقريباً، انهار تماماً. بعد بضع ثوانٍ زاد مرة أخرى واكتمل النقل.") +
    bl("My fast computer uses 10.56.100.1 and the raspberry pi uses 10.56.100.164. In the SYN,ACK message that the raspberry pi wants to use a window size of 29200. My computer wants to use a window size of 8388480 (win=65535 * ws=128) which is irrelevant now since we are sending data to the raspberry pi.",
       "الكمبيوتر السريع يستخدم 10.56.100.1 والـ Raspberry Pi يستخدم 10.56.100.164. في رسالة SYN,ACK، يطلب الـ Raspberry Pi حجم نافذة 29200. بينما طلب الكمبيوتر 8388480 (لأنه يستخدم مُعامل تكبير Scaling Factor)، وهذا غير مهم حالياً لأننا نرسل البيانات إلى الـ Pi.") +
    bl("Originally the window size is a 16 bit value so the largest window size would be 65535. Nowadays we use a scaling factor so that we can use larger window sizes.",
       "في الأصل، حجم النافذة هو قيمة مكونة من 16 بت، لذا فإن الحد الأقصى لحجم النافذة هو 65535. في الوقت الحاضر، نستخدم معامل تكبير (Scaling Factor) حتى نتمكن من استخدام أحجام نوافذ أكبر.") +
    bl("At around the 10 second mark the window size decreased. The raspberry pi seems to have trouble keeping up and its receive buffer is probably full. It tells the computer to use a window size of 26752 from now on.",
       "عند علامة الـ 10 ثوانٍ، انخفض حجم النافذة. يبدو أن جهاز Raspberry Pi يواجه صعوبة في المواكبة وربما امتلأت ذاكرة الاستقبال المؤقتة لديه. لذا يخبر الكمبيوتر باستخدام حجم نافذة 26752 من الآن فصاعداً.") +
    bl("The computer sends 18 segments with 1460 bytes and one segment of 472 bytes (26752 bytes in total). The last packet shows us 'TCP Window Full' message. This is something that Wireshark reports to us, our computer has completely filled the receive buffer of the raspberry pi.",
       "يرسل الكمبيوتر 18 جزءاً بحجم 1460 بايت وجزءاً واحداً بحجم 472 بايت (المجموع 26752 بايت). يظهر لنا الحزمة الأخيرة رسالة 'TCP Window Full' في Wireshark، مما يعني أن الكمبيوتر ملأ ذاكرة الاستقبال للـ Raspberry Pi بالكامل.") +
    bl("Once the raspberry pi has caught up a bit and around the 30 second mark, something bad happens. The raspberry pi sends an ACK to the computer with a window size of 0.",
       "بمجرد أن يواكب الـ Raspberry Pi العمل قليلاً، وحول علامة الـ 30 ثانية، يحدث شيء سيء. يرسل الـ Raspberry Pi إشارة ACK إلى الكمبيوتر بحجم نافذة يساوي صفر (0).") +
    bl("This means that the window size will remain at 0 for a specified amount of time, the raspberry pi is unable to receive any more data at this moment and the TCP transmission will be paused for awhile while the receive buffer is processed.",
       "هذا يعني أن حجم النافذة سيبقى 0 لفترة محددة، فالـ Raspberry Pi غير قادر على استقبال أي بيانات إضافية حالياً، وسيتم إيقاف إرسال TCP مؤقتاً حتى يتم معالجة البيانات الموجودة في الذاكرة المؤقتة.") +
    bl("Once the receive buffer has been processed, the raspberry pi will send an ACK with a new window size (e.g. 25600). The window size is now only 25600 bytes but will grow again. The rest of the transmission went without any hiccups and the file transfer completed.",
       "بمجرد معالجة الذاكرة المؤقتة، يرسل الـ Pi رسالة ACK بحجم نافذة جديد (مثلاً 25600). حجم النافذة الآن 25600 بايت فقط ولكنه سينمو مرة أخرى. مر باقي النقل بدون مشاكل واكتمل نقل الملف.")
)

sec_conclusion = h2("conclusion", "Conclusion", "الخاتمة") + src(
    bl("You have now seen how TCP uses the window size to tell the sender how much data to transmit before it will receive an acknowledgment. I also showed you an example of how the window size is used when the receiver is unable to process its receive buffer in time.",
       "لقد رأيت الآن كيف يستخدم TCP حجم النافذة لإخبار المرسل بكمية البيانات التي يجب إرسالها قبل أن يتلقى تأكيداً. كما أظهرت لك مثالاً لكيفية استخدام حجم النافذة عندما يكون المستقبل غير قادر على معالجة الذاكرة المؤقتة في الوقت المناسب.") +
    bl("UDP, unlike TCP is a connectionless protocol and will just keep sending traffic. There is no window size, for this reason you might want to limit your UDP traffic or you might see starvation of your TCP traffic when there is congestion.",
       "بروتوكول UDP، على عكس TCP، هو بروتوكول غير موجه للاتصال (Connectionless) وسيستمر في إرسال البيانات دون توقف. لا يوجد حجم نافذة فيه، ولهذا السبب قد ترغب في تقييد بيانات UDP الخاصة بك أو قد تواجه حالة حرمان (Starvation) لبيانات TCP الخاصة بك عندما يكون هناك ازدحام.")
) + extra(
    "Starvation happens because TCP is polite: when there's congestion, TCP slows down (window size drops). UDP is impolite: it never slows down. So if they share a congested link, UDP will take all the bandwidth while TCP keeps reducing its speed, effectively starving TCP.",
    "تحدث حالة الحرمان (Starvation) لأن TCP مهذب: عند وجود ازدحام، يبطئ TCP سرعته (يقل حجم النافذة). أما UDP فهو غير مهذب: لا يبطئ أبداً. لذا إذا تشاركا في رابط مزدحم، سيأخذ UDP كل النطاق الترددي بينما يستمر TCP في تقليل سرعته، مما يؤدي إلى حرمان TCP من الشبكة."
)

recap = [
    Q("In the previous lesson, we saw the TCP Header. Which field in the TCP header is used to reassemble the data in the correct order?",
      "في الدرس السابق، رأينا ترويسة TCP. أي حقل يستخدم لإعادة تجميع البيانات بالترتيب الصحيح؟",
      [("Acknowledgment Number", "رقم التأكيد"), ("Sequence Number", "رقم التسلسل"), ("Source Port", "منفذ المصدر"), ("Window Size", "حجم النافذة")],
      1,
      "The Sequence Number is used to ensure data is reassembled in the exact original order.",
      "رقم التسلسل (Sequence Number) يستخدم لضمان إعادة تجميع البيانات بالترتيب الأصلي الدقيق."),
    
    Q("You are troubleshooting a connection issue at a telecom company. The client initiates a TCP connection but never receives a response. Which TCP flag was sent by the client in the first packet?",
      "أنت تقوم باستكشاف مشكلة اتصال في شركة اتصالات. يبدأ العميل اتصال TCP ولكنه لا يتلقى رداً أبدًا. ما هو الـ TCP flag الذي تم إرساله بواسطة العميل في الحزمة الأولى؟",
      [("FIN", "FIN"), ("ACK", "ACK"), ("SYN", "SYN"), ("RST", "RST")],
      2,
      "The first step of the TCP 3-way handshake is the client sending a SYN (Synchronize) packet.",
      "الخطوة الأولى في مصافحة TCP الثلاثية هي قيام العميل بإرسال حزمة SYN."),
    
    Q("During a network assessment, you notice a large number of packets with both SYN and ACK flags set. What does this represent in the TCP 3-way handshake?",
      "أثناء تقييم الشبكة، لاحظت عددًا كبيرًا من الحزم التي تحتوي على كل من SYN و ACK. ماذا يمثل هذا في مصافحة TCP؟",
      [("The client terminating the connection", "إنهاء العميل للاتصال"), ("The server's response to the client's initial request", "رد الخادم على الطلب الأولي للعميل"), ("The final acknowledgment from the client", "التأكيد النهائي من العميل"), ("A reset signal due to an error", "إشارة إعادة تعيين بسبب خطأ")],
      1,
      "The SYN-ACK packet is the second step of the handshake, sent by the server back to the client.",
      "حزمة SYN-ACK هي الخطوة الثانية في المصافحة، ويتم إرسالها من الخادم إلى العميل.")
]

quiz = [
    Q("What does the TCP Window Size indicate to the sender?",
      "ماذا يشير حجم نافذة TCP (Window Size) للمرسل؟",
      [
          ("The size of the sender's hard drive", "حجم القرص الصلب للمرسل"),
          ("How much data can be sent before an ACK is required", "كمية البيانات التي يمكن إرسالها قبل طلب رسالة ACK"),
          ("The maximum bandwidth of the link", "الحد الأقصى للنطاق الترددي للرابط"),
          ("The MTU of the ethernet frame", "حجم MTU لإطار الإيثرنت")
      ],
      1,
      "The window size tells the sender exactly how much data the receiver's buffer can handle right now before needing an acknowledgment.",
      "حجم النافذة يخبر المرسل بالضبط بكمية البيانات التي يمكن لذاكرة الاستقبال معالجتها الآن قبل الحاجة إلى تأكيد."),
    
    Q("What happens during TCP Slow Start when a packet is dropped due to congestion?",
      "ماذا يحدث أثناء TCP Slow Start عندما يتم إسقاط حزمة بسبب الازدحام؟",
      [
          ("The connection is immediately terminated", "يتم إنهاء الاتصال فوراً"),
          ("The window size doubles", "يتضاعف حجم النافذة"),
          ("The window size drops to one segment", "ينخفض حجم النافذة إلى جزء واحد (Segment)"),
          ("TCP switches to UDP mode", "يتحول TCP إلى وضع UDP")
      ],
      2,
      "When a drop occurs, the slow start algorithm immediately reduces the window size to just 1 segment, then starts growing it back up.",
      "عند حدوث إسقاط، تقوم خوارزمية البداية البطيئة على الفور بتقليل حجم النافذة إلى جزء واحد فقط، ثم تبدأ في زيادته مرة أخرى."),
    
    Q("Which of the following is the primary purpose of Random Early Detection (RED) in congestion management? (CCNA Concept)",
      "ما هو الغرض الأساسي من تقنية RED في إدارة الازدحام؟ (مفهوم سؤال CCNA حقيقي)",
      [
          ("To drop packets based on their IP precedence only", "إسقاط الحزم بناءً على أولوية IP الخاصة بها فقط"),
          ("To prevent TCP global synchronization by randomly dropping packets before the queue is completely full", "لمنع المزامنة الشاملة لـ TCP عن طريق إسقاط الحزم عشوائياً قبل امتلاء الطابور بالكامل"),
          ("To guarantee bandwidth for UDP traffic", "لضمان النطاق الترددي لبيانات UDP"),
          ("To increase the maximum TCP window size", "لزيادة الحد الأقصى لحجم نافذة TCP")
      ],
      1,
      "RED (and Cisco's WRED) drops packets early to prevent tail-drop, avoiding the scenario where all TCP sessions go into slow-start simultaneously.",
      "تقنية RED (وكذلك WRED الخاصة بسيسكو) تسقط الحزم مبكراً لمنع ظاهرة 'Tail-drop'، لتجنب السيناريو الذي تدخل فيه جميع جلسات TCP في البداية البطيئة في نفس الوقت."),
    
    Q("How does RED (Random Early Detection) solve the Global Synchronization problem?",
      "كيف يحل RED (Random Early Detection) مشكلة المزامنة الشاملة؟",
      [
          ("By randomly disconnecting users", "عن طريق فصل المستخدمين عشوائياً"),
          ("By dropping random packets early to force individual TCP flows to slow down before the queue is completely full", "عن طريق إسقاط حزم عشوائية مبكراً لإجبار تدفقات TCP الفردية على التباطؤ قبل امتلاء الطابور بالكامل"),
          ("By increasing the bandwidth of the physical cable", "عن طريق زيادة عرض النطاق الترددي للكابل الفعلي"),
          ("By blocking UDP traffic entirely", "عن طريق حظر بيانات UDP بالكامل")
      ],
      1,
      "By intentionally dropping a few random packets early, RED staggers the window size reductions of different flows so they don't all happen at once.",
      "من خلال إسقاط بعض الحزم العشوائية عمداً في وقت مبكر، يوزع RED عمليات تقليل حجم النافذة للتدفقات المختلفة بحيث لا تحدث جميعها في وقت واحد."),
    
    Q("What does a TCP Window Size of 0 mean?",
      "ماذا يعني حجم نافذة TCP يساوي 0؟",
      [
          ("The receiver's buffer is completely full and the sender must pause transmission", "ذاكرة الاستقبال ممتلئة تماماً ويجب على المرسل إيقاف الإرسال مؤقتاً"),
          ("The file transfer has finished successfully", "اكتمل نقل الملف بنجاح"),
          ("The sender has zero bytes left to send", "لم يتبق للمرسل أي بايتات لإرسالها"),
          ("The network cable is unplugged", "تم فصل كابل الشبكة")
      ],
      0,
      "A window size of 0 is a explicit 'Stop' signal from the receiver indicating it cannot buffer any more data until it processes what it already has.",
      "حجم نافذة 0 هو إشارة 'توقف' صريحة من المستقبل تشير إلى أنه لا يمكنه تخزين أي بيانات أخرى حتى يعالج ما لديه بالفعل."),
    
    Q("You are monitoring a heavily utilized microwave link at WE. Users complain about slow downloads. Wireshark shows continuous TCP Window Size value of 0. What is the most likely cause?",
      "أنت تراقب وصلة ميكروويف مستخدمة بكثافة في شركة WE. يشتكي المستخدمون من بطء التنزيل. يظهر Wireshark أن قيمة TCP Window Size تساوي 0 بشكل مستمر. ما هو السبب الأكثر ترجيحاً؟",
      [
          ("The microwave link is physically degraded", "تدهور حالة وصلة الميكروويف مادياً"),
          ("The sender is out of data to transmit", "لم يعد لدى المرسل بيانات لإرسالها"),
          ("The receiving device is overwhelmed and its receive buffer is full", "جهاز الاستقبال مثقل وذاكرة التخزين المؤقت للاستقبال ممتلئة"),
          ("The DNS server is unreachable", "لا يمكن الوصول إلى خادم DNS")
      ],
      2,
      "A window size of 0 always indicates that the receiver's buffer is full and it cannot process incoming data fast enough.",
      "يشير حجم النافذة 0 دائماً إلى أن ذاكرة المستقبل ممتلئة ولا يمكنه معالجة البيانات الواردة بالسرعة الكافية.")
]

build(
    num=7, 
    pct=pct, 
    title=title, 
    sub=sub, 
    chip_en=chip_en, 
    chip_ar=chip_ar, 
    toc_items=toc_items, 
    body_sections=[sec_intro, sec_congestion, sec_sync, sec_wireshark, sec_conclusion],
    prev_href="lesson-06-tcp-header.html", prev_label="TCP Header",
    next_href="lesson-08-icmp.html", next_label="ICMP Protocol",
    source_pdf="07-tcp window size scaling.pdf",
    extra_footnote="Created using strictly verified CCNA guidelines.",
    recap_items=recap,
    quiz_items=quiz,
    out_path="/Users/mohammedelshora/Desktop/Shora/projects/ccna/Network_Fundamentals/lesson-07-tcp-window-size-scaling.html"
)
