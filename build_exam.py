# -*- coding: utf-8 -*-
"""
Builder for Unit 2 Comprehensive Exam & Question Bank:
CCNA 200-301 - Unit 2: Network Fundamentals (Lessons 01 - 11)
"""

import json
import re

OUT_FILE = "exam-unit-02-network-fundamentals.html"

# 25 Realistic CCNA Multiple Choice Questions
mcqs = [
    {
        "id": "mcq1",
        "lesson": "Lesson 01: OSI Model",
        "q_en": "At which layer of the OSI model does data get encapsulated into a 'Segment', and what primary information is added?",
        "q_ar": "في أي طبقة من نموذج OSI يتم تغليف البيانات في شكل 'Segment' (جزء)، وما هي المعلومة الأساسية التي تُضاف؟",
        "opts_en": [
            "Layer 4 (Transport); Source and Destination Port numbers",
            "Layer 3 (Network); Source and Destination IP addresses",
            "Layer 2 (Data Link); Source and Destination MAC addresses",
            "Layer 5 (Session); Session IDs and Synchronization tokens"
        ],
        "opts_ar": [
            "الطبقة الرابعة (النقل Transport)؛ أرقام منافذ المصدر والوجهة (Port numbers)",
            "الطبقة الثالثة (الشبكة Network)؛ عناوين IP للمصدر والوجهة",
            "الطبقة الثانية (ربط البيانات Data Link)؛ عناوين MAC الفيزيائية",
            "الطبقة الخامسة (الجلسة Session)؛ معرفات الجلسة ورموز المزامنة"
        ],
        "ans": 0,
        "exp_en": "Layer 4 (Transport) encapsulates data into Segments by adding Layer 4 headers containing Source and Destination Port numbers (e.g. TCP/UDP) to identify running applications. Layer 3 adds IP addresses (Packets), and Layer 2 adds MAC addresses (Frames).",
        "exp_ar": "الطبقة الرابعة (Transport) تغلف البيانات في وحدات تُسمى Segments بإضافة أرقام منافذ المصدر والوجهة (Source & Destination Ports) لتحديد التطبيقات المعنية. الطبقة الثالثة تضيف عناوين IP وتنتج Packets، والطبقة الثانية تضيف عناوين MAC وتنتج Frames."
    },
    {
        "id": "mcq2",
        "lesson": "Lesson 01: OSI Model",
        "q_en": "What is the correct order of data encapsulation as payload moves DOWN the protocol stack during transmission?",
        "q_ar": "ما هو الترتيب الصحيح لعملية تغليف البيانات (Encapsulation) أثناء نزولها عبر طبقات الشبكة عند الإرسال؟",
        "opts_en": [
            "Data -> Segment -> Packet -> Frame -> Bits",
            "Data -> Packet -> Segment -> Frame -> Bits",
            "Bits -> Frame -> Packet -> Segment -> Data",
            "Data -> Frame -> Segment -> Packet -> Bits"
        ],
        "opts_ar": [
            "بيانات (Data) -> جزء (Segment) -> حزمة (Packet) -> إطار (Frame) -> بتات (Bits)",
            "بيانات (Data) -> حزمة (Packet) -> جزء (Segment) -> إطار (Frame) -> بتات (Bits)",
            "بتات (Bits) -> إطار (Frame) -> حزمة (Packet) -> جزء (Segment) -> بيانات (Data)",
            "بيانات (Data) -> إطار (Frame) -> جزء (Segment) -> حزمة (Packet) -> بتات (Bits)"
        ],
        "ans": 0,
        "exp_en": "During encapsulation, Application Data is segmented at Layer 4 (Segment), addressed at Layer 3 (Packet), framed with MAC headers and FCS trailers at Layer 2 (Frame), and physically encoded onto media at Layer 1 (Bits).",
        "exp_ar": "أثناء التغليف (Encapsulation)، تتحول البيانات أولاً في الطبقة 4 إلى Segment، ثم في الطبقة 3 إلى Packet، ثم في الطبقة 2 إلى Frame بإضافة ترويسة MAC وذيل الفحص FCS، وأخيراً تتحول في الطبقة 1 إلى Bits كهربائية أو ضوئية."
    },
    {
        "id": "mcq3",
        "lesson": "Lesson 02: IPv4",
        "q_en": "What is the default subnet mask and first octet range for a Class B IPv4 network in classful addressing?",
        "q_ar": "ما هو قناع الشبكة الافتراضي ونطاق البايت الأول لعناوين IPv4 من الفئة B (Class B)؟",
        "opts_en": [
            "128.0.0.0 to 191.255.255.255 with default mask 255.255.0.0 (/16)",
            "192.0.0.0 to 223.255.255.255 with default mask 255.255.255.0 (/24)",
            "1.0.0.0 to 126.255.255.255 with default mask 255.0.0.0 (/8)",
            "224.0.0.0 to 239.255.255.255 with default mask 255.255.255.255 (/32)"
        ],
        "opts_ar": [
            "من 128.0.0.0 إلى 191.255.255.255 مع قناع افتراضي 255.255.0.0 (/16)",
            "من 192.0.0.0 إلى 223.255.255.255 مع قناع افتراضي 255.255.255.0 (/24)",
            "من 1.0.0.0 إلى 126.255.255.255 مع قناع افتراضي 255.0.0.0 (/8)",
            "من 224.0.0.0 إلى 239.255.255.255 مع قناع افتراضي 255.255.255.255 (/32)"
        ],
        "ans": 0,
        "exp_en": "Class B first octet starts with binary '10' (decimal 128 to 191). The default classful mask allocates 16 bits for the network and 16 bits for hosts (255.255.0.0 or /16).",
        "exp_ar": "يبدأ البايت الأول للفئة B بالبتين '10' ثنائياً (النطاق العشري 128 إلى 191). القناع الافتراضي يخصص 16 بت للشبكة و 16 بت للأجهزة (255.255.0.0 أو /16)."
    },
    {
        "id": "mcq4",
        "lesson": "Lesson 02: IPv4",
        "q_en": "Given the host IP address 172.16.45.100 with a subnet mask of 255.255.255.192 (/26), what is the valid subnet Network ID and Broadcast address?",
        "q_ar": "بمعلومية عنوان الجهاز 172.16.45.100 وقناع الشبكة 255.255.255.192 (/26)، ما هو عنوان معرف الشبكة (Network ID) وعنوان البث (Broadcast)؟",
        "opts_en": [
            "Network ID: 172.16.45.64; Broadcast: 172.16.45.127",
            "Network ID: 172.16.45.0; Broadcast: 172.16.45.63",
            "Network ID: 172.16.45.64; Broadcast: 172.16.45.128",
            "Network ID: 172.16.45.96; Broadcast: 172.16.45.127"
        ],
        "opts_ar": [
            "معرف الشبكة: 172.16.45.64؛ عنوان البث: 172.16.45.127",
            "معرف الشبكة: 172.16.45.0؛ عنوان البث: 172.16.45.63",
            "معرف الشبكة: 172.16.45.64؛ عنوان البث: 172.16.45.128",
            "معرف الشبكة: 172.16.45.96؛ عنوان البث: 172.16.45.127"
        ],
        "ans": 0,
        "exp_en": "With mask /26 (255.255.255.192), the block size (magic number) in the 4th octet is 256 - 192 = 64. Subnet intervals are 0, 64, 128, 192. Since 100 falls between 64 and 127, the Network ID is 172.16.45.64, usable hosts are .65 - .126, and the Broadcast is 172.16.45.127.",
        "exp_ar": "مع القناع /26 (255.255.255.192)، يكون حجم الكتلة (الرقم السحري) في البايت الرابع هو 256 - 192 = 64. الشبكات الفرعية تبدأ عند: 0، 64، 128، 192. بما أن 100 يقع بين 64 و 127، فإن عنوان الشبكة هو 172.16.45.64، والأجهزة الصالحة من 65 إلى 126، وعنوان البث هو 172.16.45.127."
    },
    {
        "id": "mcq5",
        "lesson": "Lesson 02: IPv4",
        "q_en": "What is the primary purpose of the Class D IPv4 address range (224.0.0.0 to 239.255.255.255)?",
        "q_ar": "ما هو الغرض الأساسي من فئة العناوين Class D في بروتوكول IPv4 (من 224.0.0.0 إلى 239.255.255.255)؟",
        "opts_en": [
            "Multicast communications (one-to-many group transmission)",
            "Experimental and research purposes reserved by IETF",
            "Default public unicast web server addresses",
            "Direct loopback testing on local interfaces"
        ],
        "opts_ar": [
            "البث متعدد الوجهات (Multicast) لإرسال حزم لمجموعة أجهزة محددة",
            "الأبحاث والتجارب العلمية المحجوزة من هيئة IETF",
            "عناوين البث الفردي العامة المخصصة لمواقع الويب",
            "اختبار الاتصال الداخلي لكارت الشبكة (Loopback)"
        ],
        "ans": 0,
        "exp_en": "Class D (224.0.0.0 - 239.255.255.255) is strictly reserved for Multicast traffic (e.g. OSPF hello packets to 224.0.0.5, video streams). Class E (240-255) is reserved for experimental research.",
        "exp_ar": "الفئة D (من 224.0.0.0 إلى 239.255.255.255) محجوزة بالكامل للبث متعدد الوجهات (Multicast) مثل إرسال رسائل بروتوكول OSPF إلى 224.0.0.5 أو بث الفيديو لمجموعة أجهزة. الفئة E هي المحجوزة للأبحاث."
    },
    {
        "id": "mcq6",
        "lesson": "Lesson 03: IPv4 Packet Header",
        "q_en": "Which protocol number in the IPv4 header's 'Protocol' field designates ICMP, TCP, and UDP respectively?",
        "q_ar": "ما هي أرقام البروتوكولات في حقل 'Protocol' بهيدر IPv4 التي تشير إلى ICMP و TCP و UDP على التوالي؟",
        "opts_en": [
            "ICMP = 1, TCP = 6, UDP = 17",
            "ICMP = 2, TCP = 17, UDP = 6",
            "ICMP = 6, TCP = 1, UDP = 17",
            "ICMP = 1, TCP = 80, UDP = 443"
        ],
        "opts_ar": [
            "ICMP = 1، و TCP = 6، و UDP = 17",
            "ICMP = 2، و TCP = 17، و UDP = 6",
            "ICMP = 2، و TCP = 1، و UDP = 17",
            "ICMP = 1، و TCP = 80، و UDP = 443"
        ],
        "ans": 0,
        "exp_en": "The IPv4 Protocol field uses 8 bits to identify the next higher-layer protocol: 1 for ICMP, 6 for TCP, and 17 for UDP. (80 and 443 are TCP port numbers, not IP protocol numbers!).",
        "exp_ar": "حقل Protocol في هيدر IP يحدد البروتوكول المحمول في الطبقة الأعلى: القيمة 1 لبروتوكول ICMP، و 6 لـ TCP، و 17 لـ UDP. (أرقام 80 و 443 هي أرقام منافذ في طبقة النقل وليست أرقام بروتوكول IP!)."
    },
    {
        "id": "mcq7",
        "lesson": "Lesson 03: IPv4 Packet Header",
        "q_en": "What action does a router take when it receives an IPv4 packet with a Time to Live (TTL) value of 1?",
        "q_ar": "ما الإجراء الذي يتخذه الراوتر عندما يستلم حزمة IPv4 قيمة حقل TTL (عمر الحزمة) فيها تساوي 1؟",
        "opts_en": [
            "Decrements TTL to 0, drops the packet, and sends an ICMP Type 11 (Time Exceeded) message to the source",
            "Forwards the packet to the next hop and resets the TTL to 255",
            "Broadcasts the packet to all active interfaces to prevent routing loops",
            "Encapsulates the packet into an ICMP Echo Request frame"
        ],
        "opts_ar": [
            "يقلل قيمة TTL إلى 0، ويسقط الحزمة (Drop)، ويرسل رسالة ICMP Type 11 (انتهت المهلة) للمرسل",
            "يمرر الحزمة للراوتر التالي ويعيد ضبط قيمة TTL إلى 255",
            "يقوم ببث الحزمة لجميع المنافذ لتفادي حلقات التوجيه",
            "يقوم بتغليف الحزمة كطلب ICMP Echo جديد"
        ],
        "ans": 0,
        "exp_en": "Routers decrement TTL by 1 before routing. If TTL reaches 0, the router discards the packet to prevent infinite looping and generates an ICMP Type 11 Code 0 (Time Exceeded) message back to the sender. This mechanism is the foundation of traceroute.",
        "exp_ar": "يقوم كل راوتر بإنقاص قيمة TTL بمقدار 1. فإذا أصبحت القيمة 0، يُسقط الراوتر الحزمة لمنع الدوران اللانهائي ويرسل رسالة ICMP Type 11 Code 0 (Time Exceeded) للمصدر. هذه الآلية هي الأساس الذي تعمل به أداة traceroute."
    },
    {
        "id": "mcq8",
        "lesson": "Lesson 03: IPv4 Packet Header",
        "q_en": "An IPv4 packet has the 'DF' (Don't Fragment) bit set to 1, but its total size exceeds the outgoing interface MTU. What happens?",
        "q_ar": "حزمة IPv4 تم تفعيل بت عدم التجزئة (DF = 1) فيها، ولكن حجمها يتجاوز الحد الأقصى للنقل (MTU) للواجهة الخارجة. ماذا يحدث؟",
        "opts_en": [
            "The router drops the packet and responds with ICMP Type 3 Code 4 (Fragmentation Needed and DF set)",
            "The router overrides the DF bit, fragments the packet, and forwards the pieces",
            "The router compresses the payload using gzip and transmits without fragmentation",
            "The packet is stored in NVRAM until the link MTU increases"
        ],
        "opts_ar": [
            "يسقط الراوتر الحزمة ويرسل للمصدر رسالة ICMP Type 3 Code 4 (مطلوب التجزئة ولكن بت DF مفعل)",
            "يتجاهل الراوتر بت DF ويقوم بتجزئة الحزمة وتمرير الأجزاء بشكل طبيعي",
            "يقوم الراوتر بضغط البيانات تلقائياً وتمريرها دون تجزئة",
            "يتم حفظ الحزمة في ذاكرة NVRAM مؤقتاً لحين زيادة سرعة الرابط"
        ],
        "ans": 0,
        "exp_en": "When MTU is exceeded and DF=1, the router cannot fragment the packet. It must discard it and return an ICMP Destination Unreachable message (Type 3, Code 4: Fragmentation Needed). This is critical for Path MTU Discovery (PMTUD).",
        "exp_ar": "عندما يتجاوز حجم الحزمة قيمة MTU مع وجود DF=1، لا يستطيع الراوتر تجزئتها، فيضطر لإسقاطها وإرسال رسالة ICMP Type 3 Code 4 تشير إلى أن الحزمة تحتاج تجزئة ولكن بت DF يمنع ذلك، وهي الرسالة الأساسية في تقنية Path MTU Discovery."
    },
    {
        "id": "mcq9",
        "lesson": "Lesson 04: ARP",
        "q_en": "When Host A needs to send an IP packet to Host B on the SAME local subnet but does not know Host B's MAC address, what destination MAC address is placed in the ARP Request frame?",
        "q_ar": "عندما يريد الجهاز A إرسال حزمة للجهاز B على نفس الشبكة المحلية ولكن لا يعرف عنوان الـ MAC للجهاز B، ما هو عنوان الـ MAC للوجهة في إطار طلب ARP؟",
        "opts_en": [
            "FF:FF:FF:FF:FF:FF (Broadcast MAC)",
            "00:00:00:00:00:00 (Null MAC)",
            "The MAC address of the default gateway router",
            "The multicast MAC address 01:00:5E:00:00:01"
        ],
        "opts_ar": [
            "FF:FF:FF:FF:FF:FF (عنوان البث العام Broadcast)",
            "00:00:00:00:00:00 (عنوان فارغ Null MAC)",
            "عنوان الـ MAC الخاص بالراوتر (Default Gateway)",
            "عنوان البث المتعدد 01:00:5E:00:00:01"
        ],
        "ans": 0,
        "exp_en": "An ARP Request is sent as a Layer 2 broadcast (FF:FF:FF:FF:FF:FF) so that every switch port floods it and all hosts on the segment receive it. The target host then replies with a Layer 2 Unicast ARP Reply directly to Host A's MAC.",
        "exp_ar": "يُرسل طلب ARP كبث عام في الطبقة الثانية (FF:FF:FF:FF:FF:FF) لكي يمرره السويتش لجميع المنافذ ويستلمه كل جهاز في الشبكة المحلية. وعندما يتعرف الجهاز المطلوب على الـ IP الخاص به، يرد بإطار ARP Reply أحادي (Unicast) مباشرة للـ MAC الخاص بالجهاز A."
    },
    {
        "id": "mcq10",
        "lesson": "Lesson 04: ARP",
        "q_en": "What is a 'Gratuitous ARP' (GARP), and how can a malicious actor exploit it?",
        "q_ar": "ما هو طلب 'Gratuitous ARP' (GARP)، وكيف يمكن للمهاجم استغلاله في هجمات الشبكة؟",
        "opts_en": [
            "An unprompted ARP announcement of an IP-to-MAC mapping; can be exploited for ARP Cache Poisoning / Spoofing (Man-in-the-Middle)",
            "A request to translate a domain name to an IP; exploited for DNS amplification",
            "A query sent to determine the router's OSPF priority; exploited for router takeover",
            "An ARP request sent with TTL=0 to map local switch hops"
        ],
        "opts_ar": [
            "إعلان ARP تلقائي غير مطلوب يربط عنوان IP بعنوان MAC؛ يمكن استغلاله في تسميم جدول الـ ARP وهجمات الرجل في المنتصف (MITM)",
            "طلب لتحويل اسم النطاق إلى IP؛ يستغل في هجمات تضخيم الـ DNS",
            "استعلام لتحديد أولوية راوتر OSPF؛ يستغل في السيطرة على الراوتر",
            "طلب ARP يرسل بقيمة TTL=0 لتحديد مسار السويتشات المحلية"
        ],
        "ans": 0,
        "exp_en": "Gratuitous ARP is sent voluntarily without being asked, typically on interface startup to detect duplicate IPs or update neighbor ARP caches. Attackers use fake GARP packets to poison the ARP cache of victims, redirecting traffic through the attacker's machine (ARP Spoofing / MITM).",
        "exp_ar": "الـ Gratuitous ARP هو إعلان يرسله الجهاز من تلقاء نفسه دون أن يسأله أحد (مثل فحص وجود IP مكرر عند بدء التشغيل). يستغله المهاجمون بإرسال رسائل GARP مزيفة لتسميم كاش الـ ARP لدى الضحايا وخداعهم بأن الـ MAC الخاص بالراوتر هو جهاز المخترق (هجوم MITM)."
    },
    {
        "id": "mcq11",
        "lesson": "Lesson 05: TCP and UDP",
        "q_en": "What is the correct flag exchange sequence during a standard TCP Three-Way Handshake?",
        "q_ar": "ما هو التسلسل الصحيح لتبادل الأعلام (Flags) أثناء المصافحة الثلاثية (Three-Way Handshake) لبروتوكول TCP؟",
        "opts_en": [
            "Client sends SYN -> Server responds with SYN-ACK -> Client responds with ACK",
            "Client sends ACK -> Server responds with SYN -> Client responds with FIN",
            "Client sends SYN -> Server responds with ACK -> Client responds with DATA",
            "Client sends RST -> Server responds with SYN -> Client responds with ACK"
        ],
        "opts_ar": [
            "العميل يرسل SYN -> الخادم يرد بـ SYN-ACK -> العميل يؤكد بـ ACK",
            "العميل يرسل ACK -> الخادم يرد بـ SYN -> العميل يرد بـ FIN",
            "العميل يرسل SYN -> الخادم يرد بـ ACK -> العميل يبدأ إرسال DATA",
            "العميل يرسل RST -> الخادم يرد بـ SYN -> العميل يؤكد بـ ACK"
        ],
        "ans": 0,
        "exp_en": "TCP establishes reliable connection via 3 steps: 1) SYN (synchronize initial sequence number), 2) SYN-ACK (server acknowledges client's SYN and sends its own SYN), 3) ACK (client acknowledges server's SYN). Data transmission can then begin.",
        "exp_ar": "يؤسس TCP الاتصال الموثوق عبر 3 خطوات: 1) إرسال SYN لبدء المزامنة، 2) رد الخادم بـ SYN-ACK لتأكيد استلام الرقم وإرسال رقمه الأولي، 3) رد العميل بـ ACK لتأكيد الاتصال، وبعدها تبدأ البيانات في التدفق."
    },
    {
        "id": "mcq12",
        "lesson": "Lesson 05: TCP and UDP",
        "q_en": "Why would an application like VoIP (Voice over IP) or real-time online gaming choose UDP instead of TCP at Layer 4?",
        "q_ar": "لماذا تفضل تطبيقات مثل المكالمات الصوتية (VoIP) والألعاب المباشرة استخدام بروتوكول UDP بدلاً من TCP؟",
        "opts_en": [
            "UDP has minimal header overhead (8 bytes) and does not delay streams with retransmissions of lost packets",
            "UDP provides guaranteed encryption and automatic error recovery",
            "UDP automatically adjusts router bandwidth allocation dynamically",
            "UDP enforces strict sequential ordering of every incoming packet"
        ],
        "opts_ar": [
            "لأن UDP ترويسته صغيرة جداً (8 بايت فقط) ولا يعطل البث بإعادة إرسال الحزم المفقودة المتأخرة",
            "لأن UDP يقدم تشفيراً مضموناً واستعادة تلقائية للأخطاء",
            "لأن UDP يرفع سرعة النطاق الترددي في الراوترات تلقائياً",
            "لأن UDP يجبر الأجهزة على إعادة ترتيب كل بايت بدقة متناهية"
        ],
        "ans": 0,
        "exp_en": "VoIP and live gaming require low latency and jitter. Retransmitting a dropped voice packet 200ms later is useless because the conversation has already moved on. UDP delivers packets with low overhead without waiting for acknowledgments or retransmissions.",
        "exp_ar": "تطبيقات الصوت المباشر والألعاب تتطلب سرعة فائقة وزمن وصول منخفض (Low Latency). إعادة إرسال حزمة صوتية فُقدت بعد مضي 200 ميلي ثانية لا فائدة منه بل يسبب تقطيعاً مزعجاً. لذلك UDP هو الأنسب لعدم انتظاره تأكيدات أو إعادة إرسال."
    },
    {
        "id": "mcq13",
        "lesson": "Lesson 06: TCP Header",
        "q_en": "In the TCP header, what is the value of the Data Offset (DO) field when NO options are included, and what does it represent?",
        "q_ar": "في هيدر TCP، ما هي قيمة حقل إزاحة البيانات (Data Offset) في حال عدم وجود خيارات (Options)، وعلام تدل؟",
        "opts_en": [
            "5 (representing 20 bytes, as the field counts in 32-bit / 4-byte words)",
            "20 (representing 20 bits of header data)",
            "0 (indicating zero options are present)",
            "10 (representing 40 bytes of standard payload)"
        ],
        "opts_ar": [
            "5 (وتعني 20 بايت، لأن الحقل يقيس الطول بوحدات الكلمة المكونة من 4 بايت / 32 بت)",
            "20 (وتعني 20 بت من بيانات الهيدر)",
            "0 (وتعني عدم وجود خيارات مضافة)",
            "10 (وتعني 40 بايت كطول ثابت)"
        ],
        "ans": 0,
        "exp_en": "The Data Offset (Header Length) field is 4 bits wide and specifies the TCP header size in 32-bit (4-byte) words. The minimum TCP header is 20 bytes, which equals 5 words (5 x 4 bytes = 20 bytes). Therefore, DO = 5 for a baseline header.",
        "exp_ar": "حقل Data Offset طوله 4 بت ويحدد طول هيدر TCP بمضاعفات 4 بايت (32-bit words). أقل طول لهيدر TCP هو 20 بايت، أي 5 كلمات (5 × 4 بايت = 20 بايت). لذلك تكون قيمة DO = 5 في الهيدر القياسي بدون Options."
    },
    {
        "id": "mcq14",
        "lesson": "Lesson 06: TCP Header",
        "q_en": "What is the functional difference between the TCP RST (Reset) flag and the FIN (Finish) flag?",
        "q_ar": "ما هو الفرق الوظيفي بين علم إعادة الضبط RST (Reset) وعلم الإنهاء FIN (Finish) في بروتوكول TCP؟",
        "opts_en": [
            "RST immediately and abruptly aborts an abnormal connection; FIN gracefully terminates a session using the standard 4-way handshake",
            "FIN abruptly aborts; RST gracefully negotiates buffer sizes",
            "RST is used during startup; FIN is used during congestion",
            "There is no difference; both initiate identical tear-down sequences"
        ],
        "opts_ar": [
            "علم RST يقطع وينهي الاتصال فوراً وبشكل مفاجئ لوجود خلل؛ بينما FIN ينهي الجلسة بطريقة مهذبة ومنظمة عبر مصافحة الإنهاء",
            "علم FIN يقطع الاتصال فجأة؛ وعلم RST يتفاوض على حجم الذاكرة المؤقتة",
            "علم RST يستخدم عند بدء التشغيل؛ وعلم FIN يستخدم عند حدوث ازدحام",
            "لا يوجد أي فرق وظيفي بينهما؛ كلاهما يقوم بنفس المهمة بالضبط"
        ],
        "ans": 0,
        "exp_en": "FIN is used in normal graceful termination: both sides send FIN and receive ACK. RST is an emergency reset flag sent when an unrecoverable error occurs, a port is closed, or a half-open connection is detected, terminating communication immediately without waiting.",
        "exp_ar": "علم FIN يُستخدم في إنهاء الاتصال الطبيعي المنظم (Graceful Teardown) حيث يرسل كل طرف FIN ويستلم ACK. أما RST فهو علم طوارئ يُرسل عند حدوث خطأ غير قابل للإصلاح أو عند إرسال بيانات لمنفذ مغلق، ليتم إسقاط الجلسة فوراً دون انتظار."
    },
    {
        "id": "mcq15",
        "lesson": "Lesson 07: TCP Window Size Scaling",
        "q_en": "During a large file transfer, a sender receives an acknowledgment packet from the receiver with 'Window Size: 0' (TCP ZeroWindow). What does this signify?",
        "q_ar": "أثناء نقل ملف كبير عبر TCP، استلم المرسل حزمة تأكيد من المستقبل تحتوي على 'Window Size: 0' (نافذة صفرية). علام يدل ذلك؟",
        "opts_en": [
            "The receiver's buffer is completely full; the sender must immediately pause transmission until a Window Update is received",
            "The physical cable has disconnected and transmission failed",
            "The file transfer is finished and all data has been written to disk",
            "The sender must immediately double its transmission rate"
        ],
        "opts_ar": [
            "ذاكرة الاستقبال (Receive Buffer) لدى المستقبل ممتلئة تماماً؛ ويجب على المرسل التوقف فوراً عن إرسال أي بيانات جديدة حتى وصول إشعار تحديث النافذة",
            "الكابل الفيزيائي انقطع وفشلت عملية الإرسال بالكامل",
            "عملية نقل الملف انتهت بنجاح وتمت كتابة كافة البيانات على القرص الصلب",
            "يجب على المرسل مضاعفة سرعة إرسال الحزم فوراً"
        ],
        "ans": 0,
        "exp_en": "A Window Size of 0 informs the sender that the receiver's receive buffer has reached capacity. The sender must stop transmitting data payload until the application drains the buffer and the receiver transmits a 'TCP Window Update' with an open window size.",
        "exp_ar": "حجم النافذة 0 يخبر المرسل بأن ذاكرة الاستقبال المؤقتة (Receive Buffer) لدى المستقبل امتلأت تماماً ولا تستوعب أي بايت إضافي. يتوقف المرسل مؤقتاً حتى يقوم تطبيق المستقبل بمعالجة البيانات وإرسال حزمة 'TCP Window Update' تفتح النافذة من جديد."
    },
    {
        "id": "mcq16",
        "lesson": "Lesson 07: TCP Window Size Scaling",
        "q_en": "What is 'TCP Global Synchronization', and how does Random Early Detection (RED) solve it?",
        "q_ar": "ما هي مشكلة 'المزامنة الشاملة لـ TCP' (Global Synchronization)، وكيف تحلها تقنية RED (الكشف المبكر العشوائي)؟",
        "opts_en": [
            "Tail drop causes all TCP connections to drop packets and shrink windows simultaneously; RED drops random packets early to desynchronize back-offs",
            "Routers lose clock synchronization; RED sends NTP timing pulses to all switches",
            "All hosts send ARP requests at the same second; RED caches MAC tables",
            "TCP sessions synchronize their sequence numbers; RED randomizes ISNs"
        ],
        "opts_ar": [
            "امتلاء طابور الراوتر (Tail Drop) يسقط حزم كل الاتصالات معاً فتنهار نوافذها لـ 1 في نفس اللحظة؛ وتقنية RED تسقط حزم عشوائية مبكراً لكسر هذا التزامن",
            "فقدان تزامن الساعات في الراوترات؛ وتقنية RED ترسل نبضات NTP لتصحيح الوقت",
            "إرسال كل الأجهزة لطلبات ARP في نفس الثانية؛ وتقنية RED توقف البث",
            "تطابق أرقام التسلسل في كل الاتصالات؛ وتقنية RED تجعلها أرقاماً عشوائية"
        ],
        "ans": 0,
        "exp_en": "When a congested queue hits 100% capacity (Tail Drop), multiple TCP connections experience dropped packets at once, causing all to drop window sizes to 1 and throttle throughput simultaneously. RED monitors queues and randomly drops individual packets before buffer overflow occurs, staggering the slow-start events and maintaining high link utilization.",
        "exp_ar": "عندما يمتلئ طابور الراوتر تماماً (Tail Drop)، تُفقد حزم من جميع اتصالات TCP في نفس اللحظة، فتدخل كلها في وضع Slow Start وينهار استخدام الخط. تقنية RED تسقط حزماً قليلة عشوائياً قبل امتلاء الطابور، مما يجعل الاتصالات تبطئ في أوقات متفرقة، فيظل الرابط مستغلاً بكفاءة."
    },
    {
        "id": "mcq17",
        "lesson": "Lesson 08: ICMP",
        "q_en": "What are the exact ICMP Type and Code numbers used by a standard ping utility for 'Echo Request' and 'Echo Reply'?",
        "q_ar": "ما هي أرقام النوع (Type) والرمز (Code) في بروتوكول ICMP لرسالتي طلب الرد (Echo Request) ورد الصدى (Echo Reply)؟",
        "opts_en": [
            "Echo Request = Type 8, Code 0; Echo Reply = Type 0, Code 0",
            "Echo Request = Type 0, Code 0; Echo Reply = Type 8, Code 0",
            "Echo Request = Type 3, Code 1; Echo Reply = Type 3, Code 3",
            "Echo Request = Type 11, Code 0; Echo Reply = Type 11, Code 1"
        ],
        "opts_ar": [
            "طلب الرد (Echo Request) = Type 8, Code 0؛ ورد الصدى (Echo Reply) = Type 0, Code 0",
            "طلب الرد (Echo Request) = Type 0, Code 0؛ ورد الصدى (Echo Reply) = Type 8, Code 0",
            "طلب الرد (Echo Request) = Type 3, Code 1؛ ورد الصدى (Echo Reply) = Type 3, Code 3",
            "طلب الرد (Echo Request) = Type 11, Code 0؛ ورد الصدى (Echo Reply) = Type 11, Code 1"
        ],
        "ans": 0,
        "exp_en": "An ICMP ping Echo Request is formatted with Type 8, Code 0. When the destination receives it, it replies with an ICMP Echo Reply formatted with Type 0, Code 0.",
        "exp_ar": "أداة ping ترسل طلب فحص الاتصال (Echo Request) بنوع Type 8 ورمز Code 0. وعندما يستلمها الجهاز المستهدف ويرد، يرسل رد الصدى (Echo Reply) بنوع Type 0 ورمز Code 0."
    },
    {
        "id": "mcq18",
        "lesson": "Lesson 08: ICMP",
        "q_en": "How does the 'traceroute' command discover the intermediate router IP addresses along an end-to-end network path?",
        "q_ar": "كيف تكتشف أداة 'traceroute' عناوين الراوترات الوسيطة على طول مسار الشبكة حتى الوجهة النهائية؟",
        "opts_en": [
            "Sends probes with progressively incrementing TTL values starting at 1, capturing ICMP Type 11 (Time Exceeded) replies from each hop",
            "Queries the central BGP route reflector for the path's autonomous systems",
            "Broadcasts ARP requests with a wildcard destination MAC address",
            "Sends SNMP trap messages to every router along the path"
        ],
        "opts_ar": [
            "ترسل حزم بقيم TTL تبدأ من 1 وتزيد تدريجياً، وتلتقط رسائل ICMP Type 11 (انتهت المهلة) الواردة من كل راوتر في الطريق",
            "تستعلم من سيرفرات BGP المركزية عن المسار الجغرافي للحزمة",
            "تبث رسائل ARP للشبكة بأكملها للتعرف على أجهزة التوجيه",
            "ترسل رسائل استعلام SNMP لجميع الراوترات في العالم"
        ],
        "ans": 0,
        "exp_en": "Traceroute sends packets with TTL=1. The first router decrements TTL to 0, drops it, and replies with ICMP Type 11 (Time Exceeded), exposing its IP. Traceroute then sends TTL=2, exposing the second router, and continues incrementing until reaching the destination.",
        "exp_ar": "ترسل أداة traceroute حزمة بـ TTL=1، فيقوم الراوتر الأول بإنقاصها لـ 0 وإسقاطها وإرسال رسالة ICMP Type 11 فينكشف عنوانه. ثم ترسل حزمة بـ TTL=2 ليكتشف الراوتر الثاني، وتستمر بزيادة TTL حتى تصل للوجهة."
    },
    {
        "id": "mcq19",
        "lesson": "Lesson 09: DNS",
        "q_en": "What is the crucial architectural difference between a 'Recursive DNS Resolver' and an 'Authoritative DNS Name Server'?",
        "q_ar": "ما هو الفرق الهيكلي الجوهري بين خادم DNS الاستدعائي (Recursive Resolver) وخادم DNS المخول (Authoritative Server)؟",
        "opts_en": [
            "A Recursive Resolver queries multiple servers on behalf of clients until finding the IP; an Authoritative Server holds the official database records for a specific zone",
            "An Authoritative Server queries the internet for users; a Recursive Resolver holds static IP addresses",
            "A Recursive Resolver is used only for IPv6; an Authoritative Server is only for IPv4",
            "There is no difference; they are synonymous terms for standard DNS servers"
        ],
        "opts_ar": [
            "الخادم الاستدعائي (Recursive) يتكفل بالبحث والتنقل بين السيرفرات نيابة عن المستخدم؛ بينما الخادم المخول (Authoritative) يمتلك السجلات الرسمية لنطاق معين",
            "الخادم المخول يبحث نيابة عن المستخدمين؛ بينما الخادم الاستدعائي يحتفظ بعناوين ثابتة",
            "الخادم الاستدعائي يعمل فقط مع IPv6؛ بينما الخادم المخول يعمل فقط مع IPv4",
            "لا يوجد أي فرق بينهما؛ كلاهما اسمان لنفس نوع السيرفر"
        ],
        "ans": 0,
        "exp_en": "A Recursive Resolver (like Google 8.8.8.8 or your ISP DNS) does the legwork: it receives a client query, traverses Root -> TLD -> Authoritative servers, and returns the final answer. An Authoritative Name Server is the definitive source that holds the actual DNS records for a domain (e.g. cisco.com).",
        "exp_ar": "الـ Recursive Resolver (مثل 8.8.8.8 أو سيرفر مزود الخدمة) يقوم برحلة البحث كاملة نيابة عن جهازك بسؤال سيرفرات الجذر ثم TLD ثم السيرفر المخول. بينما الـ Authoritative Server هو السيرفر الرسمي التابع لصاحب الموقع والذي يحتوي على سجلات الـ DNS الفعلية للنطاق."
    },
    {
        "id": "mcq20",
        "lesson": "Lesson 09: DNS",
        "q_en": "Which DNS resource record type maps a domain hostname to an IPv6 address, and which maps an alias to a canonical name?",
        "q_ar": "أي سجل من سجلات DNS يقوم بربط اسم النطاق بعنوان IPv6، وأيها يربط اسماً مستعاراً بالاسم الأصلي؟",
        "opts_en": [
            "AAAA maps to IPv6; CNAME maps an alias to a canonical name",
            "A maps to IPv6; PTR maps an alias to a canonical name",
            "MX maps to IPv6; TXT maps an alias to a canonical name",
            "NS maps to IPv6; SOA maps an alias to a canonical name"
        ],
        "opts_ar": [
            "سجل AAAA يربط بـ IPv6؛ وسجل CNAME يربط الاسم المستعار بالاسم الأصلي",
            "سجل A يربط بـ IPv6؛ وسجل PTR يربط الاسم المستعار بالاسم الأصلي",
            "سجل MX يربط بـ IPv6؛ وسجل TXT يربط الاسم المستعار بالاسم الأصلي",
            "سجل NS يربط بـ IPv6؛ وسجل SOA يربط الاسم المستعار بالاسم الأصلي"
        ],
        "ans": 0,
        "exp_en": "An 'A' record maps to an IPv4 address (32-bit). An 'AAAA' (Quad-A) record maps to a 128-bit IPv6 address. A 'CNAME' (Canonical Name) record creates an alias pointing one name to another (e.g. ftp.example.com -> www.example.com).",
        "exp_ar": "سجل A مخصص لعناوين IPv4 (32-bit). سجل AAAA مخصص لعناوين IPv6 (128-bit). سجل CNAME هو اسم مستعار يوجه اسماً معيناً إلى الاسم الحقيقي الأصلي (Canonical Name)."
    },
    {
        "id": "mcq21",
        "lesson": "Lesson 10: Cisco IOS CLI",
        "q_en": "What happens if a network administrator types configuration commands on a switch, makes changes, and reboots the switch WITHOUT saving?",
        "q_ar": "ماذا يحدث إذا قام مسؤول الشبكة بإجراء تعديلات وإعدادات على السويتش ثم أعاد تشغيله دون حفظ؟",
        "opts_en": [
            "All changes are permanently lost because 'running-config' is stored in volatile RAM",
            "The switch automatically saves the running-config into Flash memory prior to reboot",
            "The configuration is preserved in NVRAM by default",
            "The switch refuses to reload and displays an unrecoverable syntax error"
        ],
        "opts_ar": [
            "تضيع كافة التعديلات نهائياً لأن ملف 'running-config' مخزن في ذاكرة RAM المؤقتة",
            "يقوم السويتش تلقائياً بحفظ الإعدادات في ذاكرة Flash قبل إعادة التشغيل",
            "الإعدادات تظل محفوظة في ذاكرة NVRAM بشكل افتراضي",
            "يرفض السويتش إعادة التشغيل ويظهر خطأ برمجي يمنع الإغلاق"
        ],
        "ans": 0,
        "exp_en": "Active configuration changes take effect immediately in 'running-config', which resides in volatile RAM. If the device powers off or reloads before running 'copy running-config startup-config' (saving to NVRAM), all unsaved changes are lost.",
        "exp_ar": "التعديلات الحالية تطبق فوراً في ملف 'running-config' الموجود في ذاكرة RAM المؤقتة التي تفقد بياناتها عند انقطاع الكهرباء. إذا لم يقم المهندس بكتابة 'copy running-config startup-config' لحفظها في NVRAM، ستضيع كل التغييرات تماماً عند إعادة التشغيل."
    },
    {
        "id": "mcq22",
        "lesson": "Lesson 10: Cisco IOS CLI",
        "q_en": "Which key combination in Cisco IOS halts an active DNS lookup or aborts a runaway ping/traceroute command?",
        "q_ar": "ما هو اختصار لوحة المفاتيح في نظام سيسكو الذي يوقف عملية بحث DNS فاشلة أو يقطع أمر ping قيد التنفيذ فوراً؟",
        "opts_en": [
            "Ctrl + Shift + 6",
            "Ctrl + C",
            "Ctrl + Z",
            "Ctrl + Alt + Delete"
        ],
        "opts_ar": [
            "الضغط على Ctrl + Shift + 6 معاً",
            "الضغط على Ctrl + C",
            "الضغط على Ctrl + Z",
            "الضغط على Ctrl + Alt + Delete"
        ],
        "ans": 0,
        "exp_en": "Ctrl + Shift + 6 is the universal break sequence in Cisco IOS used to abort pings, traceroutes, or translation lookups when a mistyped command triggers an unintended broadcast domain lookup.",
        "exp_ar": "الضغط على الأزرار الثلاثة Ctrl + Shift + 6 معاً هو الاختصار القياسي في سيسكو لكسر وإيقاف أي عملية جارية فوراً مثل أمر ping أو محاولة بحث DNS المزعجة عند كتابة أمر بالخطأ."
    },
    {
        "id": "mcq23",
        "lesson": "Lesson 11: Security",
        "q_en": "A Cisco switch configuration has BOTH 'enable secret MySecret' and 'enable password MyPassword' configured. Which password is required to enter Privileged EXEC mode?",
        "q_ar": "سويتش سيسكو تم ضبط كلاً من 'enable secret MySecret' و 'enable password MyPassword' عليه. أي كلمة مرور سيطلبها الجهاز للدخول لوضع التمكين؟",
        "opts_en": [
            "Only 'MySecret'; Cisco IOS always prioritizes 'enable secret' and ignores 'enable password'",
            "Only 'MyPassword'; 'enable password' overrides secret commands",
            "Both passwords must be typed sequentially one after the other",
            "Neither; the device enters an error lockout state"
        ],
        "opts_ar": [
            "كلمة 'MySecret' فقط؛ لأن سيسكو تعطي الأولوية القصوى دائماً لـ 'enable secret' وتتجاهل الأخرى",
            "كلمة 'MyPassword' فقط؛ لأن أمر enable password يلغي الـ secret",
            "يجب كتابة الكلمتين معاً بالتتابع",
            "لا شيء منهما؛ يدخل الجهاز في حالة تعارض ويقفل الوصول"
        ],
        "ans": 0,
        "exp_en": "Cisco IOS always prioritizes 'enable secret' over 'enable password' because secrets use one-way cryptographic hashing instead of reversible encryption or clear text. 'enable password' is completely ignored.",
        "exp_ar": "نظام سيسكو يعطي الأولوية دائماً لأمر 'enable secret' على حساب 'enable password' لأن الأول يعتمد على التجزئة التشفيرية، ويتم إهمال 'enable password' تماماً طالما وُجد secret على الجهاز."
    },
    {
        "id": "mcq24",
        "lesson": "Lesson 11: Security",
        "q_en": "What type of encryption does the command 'service password-encryption' apply to passwords in Cisco configuration files, and what is its security limitation?",
        "q_ar": "ما نوع التشفير الذي يطبقه أمر 'service password-encryption' على كلمات المرور في ملف الإعدادات، وما هو عيبه الأمني؟",
        "opts_en": [
            "Type 7 encryption; it is an extremely weak XOR cipher that can be decrypted in milliseconds using freely available tools",
            "Type 5 encryption; it uses MD5 which is vulnerable to SHA collision attacks",
            "Type 8 encryption; it slows down router CPU performance during boot",
            "Type 9 encryption; it requires an expensive security license"
        ],
        "opts_ar": [
            "تشفير Type 7؛ وهو خوارزمية XOR ضعيفة جداً ومكشوفة يمكن فكها في أجزاء من الثانية بمواقع مجانية على الإنترنت",
            "تشفير Type 5؛ وهو يستخدم MD5 المعرض لهجمات التصادم",
            "تشفير Type 8؛ وهو يثقل على معالج الراوتر أثناء التشغيل",
            "تشفير Type 9؛ وهو يتطلب شراء رخصة أمنية باهظة الثمن"
        ],
        "ans": 0,
        "exp_en": "The 'service password-encryption' command applies Cisco Type 7 encoding. Type 7 uses a static key and simple XOR cipher published decades ago. Anyone with access to the config can decrypt it instantly. It only protects against casual shoulder-surfing, never against actual security attacks.",
        "exp_ar": "أمر 'service password-encryption' يطبق تشفير Type 7. وهو ليس تشفيراً حقيقياً بل تمويه بسيط (XOR) بمفتاح ثابت ومعروف منذ التسعينيات، ويمكن فكه في لحظة بمواقع مجانية. فائدته الوحيدة هي منع من يقف خلفك من قراءة الباسورد صراحة."
    },
    {
        "id": "mcq25",
        "lesson": "Lesson 11: Security",
        "q_en": "Which statement accurately describes the differences between TACACS+ and RADIUS protocols for network device administration?",
        "q_ar": "أي العبارات التالية تصف بدقة الفروق بين بروتوكولي TACACS+ و RADIUS لإدارة أجهزة الشبكة؟",
        "opts_en": [
            "TACACS+ uses TCP port 49, separates Authentication and Authorization, and encrypts the entire packet body; RADIUS uses UDP, combines Auth/Auth, and encrypts only the password",
            "RADIUS uses TCP port 49; TACACS+ uses UDP ports 1812 and 1813",
            "TACACS+ only encrypts the password; RADIUS encrypts the entire packet",
            "RADIUS separates Authentication and Authorization; TACACS+ combines them together"
        ],
        "opts_ar": [
            "بروتوكول TACACS+ يستخدم TCP منفذ 49 ويفصل المصادقة عن التخويل ويشفر كامل الحزمة؛ بينما RADIUS يستخدم UDP ويدمج المصادقة مع التخويل ويشفر كلمة المرور فقط",
            "بروتوكول RADIUS يستخدم TCP منفذ 49؛ بينما TACACS+ يستخدم UDP عبر منافذ 1812 و 1813",
            "بروتوكول TACACS+ يشفر كلمة المرور فقط؛ بينما RADIUS يشفر كامل الحزمة",
            "بروتوكول RADIUS يفصل بين المصادقة والتخويل؛ بينما TACACS+ يدمجهما معاً"
        ],
        "ans": 0,
        "exp_en": "TACACS+ is designed for device administration: it runs over reliable TCP port 49, strictly separates Authentication, Authorization (per-command authorization), and Accounting, and encrypts the entire packet payload. RADIUS uses UDP (1812/1813), combines Auth & Auth, and only encrypts the password field.",
        "exp_ar": "بروتوكول TACACS+ مخصص لإدارة الأجهزة: يعمل عبر TCP منفذ 49، ويفصل تماماً بين المصادقة والتخويل (مما يتيح تحديد الصلاحيات لكل أمر)، ويشفر كامل الحزمة. بينما RADIUS يعمل بـ UDP (1812/1813)، ويدمج المصادقة مع التخويل، ويشفر كلمة المرور فقط تاركاً باقي الحزمة مكشوفة."
    }
]

# 6 Real-World Scenarios & Troubleshooting Questions
scenarios = [
    {
        "id": "scen1",
        "title_en": "Scenario 1: Wireshark Handshake Capture Analysis",
        "title_ar": "سيناريو 1: تحليل لقطة حزم Wireshark لمصافحة TCP",
        "badge": "Wireshark & Layer 4",
        "context_en": "A network engineer captures a packet between client 192.168.1.50 (port 51234) and server 10.0.0.10 (port 443). The packet details show:<br><code>• Flags: 0x012 (SYN, ACK)<br>• Sequence Number: 0 (relative sequence number)<br>• Acknowledgment Number: 1 (relative)<br>• Window Size: 64240<br>• Options: Maximum Segment Size (MSS) 1460 bytes, Window Scale (ws=128)</code>",
        "context_ar": "التقط مهندس شبكات حزمة بين جهاز عميل 192.168.1.50 (منفذ 51234) وخادم 10.0.0.10 (منفذ 443). بيانات الحزمة في Wireshark أظهرت التالي:<br><code>• الأعلام (Flags): 0x012 (SYN, ACK)<br>• رقم التسلسل (Seq): 0 (رقم نسبي)<br>• رقم التأكيد (Ack): 1 (نسبي)<br>• حجم النافذة (Window Size): 64240<br>• الخيارات (Options): أقصى حجم للجزء (MSS) 1460 بايت، ومُعامل تكبير النافذة (Window Scale = 128)</code>",
        "q_en": "1) Which device sent this packet (client or server)?<br>2) Which step of the 3-way handshake is this?<br>3) What does Acknowledgement Number 1 signify to the receiver?<br>4) What is the true effective receive buffer size calculated with the Window Scale option?",
        "q_ar": "1) أي جهاز هو الذي أرسل هذه الحزمة (العميل أم الخادم)؟<br>2) في أي خطوة من خطوات المصافحة الثلاثية نحن الآن؟<br>3) ماذا يعني رقم التأكيد (Ack = 1) للطرف الآخر؟<br>4) ما هو حجم ذاكرة الاستقبال الفعلية الحقيقية بعد احتساب مُعامل التكبير (Window Scale)؟",
        "solution_en": "<b>Model Solution:</b><br>"
                       "1. <b>Sender:</b> The Server (10.0.0.10) sent this packet from source port 443 to client destination port 51234.<br>"
                       "2. <b>Handshake Stage:</b> Step 2 of the 3-Way Handshake (SYN-ACK). The server acknowledges the client's initial SYN and sends its own SYN.<br>"
                       "3. <b>Ack Number 1:</b> The client's initial relative sequence number was 0. The server increments it by 1 (Ack = 1) to indicate: <i>'I have successfully received your SYN (byte 0); I now expect you to send data starting at byte 1.'</i><br>"
                       "4. <b>Effective Window Size:</b> Window Size (64,240) x Window Scale Factor (128) = <b>8,222,720 bytes (~8.2 MB)</b>! The 16-bit window field alone is capped at 65,535 bytes; the scaling option enables gigabit line-rate throughput.",
        "solution_ar": "<b>الإجابة النموذجية:</b><br>"
                       "1. <b>الجهاز المرسل:</b> الخادم (10.0.0.10) أرسل الحزمة من منفذه 443 إلى منفذ العميل 51234.<br>"
                       "2. <b>مرحلة المصافحة:</b> الخطوة الثانية (SYN-ACK). الخادم يؤكد استلام طلب العميل ويرسل مزامنته الخاصة.<br>"
                       "3. <b>معنى Ack = 1:</b> العميل بدأ برقم تسلسلي نسبي 0، فيقوم الخادم بزيادته بمقدار 1 ليعني: <i>'لقد استلمت طلبك بنجاح، وأنا الآن أنتظر منك إرسال البيانات بدءاً من البايت رقم 1.'</i><br>"
                       "4. <b>حجم النافذة الفعلي:</b> حجم النافذة المسجل (64,240) × معامل التكبير (128) = <b>8,222,720 بايت (حوالي 8.2 ميجابايت)</b>! حقل النافذة الأصلي محدود بـ 65,535 بايت، وخيار Window Scale هو الذي يمكن الشبكات الحديثة من نقل بيانات ضخمة بسرعات الجيجابت."
    },
    {
        "id": "scen2",
        "title_en": "Scenario 2: The Console Lockout Incident",
        "title_ar": "سيناريو 2: حادثة القفل المفاجئ لمنفذ الكونسول",
        "badge": "Cisco CLI & Security",
        "context_en": "A junior administrator connects to a brand new Cisco Catalyst switch via console cable. Wanting to secure the switch, they execute the following commands in order:<br>"
                   "<code>Switch# configure terminal<br>Switch(config)# line console 0<br>Switch(config-line)# login local<br>Switch(config-line)# exit<br>Switch(config)# exit<br>Switch# exit</code><br>"
                   "When the administrator presses Enter to log back into the switch, the console displays:<br>"
                   "<code>User Access Verification<br>Username: </code><br>"
                   "However, every username and password combination the administrator enters is rejected.",
        "context_ar": "قام مهندس مبتدئ بالاتصال بسويتش سيسكو جديد عبر كابل الكونسول. وأراد تأمين الجهاز فنفذ الأوامر التالية بالترتيب:<br>"
                   "<code>Switch# configure terminal<br>Switch(config)# line console 0<br>Switch(config-line)# login local<br>Switch(config-line)# exit<br>Switch(config)# exit<br>Switch# exit</code><br>"
                   "عندما ضغط على زر Enter للدخول مجدداً، ظهرت له شاشة التحقق:<br>"
                   "<code>User Access Verification<br>Username: </code><br>"
                   "ولكن كلما كتب أي اسم مستخدم أو كلمة مرور، يتم رفضه ولا يستطيع الدخول نهائياً.",
        "q_en": "1) What critical configuration error did the administrator commit?<br>2) Why does the switch reject every login attempt?<br>3) What is the standard recovery procedure to regain access to the switch without erasing its configuration?",
        "q_ar": "1) ما هو الخطأ الإعدادي الفادح الذي ارتكبه المسؤول؟<br>2) لماذا يرفض السويتش أي محاولة تسجيل دخول؟<br>3) ما هي الطريقة القياسية (Password Recovery) لاستعادة السيطرة على السويتش دون مسح إعداداته؟",
        "solution_en": "<b>Model Solution:</b><br>"
                       "1. <b>The Error:</b> The administrator configured <code>login local</code> under <code>line console 0</code>, but <b>forgot to create any local user accounts</b> in global configuration mode (e.g. <code>username admin secret Cisco123</code>).<br>"
                       "2. <b>Why It Rejects:</b> <code>login local</code> instructs Cisco IOS to authenticate credentials against the device's local database. Because the local database is completely empty (0 users), no username can ever match, resulting in a total console lockout.<br>"
                       "3. <b>Recovery Procedure (Password Recovery):</b><br>"
                       "• Physically reboot the switch while holding down the <b>Mode</b> button on the front panel until the SYST LED flashes amber, entering the <b>bootloader / ROMmon</b> prompt (<code>switch:</code>).<br>"
                       "• Type <code>flash_init</code> to mount the flash memory file system.<br>"
                       "• Rename the startup configuration file to bypass it: <code>rename flash:config.text flash:config.backup</code>.<br>"
                       "• Type <code>boot</code> to load IOS without loading the locked configuration.<br>"
                       "• In Privileged EXEC mode, restore the config: <code>copy flash:config.backup running-config</code>.<br>"
                       "• Immediately configure a valid username and secret: <code>username admin privilege 15 secret CorrectPass123</code>.<br>"
                       "• Save the restored config: <code>copy running-config startup-config</code>.",
        "solution_ar": "<b>الإجابة النموذجية:</b><br>"
                       "1. <b>الخطأ المرتكب:</b> المسؤول قام بتفعيل أمر <code>login local</code> على خط الكونسول، لكنه <b>نسي إنشاء أي حساب مستخدم محلي</b> في وضع الإعداد العام (مثل <code>username admin secret Pass123</code>).<br>"
                       "2. <b>سبب الرفض:</b> أمر <code>login local</code> يجبر السويتش على مطابقة البيانات مع قاعدة المستخدمين المحلية. وبما أن قاعدة البيانات فارغة تماماً ولا تحتوي على أي مستخدم، فإنه يستحيل مطابقة أي حساب، مما يسبب قفلاً تاماً للجهاز.<br>"
                       "3. <b>طريقة استعادة الوصول (Password Recovery):</b><br>"
                       "• فصل الكهرباء عن السويتش وإعادة تشغيله مع الاستمرار في الضغط على زر <b>Mode</b> في واجهة الجهاز حتى تومض لمبة SYST باللون البرتقالي للدخول لوضع الـ <b>ROMmon</b> (الشاشة <code>switch:</code>).<br>"
                       "• كتابة أمر <code>flash_init</code> لتفعيل قراءة ذاكرة الفلاش.<br>"
                       "• إعادة تسمية ملف الإعدادات لتجاوزه عند الإقلاع: <code>rename flash:config.text flash:config.backup</code>.<br>"
                       "• تشغيل النظام بأمر <code>boot</code> ليدخل السويتش بدون أي باسورد.<br>"
                       "• استرجاع ملف الإعدادات في الـ RAM: <code>copy flash:config.backup running-config</code>.<br>"
                       "• إضافة مستخدم بصلاحيات كاملة فوراً: <code>username admin privilege 15 secret CorrectPass123</code>.<br>"
                       "• حفظ الإعدادات الصحيحة: <code>copy running-config startup-config</code>."
    },
    {
        "id": "scen3",
        "title_en": "Scenario 3: TCP Starvation by UDP Traffic",
        "title_ar": "سيناريو 3: حرمان اتصالات TCP بواسطة تدفقات UDP (Starvation)",
        "badge": "Traffic Flow & Congestion",
        "context_en": "A branch office connects to headquarters over a 20 Mbps WAN link. During business hours, employees conduct uncompressed video conference calls (UDP streams). Simultaneously, automated database replication transfers files over SFTP (TCP).<br>"
                   "Whenever video calls begin, the SFTP file transfer speed instantly plummets from 18 Mbps down to under 200 Kbps and frequently times out, whereas the video calls continue without interruption.",
        "context_ar": "فرع شركة متصل بالمقر الرئيسي عبر رابط WAN سرعته 20 ميجابت/ث. أثناء الدوام، يجري الموظفون مكالمات فيديو مباشرة (تستخدم تدفقات UDP). وفي نفس الوقت، يقوم خادم فرعي بمزامنة قواعد البيانات عبر بروتوكول SFTP (يعتمد على TCP).<br>"
                   "بمجرد بدء مكالمات الفيديو، تنهار سرعة نقل ملفات الـ SFTP فجأة من 18 ميجابت لتصبح أقل من 200 كيلوبت/ث وتفصل الجلسات باستمرار، بينما تستمر مكالمات الفيديو في العمل دون أي تأثر.",
        "q_en": "1) What networking phenomenon explains why TCP throughput collapses while UDP thrives?<br>2) Explain the behavioral difference between TCP and UDP during link congestion.<br>3) What Quality of Service (QoS) mechanism should the network engineer implement on the edge router to protect TCP while guaranteeing voice bandwidth?",
        "q_ar": "1) ما هي الظاهرة الشبكية التي تفسر انهيار سرعة TCP بينما يستمر UDP في العمل بكفاءة؟<br>2) اشرح الفرق في السلوك الداخلي بين TCP و UDP عند حدوث اختناق في الرابط (Congestion).<br>3) ما هي آلية جودة الخدمة (QoS) التي يجب على المهندس تطبيقها على راوتر الحافة لحماية TCP وتخصيص مسار محدد للصوت؟",
        "solution_en": "<b>Model Solution:</b><br>"
                       "1. <b>Phenomenon:</b> <b>TCP Starvation</b> caused by aggressive, unresponsive UDP traffic.<br>"
                       "2. <b>Behavioral Difference:</b><br>"
                       "• <b>TCP is 'Polite' (Congestion-Responsive):</b> When packets are dropped in the congested router buffer, TCP detects missing ACKs. Its congestion avoidance algorithms kick in: it slashes its Congestion Window (cwnd) to 1 segment (Slow Start) and throttles its transmission rate.<br>"
                       "• <b>UDP is 'Impolite' (Non-Responsive):</b> UDP has no windowing, acknowledgments, or flow control. It pumps packets at maximum rate regardless of network packet drops. As UDP fills the queues, TCP constantly backs off and yields bandwidth until it starves completely.<br>"
                       "3. <b>Solution:</b> Implement <b>QoS (Quality of Service) with Queuing / Rate Limiting (e.g. CBWFQ / LLQ / Policers)</b> on the edge router. Allocate a dedicated Priority Queue (PQ) capped at a strict bandwidth (e.g. 6 Mbps) for VoIP/Video, guaranteeing the remaining 14 Mbps for TCP data traffic.",
        "solution_ar": "<b>الإجابة النموذجية:</b><br>"
                       "1. <b>الظاهرة الشبكية:</b> ظاهرة <b>حرمان بروتوكول TCP (TCP Starvation)</b> بواسطة تدفقات UDP العنيفة.<br>"
                       "2. <b>الفرق في السلوك:</b><br>"
                       "• <b>بروتوكول TCP 'مهذب' ويتفاعل مع الازدحام:</b> عندما تمتلئ طوابير الراوتر وتسقط حزم، يلاحظ TCP عدم وصول الـ ACKs، فتعمل خوارزميات التحكم في الازدحام وتخفض حجم النافذة (cwnd) فوراً إلى 1 ويبطئ سرعته لتفادي إسقاط الشبكة.<br>"
                       "• <b>بروتوكول UDP 'غير مبالٍ':</b> لا يمتلك أي نظام تأكيد أو نوافذ، ويستمر في ضخ الحزم بأقصى طاقة بغض النظر عن فقدان الحزم. ونتيجة لذلك، يستحوذ UDP على كل سعة الرابط بينما يستمر TCP في التراجع حتى يموت الاتصال.<br>"
                       "3. <b>الحل الهندسي:</b> تفعيل آليات <b>جودة الخدمة (QoS) وتقسيم الطوابير (LLQ / CBWFQ)</b> على الراوتر. يتم تخصيص طابور أولوية محدد لسعة الفيديو والصوت (مثلاً بحد أقصى 6 ميجابت)، مع حجز وضمان باقي السعة (14 ميجابت) لبيانات TCP لحمايتها من الموت."
    },
    {
        "id": "scen4",
        "title_en": "Scenario 4: Subnetting Boundary Addressing Misconfiguration",
        "title_ar": "سيناريو 4: خطأ تقسيم الشبكات وعناوين البوابات الافتراضية",
        "badge": "IPv4 & Subnetting",
        "context_en": "A network engineer configures a new server with the following static parameters:<br>"
                   "<code>• Server IP: 192.168.1.190<br>• Subnet Mask: 255.255.255.224 (/27)<br>• Default Gateway: 192.168.1.193</code><br>"
                   "The server cannot reach the default gateway, cannot ping the Internet, and displays 'Network Unreachable'.",
        "context_ar": "قام مهندس شبكات بضبط خادم جديد بالإعدادات الثابتة التالية:<br>"
                   "<code>• عنوان الـ IP للخادم: 192.168.1.190<br>• قناع الشبكة: 255.255.255.224 (/27)<br>• البوابة الافتراضية (Default Gateway): 192.168.1.193</code><br>"
                   "الخادم غير قادر على عمل ping للبوابة الافتراضية أو الاتصال بالإنترنت ويعطي خطأ 'Network Unreachable'.",
        "q_en": "1) Calculate the subnet Network ID, usable host range, and Broadcast IP for the subnet containing the server (192.168.1.190 /27).<br>2) Which subnet does the Default Gateway (192.168.1.193 /27) reside in?<br>3) Why can Host A not communicate with its default gateway, and what is the fix?",
        "q_ar": "1) احسب معرف الشبكة، ونطاق العناوين الصالحة للأجهزة، وعنوان البث للشبكة التي يقع فيها الخادم (192.168.1.190 /27).<br>2) في أي شبكة فرعية تقع البوابة الافتراضية (192.168.1.193 /27)؟<br>3) لماذا يعجز الخادم عن التواصل مع بوابته الافتراضية، وما هو التعديل الصحيح للإعدادات؟",
        "solution_en": "<b>Model Solution:</b><br>"
                       "1. <b>Server Subnet Analysis (/27):</b><br>"
                       "• Subnet mask 255.255.255.224 leaves 5 host bits (32 - 27 = 5). Block size = 2^5 = 32.<br>"
                       "• Subnet multiples in the 4th octet: 0, 32, 64, 96, 128, 160, 192.<br>"
                       "• Since .190 is between 160 and 191:<br>"
                       "  - <b>Network ID:</b> 192.168.1.160<br>"
                       "  - <b>Usable Host Range:</b> 192.168.1.161 - 192.168.1.190<br>"
                       "  - <b>Broadcast IP:</b> 192.168.1.191<br>"
                       "2. <b>Gateway Subnet:</b> 192.168.1.193 belongs to the <b>next subnet (192.168.1.192 /27)</b>, where usable hosts are 192.168.1.193 to 192.168.1.222.<br>"
                       "3. <b>The Problem & Fix:</b> A default gateway <b>MUST reside in the EXACT SAME local subnet</b> as the host. The server (in .160/27) treats the gateway (.193 in .192/27) as an off-subnet remote IP, which it cannot reach without already having a working gateway. <b>Fix:</b> Assign the server a valid gateway inside 192.168.1.160/27 (e.g. 192.168.1.161), OR move the server's IP into 192.168.1.192/27 (e.g. 192.168.1.194 /27).",
        "solution_ar": "<b>الإجابة النموذجية:</b><br>"
                       "1. <b>تحليل شبكة الخادم (/27):</b><br>"
                       "• قناع 255.255.255.224 يترك 5 بت للأجهزة (32 - 27 = 5). حجم الكتلة (القفزة) = 2^5 = 32.<br>"
                       "• بدايات الشبكات في البايت الرابع: 0، 32، 64، 96، 128، 160، 192.<br>"
                       "• بما أن عنوان الخادم هو 190، فإنه يقع بين 160 و 191:<br>"
                       "  - <b>معرف الشبكة (Network ID):</b> 192.168.1.160<br>"
                       "  - <b>نطاق الأجهزة الصالحة:</b> من 192.168.1.161 إلى 192.168.1.190<br>"
                       "  - <b>عنوان البث (Broadcast):</b> 192.168.1.191<br>"
                       "2. <b>شبكة البوابة الافتراضية:</b> العنوان 192.168.1.193 يقع في <b>الشبكة التالية (192.168.1.192 /27)</b> التي أجهزتها من 193 إلى 222.<br>"
                       "3. <b>المشكلة والحل:</b> البوابة الافتراضية (Default Gateway) <b>يجب أن تكون في نفس الشبكة الفرعية المحلية للجهاز</b>. الخادم يعتبر 193 عنواناً خارجياً يحتاج راوتر للوصول إليه ولا يستطيع إرسال ARP له مباشرة. <b>الحل:</b> تغيير البوابة الافتراضية لتكون عنوان راوتر داخل شبكة الخادم (مثلاً 192.168.1.161)، أو نقل عنوان الخادم نفسه إلى الشبكة التالية (مثلاً 192.168.1.194 /27)."
    },
    {
        "id": "scen5",
        "title_en": "Scenario 5: Traceroute Asterisks ('* * *') Troubleshooting",
        "title_ar": "سيناريو 5: تشخيص وفهم النجوم '* * *' في أداة Traceroute",
        "badge": "ICMP & Path Diagnostics",
        "context_en": "A network administrator runs <code>traceroute 8.8.8.8</code> from a corporate workstation. The terminal displays the following output:<br>"
                   "<code>1  192.168.1.1   1.2 ms  1.1 ms  1.0 ms<br>"
                   "2  10.50.0.1    4.5 ms  4.3 ms  4.6 ms<br>"
                   "3  172.16.10.2  12.1 ms 11.9 ms 12.0 ms<br>"
                   "4  * * *<br>"
                   "5  * * *<br>"
                   "6  8.8.8.8      18.4 ms 18.2 ms 18.5 ms</code>",
        "context_ar": "قام مسؤول الشبكة بتنفيذ أمر <code>traceroute 8.8.8.8</code> من جهازه في الشركة، وظهرت له النتيجة التالية:<br>"
                   "<code>1  192.168.1.1   1.2 ms  1.1 ms  1.0 ms<br>"
                   "2  10.50.0.1    4.5 ms  4.3 ms  4.6 ms<br>"
                   "3  172.16.10.2  12.1 ms 11.9 ms 12.0 ms<br>"
                   "4  * * *<br>"
                   "5  * * *<br>"
                   "6  8.8.8.8      18.4 ms 18.2 ms 18.5 ms</code>",
        "q_en": "1) Does this output indicate an active network outage or broken connection to 8.8.8.8?<br>2) Why did hops 4 and 5 display asterisks (* * *) instead of IP addresses and response times?<br>3) What ICMP message type and code are intermediate routers expected to generate during traceroute?",
        "q_ar": "1) هل تدل هذه النتيجة على وجود عطل في الشبكة أو انقطاع في الاتصال بالوجهة 8.8.8.8؟<br>2) لماذا أظهرت المحطتان 4 و 5 نجوماً (* * *) بدلاً من إظهار عناوين الـ IP وزمن الاستجابة؟<br>3) ما هو نوع ورمز رسالة ICMP التي كان يُفترض أن يرسلها هذان الراوتران لأداة traceroute؟",
        "solution_en": "<b>Model Solution:</b><br>"
                       "1. <b>Outage Assessment:</b> <b>NO outage!</b> The destination <code>8.8.8.8</code> was successfully reached at hop 6 in 18.4 ms with zero packet loss.<br>"
                       "2. <b>Why Asterisks Appear:</b> The routers at hops 4 and 5 (or their edge firewalls) are configured to <b>suppress or filter outgoing ICMP Time Exceeded messages</b> (often due to security policies or Control Plane Policing to save CPU). When traceroute sends probe packets with TTL=4 and TTL=5, the routers drop the packets at TTL=0 but do not send the ICMP reply back. The traceroute utility waits, times out, and prints <code>* * *</code>.<br>"
                       "3. <b>Expected ICMP Message:</b> Routers along the path are expected to generate <b>ICMP Type 11, Code 0 (Time Exceeded in Transit)</b>.",
        "solution_ar": "<b>الإجابة النموذجية:</b><br>"
                       "1. <b>تقييم الاتصال:</b> <b>لا يوجد أي عطل!</b> تم الوصول بنجاح للوجهة النهائية <code>8.8.8.8</code> عند القفزة رقم 6 بزمن استجابة ممتاز (18.4 ميلي ثانية) وبدون أي فقد في الحزم.<br>"
                       "2. <b>سبب ظهور النجوم (* * *):</b> الراوترات في المحطتين 4 و 5 (أو جدران الحماية التابعة لها) مبرمجة على <b>حظر أو تجاهل إرسال رسائل ICMP</b> لحماية معالجاتها من الضغط (Control Plane Policing) أو لدواعي أمنية لمنع اكتشاف هيكل شبكتها الداخلية. الراوتر يستلم الحزمة ويسقطها لانتهاء الـ TTL، لكنه لا يرسل رداً، فينتظر البرنامج حتى تنتهي مهلة الاستجابة ويطبع النجوم.<br>"
                       "3. <b>رسالة ICMP المتوقعة:</b> كان من المفترض أن يرسل الراوتر رسالة <b>ICMP Type 11 Code 0 (Time-to-Live Exceeded in Transit)</b>."
    },
    {
        "id": "scen6",
        "title_en": "Scenario 6: Hardening Cisco VTY Lines from Telnet to SSH",
        "title_ar": "سيناريو 6: تحصين خطوط VTY في سيسكو ومنع بروتوكول Telnet",
        "badge": "Cisco IOS Security Hardening",
        "context_en": "A penetration tester attaches a laptop to an office switch port and runs Wireshark. When an admin logs in remotely to configure the switch, the tester captures the complete username and password in clear plain text.<br>"
                   "The security audit reveals that remote management is running over Telnet on VTY lines 0 through 15 with a generic password.",
        "context_ar": "قام خبير اختبار اختراق بتوصيل جهازه بمنفذ في السويتش وشغل Wireshark. وعندما قام الأدمن بالدخول عن بعد لإعداد السويتش، التقط المختبر اسم المستخدم وباسورد الـ enable بنص صريح وواضح تماماً.<br>"
                   "كشف التقرير الأمني أن خطوط الإدارة عن بعد (VTY lines 0-15) مفعلة ببروتوكول Telnet وتستخدم كلمة مرور مشتركة بسيطة.",
        "q_en": "Provide the complete, step-by-step Cisco IOS CLI configuration commands required to:<br>"
               "1) Configure a secure hostname and IP domain name.<br>"
               "2) Generate a strong 2048-bit RSA encryption key.<br>"
               "3) Enforce modern SSH version 2.<br>"
               "4) Create an administrator username with a Type 8 SHA-256 secret.<br>"
               "5) Configure VTY lines 0-15 to disable Telnet entirely and enforce local authentication.",
        "q_ar": "اكتب أوامر الـ CLI الكاملة والمضبوطة خطوة بخطوة في سيسكو لتنفيذ الآتي:<br>"
               "1) ضبط اسم للجهاز (Hostname) واسم نطاق محلي (Domain name).<br>"
               "2) توليد مفتاح تشفير RSA قوي بحجم 2048 بت.<br>"
               "3) فرض استخدام الإصدار الثاني الآمن من SSH (SSH version 2).<br>"
               "4) إنشاء حساب أدمن محلي محمي بتجزئة Type 8 (SHA-256).<br>"
               "5) ضبط خطوط VTY من 0 إلى 15 لمنع Telnet نهائياً وإلزام استخدام الحسابات المحلية المشفرة.",
        "solution_en": "<b>Model Solution:</b><br>"
                       "<code>Switch# configure terminal<br>"
                       "! 1. Hostname and Domain Name<br>"
                       "Switch(config)# hostname SW-CORE-01<br>"
                       "SW-CORE-01(config)# ip domain-name company.corp<br><br>"
                       "! 2 & 3. 2048-bit RSA Key and SSH Version 2<br>"
                       "SW-CORE-01(config)# crypto key generate rsa modulus 2048<br>"
                       "SW-CORE-01(config)# ip ssh version 2<br><br>"
                       "! 4. Local User Account with Type 8 Secret<br>"
                       "SW-CORE-01(config)# username secadmin privilege 15 algorithm-type sha256 secret ComplexP@ssw0rd!2026<br><br>"
                       "! 5. Hardening VTY Lines (Block Telnet, Force SSH & Local Auth)<br>"
                       "SW-CORE-01(config)# line vty 0 15<br>"
                       "SW-CORE-01(config-line)# transport input ssh<br>"
                       "SW-CORE-01(config-line)# login local<br>"
                       "SW-CORE-01(config-line)# exit<br>"
                       "SW-CORE-01(config)# service password-encryption<br>"
                       "SW-CORE-01(config)# do copy running-config startup-config</code>",
        "solution_ar": "<b>الإجابة النموذجية:</b><br>"
                       "<code>Switch# configure terminal<br>"
                       "! 1. ضبط اسم السويتش واسم النطاق (مطلوبان لتوليد المفاتيح)<br>"
                       "Switch(config)# hostname SW-CORE-01<br>"
                       "SW-CORE-01(config)# ip domain-name company.corp<br><br>"
                       "! 2 و 3. توليد مفتاح RSA بقوة 2048 بت وفرض SSHv2<br>"
                       "SW-CORE-01(config)# crypto key generate rsa modulus 2048<br>"
                       "SW-CORE-01(config)# ip ssh version 2<br><br>"
                       "! 4. إنشاء حساب محلي بصلاحيات كاملة وتجزئة Type 8 المشفرة بـ SHA-256<br>"
                       "SW-CORE-01(config)# username secadmin privilege 15 algorithm-type sha256 secret ComplexP@ssw0rd!2026<br><br>"
                       "! 5. تحصين خطوط VTY (حظر Telnet وفرض SSH والمصادقة المحلية)<br>"
                       "SW-CORE-01(config)# line vty 0 15<br>"
                       "SW-CORE-01(config-line)# transport input ssh<br>"
                       "SW-CORE-01(config-line)# login local<br>"
                       "SW-CORE-01(config-line)# exit<br>"
                       "SW-CORE-01(config)# service password-encryption<br>"
                       "SW-CORE-01(config)# do copy running-config startup-config</code>"
    }
]

# 5 Deep-Dive Conceptual Essay Questions with Detailed Model Answers
essays = [
    {
        "id": "essay1",
        "title_en": "Essay 1: The Complete Journey of a Web Request Across All 7 OSI Layers",
        "title_ar": "سؤال مقالي 1: الرحلة الكاملة لطلب صفحة ويب عبر طبقات OSI السبع",
        "badge": "Comprehensive Architecture & Protocols",
        "prompt_en": "Trace in granular, step-by-step detail what happens across the entire network protocol stack when an employee sits at a newly booted PC on a corporate LAN, opens a web browser, and navigates to <code>http://www.cisco.com</code>.<br><br>"
                     "Your explanation must detail:<br>"
                     "1. The local gateway resolution (ARP).<br>"
                     "2. The DNS resolution process from client to recursive resolver to authoritative servers.<br>"
                     "3. The TCP transport connection establishment (3-way handshake, ISNs, ports).<br>"
                     "4. The HTTP Application request and encapsulation/de-encapsulation transitions as the frame traverses a local switch and a default gateway router.",
        "prompt_ar": "تتبع بالتفصيل الدقيق خطوة بخطوة ما يحدث عبر طبقات الشبكة عندما يجلس موظف أمام جهاز كمبيوتر تم تشغيله للتو على شبكة محلية (LAN)، ويفتح المتصفح ويكتب <code>http://www.cisco.com</code>.<br><br>"
                     "يجب أن تتضمن إجابتك الشاملة:<br>"
                     "1. آلية اكتشاف البوابة الافتراضية عبر بروتوكول ARP.<br>"
                     "2. رحلة استعلام DNS من جهاز العميل إلى السيرفر الاستدعائي وحتى السيرفر المخول.<br>"
                     "3. مرحلة تأسيس اتصال الـ TCP (المصافحة الثلاثية والمنافذ وأرقام التسلسل).<br>"
                     "4. إرسال طلب HTTP وتفاصيل عمليتي التغليف (Encapsulation) وفك التغليف (De-encapsulation) أثناء مرور الإطار عبر السويتش والراوتر.",
        "model_en": "<b>Comprehensive Model Answer:</b><br><br>"
                    "<b>Phase 1: DNS Resolution (Resolving www.cisco.com):</b><br>"
                    "1. The browser checks its internal DNS cache and OS cache. Finding nothing, it prepares a DNS query for <code>www.cisco.com</code> (Type A record).<br>"
                    "2. The OS encapsulates the DNS query into a UDP segment (Destination Port 53, ephemeral source port like 54321), then into an IPv4 packet with Destination IP = configured DNS server (e.g., <code>8.8.8.8</code>).<br>"
                    "3. To send this packet out of the local subnet, the host checks its routing table: <code>8.8.8.8</code> is on an external network, so it must be forwarded to the <b>Default Gateway (Router)</b>.<br><br>"
                    "<b>Phase 2: Layer 2 ARP Resolution for the Gateway:</b><br>"
                    "4. The PC checks its local ARP cache for the default gateway's MAC address. Since it was just booted, the cache is empty.<br>"
                    "5. The PC broadcasts an <b>ARP Request</b> (Destination MAC: <code>FF:FF:FF:FF:FF:FF</code>) asking: <i>'Who has 192.168.1.1? Tell 192.168.1.100'</i>.<br>"
                    "6. The local switch floods the broadcast frame out all ports. The router receives it and responds with a unicast <b>ARP Reply</b> containing its physical MAC address.<br>"
                    "7. The PC stores the router's MAC in its ARP table, encapsulates the DNS IP packet into an Ethernet frame with Dest MAC = Router's MAC, and transmits it.<br><br>"
                    "<b>Phase 3: The Recursive DNS Lookup Journey:</b><br>"
                    "8. The DNS recursive resolver receives the query. If not cached, it queries a <b>Root Name Server</b> (which refers it to the <code>.com</code> TLD servers).<br>"
                    "9. The resolver queries the <code>.com</code> TLD server, which returns the NS records for <code>cisco.com</code>.<br>"
                    "10. The resolver queries Cisco's <b>Authoritative DNS Server</b>, which returns the A record (e.g., <code>72.163.4.161</code>).<br>"
                    "11. The resolver caches the record and returns the IP address to the PC.<br><br>"
                    "<b>Phase 4: TCP Three-Way Handshake:</b><br>"
                    "12. The PC's browser initiates a Layer 4 connection to <code>72.163.4.161</code> on Port 80 (HTTP).<br>"
                    "13. <b>SYN:</b> PC generates a random Initial Sequence Number (ISN_client) and transmits a TCP SYN packet.<br>"
                    "14. <b>SYN-ACK:</b> Cisco's web server responds with its own ISN_server and Ack = ISN_client + 1.<br>"
                    "15. <b>ACK:</b> PC acknowledges with Ack = ISN_server + 1. The socket connection enters the ESTABLISHED state.<br><br>"
                    "<b>Phase 5: HTTP Request & Router Forwarding:</b><br>"
                    "16. The browser issues an <code>HTTP GET / HTTP/1.1</code> request.<br>"
                    "17. Layer 4 encapsulates it into a TCP segment with flags PSH and ACK.<br>"
                    "18. Layer 3 encapsulates it into an IPv4 packet with Source IP = 192.168.1.100, Dest IP = 72.163.4.161, TTL = 128.<br>"
                    "19. Layer 2 encapsulates it into an Ethernet frame with Dest MAC = Gateway Router MAC.<br>"
                    "20. <b>Router Processing:</b> The router de-encapsulates Layer 2, verifies the FCS, decrements TTL by 1, consults its IP routing table, encapsulates the packet into a new Layer 2 frame appropriate for the WAN link, and forwards it to the next hop ISP router until it reaches Cisco's web server.",
        "model_ar": "<b>الإجابة النموذجية الشاملة:</b><br><br>"
                    "<b>المرحلة الأولى: استعلام الـ DNS لمعرفة IP الموقع:</b><br>"
                    "1. يتحقق المتصفح من الذاكرة المؤقتة، ولأنه لا يجد شيئاً يجهز استعلام DNS للبحث عن سجل A لنطاق <code>www.cisco.com</code>.<br>"
                    "2. يغلف نظام التشغيل الاستعلام داخل حزمة UDP (منفذ الوجهة 53، ومنفذ عشوائي للمصدر)، ثم داخل حزمة IPv4 موجهة لعنوان خادم الـ DNS (مثلاً <code>8.8.8.8</code>).<br>"
                    "3. يفحص الجهاز جدول التوجيه: بما أن 8.8.8.8 في شبكة خارجية، يجب إرسال الحزمة إلى <b>البوابة الافتراضية (الراوتر)</b>.<br><br>"
                    "<b>المرحلة الثانية: اكتشاف ماك الراوتر عبر بروتوكول ARP:</b><br>"
                    "4. يبحث الجهاز في كاش الـ ARP عن عنوان الـ MAC للراوتر، ولأن الجهاز تم تشغيله للتو، فالجدول فارغ.<br>"
                    "5. يرسل الجهاز إطار <b>ARP Request</b> كبث عام (Dest MAC: <code>FF:FF:FF:FF:FF:FF</code>) يسأل فيه: <i>'من يمتلك 192.168.1.1؟ أخبر 192.168.1.100'</i>.<br>"
                    "6. يمرر السويتش البث لجميع المنافذ، ويستلمه الراوتر ويرد بـ <b>ARP Reply</b> أحادي (Unicast) يحتوي على عنوان الـ MAC الفيزيائي لمنفذه.<br>"
                    "7. يحفظ الجهاز ماك الراوتر في جدول الـ ARP، ويغلف حزمة استعلام الـ DNS داخل إطار إيثرنت متجهاً لماك الراوتر.<br><br>"
                    "<b>المرحلة الثالثة: رحلة خادم الـ DNS الاستدعائي:</b><br>"
                    "8. يستلم خادم الـ DNS الاستدعائي الطلب ويسأل أحد <b>سيرفرات الجذر (Root Servers)</b>، والتي تدله على سيرفرات النطاق الأعلى <code>.com</code>.<br>"
                    "9. يسأل سيرفر الـ <code>.com</code>، فيدله على خوادم أسماء سيسكو المخولة.<br>"
                    "10. يسأل <b>الخادم المخول لسيسكو (Authoritative DNS)</b>، فيحصل على الـ IP الفعلي للموقع (مثلاً <code>72.163.4.161</code>).<br>"
                    "11. يعيد السيرفر العنوان إلى جهاز الموظف ليتم حفظه بالكاش.<br><br>"
                    "<b>المرحلة الرابعة: المصافحة الثلاثية لـ TCP (Three-Way Handshake):</b><br>"
                    "12. يبدأ المتصفح اتصال طبقة النقل مع IP الموقع على منفذ الويب 80.<br>"
                    "13. <b>SYN:</b> يرسل العميل حزمة مزامنة برقم تسلسلي أولي عشوائي (ISN).<br>"
                    "14. <b>SYN-ACK:</b> يرد سيرفر سيسكو بتأكيد استلام رقم العميل وإرسال رقمه الأولي الخاص.<br>"
                    "15. <b>ACK:</b> يؤكد العميل استلام رقم السيرفر، ويصبح الاتصال مؤكداً وجاهزاً لتبادل البيانات.<br><br>"
                    "<b>المرحلة الخامسة: إرسال طلب الويب ومعالجة الراوتر:</b><br>"
                    "16. يرسل المتصفح طلب <code>HTTP GET /</code>.<br>"
                    "17. الطبقة 4 تغلف الطلب كـ TCP Segment بعلمي PSH و ACK.<br>"
                    "18. الطبقة 3 تغلفه كـ IPv4 Packet مع تقليل TTL وتحديد عناوين IP المصدر والوجهة.<br>"
                    "19. الطبقة 2 تغلفه كـ Ethernet Frame متجهاً لعنوان MAC الخاص بالراوتر.<br>"
                    "20. <b>دور الراوتر:</b> يفك الراوتر ترويسة الطبقة 2، ويفحص ذيل التدقيق FCS، وينقص قيمة TTL بمقدار 1، ويبحث في جدول التوجيه، ثم يعيد تغليف الحزمة في إطار طبقة ثانية جديد يناسب رابط الـ WAN ليمرره للراوتر التالي حتى يصل لسيرفر سيسكو."
    },
    {
        "id": "essay2",
        "title_en": "Essay 2: Flow Control vs Congestion Control & Global Synchronization",
        "title_ar": "سؤال مقالي 2: المقارنة بين التحكم بالتدفق والتحكم بالازدحام وظاهرة المزامنة الشاملة",
        "badge": "TCP Mechanisms & Flow Control",
        "prompt_en": "Explain the architectural difference between <b>Flow Control</b> and <b>Congestion Control</b> in TCP.<br><br>"
                     "In your essay, address:<br>"
                     "1. The role of the Receive Window (rwnd) versus the Congestion Window (cwnd).<br>"
                     "2. How the Slow Start and Congestion Avoidance algorithms operate.<br>"
                     "3. How router Tail Drop causes TCP Global Synchronization, and the exact mathematical and queuing mechanisms used by Random Early Detection (RED) and Weighted RED (WRED) to resolve it.",
        "prompt_ar": "اشرح الفرق المعماري الدقيق بين <b>التحكم في التدفق (Flow Control)</b> و<b>التحكم في الازدحام (Congestion Control)</b> في بروتوكول TCP.<br><br>"
                     "يجب أن تتناول في مقالك:<br>"
                     "1. دور نافذة الاستقبال (rwnd) مقارنة بنافذة الازدحام (cwnd).<br>"
                     "2. آلية عمل خوارزميتي البداية البطيئة (Slow Start) وتفادي الازدحام (Congestion Avoidance).<br>"
                     "3. كيف يتسبب إسقاط الحزم التقليدي (Tail Drop) في حدوث المزامنة الشاملة (Global Synchronization)، وكيف تحلها تقنيتا RED و WRED.",
        "model_en": "<b>Comprehensive Model Answer:</b><br><br>"
                    "<b>1. Flow Control vs Congestion Control:</b><br>"
                    "• <b>Flow Control (End-to-End):</b> Protects the <i>receiving host</i> from being overwhelmed by a sender that transmits faster than the receiver's application can read from its receive buffer. It is governed by the <b>Receive Window (rwnd)</b> advertised in the TCP header by the receiver.<br>"
                    "• <b>Congestion Control (Network-Wide):</b> Protects the <i>underlying network transit path</i> (routers, switches, links) from buffer saturation and packet loss. It is governed by the <b>Congestion Window (cwnd)</b>, maintained privately by the sender based on packet loss and round-trip time.<br>"
                    "• <b>Effective Window Rule:</b> The sender can never transmit more than <code>min(rwnd, cwnd)</code> in flight without acknowledgment.<br><br>"
                    "<b>2. Slow Start and Congestion Avoidance:</b><br>"
                    "• <b>Slow Start:</b> Starts with a small cwnd (typically 1 to 10 segments). For every ACK received, cwnd increases by 1 MSS, effectively <b>doubling exponentially</b> every round-trip time (1 -> 2 -> 4 -> 8 -> 16). This continues until reaching the Slow Start Threshold (ssthresh).<br>"
                    "• <b>Congestion Avoidance:</b> Once cwnd reaches ssthresh, growth switches from exponential to <b>linear</b> (additive increase: +1 MSS per RTT) to probe for bandwidth cautiously.<br>"
                    "• <b>Loss Recovery:</b> When a packet drop occurs (timeout), ssthresh is cut to half of current cwnd, and cwnd resets to 1 segment (in classic TCP Reno/Tahoe), collapsing transmission throughput.<br><br>"
                    "<b>3. Global Synchronization & RED/WRED:</b><br>"
                    "• <b>Tail Drop:</b> By default, routers queue packets until the buffer is 100% full. Once full, all subsequent incoming packets are dropped ('tail dropped').<br>"
                    "• <b>Global Synchronization:</b> When tail drop happens on a congested interface, packets from dozens or hundreds of concurrent TCP connections are dropped at the exact same moment. Consequently, all connections drop their windows to 1 simultaneously, causing bandwidth utilization to plummet. Then, all connections ramp up together, causing another collision, repeating a jagged 'sawtooth' pattern with very poor average throughput.<br>"
                    "• <b>Random Early Detection (RED):</b> Monitors average queue depth. When buffer utilization crosses a minimum threshold, RED starts dropping random packets at a probabilistic rate before the queue fills up. The affected flows throttle back individually, desynchronizing the back-off events and keeping average link utilization consistently high.<br>"
                    "• <b>Weighted RED (WRED):</b> Cisco's enhancement that factors in QoS priority (IP Precedence / DSCP). Lower-priority packets are dropped earlier, ensuring mission-critical enterprise traffic is protected.",
        "model_ar": "<b>الإجابة النموذجية الشاملة:</b><br><br>"
                    "<b>1. التحكم في التدفق مقابل التحكم في الازدحام:</b><br>"
                    "• <b>التحكم في التدفق (Flow Control):</b> هدفه حماية <i>الجهاز المستقبل</i> من الغرق بالبيانات إذا كان المرسل أسرع من قدرة تطبيق المستقبل على المعالجة. ويتحكم به حجم <b>نافذة الاستقبال (rwnd)</b> التي يعلنها المستقبل في هيدر TCP.<br>"
                    "• <b>التحكم في الازدحام (Congestion Control):</b> هدفه حماية <i>مسار الشبكة والراوترات</i> من امتلاء الطوابير وفقدان الحزم. ويتحكم به حجم <b>نافذة الازدحام (cwnd)</b> التي يحسبها المرسل داخلياً بناءً على فقدان الحزم وزمن الاستجابة.<br>"
                    "• <b>القاعدة الذهبية:</b> كمية البيانات المسموح للمرسل بضخها على السلك لا تتجاوز القيمة الأصغر بينهما: <code>min(rwnd, cwnd)</code>.<br><br>"
                    "<b>2. البداية البطيئة وتفادي الازدحام:</b><br>"
                    "• <b>البداية البطيئة (Slow Start):</b> يبدأ الاتصال بنافذة صغيرة (مثلاً جزء واحد)، ومع كل ACK مستلم تتضاعف النافذة بشكل أسي (1 -> 2 -> 4 -> 8 -> 16) حتى تصل إلى حد معين يُسمى (ssthresh).<br>"
                    "• <b>تفادي الازدحام (Congestion Avoidance):</b> بعد تخطي ssthresh، يتحول النمو من أسي إلى خطي (+1 مع كل دورة RTT) لاختبار أقصى سعة للرابط بحذر.<br>"
                    "• <b>عند فقدان حزمة (Drop):</b> ينخفض حد ssthresh إلى نصف الحجم الحالي، ويعود حجم النافذة cwnd إلى 1 جزء مما يسبب انهياراً مؤقتاً في سرعة النقل.<br><br>"
                    "<b>3. المزامنة الشاملة ودور تقنيات RED و WRED:</b><br>"
                    "• <b>إسقاط الذيل (Tail Drop):</b> الوضع الافتراضي في الراوتر هو استقبال الحزم حتى يمتلئ طابور الانتظار بنسبة 100%، وعندها تسقط أي حزمة جديدة تصل.<br>"
                    "• <b>المزامنة الشاملة (Global Synchronization):</b> عند امتلاء الطابور، تسقط حزم من عشرات اتصالات TCP في نفس الثانية. وبما أن بروتوكول TCP مهذب، تنهار نوافذ كل الاتصالات إلى 1 معاً في نفس اللحظة! ويهبط استخدام الخط للصفر، ثم تبدأ كلها في التسارع معاً فيمتلئ الطابور مجدداً وتتكرر المشكلة في شكل موجات سن المنشار (Sawtooth) دون استغلال كامل لسعة الرابط.<br>"
                    "• <b>الحل بـ RED:</b> يراقب الراوتر متوسط امتلاء الطابور، ويبدأ في إسقاط حزم عشوائية بنسبة مئوية بسيطة قبل امتلاء الطابور. فتبطئ بعض الاتصالات بينما تستمر الأخرى، مما يكسر التزامن ويحافظ على استقرار تدفق البيانات بأعلى كفاءة.<br>"
                    "• <b>تقنية WRED من سيسكو:</b> تقوم بنفس الدور ولكنها تفاضل بين الحزم بناءً على أولويات QoS (مثل علامات DSCP)، فتسقط حزم البيانات العادية أولاً وتحافظ على حزم البيانات الحساسة."
    },
    {
        "id": "essay3",
        "title_en": "Essay 3: Cryptographic Evolution of Cisco Passwords (Type 0 to Type 9)",
        "title_ar": "سؤال مقالي 3: التطور التشفيري لكلمات مرور سيسكو من النوع 0 إلى النوع 9",
        "badge": "Cisco IOS Security Architecture",
        "prompt_en": "Analyze the technical and cryptographic evolution of password storage across Cisco IOS generations.<br><br>"
                     "Your analysis must evaluate:<br>"
                     "1. Why Type 0 cleartext is unacceptable in production environments.<br>"
                     "2. The exact mathematical nature and vulnerability of Type 7 encoding (Vigenère/XOR).<br>"
                     "3. The vulnerability of Type 5 MD5 secrets against modern GPU-accelerated dictionary and rainbow table attacks.<br>"
                     "4. Why modern Cisco enterprise deployments mandate Type 8 (PBKDF2 SHA-256) and Type 9 (Scrypt), explaining the concept of 'memory-hard' functions.",
        "prompt_ar": "حلل التطور التقني والتشفيري لطرق تخزين كلمات المرور عبر أجيال نظام تشغيل سيسكو (Cisco IOS).<br><br>"
                     "يجب أن يتضمن تحليلك:<br>"
                     "1. لماذا يعتبر تخزين Type 0 بالنص الصريح خطراً فادحاً في بيئات العمل.<br>"
                     "2. الطبيعة الرياضية لتشفير Type 7 ونقاط ضعفه القاتلة.<br>"
                     "3. ضعف تجزئة MD5 (Type 5) أمام هجمات التخمين الحديثة عبر كروت الشاشة وجداول Rainbow Tables.<br>"
                     "4. لماذا تفرض معايير الأمان الحديثة استخدام Type 8 و Type 9، مع شرح مفهوم دوال التجزئة المعتمدة على استهلاك الذاكرة (Memory-hard).",
        "model_en": "<b>Comprehensive Model Answer:</b><br><br>"
                    "<b>1. Type 0 (Cleartext Unencrypted):</b><br>"
                    "Passwords entered using <code>password &lt;string&gt;</code> without encryption are stored as Type 0 plaintext in NVRAM. Anyone viewing <code>show running-config</code>, auditing backups, or capturing unencrypted TFTP configs instantly obtains full credentials.<br><br>"
                    "<b>2. Type 7 Encoding (Cisco Vigenère / Static XOR):</b><br>"
                    "• <b>Mechanism:</b> Activated by <code>service password-encryption</code>. It takes a static, hardcoded 16-byte key created by Cisco engineers in the early 1990s and performs an XOR operation against the password characters, encoding the result in hexadecimal.<br>"
                    "• <b>Vulnerability:</b> Type 7 is <b>not cryptography</b> — it is weak obfuscation. Because the key has been public knowledge since 1995, any browser tool or script can reverse any Type 7 string back to plaintext in under 1 millisecond. Its sole purpose is preventing casual shoulder-surfing, offering zero defense against attackers.<br><br>"
                    "<b>3. Type 5 Hashing (MD5 with Salt):</b><br>"
                    "• <b>Mechanism:</b> Introduced with <code>enable secret</code>. It applies a one-way MD5 hash with a random 4-character salt (e.g. <code>$1$CANW$...</code>).<br>"
                    "• <b>Vulnerability:</b> While one-way (cannot be reversed via a formula), MD5 is computationally lightweight. Modern multi-GPU cracking rigs (using Hashcat) can calculate over <b>100 billion MD5 hashes per second</b>. Simple dictionary passwords like 'cisco' or 'Admin123' are cracked within seconds using precomputed rainbow tables or brute force.<br><br>"
                    "<b>4. Modern Standards: Type 8 (PBKDF2 SHA-256) and Type 9 (Scrypt):</b><br>"
                    "• <b>Type 8 (PBKDF2-HMAC-SHA256):</b> Uses Password-Based Key Derivation Function 2 with a cryptographic salt and <b>20,000 iterations</b> of SHA-256. The repeated iterations introduce intentional computational delay, slowing down brute-force attacks by orders of magnitude.<br>"
                    "• <b>Type 9 (Scrypt):</b> Represents the pinnacle of Cisco password security. Unlike SHA-256 which is compute-bound, Scrypt is <b>memory-hard</b>: it deliberately requires large amounts of RAM to compute each hash attempt. This design specifically neutralizes custom ASIC hardware and GPU parallelization clusters, making mass offline cracking economically and physically unfeasible.",
        "model_ar": "<b>الإجابة النموذجية الشاملة:</b><br><br>"
                    "<b>1. النوع 0 (Type 0 - النص الصريح):</b><br>"
                    "الكلمات التي تُكتب بأمر <code>password</code> تظهر كما هي بنص صريح. أي شخص يفتح أمر <code>show running-config</code> أو يطلع على ملفات النسخ الاحتياطي (Backups) يرى كلمات المرور فوراً، وهو ما يمثل خطراً أمنياً كارثياً.<br><br>"
                    "<b>2. تشفير Type 7 (تمويه Vigenère XOR):</b><br>"
                    "• <b>آلية عمله:</b> يتم تفعيله بأمر <code>service password-encryption</code>. يعتمد على مفتاح ثابت مكون من 16 بايت تم وضعه في أوائل التسعينيات، ويقوم بعملية XOR رياضية بسيطة مع حروف كلمة المرور وتحويلها لرموز سداسية عشرية.<br>"
                    "• <b>نقطة ضعفه:</b> Type 7 <b>ليس تشفيراً حقيقياً</b> بل هو تمويه. مفتاح التشفير معروف ومنشور في العالم كله منذ عام 1995، ويمكن لأي أداة أو كود بايثون بسيط فكه في جزء من الألف من الثانية. فائدته الوحيدة حجب الرؤية عن الشخص الواقف بجوارك فقط.<br><br>"
                    "<b>3. تجزئة Type 5 (تجزئة MD5 مع Salt):</b><br>"
                    "• <b>آلية عمله:</b> جاء مع أمر <code>enable secret</code>. يعتمد على دالة تجزئة أحادية الاتجاه (One-Way Hash) مع قيمة عشوائية (Salt) لمنع الهجمات المباشرة.<br>"
                    "• <b>نقطة ضعفه:</b> خوارزمية MD5 خفيفة وسريعة حسابياً. ومع تطور كروت الشاشة الحديثة، تستطيع مزارع التخمين (Hashcat) تجربة أكثر من <b>100 مليار كلمة في الثانية الواحدة</b>، مما يجعل كسر الكلمات المعتادة مثل 'cisco' أو 'Admin2020' مسألة ثوانٍ معدودة عبر جداول Rainbow Tables.<br><br>"
                    "<b>4. المعايير الحديثة: Type 8 (SHA-256) و Type 9 (Scrypt):</b><br>"
                    "• <b>تجزئة Type 8 (PBKDF2 SHA-256):</b> تعتمد على خوارزمية SHA-256 القوية مع تكرار عملية التجزئة <b>20,000 مرة متتالية</b> مع قيمة Salt قوية. هذا التكرار يفرض عبئاً زمنياً مقصوداً يجعل تجربة ملايين الكلمات أمراً بالغ الصعوبة والبطء.<br>"
                    "• <b>تجزئة Type 9 (Scrypt):</b> قمة الأمان في أنظمة سيسكو. تتميز بأنها <b>Memory-hard (تستهلك الذاكرة عمداً)</b>، حيث تتطلب كل محاولة تجزئة حجز مساحة كبيرة من الرام. هذا يمنع المعالجات المتخصصة (ASICs) وكروت الشاشة من تجربة مليارات المحاولات بالتوازي، مما يجعل كسرها مستحيلاً عملياً."
    },
    {
        "id": "essay4",
        "title_en": "Essay 4: Enterprise AAA Architecture: TACACS+ vs RADIUS In-Depth",
        "title_ar": "سؤال مقالي 4: مقارنة معمارية مفصلة بين خوادم TACACS+ و RADIUS في بيئات المؤسسات",
        "badge": "Centralized AAA & Access Control",
        "prompt_en": "Compare and contrast the <b>TACACS+</b> and <b>RADIUS</b> protocols in modern enterprise network environments.<br><br>"
                     "In your comparative analysis, you must explain:<br>"
                     "1. Why network operations teams mandate TACACS+ for switch and router administrative management (device administration).<br>"
                     "2. Why identity and security teams deploy RADIUS for 802.1X network access control (NAC), VPN, and Wi-Fi authentication.<br>"
                     "3. The architectural differences regarding transport protocol, packet encryption, and the separation of Authentication, Authorization, and Accounting.",
        "prompt_ar": "قارن مقارنة معمارية دقيقة بين بروتوكولي <b>TACACS+</b> و <b>RADIUS</b> في شبكات المؤسسات الكبرى الحديثة.<br><br>"
                     "يجب أن توضح في تحليلك المقارن:<br>"
                     "1. لماذا تصر فرق إدارة الشبكات على استخدام TACACS+ للتحكم في إدارة الراوترات والسويتشات (Device Administration).<br>"
                     "2. لماذا تستخدم فرق الأمن والوصول بروتوكول RADIUS لمصادقة المستخدمين في شبكات 802.1X والـ VPN والواي فاي (Network Access).<br>"
                     "3. الفروق الهيكلية في بروتوكول النقل (Transport)، وتشفير الحزم (Encryption)، وفصل وظائف المصادقة والتخويل والمحاسبة (AAA Planes).",
        "model_en": "<b>Comprehensive Model Answer:</b><br><br>"
                    "<b>1. Architectural Comparison Matrix:</b><br>"
                    "• <b>Transport Protocol:</b> TACACS+ runs over <b>TCP port 49</b> (guaranteeing reliable transport, sequence tracking, and immediate session error detection). RADIUS runs over <b>UDP ports 1812 (Auth) and 1813 (Acct)</b> or legacy 1645/1646, requiring application-layer retransmission timers.<br>"
                    "• <b>Packet Confidentiality:</b> TACACS+ encrypts the <b>ENTIRE payload of the packet</b> (everything except the standard 12-byte header), completely concealing usernames, authorization queries, and command arguments. RADIUS encrypts <b>ONLY the Password attribute</b> inside the packet; packet headers, usernames, and vendor-specific attributes travel in clear unencrypted text across the network.<br>"
                    "• <b>Separation of AAA Planes:</b> TACACS+ maintains <b>complete modular separation</b> between Authentication, Authorization, and Accounting. RADIUS <b>combines Authentication and Authorization</b> into a single Access-Request / Access-Accept exchange.<br><br>"
                    "<b>2. Why TACACS+ Dominates Device Administration:</b><br>"
                    "Because TACACS+ separates Authorization from Authentication, it enables <b>per-command authorization and accounting</b>. When an engineer types a command in Privileged EXEC mode (e.g. <code>reload</code> or <code>interface GigabitEthernet 0/1</code>), the Cisco router sends a real-time TACACS+ authorization request to Cisco ISE asking: <i>'Is user Ahmed authorized to execute this specific command at this privilege level?'</i> The server can approve or deny individual commands without terminating the user's session, maintaining a flawless, granular audit trail.<br><br>"
                    "<b>3. Why RADIUS Dominates Network Access Control (NAC):</b><br>"
                    "RADIUS was engineered for high-volume network access. In large enterprises with 50,000 employees connecting via 802.1X (wired switchports, corporate Wi-Fi, GlobalProtect VPNs), combining Authentication and Authorization in one UDP transaction minimizes latency and server overhead. When an employee logs in, the RADIUS server authenticates them and simultaneously returns their authorization parameters (VLAN ID, ACL string, QoS profile) in the single Access-Accept response.",
        "model_ar": "<b>الإجابة النموذجية الشاملة:</b><br><br>"
                    "<b>1. المقارنة الهيكلية والمعمارية:</b><br>"
                    "• <b>بروتوكول النقل (Transport):</b> يستخدم TACACS+ بروتوكول <b>TCP عبر المنفذ 49</b> مما يضمن موثوقية عالية وكشفاً فورياً لانقطاع الاتصال. بينما يعتمد RADIUS على <b>UDP عبر المنفذين 1812 و 1813</b> ويتطلب تطبيق آليات إعادة الإرسال برمجياً.<br>"
                    "• <b>تشفير الحزم (Packet Confidentiality):</b> يشفر TACACS+ <b>كامل محتوى الحزمة</b> باستثناء ترويسة بسيطة، مما يخفي أسماء المستخدمين والصلاحيات والأوامر بالكامل عن المتطفلين. أما RADIUS فيشفر <b>حقل كلمة المرور فقط</b> تاركاً اسم المستخدم وباقي الحقول بنص صريح مكشوف على الأسلاك.<br>"
                    "• <b>فصل عناصر AAA:</b> يفصل TACACS+ تماماً بين المصادقة (Authentication) والتخويل (Authorization) والمحاسبة (Accounting). بينما يدمج RADIUS المصادقة مع التخويل معاً في حزمة واحدة.<br><br>"
                    "<b>2. لماذا يُفضل TACACS+ لإدارة الأجهزة (Device Administration):</b><br>"
                    "بفضل فصل التخويل عن المصادقة، يتيح TACACS+ ميزة <b>التحكم في الأوامر أمراً بأمر (Per-command Authorization)</b>. عندما يكتب المهندس أمراً مثل <code>reload</code>، يرسل السويتش استفساراً لحظياً لخادم ISE: <i>'هل مسموح لأحمد تنفيذ هذا الأمر تحديداً؟'</i> ويمكن للخادم السماح بأوامر العرض (show) ورفض أوامر التعديل لكل مستخدم على حدة وتسجيل كل أمر بدقة فائقة في سجلات التدقيق.<br><br>"
                    "<b>3. لماذا يُفضل RADIUS للتحكم في وصول المستخدمين (Network Access):</b><br>"
                    "صُمم RADIUS للتعامل مع أعداد ضخمة من المستخدمين (عشرات الآلاف من موظفي الـ Wi-Fi والـ VPN و 802.1X). دمج المصادقة والتخويل في خطوة واحدة عبر حزمة UDP سريعة يقلل زمن الاستجابة والضغط على السيرفرات، حيث يتحقق السيرفر من هوية الموظف وفي نفس اللحظة يرسل رقم الـ VLAN وقواعد الجدار الناري المخصصة له في رد واحد."
    },
    {
        "id": "essay5",
        "title_en": "Essay 5: ICMP in Network Troubleshooting: Echo, PMTUD, and Traceroute",
        "title_ar": "سؤال مقالي 5: تشخيص أعطال الشبكات عبر ICMP: آليات الفحص واكتشاف MTU والمسار",
        "badge": "ICMP Mechanics & Network Troubleshooting",
        "prompt_en": "Evaluate the role of ICMP as both the primary diagnostic utility and a potential security risk in modern enterprise networks.<br><br>"
                     "Your technical response must explain:<br>"
                     "1. The internal header structure of ICMP messages and the difference between Type and Code fields.<br>"
                     "2. How Path MTU Discovery (PMTUD) operates using ICMP Type 3 Code 4, and the disastrous consequence of 'ICMP Black Holes'.<br>"
                     "3. How enterprise firewalls should be configured to balance security (preventing ICMP recon/DOS) against essential path diagnostics.",
        "prompt_ar": "قيّم دور بروتوكول ICMP كأداة تشخيص أساسية وسلاح ذو حدين يمثل ثغرة أمنية إذا لم يتم التعامل معه بحذر.<br><br>"
                     "يجب أن تشرح في تقييمك الفني:<br>"
                     "1. الهيكل الداخلي لهيدر ICMP والفرق بين حقلي النوع (Type) والرمز (Code).<br>"
                     "2. آلية عمل تقنية اكتشاف MTU للمسار (Path MTU Discovery) عبر رسالة ICMP Type 3 Code 4، وما هي ظاهرة 'الثقب الأسود لـ ICMP'.<br>"
                     "3. الممارسات الموصى بها في إعداد جدران الحماية للموازنة بين حماية الشبكة من هجمات الاستكشاف ومنع الأعطال الخفية.",
        "model_en": "<b>Comprehensive Model Answer:</b><br><br>"
                    "<b>1. ICMP Header Structure (Type vs Code):</b><br>"
                    "ICMP is encapsulated directly inside IPv4 packets (IP Protocol number 1). The 8-byte base ICMP header contains:<br>"
                    "• <b>Type (8 bits):</b> Defines the general category or function of the message (e.g., Type 0 = Echo Reply, Type 3 = Destination Unreachable, Type 8 = Echo Request, Type 11 = Time Exceeded).<br>"
                    "• <b>Code (8 bits):</b> Provides granular, specific diagnostic details within that Type category. For example, under Type 3 (Destination Unreachable), Code 0 = Network Unreachable, Code 1 = Host Unreachable, Code 3 = Port Unreachable, and Code 4 = Fragmentation Needed.<br>"
                    "• <b>Checksum (16 bits):</b> Detects corruption across the entire ICMP message.<br><br>"
                    "<b>2. Path MTU Discovery (PMTUD) & ICMP Black Holes:</b><br>"
                    "• <b>How PMTUD Operates:</b> Hosts transmit IP packets with the Don't Fragment (DF) flag set to 1. If an intermediate router's outgoing link has an MTU smaller than the packet size, the router cannot fragment the packet. It discards it and returns an <b>ICMP Type 3, Code 4</b> message containing the 'Next-Hop MTU' value. The sender reduces its packet size to match and retransmits.<br>"
                    "• <b>The ICMP Black Hole Disaster:</b> Overly aggressive security engineers often configure firewalls to blindly block ALL ICMP traffic. If a firewall blocks ICMP Type 3 Code 4, the sender never receives the MTU warning! Small TCP packets (like the 3-way handshake) pass through, but as soon as full-sized data packets (1500 bytes) are sent, they are dropped silently by intermediate routers. To the user, the connection hangs indefinitely or displays spinning loading wheels. This is known as an <b>ICMP Black Hole</b>.<br><br>"
                    "<b>3. Best-Practice Firewall Hardening for ICMP:</b><br>"
                    "• Never block ICMP unconditionally. Modern enterprise firewalls should implement granular stateful inspection:<br>"
                    "  - <b>PERMIT:</b> ICMP Type 3, Code 4 (Fragmentation Needed) to preserve PMTUD and avoid black holes.<br>"
                    "  - <b>PERMIT:</b> ICMP Type 11 (Time Exceeded) to allow legitimate traceroute path diagnostics.<br>"
                    "  - <b>RATE LIMIT / CONTROL:</b> ICMP Type 8 (Echo Request) on edge WAN interfaces to mitigate Ping of Death, Smurf attacks, and external reconnaissance, while allowing internal troubleshooting.",
        "model_ar": "<b>الإجابة النموذجية الشاملة:</b><br><br>"
                    "<b>1. هيكل هيدر ICMP والفرق بين Type و Code:</b><br>"
                    "يتم تغليف ICMP مباشرة داخل حزمة IP (بروتوكول رقم 1). يتكون الهيدر الأساسي من 8 بايت:<br>"
                    "• <b>حقل النوع (Type - 8 bits):</b> يحدد التصنيف العام للرسالة (مثل: Type 8 للطلب، Type 0 للرد، Type 3 لعدم إمكانية الوصول، Type 11 لانتهاء المهلة).<br>"
                    "• <b>حقل الرمز (Code - 8 bits):</b> يحدد السبب التفصيلي الدقيق داخل هذا التصنيف. فمثلاً تحت Type 3، نجد Code 0 لعدم وصول للشبكة، و Code 1 لعدم وصول للجهاز، و Code 3 لغلق المنفذ، و Code 4 للحاجة الماسة للتجزئة.<br>"
                    "• <b>حقل فحص الخطأ (Checksum - 16 bits):</b> لفحص سلامة رسالة ICMP بالكامل.<br><br>"
                    "<b>2. تقنية Path MTU Discovery وظاهرة الثقب الأسود (ICMP Black Hole):</b><br>"
                    "• <b>آلية عمل PMTUD:</b> يرسل العميل حزم IP مع تفعيل بت عدم التجزئة (DF=1). إذا واجهت الحزمة رابطاً ذو MTU أصغر (مثلاً نفق VPN بـ 1400 بايت)، يسقط الراوتر الحزمة ويرسل للمصدر <b>ICMP Type 3 Code 4</b> موضحاً فيه حجم الـ MTU المتاح، فيقوم العميل بإنقاص حجم حزمه وإعادة الإرسال.<br>"
                    "• <b>كارثة الثقب الأسود (ICMP Black Hole):</b> عندما يقوم مسؤول حماية مفرط بحظر كافة رسائل ICMP في الجدار الناري دون تمييز، تسقط رسالة التنبيه (Type 3 Code 4) ولا تصل للمرسل! والنتيجة: تنجح المصافحة الثلاثية الأولية لأن حزمها صغيرة، ولكن بمجرد بدء نقل صفحات الويب أو الملفات بحجم 1500 بايت، تسقط الحزم في صمت مطبق دون أن يعرف العميل السبب، فيعلق الاتصال للأبد فيما يُعرف بـ 'الثقب الأسود لـ ICMP'.<br><br>"
                    "<b>3. أفضل الممارسات الأمنية لإعدادات الجدران النارية:</b><br>"
                    "• عدم حظر ICMP عشوائياً، بل تطبيق فلاتر دقيقة:<br>"
                    "  - <b>السماح دائماً:</b> برسالة ICMP Type 3 Code 4 لضمان عمل PMTUD وتفادي الثقوب السوداء.<br>"
                    "  - <b>السماح:</b> برسالة ICMP Type 11 لتشغيل أدوات تشخيص المسار traceroute.<br>"
                    "  - <b>تقنين وتحديد معدل (Rate-Limit):</b> رسائل Echo Request (Type 8) على منافذ الإنترنت الخارجية لمنع هجمات حجب الخدمة (Smurf / Ping Floods) وهجمات مسح الشبكة."
    }
]

print(f"Loaded {len(mcqs)} MCQs, {len(scenarios)} Scenarios, and {len(essays)} Essays.")

# Assemble the full HTML document
# We borrow the premium styling and scripts from lesson_lib.HEAD / lesson_lib.SCRIPT
# and enhance it with live scoring, filter tabs, and model answer drawers.

with open("lesson_lib.py", "r", encoding="utf-8") as f:
    lib_content = f.read()

# Extract HEAD and SCRIPT
import lesson_lib
head_template = lesson_lib.HEAD
script_template = lesson_lib.SCRIPT

# Customize title and badges in HEAD
head_html = head_template.replace("{NUM}", "Exam").replace("{PCT}", "100").replace("{TITLE}", "Unit 2: Network Fundamentals — Comprehensive Exam & Question Bank")

# Additional CSS specific to Exam Dashboard
exam_styles = """
<style>
/* Exam Specific Dashboard Styles */
.exam-header {
  background: linear-gradient(135deg, rgba(37,99,235,0.08) 0%, rgba(99,102,241,0.08) 100%);
  border: 1px solid var(--accent);
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
}
.exam-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
  margin-top: 16px;
}
.stat-card {
  background: var(--panel2);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px;
  text-align: center;
}
.stat-val {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--accent);
  font-family: var(--font-mono);
}
.stat-label {
  font-size: 0.85rem;
  color: var(--muted);
  margin-top: 4px;
}
.exam-tabs {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin: 24px 0 16px 0;
  border-bottom: 1px solid var(--line);
  padding-bottom: 8px;
}
.tab-btn {
  background: var(--panel);
  border: 1px solid var(--line);
  color: var(--text);
  padding: 10px 18px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.tab-btn.active, .tab-btn:hover {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}
.score-badge-pass {
  background: rgba(34,197,94,0.15);
  color: var(--good);
  border: 1px solid var(--good);
  padding: 4px 10px;
  border-radius: 999px;
  font-weight: 600;
  display: inline-block;
}
.score-badge-fail {
  background: rgba(239,68,68,0.15);
  color: var(--err);
  border: 1px solid var(--err);
  padding: 4px 10px;
  border-radius: 999px;
  font-weight: 600;
  display: inline-block;
}
.scenario-box, .essay-box {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.scenario-box {
  border-inline-start: 4px solid var(--accent);
}
.essay-box {
  border-inline-start: 4px solid #f59e0b;
}
.model-answer-drawer {
  display: none;
  background: var(--panel2);
  border: 1px solid var(--good);
  border-radius: 8px;
  padding: 18px;
  margin-top: 16px;
}
.model-answer-drawer.open {
  display: block;
  animation: fadeIn 0.3s ease;
}
.model-btn {
  background: var(--panel);
  border: 1px solid var(--accent);
  color: var(--accent);
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 12px;
  transition: all 0.2s;
}
.model-btn:hover {
  background: var(--accent);
  color: #fff;
}
.user-notes {
  width: 100%;
  min-height: 90px;
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 10px;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--text);
  margin-top: 12px;
  resize: vertical;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
"""

# Inject custom styles into head
head_html = head_html.replace("</head>", f"{exam_styles}\n</head>")

# Build top Hero and Dashboard
hero_html = f"""
<div class="shell">
<nav class="toc">
  <div class="toc-title"><span class="en">Exam Sections</span><span class="ar">أقسام الاختبار</span></div>
  <a href="#overview"><span class="en">Exam Overview</span><span class="ar">نظرة عامة والدرجات</span></a>
  <a href="#part1-mcq"><span class="en">Part 1: CCNA MCQs (25)</span><span class="ar">القسم 1: أسئلة اختيارية (25)</span></a>
  <a href="#part2-scenarios"><span class="en">Part 2: Scenarios & Debug (6)</span><span class="ar">القسم 2: سيناريوهات وتتبع أخطاء (6)</span></a>
  <a href="#part3-essays"><span class="en">Part 3: Deep-Dive Essays (5)</span><span class="ar">القسم 3: أسئلة مقالية ومفاهيمية (5)</span></a>
</nav>

<main>
<div class="hero">
  <div class="chip"><span class="en">Unit 2: Network Fundamentals — Final Comprehensive Exam</span><span class="ar">الوحدة الثانية: أساسيات الشبكات — الامتحان الشامل النهائي</span></div>
  <h1><span class="en">Unit 2 Comprehensive Exam & Question Bank</span><span class="ar">امتحان الوحدة الثانية الشامل وبنك الأسئلة التفاعلي</span></h1>
  <div class="sub">
    <span class="en">Covering Lessons 01 to 11 — 25 Multiple-Choice Questions, 6 Real-World Scenarios, and 5 Deep-Dive Essays with Model Answers</span>
    <span class="ar">يغطي الدروس من 01 إلى 11 — 25 سؤال اختيار من متعدد، 6 سيناريوهات عملية، و5 أسئلة مقالية معمقة مع الإجابات النموذجية</span>
  </div>
</div>

<section id="overview" class="exam-header">
  <h2><span class="en">🎯 Live Performance Dashboard</span><span class="ar">🎯 لوحة الأداء والتقييم اللحظي</span></h2>
  <div class="para-block">
    <div class="en">This comprehensive exam covers the entire curriculum of <b>Unit 2: Network Fundamentals</b> (OSI Model, IPv4 Addressing, Headers, ARP, TCP, UDP, Window Scaling, ICMP, DNS, Cisco CLI, and Device Security). Test your knowledge with realistic CCNA simulations, troubleshooting scenarios, and conceptual essay questions.</div>
    <div class="ar">هذا الامتحان الشامل يغطي منهج <b>الوحدة الثانية: أساسيات الشبكات</b> بالكامل (نموذج OSI، عناوين IPv4، ترويسات الحزم، بروتوكولات ARP و TCP و UDP والتحكم بالنافذة، بروتوكول ICMP و DNS، وواجهة سيسكو CLI وأمان الأجهزة). اختبر معلوماتك بأسئلة امتحانات CCNA الحقيقية، والسيناريوهات العملية، والأسئلة المقالية.</div>
    <button class="tr-btn" onclick="toggleParaLang(this)"></button>
  </div>
  
  <div class="exam-stats">
    <div class="stat-card">
      <div id="statAnswered" class="stat-val">0 / 25</div>
      <div class="stat-label"><span class="en">MCQs Answered</span><span class="ar">الأسئلة الاختيارية المكتملة</span></div>
    </div>
    <div class="stat-card">
      <div id="statScore" class="stat-val">0%</div>
      <div class="stat-label"><span class="en">Current Score</span><span class="ar">الدرجة الحالية</span></div>
    </div>
    <div class="stat-card">
      <div id="statBenchmark" class="stat-val">82.5%</div>
      <div class="stat-label"><span class="en">Cisco CCNA Passing Target</span><span class="ar">حد اجتياز امتحان سيسكو</span></div>
    </div>
    <div class="stat-card">
      <div id="statStatus" class="stat-val"><span class="score-badge-fail"><span class="en">In Progress</span><span class="ar">قيد الحل</span></span></div>
      <div class="stat-label"><span class="en">Evaluation</span><span class="ar">التقييم العام</span></div>
    </div>
  </div>

  <div style="margin-top:16px;display:flex;gap:12px;flex-wrap:wrap;">
    <button class="tr-btn" style="padding:8px 16px;border-radius:6px;border:1px solid var(--line);background:var(--panel);cursor:pointer;" onclick="resetExam()"><span class="en">🔄 Reset All Answers</span><span class="ar">🔄 إعادة ضبط الاختبار بالكامل</span></button>
    <button class="tr-btn" style="padding:8px 16px;border-radius:6px;border:1px solid var(--accent);background:var(--panel);color:var(--accent);cursor:pointer;" onclick="toggleAllDrawers()"><span class="en">📖 Toggle All Model Answers</span><span class="ar">📖 فتح / إغلاق كل الإجابات النموذجية</span></button>
  </div>
</section>
"""

# Build Part 1: MCQs
part1_html = """
<section id="part1-mcq">
  <span class="badge"><span class="en">Part 1</span><span class="ar">القسم الأول</span></span>
  <h2><span class="en">Part 1: Realistic CCNA Multiple Choice Questions (25 Questions)</span><span class="ar">القسم 1: أسئلة الاختيار من متعدد القياسية لامتحان CCNA (25 سؤالاً)</span></h2>
  <p class="quiz-intro"><span class="en">Click an option to test your answer. Correct answers light up in green; incorrect options turn red with instant detailed explanations. You can toggle language per question.</span><span class="ar">اختر إجابة للتحقق الفوري. تضيء الإجابة الصحيحة بالأخضر والخطأ بالأحمر مع شرح تفصيلي فوري. يمكنك تبديل لغة كل سؤال بزرار الترجمة.</span></p>
  <div id="examMcqArea"></div>
</section>
"""

# Build Part 2: Scenarios & Troubleshooting
part2_items = []
for s in scenarios:
    item = f"""
<div class="scenario-box" id="{s['id']}">
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px;">
    <span class="badge" style="background:var(--accent);color:#fff;">{s['badge']}</span>
    <button class="tr-btn" onclick="toggleCardLang(this)"></button>
  </div>
  <h3><span class="en">{s['title_en']}</span><span class="ar">{s['title_ar']}</span></h3>
  
  <div class="para-block">
    <div class="en">{s['context_en']}</div>
    <div class="ar">{s['context_ar']}</div>
  </div>
  
  <div style="background:var(--panel2);border:1px solid var(--line);border-radius:6px;padding:14px;margin:14px 0;">
    <div class="en"><b>Questions to solve:</b><br>{s['q_en']}</div>
    <div class="ar"><b>المطلوب حله وتشخيصه:</b><br>{s['q_ar']}</div>
  </div>

  <textarea class="user-notes" placeholder="Type your troubleshooting notes or analysis here before revealing the answer... (اكتب تحليلك هنا للتدريب قبل رؤية الحل)"></textarea>

  <button class="model-btn" onclick="toggleDrawer('{s['id']}_drawer')">
    <span class="en">🔍 Reveal Solution &amp; Deep Explanation</span>
    <span class="ar">🔍 إظهار الحل النموذجي والشرح التفصيلي</span>
  </button>

  <div id="{s['id']}_drawer" class="model-answer-drawer">
    <div class="en">{s['solution_en']}</div>
    <div class="ar">{s['solution_ar']}</div>
  </div>
</div>
"""
    part2_items.append(item)

part2_html = f"""
<section id="part2-scenarios">
  <span class="badge"><span class="en">Part 2</span><span class="ar">القسم الثاني</span></span>
  <h2><span class="en">Part 2: Real-World Scenarios &amp; Troubleshooting (6 Scenarios)</span><span class="ar">القسم 2: سيناريوهات عملية واستكشاف أخطاء الشبكات (6 سيناريوهات)</span></h2>
  <p class="quiz-intro"><span class="en">Analyze real Wireshark captures, command outputs, subnetting failures, and configuration incidents. Formulate your solution in the notes box, then reveal the authoritative model answer.</span><span class="ar">حلل لقطات Wireshark، مخرجات الأوامر، أخطاء تقسيم الشبكات، والحوادث الأمنية الحقيقية. اكتب ملاحظاتك ثم افتح الحل النموذجي المعتمد للمقارنة والتقييم.</span></p>
  {"".join(part2_items)}
</section>
"""

# Build Part 3: Deep-Dive Essays & Conceptual Questions
part3_items = []
for e in essays:
    item = f"""
<div class="essay-box" id="{e['id']}">
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:12px;">
    <span class="badge" style="background:#f59e0b;color:#fff;">{e['badge']}</span>
    <button class="tr-btn" onclick="toggleCardLang(this)"></button>
  </div>
  <h3><span class="en">{e['title_en']}</span><span class="ar">{e['title_ar']}</span></h3>

  <div class="para-block">
    <div class="en">{e['prompt_en']}</div>
    <div class="ar">{e['prompt_ar']}</div>
  </div>

  <textarea class="user-notes" style="min-height:140px;" placeholder="Draft your complete technical explanation here... (اكتب شرحك وإجابتك الفنية هنا قبل مقارنتها بالإجابة النموذجية)"></textarea>

  <button class="model-btn" onclick="toggleDrawer('{e['id']}_drawer')">
    <span class="en">💡 Show Complete Model Answer &amp; Scoring Rubric</span>
    <span class="ar">💡 إظهار الإجابة النموذجية الكاملة ومعايير التقييم</span>
  </button>

  <div id="{e['id']}_drawer" class="model-answer-drawer">
    <div class="en">{e['model_en']}</div>
    <div class="ar">{e['model_ar']}</div>
  </div>
</div>
"""
    part3_items.append(item)

part3_html = f"""
<section id="part3-essays">
  <span class="badge"><span class="en">Part 3</span><span class="ar">القسم الثالث</span></span>
  <h2><span class="en">Part 3: Deep-Dive Conceptual &amp; Essay Questions (5 Essays)</span><span class="ar">القسم 3: أسئلة مقالية ومفاهيمية معمقة لمهندسي الشبكات (5 أسئلة)</span></h2>
  <p class="quiz-intro"><span class="en">High-level architectural questions testing deep protocol understanding, encapsulation transitions, cryptographic algorithms, and traffic engineering. Compare your answers with the comprehensive model solution.</span><span class="ar">أسئلة معمارية رفيعة المستوى تختبر فهمك العميق للبروتوكولات، وعمليات التغليف، وخوارزميات التشفير، وهندسة تدفق البيانات. قارن إجابتك بالإجابة النموذجية الكاملة.</span></p>
  {"".join(part3_items)}
</section>
"""

# Navigation footer
footer_html = """
<div class="lesson-nav">
  <a class="prev" href="lesson-11-user-mode-privileged-mode-security.html">
    <span class="k"><span class="en">Previous Lesson</span><span class="ar">الدرس السابق</span></span>
    <strong>Lesson 11: User &amp; Privileged Mode Security</strong>
  </a>
  <a class="next" href="index.html">
    <span class="k"><span class="en">Course Hub</span><span class="ar">الفهرس الرئيسي</span></span>
    <strong>CCNA Study Hub — All Units</strong>
  </a>
</div>

<div class="source-footer">
  <div class="en">
    🎓 <strong>Unit 2 Mastery:</strong> Congratulations on completing all 11 lessons of Unit 2: Network Fundamentals! This comprehensive exam covers every topic required by the official Cisco CCNA 200-301 blueprint.
  </div>
  <div class="ar">
    🎓 <strong>إتقان الوحدة الثانية:</strong> تهانينا على إتمام جميع دروس الوحدة الثانية (أساسيات الشبكات)! هذا الامتحان الشامل يغطي كل متطلبات مخطط امتحان سيسكو CCNA 200-301 الرسمي بدقة متناهية.
  </div>
</div>
</main>
</div>
"""

# JavaScript for live grading, filter, and interactive drawers
exam_js = f"""
<script>
const EXAM_MCQS = {json.dumps(mcqs, ensure_ascii=False)};

let answeredCount = 0;
let correctCount = 0;

function renderExamMcqs() {{
  const area = document.getElementById('examMcqArea');
  if(!area) return;
  area.innerHTML = '';

  EXAM_MCQS.forEach((item, idx) => {{
    const card = document.createElement('div');
    card.className = 'q-card';
    card.id = 'mcq_card_' + idx;
    card.dataset.lang = document.documentElement.classList.contains('lang-ar') ? 'ar' : 'en';

    const topBar = document.createElement('div');
    topBar.className = 'q-top';
    topBar.innerHTML = `<span class="q-num"><span class="en">${{item.lesson}} — Q${{idx+1}} of 25</span><span class="ar">${{item.lesson}} — سؤال ${{idx+1}} من 25</span></span>
                        <button class="q-lang-btn" onclick="toggleMcqLang(this, ${{idx}})">${{card.dataset.lang === 'ar' ? '🌐 English' : '🌐 العربية'}}</button>`;

    const qText = document.createElement('div');
    qText.className = 'q-text';
    qText.innerHTML = `<span class="en">${{item.q_en}}</span><span class="ar">${{item.q_ar}}</span>`;

    const optsDiv = document.createElement('div');
    optsDiv.className = 'q-opts';

    item.opts_en.forEach((optEn, oIdx) => {{
      const optAr = item.opts_ar[oIdx];
      const lab = document.createElement('label');
      lab.className = 'q-opt';
      lab.innerHTML = `<input type="radio" name="exam_mcq_${{idx}}" value="${{oIdx}}" onchange="checkMcqAnswer(${{idx}}, ${{oIdx}})">
                       <span class="opt-txt"><span class="en">${{optEn}}</span><span class="ar">${{optAr}}</span></span>`;
      optsDiv.appendChild(lab);
    }});

    const expDiv = document.createElement('div');
    expDiv.className = 'q-explain';
    expDiv.id = 'exp_mcq_' + idx;
    expDiv.innerHTML = `<div class="exp-title"><span class="en">💡 Official Cisco Model Explanation:</span><span class="ar">💡 الشرح النموذجي المعتمد:</span></div>
                        <div class="exp-body"><span class="en">${{item.exp_en}}</span><span class="ar">${{item.exp_ar}}</span></div>`;

    card.appendChild(topBar);
    card.appendChild(qText);
    card.appendChild(optsDiv);
    card.appendChild(expDiv);
    area.appendChild(card);
  }});
}}

function checkMcqAnswer(qIdx, selectedOpt) {{
  const card = document.getElementById('mcq_card_' + qIdx);
  if(card.dataset.answered) return;
  card.dataset.answered = "true";

  const item = EXAM_MCQS[qIdx];
  const labels = card.querySelectorAll('.q-opt');
  const expDiv = document.getElementById('exp_mcq_' + qIdx);

  labels.forEach((l, idx) => {{
    l.classList.add('disabled');
    if(idx === item.ans) {{
      l.classList.add('correct');
    }} else if(idx === selectedOpt) {{
      l.classList.add('wrong');
    }}
  }});

  answeredCount++;
  if(selectedOpt === item.ans) {{
    correctCount++;
  }}

  expDiv.classList.add('show');
  updateDashboard();
}}

function updateDashboard() {{
  const statAnswered = document.getElementById('statAnswered');
  const statScore = document.getElementById('statScore');
  const statStatus = document.getElementById('statStatus');

  const total = EXAM_MCQS.length;
  statAnswered.textContent = answeredCount + " / " + total;

  const pct = answeredCount > 0 ? Math.round((correctCount / total) * 100) : 0;
  statScore.textContent = pct + "%";

  if(answeredCount === total) {{
    if(pct >= 82.5) {{
      statStatus.innerHTML = `<span class="score-badge-pass"><span class="en">PASSED (ممتاز - ناجح)</span><span class="ar">ناجح ومؤهل للامتحان</span></span>`;
    }} else {{
      statStatus.innerHTML = `<span class="score-badge-fail"><span class="en">NEEDS REVIEW (يحتاج مراجعة)</span><span class="ar">يحتاج مراجعة إضافية</span></span>`;
    }}
  }} else {{
    statStatus.innerHTML = `<span class="score-badge-fail"><span class="en">In Progress (${{answeredCount}}/${{total}})</span><span class="ar">قيد الحل (${{answeredCount}}/${{total}})</span></span>`;
  }}
}}

function resetExam() {{
  if(confirm("Are you sure you want to reset all answers? / هل أنت متأكد من إعادة ضبط الاختبار بالكامل؟")) {{
    answeredCount = 0;
    correctCount = 0;
    renderExamMcqs();
    updateDashboard();
    document.querySelectorAll('.model-answer-drawer').forEach(d => d.classList.remove('open'));
    document.querySelectorAll('.user-notes').forEach(t => t.value = '');
    window.scrollTo({{top: 0, behavior: 'smooth'}});
  }}
}}

function toggleDrawer(id) {{
  const d = document.getElementById(id);
  if(d) d.classList.toggle('open');
}}

function toggleAllDrawers() {{
  const drawers = document.querySelectorAll('.model-answer-drawer');
  const anyOpen = Array.from(drawers).some(d => d.classList.contains('open'));
  drawers.forEach(d => {{
    if(anyOpen) d.classList.remove('open');
    else d.classList.add('open');
  }});
}}

function toggleMcqLang(btn, qIdx) {{
  const card = document.getElementById('mcq_card_' + qIdx);
  const cur = card.dataset.lang;
  const next = cur === 'ar' ? 'en' : 'ar';
  card.dataset.lang = next;
  btn.textContent = next === 'ar' ? '🌐 English' : '🌐 العربية';
}}

function toggleCardLang(btn) {{
  const box = btn.closest('.scenario-box, .essay-box');
  if(!box) return;
  box.classList.toggle('flip');
}}

document.addEventListener("DOMContentLoaded", () => {{
  renderExamMcqs();
  updateDashboard();
}});
</script>
</body>
</html>
"""

full_html = head_html + hero_html + part1_html + part2_html + part3_html + footer_html + script_template + exam_js

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated {OUT_FILE}!")
