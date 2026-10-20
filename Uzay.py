"""Bilingual, source-linked educational articles supplied for the space project."""


def make_article(title, summary, detail, image, sources):
    return {
        "title": title,
        "summary": summary,
        "detail": detail,
        "image": image,
        "sources": sources,
    }


NASA_STARS = (
    ("NASA Science — Stars", "NASA Science — Yıldızlar", "https://science.nasa.gov/universe/stars/"),
    (
        "NASA Science — Types of Stars",
        "NASA Science — Yıldız Türleri",
        "https://science.nasa.gov/universe/stars/types/",
    ),
)
TUA = (
    "Türkiye Uzay Ajansı — Süpernova Nedir?",
    "Türkiye Uzay Ajansı — Süpernova Nedir?",
    "https://tua.gov.tr/tr/blog/evren/supernova-nedir",
)
TUBITAK_GIANTS = (
    "TÜBİTAK Bilim Genç — Stars Thousands of Times Larger Than the Sun",
    "TÜBİTAK Bilim Genç — Güneş'ten Binlerce Kat Büyük Yıldızlar",
    "https://bilimgenc.tubitak.gov.tr/makale/gunesten-binlerce-kat-buyuk-yildizlar",
)
TUBITAK_BUBBLES = (
    "TÜBİTAK Bilim Genç — Giant Bubbles Observed on a Giant Star",
    "TÜBİTAK Bilim Genç — Bir Dev Yıldızın Yüzeyinde Devasa Kabarcıklar Gözlendi",
    "https://bilimgenc.tubitak.gov.tr/makale/bir-dev-yildizin-yuzeyinde-devasa-boyutlarda-kabarciklar-gozlendi",
)
NASA_DEBRIS = (
    "NASA — Orbital Debris",
    "NASA — Yörünge Enkazı",
    "https://sma.nasa.gov/sma-disciplines/orbital-debris",
)
ESA_DEBRIS_REPORT = (
    "ESA — Space Environment Report 2026",
    "ESA — 2026 Uzay Çevresi Raporu",
    "https://www.esa.int/Space_Safety/Space_Debris/ESA_Space_Environment_Report_2026",
)
ESA_DEBRIS_STATS = (
    "ESA — Space Environment Statistics",
    "ESA — Uzay Çevresi İstatistikleri",
    "https://sdup.esoc.esa.int/discosweb/statistics/",
)

PDF_ARTICLES = {
    "scientists": [
        make_article(
            (
                "Yıldız tayflarını sınıflandıran gökbilimciler",
                "Astronomers Who Classified Stellar Spectra",
            ),
            (
                "Tayf çizgileri, yıldızların sıcaklık ve bileşimini ölçmenin temel yollarından biridir.",
                "Spectral lines are a fundamental way to measure stellar temperature and composition.",
            ),
            (
                "Annie Jump Cannon, Harvard College Gözlemevi'nde yıldız tayflarını düzenleyerek O, B, A, F, G, K, M sıralamasının yaygınlaşmasına katkıda bulundu. Gökbilimciler tayfölçerlerle yıldız ışığını dalga boylarına ayırır; soğurma çizgilerinin konumu ve şiddeti atmosfer koşulları hakkında ipucu verir. Günümüzde uzay ve yer teleskopları farklı dalga boylarında ölçümler yaparak sınıflandırmayı ve yıldız evrimi araştırmalarını destekler.",
                "At Harvard College Observatory, Annie Jump Cannon organized stellar spectra and helped popularize the O, B, A, F, G, K, M sequence. Astronomers use spectrographs to separate starlight by wavelength; the positions and strengths of absorption lines reveal atmospheric conditions. Today, space- and ground-based telescopes observe across different wavelengths to support classification and stellar-evolution research.",
            ),
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200",
            NASA_STARS,
        ),
        make_article(
            (
                "Atarca sinyallerini fark eden bilim insanı",
                "The Scientist Who Detected Pulsar Signals",
            ),
            (
                "Jocelyn Bell Burnell'in 1967'de fark ettiği düzenli radyo sinyalleri nötron yıldızlarına ilişkin ilk kanıtlara ulaştırdı.",
                "Regular radio signals noticed by Jocelyn Bell Burnell in 1967 led to early evidence for neutron stars.",
            ),
            (
                "Gökbilimci Jocelyn Bell Burnell, 1967'de düzenli radyo darbeleri gösteren bir sinyali belirledi. Daha sonra sinyallerin hızla dönen nötron yıldızlarından, yani atarcalardan kaynaklandığı anlaşıldı. Nötron yıldızları bugün radyo, X-ışını ve gama ışını gözlemleriyle inceleniyor. NASA'nın NICER aygıtı ISS'ten X-ışını ölçümleri yaparak bu yıldızların boyutlarını ve iç yapılarını anlamaya yardımcı oluyor.",
                "Astronomer Jocelyn Bell Burnell identified a signal with regular radio pulses in 1967. The pulses were later understood to come from rapidly rotating neutron stars, or pulsars. Neutron stars are now studied in radio, X-ray, and gamma-ray wavelengths. NASA's NICER instrument makes X-ray measurements from the ISS to help constrain their sizes and internal structure.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Neutron Stars", "NASA — Nötron Yıldızları", "https://science.nasa.gov/neutron-stars/"),
                ("TÜBİTAK Bilim Genç — What Is a Neutron Star?", "TÜBİTAK Bilim Genç — Nötron Yıldızı Nedir?", "https://bilimgenc.tubitak.gov.tr/makale/notron-yildizi-nedir"),
            ),
        ),
        make_article(
            (
                "Yıldız yüzeylerindeki dev gaz hareketlerini araştırmak",
                "Studying Giant Gas Motions on Stellar Surfaces",
            ),
            (
                "Teleskop gözlemleri yıldız atmosferlerindeki kabarcıkları, gaz akışlarını ve enerji taşınımını ortaya çıkarabilir.",
                "Telescope observations can reveal bubbles, gas flows, and energy transport in stellar atmospheres.",
            ),
            (
                "TÜBİTAK Bilim Genç'in aktardığı R Doradus gözlemleri, Güneş dışındaki bir yıldızın yüzeyindeki büyük gaz kabarcıklarını ayrıntılı biçimde gösterdi. Bu hareketler, yıldız içindeki enerjinin yüzeye taşınmasıyla ilişkilidir. Farklı dalga boylarındaki teleskop ölçümleri ve yıldız tayfları bu süreçlerin anlaşılmasına katkıda bulunur.",
                "Observations of R Doradus reported by TÜBİTAK Bilim Genç resolved large gas bubbles on the surface of a star other than the Sun. These motions are related to energy transport from a star's interior to its surface. Telescope observations at different wavelengths and stellar spectra help researchers understand the process.",
            ),
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200",
            (TUBITAK_BUBBLES, NASA_STARS[0]),
        ),
        make_article(
            (
                "Expedition 1 ekibi ISS'te araştırma dönemini başlattı",
                "The Expedition 1 Crew Begins Research Aboard the ISS",
            ),
            (
                "2000'de ISS'e yerleşen ilk sürekli ekip, istasyon araştırmalarının temelini kurdu.",
                "The first permanent crew, arriving at the ISS in 2000, established the basis for station research.",
            ),
            (
                "William Shepherd, Yuri Gidzenko ve Sergei Krikalev'den oluşan Expedition 1, 2 Kasım 2000'de Uluslararası Uzay İstasyonu'na ulaştı. Mürettebat istasyonun sistemlerini devreye alarak yörüngede kesintisiz insan varlığını ve uzun süreli bilimsel araştırmaları başlattı.",
                "Expedition 1, consisting of William Shepherd, Yuri Gidzenko, and Sergei Krikalev, arrived at the International Space Station on November 2, 2000. The crew activated station systems and began continuous human presence and long-duration research in orbit.",
            ),
            "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=1200",
            (
                ("NASA — International Space Station", "NASA — Uluslararası Uzay İstasyonu", "https://www.nasa.gov/international-space-station/"),
            ),
        ),
        make_article(
            (
                "Perseverance'ın Mars bilim ekibi",
                "The Perseverance Mars Science Team",
            ),
            (
                "2020'de fırlatılan gezginin ekibi Jezero Krateri'ni ve eski yaşam koşullarına ilişkin izleri araştırıyor.",
                "The rover launched in 2020; its team studies Jezero Crater and clues to ancient habitable environments.",
            ),
            (
                "NASA'nın Perseverance gezgini 30 Temmuz 2020'de fırlatıldı ve 2021'de Jezero Krateri'ne indi. Bilim ekibi, Mars'ın jeolojik geçmişini inceliyor ve gelecekte Dünya'ya getirilebilecek kaya örneklerini topluyor. Bu görev, gezegen bilimi, mühendislik ve örnek analizi ekiplerinin ortak çalışmasına dayanır.",
                "NASA's Perseverance rover launched on July 30, 2020, and landed in Jezero Crater in 2021. Its science team studies Mars's geological past and collects rock samples that could be returned to Earth in the future. The mission brings together planetary science, engineering, and sample-analysis teams.",
            ),
            "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=1200",
            (
                ("NASA — Mars 2020 Perseverance", "NASA — Mars 2020 Perseverance", "https://science.nasa.gov/mission/mars-2020-perseverance/"),
            ),
        ),
    ],
    "inventions": [
        make_article(
            (
                "Uzay teleskopları ve gözlem teknolojileri",
                "Space Telescopes and Observing Technology",
            ),
            (
                "Hubble, SOHO, SDO ve Parker gibi görevler farklı gözlem araçlarıyla uzaydan bilimsel veri topluyor.",
                "Missions such as Hubble, SOHO, SDO, and Parker collect scientific data from space using different instruments.",
            ),
            (
                "Uzay teleskopları ve gözlemevleri, Dünya atmosferinin engellediği veya zayıflattığı ışığı ölçebilir. Hubble 1990'dan beri uzayın optik ve morötesi gözlemlerini yapıyor; SOHO ve SDO Güneş'i sürekli izliyor. Parker Solar Probe, korona içinden geçerek Güneş'e yakın ortamı yerinde ölçtü. Bu araçlar teleskop, tayfölçer, kamera ve iletişim sistemlerindeki mühendislik gelişmelerini temsil eder.",
                "Space telescopes and observatories can measure light that Earth's atmosphere blocks or weakens. Hubble has observed the universe in optical and ultraviolet wavelengths since 1990; SOHO and SDO continuously monitor the Sun. Parker Solar Probe sampled the environment close to the Sun by flying through its corona. These missions represent advances in telescopes, spectrometers, cameras, and communications systems.",
            ),
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
            (
                ("NASA — Hubble", "NASA — Hubble", "https://science.nasa.gov/mission/hubble/"),
                ("NASA — SOHO", "NASA — SOHO", "https://science.nasa.gov/mission/soho/"),
                ("NASA — SDO", "NASA — SDO", "https://science.nasa.gov/mission/sdo/"),
                ("NASA — Parker Solar Probe", "NASA — Parker Solar Probe", "https://science.nasa.gov/mission/parker-solar-probe/"),
            ),
        ),
        make_article(
            (
                "Sputnik'ten Voyager'a: uzay aracı teknolojisi",
                "From Sputnik to Voyager: Spacecraft Technology",
            ),
            (
                "Yörüngeye radyo sinyali gönderen ilk uydudan yıldızlararası uzayda çalışan sondayla, uzay aracı tasarımı gelişti.",
                "Spacecraft design evolved from the first satellite sending radio signals in orbit to a probe operating in interstellar space.",
            ),
            (
                "Sputnik 1, dört anteniyle radyo sinyalleri göndererek iyonosfer ve yörünge çalışmaları için veri sağladı. Apollo 11'in Ay modülü ve örnek toplama araçları insanlı keşfi mümkün kıldı. Voyager sondaları uzak mesafelerden iletişim kurmak için anten, otonom sistem ve uzun ömürlü güç kaynakları taşıdı; ayrıca Voyager Golden Record'u taşıdı. Her görev farklı teknik yenilikleri ve dönemin hedeflerini yansıtır.",
                "Sputnik 1 sent radio signals through four antennas, providing data for ionosphere and orbital studies. Apollo 11's lunar module and sample-collection tools enabled crewed exploration. Voyager probes carried antennas, autonomous systems, and long-lived power sources to communicate across vast distances; they also carried the Voyager Golden Record. Each mission reflects different engineering advances and goals of its era.",
            ),
            "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=1200",
            (
                ("NASA History — Apollo 11", "NASA Tarihi — Apollo 11", "https://www.nasa.gov/mission/apollo-11/"),
                ("NASA/JPL — Voyager", "NASA/JPL — Voyager", "https://voyager.jpl.nasa.gov/"),
                ("NASA History — Sputnik", "NASA Tarihi — Sputnik", "https://www.nasa.gov/history/60-years-ago-sputnik-starts-the-space-age/"),
            ),
        ),
        make_article(
            (
                "Hubble Uzay Teleskobu yörüngeye yerleşti",
                "The Hubble Space Telescope Reaches Orbit",
            ),
            (
                "Hubble, 24 Nisan 1990'da fırlatılarak atmosferin dışından evreni gözlemlemeye başladı.",
                "Hubble launched on April 24, 1990, and began observing the universe from above the atmosphere.",
            ),
            (
                "Uzay Mekiği Discovery, Hubble Uzay Teleskobu'nu 24 Nisan 1990'da yörüngeye taşıdı. Atmosferin bulanıklaştırıcı etkisinin üzerindeki konumu, evrenin keskin görüntülerini elde etmesini sağladı. Yörüngede bakım yapılabilecek biçimde tasarlanması, teleskobun görevini sürdürmesine yardımcı oldu.",
                "Space Shuttle Discovery carried the Hubble Space Telescope to orbit on April 24, 1990. Its position above atmospheric distortion allowed it to capture sharp views of the universe. Its serviceable design helped the telescope continue its mission.",
            ),
            "https://images.unsplash.com/photo-1484589065579-248aad0d8b13?w=1200",
            (
                ("NASA — Hubble Space Telescope", "NASA — Hubble Uzay Teleskobu", "https://science.nasa.gov/mission/hubble/"),
            ),
        ),
        make_article(
            (
                "ISS: yörüngedeki modüler laboratuvar",
                "The ISS: A Modular Laboratory in Orbit",
            ),
            (
                "Uluslararası Uzay İstasyonu, farklı ülkelerin modüllerini birleştirerek uzun süreli mikro yerçekimi araştırmalarına olanak verdi.",
                "The International Space Station combined modules from multiple countries to enable long-term microgravity research.",
            ),
            (
                "Uluslararası Uzay İstasyonu, yörüngede birleştirilen modüllerden oluşan bir araştırma laboratuvarıdır. 2000'de ilk sürekli mürettebatın gelişiyle istasyonda aralıksız insanlı araştırma dönemi başladı. Mikro yerçekimi deneyleri biyoloji, fizik, malzeme bilimi ve uzayda yaşam sistemleri alanlarını kapsar.",
                "The International Space Station is a research laboratory assembled in orbit from modules. With the arrival of its first permanent crew in 2000, continuous human research began aboard the station. Microgravity experiments span biology, physics, materials science, and life-support systems.",
            ),
            "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=1200",
            (
                ("NASA — International Space Station", "NASA — Uluslararası Uzay İstasyonu", "https://www.nasa.gov/international-space-station/"),
            ),
        ),
    ],
    "debris": [
        make_article(
            (
                "Uzay çöpleri: yörüngedeki görünmeyen tehlike",
                "Space Debris: The Hidden Hazard in Orbit",
            ),
            (
                "İşlevini yitirmiş uydular, roket parçaları ve çarpışma kalıntıları çalışan uzay araçları için risk oluşturur.",
                "Inactive satellites, rocket parts, and collision fragments pose risks to operational spacecraft.",
            ),
            (
                "Uzay enkazı; görevini tamamlamış araçları, roket gövdelerini ve parçalanma ya da çarpışmalardan kalan yapay parçaları kapsar. Yüksek yörünge hızlarında küçük parçalar bile uydılara ve ISS'e zarar verebilir. İzleme, çarpışmadan kaçınma, görev sonu yörüngeden çıkarma ve enkazı azaltmaya yönelik tasarım çözümleri birlikte önem taşır. Kessler Sendromu, çarpışmaların yeni enkaz üretip riski artırabileceği bir senaryodur; kaçınılmaz bir gelecek olayı değildir.",
                "Orbital debris includes retired spacecraft, rocket bodies, and fragments from breakups or collisions. At orbital speeds, even small pieces can damage satellites and the ISS. Tracking, collision avoidance, end-of-mission disposal, and debris-mitigation design all matter. The Kessler syndrome describes a possible cascade in which collisions create more debris; it is not an inevitable outcome.",
            ),
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
            (NASA_DEBRIS, ESA_DEBRIS_REPORT, ESA_DEBRIS_STATS),
        ),
        make_article(
            (
                "2026 uzay enkazı verileri ve ne anlattıkları",
                "2026 Orbital Debris Figures and What They Mean",
            ),
            (
                "ESA'nın 2026 raporundaki katalog sayıları ile küçük enkaz parçalarının model tahminleri farklı ölçümlerdir.",
                "The 2026 ESA report's catalog counts and model estimates for small debris refer to different measurements.",
            ),
            (
                "Paylaşılan araştırma metni; 14 Ekim 2026 tarihli istatistiklerde yaklaşık 47.140 kataloglanmış cisim, 17.400 tondan fazla toplam yörünge kütlesi ve daha küçük parçalar için model tahminleri bildiriyor. Kataloglanan cisimlerin tümü enkaz değildir; faal uydular da toplama dahildir. 1–10 cm ve milimetre boyutundaki parça sayıları tek tek sayım değil, istatistiksel tahminlerdir. Bu rakamlar ESA'nın belirtilen tarihli sayfasından kontrol edilmelidir; canlı istatistikler değişebilir.",
                "The supplied research text reports about 47,140 cataloged objects, more than 17,400 tonnes of total orbital mass, and model estimates for smaller fragments in statistics dated October 14, 2026. Not every cataloged object is debris; active satellites are included. Counts for 1–10 cm and millimeter-sized fragments are statistical estimates, not individual detections. Check the cited ESA page for the stated date because live statistics change.",
            ),
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
            (ESA_DEBRIS_STATS, ESA_DEBRIS_REPORT, NASA_DEBRIS),
        ),
        make_article(
            (
                "Uzay enkazı: tarihçe ve azaltma çalışmaları",
                "Orbital Debris: History and Mitigation",
            ),
            (
                "Sputnik 1, Fengyun-1C ve Iridium 33–Cosmos 2251 olayları, yörüngedeki faaliyetlerin enkazı nasıl etkilediğini gösterir.",
                "Sputnik 1, Fengyun-1C, and the Iridium 33–Cosmos 2251 collision illustrate how activity can add debris to orbit.",
            ),
            (
                "1957'de Sputnik 1'in fırlatılması uydu çağını başlattı. 2007'de Fengyun-1C'nin imhası ve 2009'da Iridium 33 ile Cosmos 2251'in çarpışması çok sayıda enkaz parçası oluşturdu. ESA'nın Zero Debris yaklaşımı, gelecekteki görevlerden kaynaklanan enkazı azaltmayı hedefler; mevcut bütün enkazın 2030'a kadar temizleneceği anlamına gelmez. Aktif enkaz kaldırma, görev sonu bertarafı ve yeniden giriş güvenliği de çözüm çalışmalarındandır.",
                "Sputnik 1's launch in 1957 began the satellite era. The 2007 destruction of Fengyun-1C and the 2009 Iridium 33–Cosmos 2251 collision generated many debris fragments. ESA's Zero Debris approach aims to reduce debris from future missions; it does not mean all existing debris will be removed by 2030. Active removal, end-of-mission disposal, and safe re-entry are also part of mitigation.",
            ),
            "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=1200",
            (ESA_DEBRIS_REPORT, NASA_DEBRIS),
        ),
    ],
    "stars": [
        make_article(
            (
                "Güneş: geçmişten geleceğe bir yıldızın hikâyesi",
                "The Sun: A Star's Story from Past to Future",
            ),
            (
                "Güneş yaklaşık 4,6 milyar yaşında, hidrojen füzyonuyla enerji üreten ve Güneş Sistemi kütlesinin büyük bölümünü taşıyan bir yıldızdır.",
                "The Sun is about 4.6 billion years old, generates energy through hydrogen fusion, and contains most of the solar system's mass.",
            ),
            (
                "Güneş, yaklaşık 4,6 milyar yıl önce Güneş Bulutsusu adı verilen gaz ve toz bulutunun kütleçekimiyle çökmesiyle oluştu. Merkeze doğru biriken madde sıkışıp ısındı; yeterli sıcaklık ve basınç oluştuğunda hidrojen çekirdekleri birleşerek helyuma dönüşmeye başladı. Bu füzyon bugün de Güneş'in ışık ve ısısının kaynağıdır. Güneş Sistemi'nin toplam kütlesinin yaklaşık yüzde 99,86'sını taşır ve gezegenleri kütleçekimiyle yörüngelerinde tutar.\n\nGüneş'in çapı yaklaşık 1,39 milyon kilometredir; Dünya'ya ortalama uzaklığı 150 milyon kilometredir. Görünür fotosferinin sıcaklığı yaklaşık 5.500 °C, çekirdeğinin sıcaklığı yaklaşık 15 milyon °C'dir. Işığın Güneş'ten Dünya'ya ulaşması yaklaşık 8 dakika 20 saniye sürer. Enerji merkezden önce ışınımla, sonra sıcak maddenin hareketleriyle taşınır. Dış atmosferi olan korona, görünür yüzeyden çok daha sıcak olabilir; bu fark Güneş fiziğinin araştırma konularından biridir.\n\nBugün Güneş, çekirdeğindeki hidrojenin çoğunu helyuma dönüştürdüğü ana kol evresindedir. Yüzeydeki Güneş lekeleri daha soğuk ve güçlü manyetik alanlı bölgelerdir; genel manyetik etkinlik yaklaşık 11 yıllık döngüyle değişir. Patlamalar ve koronal kütle atımları uyduları, haberleşmeyi ve elektrik altyapısını etkileyebilen uzay havası olaylarıdır. Bitkiler fotosentez için Güneş ışığını kullanır; Güneş enerjisi su döngüsünü ve iklimi de yönlendirir. Morötesi ışınlar ise korunmasız cilt ve gözlere zarar verebilir.\n\nYaklaşık 5 milyar yıl sonra çekirdekteki hidrojen azalınca Güneş'in dış katmanları genişleyerek kırmızı deve dönüşecek. Merkür ve Venüs'ün yutulması bekleniyor; Dünya'nın o aşamadaki kesin durumu belirsiz olsa da artan parlaklık yaşam koşullarını çok daha önce zorlaştırabilir. Sonrasında dış katmanlar uzaya atılacak ve sıcak çekirdek beyaz cüce olarak kalacak. Güneş'in kütlesi süpernova patlaması için yeterli değildir. SOHO (1995), SDO (2010), Parker Solar Probe (2018; 2021'de ilk korona geçişi) ve Solar Orbiter (2020) bu yıldızın farklı katmanlarını ve etkinliğini araştırıyor.",
                "The Sun formed about 4.6 billion years ago when a cloud of gas and dust called the solar nebula collapsed under gravity. Matter gathered and heated at its center; once temperature and pressure were high enough, hydrogen nuclei began fusing into helium. That fusion still powers the Sun's light and heat. The Sun contains about 99.86 percent of the solar system's mass and holds planets in orbit through gravity.\n\nThe Sun is about 1.39 million kilometers across and averages 150 million kilometers from Earth. Its visible photosphere is about 5,500 °C, while its core reaches about 15 million °C. Sunlight takes about 8 minutes and 20 seconds to reach Earth. Energy moves outward first through radiation and then through the motion of hot gas. The corona, the outer atmosphere, can be much hotter than the visible surface; explaining this difference remains an area of solar physics.\n\nToday the Sun is in its main-sequence phase, fusing hydrogen into helium in its core. Sunspots are cooler regions associated with strong magnetic fields; overall magnetic activity varies on an approximately 11-year cycle. Flares and coronal mass ejections create space-weather events that can affect satellites, communications, and power infrastructure. Plants use sunlight for photosynthesis, and solar energy drives the water cycle and climate. Ultraviolet radiation can also harm unprotected skin and eyes.\n\nIn about five billion years, as core hydrogen declines, the Sun's outer layers will expand and it will become a red giant. Mercury and Venus are expected to be engulfed; Earth's exact fate is uncertain, although increasing brightness may make conditions hostile to life much earlier. The Sun will later shed its outer layers, leaving a hot white-dwarf core. Its mass is insufficient for a supernova. SOHO (1995), SDO (2010), Parker Solar Probe (2018; first coronal crossing in 2021), and Solar Orbiter (2020) study different parts and activity of our star.",
            ),
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200",
            (
                ("NASA Science — Sun Facts", "NASA Science — Güneş Bilgileri", "https://science.nasa.gov/sun/facts/"),
                ("NASA — SOHO", "NASA — SOHO", "https://science.nasa.gov/mission/soho/"),
                ("NASA — Solar Dynamics Observatory", "NASA — Solar Dynamics Observatory", "https://science.nasa.gov/mission/sdo/"),
                ("NASA — Parker Solar Probe", "NASA — Parker Solar Probe", "https://science.nasa.gov/mission/parker-solar-probe/"),
                ("NASA — Solar Orbiter", "NASA — Solar Orbiter", "https://science.nasa.gov/mission/solar-orbiter/"),
            ),
        ),
        make_article(
            (
                "Yıldızların spektral sınıfları",
                "Stellar Spectral Classes",
            ),
            (
                "O, B, A, F, G, K, M sıralaması yıldızları yüzey sıcaklığı ve tayf özelliklerine göre en sıcaktan en soğuğa dizer.",
                "The O, B, A, F, G, K, M sequence orders stars from hottest to coolest by surface temperature and spectral features.",
            ),
            (
                "Bir yıldızın ışığı tayfölçerle dalga boylarına ayrıldığında, hangi renklerin ne kadar güçlü olduğu ve atmosferde hangi dalga boylarının soğurulduğu görülür. Bu çizgiler yıldızın yüzey sıcaklığına ve kimyasal bileşimine ilişkin ipucu verir. En sıcaktan en soğuğa doğru O, B, A, F, G, K, M sırası kullanılır: O mavi, B mavi-beyaz, A beyaz, F sarı-beyaz, G sarı, K turuncu, M kırmızı görünür. Güneş yaklaşık 5.500 °C yüzey sıcaklığıyla G2 sınıfındadır.\n\nSınıflandırmada renk tek başına yeterli değildir. Örneğin hidrojen soğurma çizgileri A sınıfı tayflarda özellikle belirgindir; farklı sıcaklıklarda başka atomların veya moleküllerin çizgileri öne çıkar. Harfin yanındaki 0–9 alt sınıfı aynı harf grubundaki sıcaklık farklarını gösterir; G2, G sınıfının sıcak tarafındadır. Spektral sınıf parlaklık sınıfı, büyüklük ya da yaş anlamına gelmez: aynı sıcaklık sınıfında ana dizi yıldızı, dev veya süperdev bulunabilir.\n\nSistem 19. yüzyıldaki tayf gözlemlerinin birikimiyle gelişti. Harvard College Gözlemevi'nde Annie Jump Cannon çok sayıda yıldız tayfını düzenledi ve bugün kullanılan sıralamanın yaygınlaşmasında belirleyici rol oynadı. Yer teleskoplarıyla uzay teleskoplarının farklı dalga boylarındaki ölçümleri, yıldızların sıcaklıklarını karşılaştırmaya ve evrimlerini anlamaya devam ediyor.",
                "A spectrograph separates starlight into wavelengths, showing how much light occurs at each color and which wavelengths are absorbed in the star's atmosphere. These lines reveal clues about surface temperature and chemical composition. The sequence from hottest to coolest is O, B, A, F, G, K, M: O stars appear blue, B blue-white, A white, F yellow-white, G yellow, K orange, and M red. The Sun is a G2 star with a surface temperature of about 5,500 °C.\n\nColor alone does not determine the classification. For example, hydrogen absorption lines are especially prominent in A-type spectra, while lines from other atoms or molecules become important at different temperatures. A 0–9 subclass indicates a finer temperature position within a letter group; G2 is on the hotter side of class G. Spectral class does not mean luminosity class, size, or age: stars with similar temperatures can be main-sequence stars, giants, or supergiants.\n\nThe system developed from accumulating spectral observations in the 19th century. At Harvard College Observatory, Annie Jump Cannon organized the spectra of many stars and played a major role in popularizing the sequence used today. Measurements from ground-based and space telescopes across different wavelengths continue to help compare stellar temperatures and understand stellar evolution.",
            ),
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200",
            (
                NASA_STARS[0],
                NASA_STARS[1],
                ("Encyclopaedia Britannica — Stellar Classification", "Encyclopaedia Britannica — Yıldızların Tayfsal Sınıflandırılması", "https://www.britannica.com/science/stellar-classification"),
            ),
        ),
        make_article(
            (
                "İkili yıldız sistemleri",
                "Binary Star Systems",
            ),
            (
                "Kütleçekimle bağlı iki yıldız ortak kütle merkezleri çevresinde döner; yörünge ve parlaklık ölçümleri yıldızların özelliklerini ortaya çıkarır.",
                "Two gravitationally bound stars orbit a shared center of mass; measurements of their motion and brightness reveal their properties.",
            ),
            (
                "İkili yıldız, kütleçekimle bağlı iki yıldızın ortak kütle merkezleri çevresinde dairesel ya da elips yörüngelerde dolandığı sistemdir. Dünya'dan tek yıldız gibi görünseler bile birbirlerinin hareketini etkilerler. Kütle, sıcaklık, parlaklık ve büyüklükleri farklı olabilir; yakın çiftlerde bir yıldızdan diğerine gaz aktarılabilir. Bir yıldız kırmızı dev, süperdev veya beyaz cüce evresine geçerken eşinin evrimi de bu etkileşimlerden etkilenebilir.\n\nYörüngesi görüş doğrultumuza uygun örtülen ikililerde yıldızlar sırayla birbirlerinin önünden geçer ve toplam parlaklık düzenli olarak azalır. Işık eğrisi ile tayf çizgilerindeki Doppler hareketi birlikte kullanılarak yıldızların kütleleri, çapları ve yörünge süreleri hesaplanabilir. Beyaz cüce eşinden madde çekerse nova parlamaları görülebilir; iki nötron yıldızlı sistemler kütleçekim dalgaları yayarak birleşebilir. Büyük kütleli yıldız rüzgârlarının çarpışması WR 140 gibi sistemlerde toz üretir.\n\nGezegenler bir yıldızın çevresinde veya iki yıldızın ortak kütle merkezi çevresinde dolanabilir. Bu yıldız çiftleri, kütle ve yarıçap ölçümü için doğal laboratuvar olduğu kadar gezegenlerin oluşabileceği koşulları anlamak için de önemlidir. NASA'nın TESS verileri örtülen ikilileri ve olası gezegenleri araştırmada kullanılır; James Webb'in WR 140 gözlemleri yıldız rüzgârlarının çarpışmasını incelemeye yardımcı olur.",
                "A binary star is a system in which two gravitationally bound stars orbit their shared center of mass along circular or elliptical paths. They may look like one star from Earth, yet their motions affect each other. Their masses, temperatures, brightness, and sizes can differ; in close pairs, gas may flow from one star to the other. When one star evolves into a red giant, supergiant, or white dwarf, these interactions can affect its companion's evolution.\n\nIn an eclipsing binary whose orbit is aligned with our line of sight, the stars pass in front of each other and the combined brightness falls regularly. Combining the light curve with Doppler shifts in spectral lines lets astronomers calculate stellar masses, diameters, and orbital periods. A white dwarf drawing matter from its companion can produce nova outbursts; systems containing two neutron stars can emit gravitational waves as they merge. Colliding winds from massive stars create dust in systems such as WR 140.\n\nPlanets can orbit one star or the shared center of mass of both stars. Binary systems are natural laboratories for measuring stellar masses and radii, and help researchers understand the conditions in which planets can form. NASA's TESS data are used to investigate eclipsing binaries and possible planets; James Webb observations of WR 140 help study colliding stellar winds.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Multiple Star Systems", "NASA — Çoklu Yıldız Sistemleri", "https://science.nasa.gov/universe/stars/multiple-star-systems/"),
                ("NASA — Binary Stars", "NASA — İkili Yıldızlar", "https://science.nasa.gov/category/universe/stars/binary-stars/"),
                ("NASA Webb — WR 140", "NASA Webb — WR 140", "https://science.nasa.gov/asset/webb/wr-140-binary-system-top-view/"),
                ("TÜBİTAK Bilim Genç — Planets with Two Suns?", "TÜBİTAK Bilim Genç — İki Yıldıza Sahip Gezegenler Var mı?", "https://bilimgenc.tubitak.gov.tr/makale/iki-yildiza-sahip-gezegenler-var-mi"),
                ("Encyclopaedia Britannica — Binary Star", "Encyclopaedia Britannica — İkili Yıldız", "https://www.britannica.com/science/binary-star"),
            ),
        ),
        make_article(
            (
                "Ana dizi yıldızları ve yıldız dengesi",
                "Main-Sequence Stars and Stellar Balance",
            ),
            (
                "Yıldızlar ömürlerinin büyük bölümünde çekirdeklerinde hidrojen füzyonu yapar; kütleleri parlaklıklarını ve ömürlerini güçlü biçimde etkiler.",
                "Stars spend most of their lives fusing hydrogen in their cores; mass strongly affects their luminosity and lifetime.",
            ),
            (
                "Ana dizi, yıldızların yaşamlarının büyük bölümünü geçirdiği kararlı evredir: çekirdeklerinde hidrojen füzyonuyla helyum üretirler. Hertzsprung–Russell diyagramında yıldızların sıcaklık ve parlaklıklarına göre dizildiği ana banttır. Yıldızın içe doğru kütleçekimiyle füzyondan kaynaklanan dışa doğru gaz ve ışınım basıncı birbirini dengeleyerek hidrostatik dengeyi kurar.\n\nGüneş benzeri yıldızlarda proton-proton zinciri başlıca enerji kaynağıdır. Daha kütleli ve sıcak yıldızlarda karbon, azot ve oksijeni katalizör olarak kullanan CNO döngüsü baskın hâle gelir. Spektral sınıflar O, B, A, F, G, K ve M biçiminde en sıcaktan en soğuğa sıralanır. Başlangıç kütlesi hem parlaklığı hem de yakıt tüketim hızını belirler: büyük kütleli yıldızlar daha parlak olsa da yakıtlarını hızla tüketip ana diziden daha erken ayrılır; düşük kütleli kırmızı cüceler çok uzun ömürlü olabilir.\n\nKütle-parlaklık ilişkisi için L ∝ M^3.5 sık kullanılan yaklaşık bir anlatımdır. Gerçek ilişki yıldızın kütle aralığına ve özelliklerine göre değiştiğinden bu bağıntı kesin, her durumda geçerli bir yasa gibi okunmamalıdır. Ana dizi yıldızlarının karşılaştırılması yıldızların yaşını, gelecekteki evrimini ve galaksilerin yıldız topluluklarını anlamaya yardımcı olur.",
                "The main sequence is the stable phase in which stars spend most of their lives producing helium by fusing hydrogen in their cores. On the Hertzsprung–Russell diagram it forms the main band where stars are arranged by temperature and luminosity. Inward gravity balances the outward gas and radiation pressure produced by fusion, establishing hydrostatic equilibrium.\n\nThe proton–proton chain is the main energy source in Sun-like stars. In hotter, more massive stars, the CNO cycle, which uses carbon, nitrogen, and oxygen as catalysts, becomes dominant. Spectral classes run from hottest to coolest as O, B, A, F, G, K, M. Initial mass determines both luminosity and the rate at which fuel is consumed: massive stars are brighter but use fuel quickly and leave the main sequence sooner, while low-mass red dwarfs can live for a very long time.\n\nThe mass–luminosity relation is often summarized approximately as L ∝ M^3.5. The actual relation varies with mass range and stellar properties, so this should not be treated as an exact universal law. Comparing main-sequence stars helps researchers understand stellar ages, future evolution, and the stellar populations of galaxies.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            NASA_STARS,
        ),
        make_article(
            (
                "Beyaz cüceler: yıldızların yoğun kalıntıları",
                "White Dwarfs: Dense Stellar Remnants",
            ),
            (
                "Güneş benzeri yıldızların dış katmanlarını atmasından sonra kalan sıcak çekirdek beyaz cüceye dönüşür.",
                "After Sun-like stars shed their outer layers, the remaining hot core becomes a white dwarf.",
            ),
            (
                "Güneş benzeri düşük ve orta kütleli bir yıldız çekirdeğindeki yakıtı tüketince genişleyerek kırmızı dev olur. Helyum füzyonu karbon ve oksijen üretir; yıldız yeterince kütleli değilse karbonu yakacak sıcaklığa erişemez. Dış katmanları yıldız rüzgârlarıyla uzaya savrulur ve merkezdeki sıcak çekirdek görünür hâle gelir. Bu gaz bulutu çekirdeğin morötesi ışığıyla parlayarak gezegenimsi bulutsu oluşturabilir; geride kalan çekirdek beyaz cücedir.\n\nBeyaz cüce artık çekirdeğinde hidrojen füzyonuyla enerji üretmez. Yaklaşık Güneş kütlesini Dünya boyutlarında bir hacme sığdırabilir. Yıldız maddesi sıkışırken elektronlar aynı kuantum durumunu paylaşamadığından elektron dejenere basıncı çökmeye karşı koyar. Bu destek yaklaşık 1,4 Güneş kütlesindeki Chandrasekhar sınırına kadar yeterlidir. Yakın eşinden madde toplayan bir beyaz cüce sınırına yaklaşırsa Tip Ia süpernova patlaması gibi sonuçlar doğabilir; bu her beyaz cücenin başına gelecek bir son değildir.\n\nYeni nükleer enerji kaynağı olmadan beyaz cüce milyarlarca yıl yavaşça soğur. Kuramsal olarak çok uzak gelecekte kara cüceye dönüşebilir, ancak evren henüz bu aşamanın oluşmasına yetecek kadar yaşlı değildir. Sirius B kütle- yarıçap ilişkisi ve kütleçekimsel kırmızıya kayma araştırmalarında önemli bir örnektir. Janus'un yüzeyinde hidrojen ve helyum bakımından farklı iki bölge gözlenmiştir; güçlü, asimetrik manyetik alanların rolü araştırılmaktadır.",
                "When a low- or intermediate-mass star like the Sun uses up its core fuel, it expands into a red giant. Helium fusion produces carbon and oxygen; if the star is not massive enough, its core cannot reach the temperature needed to fuse carbon. Stellar winds expel the outer layers into space, exposing the hot core. The gas can glow as a planetary nebula under ultraviolet radiation from the core; the remaining core is a white dwarf.\n\nA white dwarf no longer produces energy through core hydrogen fusion. It can pack roughly a Sun's mass into a volume about the size of Earth. As stellar matter is compressed, electrons cannot share the same quantum state, and electron degeneracy pressure resists collapse. This support is limited by the Chandrasekhar limit, about 1.4 solar masses. A white dwarf accreting material from a close companion and approaching the limit can lead to outcomes such as a Type Ia supernova; this is not the fate of every white dwarf.\n\nWithout a new nuclear energy source, a white dwarf cools slowly for billions of years. In theory it may eventually become a black dwarf, but the universe is not old enough for this stage to have occurred. Sirius B is an important example for studying the mass–radius relation and gravitational redshift. Janus has two surface regions with different hydrogen and helium abundances; researchers are investigating the role of its strong asymmetric magnetic field.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                NASA_STARS[0],
                ("NASA Imagine — White Dwarfs", "NASA Imagine — Beyaz Cüceler", "https://imagine.gsfc.nasa.gov/science/objects/dwarfs1.html"),
                ("TÜBİTAK Bilim Genç — Janus", "TÜBİTAK Bilim Genç — İki Yüzlü Yıldız Keşfedildi", "https://bilimgenc.tubitak.gov.tr/makale/iki-yuzlu-yildiz-kesfedildi"),
                ("TÜBİTAK Bilim Genç — White Dwarf Evolution", "TÜBİTAK Bilim Genç — Beyaz Cücelerin Serüveni", "https://bilimgenc.tubitak.gov.tr/makale/beyaz-cucelerin-kara-cuceye-donusmeseruveni"),
                ("Encyclopaedia Britannica — White Dwarf", "Encyclopaedia Britannica — Beyaz Cüce", "https://www.britannica.com/science/white-dwarf-star"),
            ),
        ),
        make_article(
            (
                "Nötron yıldızları, atarcalar ve magnetarlar",
                "Neutron Stars, Pulsars, and Magnetars",
            ),
            (
                "Büyük yıldızların çöken çekirdekleri şehir ölçeğinde, olağanüstü yoğun yıldız kalıntıları bırakabilir.",
                "The collapsing cores of massive stars can leave extraordinarily dense stellar remnants about the size of a city.",
            ),
            (
                "Büyük kütleli bir yıldızın çekirdeği kendi kütleçekimi altında çöktüğünde, çoğu durumda dış katmanları süpernova patlamasıyla uzaya saçılır ve çok yoğun çekirdek kalıntısı oluşur. Nötron yıldızının çapı çoğunlukla yaklaşık 20 km, kütlesi ise Güneş'inkinin bir ila iki katı veya daha fazlasıdır. Çökme sırasında protonlar ile elektronların birleşmesi nötron oluşumuna katkı verir; maddenin bu aşırı yoğunlukta tam olarak nasıl davrandığı hâlâ araştırılıyor.\n\nNötron yıldızları radyo, X-ışını ve gama ışını dalga boylarında gözlenir. Hızlı dönen ve ışınım demetleri dönme sırasında Dünya'ya yöneldiğinde düzenli sinyaller verdiği için gözlenen türlerine pulsar, Türkçede atarca denir. Çok güçlü manyetik alana sahip olanlar magnetardır. 1967'de Jocelyn Bell Burnell'in düzenli radyo darbelerini keşfetmesi, pulsarların ve nötron yıldızlarının varlığına ilişkin ilk önemli gözlemsel kanıtlardan birini sağladı.\n\nNASA'nın NICER aygıtı Uluslararası Uzay İstasyonu'ndan gelen X-ışınlarını ölçerek yıldızların boyutlarını ve iç yapısını sınırlar. İkili nötron yıldızlarının yörünge hareketi kütleçekim dalgalarıyla enerji kaybını ve birleşmeye doğru ilerlemeyi gösterir. Bu birleşmeler ağır elementlerin oluşumu ve yayılımı hakkında da bilgi verebilir.",
                "When the core of a massive star collapses under its own gravity, the outer layers are often expelled in a supernova, leaving an extremely dense remnant. A neutron star is typically about 20 km across but can contain one to more than two solar masses. During collapse, protons and electrons combine to help form neutrons; how matter behaves at these extreme densities remains an active research question.\n\nNeutron stars are observed in radio, X-ray, and gamma-ray wavelengths. Rapidly rotating stars whose radiation beams sweep toward Earth as regular signals are called pulsars. Those with exceptionally strong magnetic fields are magnetars. In 1967 Jocelyn Bell Burnell discovered regular radio pulses, providing one of the first major observational indications of pulsars and neutron stars.\n\nNASA's NICER instrument measures X-rays from the International Space Station to constrain neutron-star sizes and interiors. Orbital motion in binary neutron-star systems reveals energy loss through gravitational waves and gradual inspiral toward a merger. Such mergers can also inform researchers about the formation and dispersal of heavy elements.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Neutron Stars Are Weird", "NASA — Nötron Yıldızları Çok İlginç", "https://science.nasa.gov/universe/stories/quick-reads/neutron-stars-are-weird/"),
                NASA_STARS[1],
                ("NASA — Neutron Stars", "NASA — Nötron Yıldızları", "https://science.nasa.gov/neutron-stars/"),
                ("TÜBİTAK Bilim Genç — What Is a Neutron Star?", "TÜBİTAK Bilim Genç — Nötron Yıldızı Nedir?", "https://bilimgenc.tubitak.gov.tr/makale/notron-yildizi-nedir"),
                ("TÜBİTAK Bilim Genç — Neutron Star Density", "TÜBİTAK Bilim Genç — Nötron Yıldızları Çok Yoğundur", "https://bilimgenc.tubitak.gov.tr/makale/notron-yildizlari-cok-yogundur"),
                ("Encyclopaedia Britannica — Neutron Star", "Encyclopaedia Britannica — Nötron Yıldızı", "https://www.britannica.com/science/neutron-star"),
            ),
        ),
        make_article(
            (
                "Dev ve süperdev yıldızlar",
                "Giant and Supergiant Stars",
            ),
            (
                "Yıldızlar evrimlerinin ileri evrelerinde genişleyebilir; süperdevlerin sıcaklık, parlaklık ve yarıçapları çok farklı olabilir.",
                "Stars can expand in later evolutionary stages; supergiants vary greatly in temperature, luminosity, and radius.",
            ),
            (
                "Yıldızın çekirdeğinde yakıt azaldıkça basınç ve kütleçekim dengesi değişir; dış katmanlar büyük ölçüde genişleyebilir. Yüzey genişleyip soğuduğunda yıldız kırmızımsı görünür ve kırmızı dev ya da kırmızı süperdev evresine geçebilir. Mavi süperdevler ise çok yüksek yüzey sıcaklığına ve parlaklığa sahip, genellikle büyük kütleli yıldızlardır. Mavi rengin kırmızıya göre daha yüksek sıcaklığa işaret etmesi yıldız ışığının tayfsal ölçümleriyle doğrulanır.\n\nUY Scuti gibi kırmızı süperdevlerin yarıçapı Güneş'le karşılaştırılır; verilen değerler yıldız atmosferinin, uzaklığın ve ölçüm yönteminin belirsizliklerinden etkilenebilir. Bu nedenle “en büyük yıldız” sıralamaları kesin ve değişmez değildir. Stephenson 2-18 de çok büyük süperdev adayları arasında anılır. R Doradus gözlemlerinde Güneş dışındaki bir yıldızın yüzeyinde dev gaz kabarcıkları çözümlenmiştir; bu kabarcıklar yıldız içinden yüzeye enerji taşıyan hareketlerle ilişkilidir.\n\nKütleli yıldızların bir bölümü yaşamlarının sonunda çekirdek çökmesiyle süpernova olabilir. Dış katmanlara yayılan maddeler yeni yıldız ve gezegen sistemlerinin hammaddesine katkı sağlar; merkezde nötron yıldızı ya da kara delik kalabilir. Ancak her dev yıldız aynı biçimde sonlanmaz: sonuç başlangıç kütlesi ve yıldızın evrimiyle belirlenir.",
                "As fuel in a star's core declines, the balance between pressure and gravity changes and the outer layers can expand greatly. The surface cools as it expands, making the star appear reddish as it enters a red-giant or red-supergiant phase. Blue supergiants are very hot, luminous stars that are often massive. Spectral measurements confirm that blue color corresponds to higher surface temperature than red.\n\nThe radii of red supergiants such as UY Scuti are compared with the Sun's, but estimates can be affected by uncertainties in distance, stellar atmospheres, and measurement methods. Rankings of the “largest star” are therefore not fixed facts. Stephenson 2-18 is also mentioned among candidates for very large supergiants. Observations of R Doradus resolved giant gas bubbles on the surface of a star other than the Sun; these are associated with motions that carry energy from the interior to the surface.\n\nSome massive stars end in core-collapse supernovae. Material ejected into space contributes raw material for new stars and planetary systems, while a neutron star or black hole may remain at the center. Not every giant star has the same ending: the outcome depends on its initial mass and evolutionary history.",
            ),
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200",
            (
                NASA_STARS[0],
                NASA_STARS[1],
                ("NASA Glossary — Blue Supergiant", "NASA Sözlüğü — Mavi Süperdev", "https://science.nasa.gov/universe/glossary/"),
                TUA,
                TUBITAK_GIANTS,
                TUBITAK_BUBBLES,
                ("Encyclopaedia Britannica — Star", "Encyclopaedia Britannica — Yıldız", "https://www.britannica.com/science/star-astronomy"),
            ),
        ),
    ],
    "missions": [
        make_article(
            (
                "Güneş görevleri: SOHO, SDO, Parker ve Solar Orbiter",
                "Solar Missions: SOHO, SDO, Parker, and Solar Orbiter",
            ),
            (
                "Dört uzay gözlemevi Güneş'in içini, atmosferini, manyetik alanını ve uzay havasını farklı dönemlerde inceledi.",
                "Four space observatories studied the Sun's interior, atmosphere, magnetic field, and space weather across different eras.",
            ),
            (
                "SOHO ortak NASA–ESA görevi olarak 1995'te fırlatıldı. NASA'nın Solar Dynamics Observatory'si 2010'da göreve başladı. Parker Solar Probe 2018'de fırlatıldı; 2021'de Güneş koronası içinden geçen ilk uzay aracı oldu ve 24 Aralık 2024'te görünür yüzeye yaklaşık 6,2 milyon kilometre yaklaştı. NASA–ESA Solar Orbiter 2020'de fırlatılarak Güneş'in kutupları, manyetik alanı ve uzaya yayılan parçacıkları araştırdı.",
                "The joint NASA–ESA SOHO mission launched in 1995. NASA's Solar Dynamics Observatory began its mission in 2010. Parker Solar Probe launched in 2018, became the first spacecraft to fly through the solar corona in 2021, and passed about 6.2 million km from the visible surface on December 24, 2024. NASA–ESA Solar Orbiter launched in 2020 to study the Sun's poles, magnetic field, and particles flowing into space.",
            ),
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200",
            (
                ("NASA — Sun Facts", "NASA — Güneş Bilgileri", "https://science.nasa.gov/sun/facts/"),
                ("NASA — SOHO", "NASA — SOHO", "https://science.nasa.gov/mission/soho/"),
                ("NASA — SDO", "NASA — SDO", "https://science.nasa.gov/mission/sdo/"),
                ("NASA — Parker Solar Probe", "NASA — Parker Solar Probe", "https://science.nasa.gov/mission/parker-solar-probe/"),
                ("NASA — Solar Orbiter", "NASA — Solar Orbiter", "https://science.nasa.gov/mission/solar-orbiter/"),
            ),
        ),
        make_article(
            (
                "Uzay tarihinden önemli fırlatmalar",
                "Milestone Launches in Spaceflight History",
            ),
            (
                "Sputnik 1, Apollo 11, Voyager 1, Hubble ve Türksat 6A farklı dönemlerde keşif ve uydu teknolojisini ileri taşıdı.",
                "Sputnik 1, Apollo 11, Voyager 1, Hubble, and Türksat 6A advanced exploration and satellite technology in different eras.",
            ),
            (
                "Sputnik 1, 4 Ekim 1957'de fırlatılarak ilk yapay uydu oldu. Apollo 11, 1969'da Ay'a insan indirdi. Voyager 1, 1977'de fırlatıldı ve 2012'de heliopozu geçerek yıldızlararası uzaya ulaşan ilk insan yapımı araç oldu. Hubble, 1990'da yörüngeye yerleşti. Türksat 6A, 8 Temmuz 2024'te fırlatıldı ve Türkiye'nin ilk yerli haberleşme uydusu olarak hizmete girdi. Kart, olay tarihlerini belirtir; bu tarihler seçili arşiv yılıyla aynı olmak zorunda değildir.",
                "Sputnik 1 launched on October 4, 1957, becoming the first artificial satellite. Apollo 11 landed humans on the Moon in 1969. Voyager 1 launched in 1977 and crossed the heliopause in 2012, becoming the first human-made spacecraft to enter interstellar space. Hubble entered orbit in 1990. Türksat 6A launched on July 8, 2024, as Türkiye's first domestically developed communications satellite. The card preserves each event's date; event years need not match the selected archive year.",
            ),
            "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=1200",
            (
                ("NASA — Hubble", "NASA — Hubble", "https://science.nasa.gov/mission/hubble/"),
                ("NASA/JPL — Voyager", "NASA/JPL — Voyager", "https://voyager.jpl.nasa.gov/"),
                ("NASA History — Apollo 11", "NASA Tarihi — Apollo 11", "https://www.nasa.gov/mission/apollo-11/"),
                ("TÜBİTAK UZAY", "TÜBİTAK UZAY", "https://uzay.tubitak.gov.tr/"),
            ),
        ),
        make_article(
            (
                "Tamamlanan keşif görevleri: Cassini'den Rosetta'ya",
                "Completed Exploration Missions: Cassini to Rosetta",
            ),
            (
                "Cassini, Kepler, Opportunity ve Rosetta görevleri 2016–2019 arasında sona erdi; her biri kalıcı bilimsel veriler bıraktı.",
                "Cassini, Kepler, Opportunity, and Rosetta ended between 2016 and 2019, each leaving a lasting scientific legacy.",
            ),
            (
                "Rosetta, 2016'da 67P kuyruklu yıldızına kontrollü inişle sona erdi. Cassini, 15 Eylül 2017'de Satürn atmosferine yönlendirilerek Titan ve Enceladus'un olası kirlenmesi önlendi. Opportunity, 2018'deki Mars toz fırtınasının ardından iletişimi kaybetti; NASA görevi 2019'da sonlandırdı. Kepler, yakıtı tükendiğinde 2018'de bilim faaliyetlerini bitirdi. Bu görev sonları, gezegen koruma ve görev planlamasına örnektir.",
                "Rosetta ended with a controlled descent to comet 67P in 2016. Cassini was directed into Saturn's atmosphere on September 15, 2017, helping avoid possible contamination of Titan and Enceladus. Opportunity lost contact after a 2018 Martian dust storm; NASA ended the mission in 2019. Kepler concluded science operations in 2018 after fuel depletion. These mission endings illustrate planetary protection and mission planning.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Cassini", "NASA — Cassini", "https://science.nasa.gov/mission/cassini/"),
                ("NASA — Kepler", "NASA — Kepler", "https://science.nasa.gov/mission/kepler/"),
                ("NASA — Mars Exploration Rover", "NASA — Mars Exploration Rover", "https://mars.nasa.gov/mer/"),
                ("ESA — Rosetta", "ESA — Rosetta", "https://www.esa.int/Enabling_Support/Operations/Rosetta"),
                ("TÜBİTAK UZAY", "TÜBİTAK UZAY", "https://uzay.tubitak.gov.tr/"),
                ("Türkiye Uzay Ajansı — National Space Program", "Türkiye Uzay Ajansı — Millî Uzay Programı", "https://tua.gov.tr/tr/milli-uzayprogrami"),
            ),
        ),
        make_article(
            (
                "Türkiye'nin uzay teknolojileri",
                "Türkiye's Space Technologies",
            ),
            (
                "BİLSAT, RASAT, İMECE, Türksat 6A ve Ay görevleri Türkiye'nin uzay çalışmalarındaki kilometre taşlarıdır.",
                "BİLSAT, RASAT, İMECE, Türksat 6A, and lunar missions are milestones in Türkiye's space program.",
            ),
            (
                "BİLSAT (2003) ve RASAT (2011) Türkiye'nin gözlem uydusu çalışmalarında erken adımlardı. İMECE, yerli elektro-optik gözlem uydusudur; Türksat 6A ise 2024'te fırlatılan yerli haberleşme uydusudur. Ay Araştırma Programı (AYAP) ve uzay kalifiye alt sistemler, devam eden program başlıklarıdır. Görev durumu ve teknik ayrıntılar değişebileceğinden güncel bilgi için TÜBİTAK UZAY ve Türkiye Uzay Ajansı kaynaklarına bakılmalıdır.",
                "BİLSAT (2003) and RASAT (2011) were early steps in Türkiye's Earth-observation satellite work. İMECE is a domestically developed electro-optical Earth-observation satellite; Türksat 6A is a communications satellite launched in 2024. The Moon Research Program (AYAP) and space-qualified subsystems are ongoing program areas. Mission status and technical details can change, so consult TÜBİTAK UZAY and the Turkish Space Agency for current information.",
            ),
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
            (
                ("TÜBİTAK UZAY", "TÜBİTAK UZAY", "https://uzay.tubitak.gov.tr/"),
                ("Türkiye Uzay Ajansı — National Space Program", "Türkiye Uzay Ajansı — Millî Uzay Programı", "https://tua.gov.tr/tr/milli-uzayprogrami"),
            ),
        ),
        make_article(
            (
                "Expedition 1: ISS'te sürekli insanlı yaşam",
                "Expedition 1: Continuous Human Presence on the ISS",
            ),
            (
                "William Shepherd, Yuri Gidzenko ve Sergei Krikalev 2 Kasım 2000'de ISS'e ulaştı.",
                "William Shepherd, Yuri Gidzenko, and Sergei Krikalev arrived at the ISS on November 2, 2000.",
            ),
            (
                "Expedition 1'in gelişi Uluslararası Uzay İstasyonu'nda kesintisiz insan varlığını başlattı. Ekip, istasyon sistemlerini devreye alıp uzun süreli yörünge araştırmaları için temel hazırladı. İstasyon o tarihten beri dönüşümlü uluslararası ekiplerle kullanılan bir araştırma laboratuvarıdır.",
                "The arrival of Expedition 1 began continuous human presence aboard the International Space Station. The crew activated station systems and established a basis for long-duration orbital research. Since then, the station has served as a research laboratory staffed by rotating international crews.",
            ),
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200",
            (
                ("NASA — International Space Station", "NASA — Uluslararası Uzay İstasyonu", "https://www.nasa.gov/international-space-station/"),
            ),
        ),
    ],
    "black_holes": [
        make_article(
            (
                "Karadelikler: oluşumları ve gözlemlenmeleri",
                "Black Holes: Formation and Observation",
            ),
            (
                "Olay ufkunun içinden ışık kaçamaz; kara delikler çevrelerindeki yıldızların hareketleri ve sıcak gazdan yayılan ışıkla incelenir.",
                "Light cannot escape from within an event horizon; black holes are studied through nearby stars and radiation from hot gas.",
            ),
            (
                "Kara delik, boşluk değil, çok büyük miktarda maddenin çok küçük bir hacimde yoğunlaşmasıyla uzay-zamanın güçlü biçimde eğrildiği bölgedir. Olay ufku, içinden dışarı kaçışın mümkün olmadığı sınırdır. Büyük kütleli yıldızın yakıtı tükendiğinde çekirdeği kendi kütleçekimi altında çökebilir ve yeterince büyükse yıldız kütleli kara delik oluşturabilir. Galaksilerin merkezindeki süper kütleli kara deliklerin nasıl bu kadar büyüdüğü ise açık araştırma konularındandır; gaz biriktirme ve kara delik birleşmeleri olası büyüme yollarıdır.\n\nKara deliğin kendisi ışık yaymadığından doğrudan görünmez. Yakınındaki yıldızların yörüngeleri görünmeyen kütleyi gösterir; kara deliğe düşen gaz ve toz ısınıp birikim diskinde ışınım üretebilir. Bazı aktif sistemlerde güçlü jetler uzaya madde ve enerji taşır. Kara delikler her şeyi uzaktan elektrik süpürgesi gibi çekmez: aynı kütledeki bir cisimle aynı uzaklıkta kütleçekim etkileri karşılaştırılabilir; tehlike çok yakına gelindiğinde ve olay ufkuna yaklaşıldığında ortaya çıkar.\n\nKaradelikler yıldız kütleli ve süper kütleli gibi farklı kütle ölçeklerinde incelenir. Gözlemler görünür ışıkla sınırlı değildir: radyo teleskopları, X-ışını gözlemevleri, yıldız hareketlerinin hassas ölçümü ve kütleçekim dalgaları farklı kanıtlar sağlar. Bu yöntemler birlikte kara deliklerin çevresi, büyümesi ve galaksilerin evrimiyle ilişkisi hakkında bilgi verir.",
                "A black hole is not an empty hole but a region where enormous amounts of matter curve spacetime intensely by being compressed into a small volume. The event horizon marks the boundary from which escape is impossible. When a massive star runs out of fuel, its core can collapse under gravity and, if massive enough, form a stellar-mass black hole. How supermassive black holes at galactic centers grew so large remains an open research question; accretion of gas and mergers are possible growth paths.\n\nA black hole itself emits no light and cannot be seen directly. Orbits of nearby stars reveal invisible mass, while gas and dust falling toward a black hole can heat up and radiate in an accretion disk. Some active systems launch powerful jets that carry matter and energy into space. Black holes do not act like vacuum cleaners that pull in everything from far away: at the same mass and distance, their gravitational effect can be compared with that of any other object; danger arises when matter comes very close to the event horizon.\n\nBlack holes are studied across different mass scales, including stellar-mass and supermassive examples. Observations are not limited to visible light: radio telescopes, X-ray observatories, precise measurements of stellar motion, and gravitational waves provide complementary evidence. Together these methods reveal their surroundings, growth, and relationship to galaxy evolution.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Black Holes", "NASA — Karadelikler", "https://science.nasa.gov/universe/black-holes/"),
                ("NASA — What Are Black Holes?", "NASA — Karadelikler Nedir?", "https://www.nasa.gov/universe/what-are-black-holes/"),
            ),
        ),
        make_article(
            (
                "Sagittarius A* ve Samanyolu'nun merkezi",
                "Sagittarius A* and the Center of the Milky Way",
            ),
            (
                "Samanyolu'nun merkezindeki yaklaşık dört milyon Güneş kütleli kara deliğin ilk görüntüsü 2022'de açıklandı.",
                "The first image of the Milky Way's central black hole, with about four million solar masses, was announced in 2022.",
            ),
            (
                "Sagittarius A* Dünya'dan yaklaşık 26.000 ışık yılı uzakta, Samanyolu'nun merkezindedir ve kütlesi Güneş'in yaklaşık 4 milyon katıdır. Merkezin çevresindeki yıldızlar, özellikle uzun yıllar izlenen yıldızların yörüngeleri, görünmeyen kütlenin çok küçük bir bölgede toplandığını gösterir. Bu yörünge ölçümleri kara deliğin kütlesi ve konumu için güçlü kanıtlardandır.\n\nOlay Ufku Teleskobu iş birliği 12 Mayıs 2022'de Sagittarius A*'nın ilk görüntüsünü yayımladı. Görselde kara deliğin kendisi değil, çevresindeki sıcak plazmanın ışığı ve ortadaki karanlık gölge seçilir. Samanyolu'nun merkezindeki gaz hızla değiştiği için görüntüyü oluşturmak, M87* gözlemine kıyasla özellikle karmaşık bir çalışmaydı. Bulgular galaksi merkezlerinin yapısını ve genel göreliliği güçlü kütleçekim alanlarında incelemeye yardımcı olur.",
                "Sagittarius A* lies about 26,000 light-years away at the center of the Milky Way and has a mass about four million times that of the Sun. Orbits of stars around the galactic center—especially stars monitored over many years—show that the invisible mass is concentrated in a very small region. These orbital measurements provide strong evidence for the black hole's mass and location.\n\nOn May 12, 2022, the Event Horizon Telescope collaboration released the first image of Sagittarius A*. The image shows not the black hole itself but light from hot plasma around it and the dark central shadow. Because gas near the Milky Way's center changes rapidly, producing the image was especially challenging compared with the M87* observation. The findings help researchers study galactic-center structure and general relativity in strong gravitational fields.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Galactic Center", "NASA — Galaksi Merkezi", "https://science.nasa.gov/mission/webb/science-overview/science-explainers/what-is-the-center-of-our-galaxy-like/"),
                ("Event Horizon Telescope — First Sgr A* Image", "Event Horizon Telescope — İlk Sgr A* Görüntüsü", "https://eventhorizontelescope.org/blog/astronomers-reveal-first-image-black-hole-heart-our-galaxy"),
            ),
        ),
        make_article(
            (
                "M87*: bir kara deliğin ilk görüntüsü",
                "M87*: The First Image of a Black Hole",
            ),
            (
                "M87 galaksisinin merkezindeki süper kütleli kara deliğin görüntüsü 2019'da yayımlandı.",
                "The image of the supermassive black hole at the center of the galaxy M87 was released in 2019.",
            ),
            (
                "M87* yaklaşık 55 milyon ışık yılı uzaktaki Messier 87 galaksisinin merkezindedir. Kütlesi Güneş'in yaklaşık 6,5 milyar katı olarak tahmin edilir ve galaksi dışına uzanan güçlü madde jetleriyle tanınır. Jetler kara deliğin içinden çıkmaz; çevresindeki manyetize gaz ve plazmanın davranışıyla ilişkilidir.\n\n10 Nisan 2019'da Event Horizon Telescope, farklı kıtalardaki radyo gözlemevlerini Dünya boyutunda sanal bir teleskop gibi birlikte kullanarak M87* çevresindeki parlak halkayı ve karanlık gölgeyi görüntüledi. Bu, kara deliğin olay ufkunun yakın çevresini görüntüleyen ilk sonuçtu. Görüntü aynı zamanda genel görelilik tahminlerini aşırı kütleçekim ortamında inceleme olanağı sağladı; takip eden ölçümler halkanın yönelimi, kutuplaşması ve değişimi hakkında yeni veriler üretti.",
                "M87* lies at the center of the Messier 87 galaxy, about 55 million light-years away. Its mass is estimated at about 6.5 billion solar masses, and it is known for powerful jets extending beyond its galaxy. The jets do not emerge from inside the black hole; they are associated with the behavior of magnetized gas and plasma around it.\n\nOn April 10, 2019, the Event Horizon Telescope combined radio observatories across continents into a virtual, Earth-sized telescope and imaged the bright ring and dark shadow around M87*. It was the first result to image a black hole's immediate surroundings near the event horizon. The image also enabled tests of general-relativity predictions in an extreme gravitational environment; follow-up observations produced new data about the ring's orientation, polarization, and variability.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Black Hole Image Makes History", "NASA — Karadelik Görüntüsü Tarih Yazdı", "https://www.nasa.gov/universe/black-hole-image-makes-history-nasa-telescopes-coordinated-observations/"),
                ("Event Horizon Telescope — M87* Image", "Event Horizon Telescope — M87* Görüntüsü", "https://eventhorizontelescope.org/press-release-april-10-2019-astronomers-capture-first-image-black-hole"),
            ),
        ),
        make_article(
            (
                "Karadelik araştırmalarında dönüm noktaları",
                "Milestones in Black Hole Research",
            ),
            (
                "Kütleçekim dalgaları ve kara delik görüntüleri, karadeliklerin dolaylı kanıttan ayrıntılı gözleme geçişini sağladı.",
                "Gravitational waves and black hole images advanced the field from indirect evidence to detailed observation.",
            ),
            (
                "1916'da Karl Schwarzschild, Einstein'ın genel görelilik denklemlerinin kara deliklerle ilişkilendirilen çözümünü ortaya koydu. 1960'larda Cygnus X-1 gibi X-ışını kaynaklarının incelenmesi, görünmeyen yoğun cisimlerin varlığına güçlü kanıtlar sağladı. 2015'te LIGO iki kara deliğin birleşmesinden yayılan kütleçekim dalgalarını ilk kez doğrudan saptadı; bu sinyal uzay-zamanın titreşimlerini ölçerek yeni bir gözlem penceresi açtı.\n\nEvent Horizon Telescope 10 Nisan 2019'da M87*'nin ilk görüntüsünü, 12 Mayıs 2022'de Samanyolu merkezindeki Sagittarius A*'nın görüntüsünü yayımladı. 2022'de Gaia verileriyle duyurulan Gaia BH1 ise çevresinden belirgin ışınım yaymayan bir kara deliğin eş yıldızının hareketinden bulunabileceğini gösterdi. Bu gelişmeler, teorik çözümlerden X-ışını ve yörünge ölçümlerine, kütleçekim dalgalarından olay ufku çevresinin görüntülenmesine uzanan farklı yöntemleri bir araya getirdi.",
                "In 1916, Karl Schwarzschild found a solution to Einstein's general-relativity equations associated with black holes. In the 1960s, the study of X-ray sources such as Cygnus X-1 provided strong evidence for unseen compact objects. In 2015, LIGO made the first direct detection of gravitational waves from two merging black holes, opening a new observational window by measuring ripples in spacetime.\n\nThe Event Horizon Telescope released the first image of M87* on April 10, 2019, and an image of Sagittarius A* at the center of the Milky Way on May 12, 2022. Gaia BH1, announced in 2022 using Gaia data, showed that a black hole with little detectable emission can be found through the motion of its companion star. Together, these milestones span theoretical solutions, X-ray and orbital measurements, gravitational waves, and imaging near an event horizon.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA — Black Holes", "NASA — Karadelikler", "https://science.nasa.gov/universe/black-holes/"),
                ("Event Horizon Telescope", "Event Horizon Telescope", "https://eventhorizontelescope.org/"),
                ("ESA — Gaia", "ESA — Gaia", "https://www.esa.int/Science_Exploration/Space_Science/Gaia"),
                ("NASA — Chandra X-ray Observatory", "NASA — Chandra X-ray Observatory", "https://chandra.harvard.edu/"),
            ),
        ),
        make_article(
            (
                "Karadelik örnekleri: Cygnus X-1, TON 618 ve Gaia BH1",
                "Black Hole Examples: Cygnus X-1, TON 618, and Gaia BH1",
            ),
            (
                "Bu sistemler kara delikleri X-ışınları, kuasar ışığı veya eş yıldızın hareketi üzerinden incelemenin farklı yollarını gösterir.",
                "These systems show different ways to study black holes through X-rays, quasar light, or a companion star's motion.",
            ),
            (
                "Cygnus X-1, Samanyolu'nda bulunan ve bir eş yıldızdan madde alan yıldız kütleli kara delik sistemidir. Çekilen gaz kara deliğin çevresinde ısınıp X-ışını yayar; sistem bu nedenle kara delikleri yalnızca kütleçekim etkileriyle değil, çevrelerindeki sıcak madde üzerinden de incelemeyi sağlar. IXPE gibi X-ışını gözlemevleri bu ışınımın kutuplaşmasını ölçerek kara deliğe yakın maddenin geometrisi ve yönelimi hakkında bilgi edinir.\n\nTON 618, çok uzak ve parlak bir kuasarın merkezinde yer alan, olağanüstü büyük kütleli kara delik adaylarından biridir. Kuasar ışığı, merkezdeki kara deliğe doğru düşen maddenin açığa çıkardığı enerjiden kaynaklanır; bu nedenle doğrudan kara delikten değil, etkin çevresinden gelen ışık incelenir. Çok uzak olduğu için özellikleri tayf ve parlaklık ölçümlerinden çıkarılır; kütle değerleri kullanılan modele göre değişebildiğinden tek bir kesin “rekor” gibi sunulmamalıdır.\n\nGaia BH1, Gaia gözlemleriyle eş yıldızının hareketinde görülen etkiden çıkarılan, çevresinden belirgin X-ışını yaymayan bir kara delik sistemidir ve 2022'de duyurulmuştur. Bu tür sessiz sistemlerde kara delik, çevresindeki yıldızı gözle görülür biçimde etkilerken kendisi ışık saçmadığı için astrometrik ve tayfsal ölçümler önem kazanır. Üç örnek, kara deliklerin farklı yöntemlerle araştırılabileceğini gösterir: X-ışını, kuasar ışığı ve yıldız yörüngeleri. Verilen kütle ve uzaklık değerleri ölçüm ve modellere bağlı tahminlerdir.",
                "Cygnus X-1 is a stellar-mass black-hole system in the Milky Way that draws material from a companion star. The captured gas heats up around the black hole and emits X-rays, allowing researchers to study black holes not only through gravity but also through their hot surroundings. X-ray observatories such as IXPE measure the polarization of this radiation to learn about the geometry and orientation of matter close to the black hole.\n\nTON 618 is among the extremely massive black-hole candidates at the center of a very distant, bright quasar. Quasar light is powered by energy released as material falls toward the central black hole, so observations study its active surroundings rather than light from the black hole itself. Because it is very distant, its properties are inferred from spectra and brightness measurements; mass estimates vary with the models used and should not be presented as one definitive record.\n\nGaia BH1 is a black-hole system announced in 2022 and inferred from the effect on its companion star's motion in Gaia observations. It does not show prominent X-ray emission from its surroundings, making astrometric and spectroscopic measurements important: the black hole noticeably affects its companion while emitting little detectable light itself. These examples demonstrate different methods of black-hole research—X-rays, quasar light, and stellar orbits. Reported masses and distances are estimates that depend on observations and models.",
            ),
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200",
            (
                ("NASA Imagine — Cygnus X-1", "NASA Imagine — Cygnus X-1", "https://imagine.gsfc.nasa.gov/features/yba/CygX1_mass/cygX1_more.html"),
                ("NASA — IXPE and Cygnus X-1", "NASA — IXPE ve Cygnus X-1", "https://www.nasa.gov/universe/nasas-ixpe-reveals-shape-orientation-of-hot-matter-around-black-hole/"),
                ("NASA — Biggest Black Holes", "NASA — En Büyük Karadelikler", "https://www.nasa.gov/universe/nasa-animation-sizes-up-the-universes-biggest-black-holes/"),
                ("ESA — Gaia Black Holes", "ESA — Gaia Karadelikleri", "https://www.esa.int/Science_Exploration/Space_Science/Gaia/Gaia_discovers_a_new_family_of_black_holes"),
                ("Harvard & Smithsonian — Gaia BH1", "Harvard & Smithsonian — Gaia BH1", "https://www.cfa.harvard.edu/news/astronomers-discover-closest-black-hole-earth"),
            ),
        ),
    ],
}

YEAR_FEATURES = {
    "missions": {
        1990: [1],
        2000: [4],
        2010: [0],
        2020: [0],
    },
    "debris": {2026: [0, 1, 2]},
    "scientists": {2000: [3], 2020: [4]},
    "inventions": {1990: [2], 2000: [3], 2010: [0], 2020: [0]},
}

IMAGE_GALLERIES = {
    "scientists": [
        "https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1200&q=85",
    ],
    "inventions": [
        "https://images.unsplash.com/photo-1484589065579-248aad0d8b13?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1517976487492-5750f3195933?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=1200&q=85",
    ],
    "missions": [
        "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1484589065579-248aad0d8b13?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1517976487492-5750f3195933?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=85",
    ],
    "debris": [
        "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1517976487492-5750f3195933?auto=format&fit=crop&w=1200&q=85",
    ],
    "black_holes": [
        "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1484589065579-248aad0d8b13?auto=format&fit=crop&w=1200&q=85",
    ],
    "stars": [
        "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1484589065579-248aad0d8b13?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=1200&q=85",
        "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1200&q=85",
    ],
}


def get_articles(category, year):
    articles = PDF_ARTICLES[category]
    if category in ("stars", "black_holes"):
        indexes = list(range(len(articles)))
    else:
        indexes = YEAR_FEATURES.get(category, {}).get(year, [])
    gallery = IMAGE_GALLERIES[category]
    return [
        {**articles[index], "image": gallery[index % len(gallery)]}
        for index in indexes
    ]


def has_year_feature(category, year):
    return bool(YEAR_FEATURES.get(category, {}).get(year, []))


def get_all_sources():
    unique_sources = {}
    for articles in PDF_ARTICLES.values():
        for item in articles:
            for source in item["sources"]:
                unique_sources[source[2]] = source
    return list(unique_sources.values())

#JSTRBDM1-2
