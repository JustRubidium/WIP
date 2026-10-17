from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st

about_page = st.query_params.get("about") == "justrubidium"
english = st.session_state.get("language", "tr") == "en"
st.set_page_config(
    page_title=(
        "About JustRubidium"
        if about_page
        else (
            "Interactive Space Timeline & Data Platform"
            if english
            else "İnteraktif Uzay Zaman Tüneli & Veri Platformu"
        )
    ),
    page_icon="🪐",
    layout="wide",
)

if about_page:
    about_path = Path(__file__).with_name("static") / "Can keyfisi.html"
    if not about_path.is_file():
        st.error(
            "About page not found. Make sure static/Can keyfisi.html "
            "is included in the repository."
        )
        st.stop()

    st.html(about_path.read_text(encoding="utf-8"))
    st.stop()

st.session_state.setdefault("language", "tr")
english = st.session_state.language == "en"

st.markdown(
    """
    <style>
    .stApp {
        background-color: #010108;
        background-image: radial-gradient(circle at 50% 50%, #0c0c24 0%, #010108 100%);
    }
    div.block-container {
        background-color: rgba(6, 6, 18, 0.94);
        padding: 2.5rem;
        border-radius: 18px;
        border: 1px solid rgba(0, 255, 255, 0.35);
        box-shadow: 0 0 35px rgba(0, 255, 255, 0.15);
    }
    h1, h2, h3 {
        color: #00ffff !important;
        font-family: 'Courier New', monospace, sans-serif;
        letter-spacing: 1px;
    }
    .newspaper-card {
        background: linear-gradient(135deg, #0d0d24 0%, #050511 100%);
        border: 2px solid #00ffff;
        border-radius: 14px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
    }
    .newspaper-title {
        font-size: 24px;
        font-weight: bold;
        color: #00ffff;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(0, 255, 255, 0.4);
        padding-bottom: 8px;
    }
    .debris-card {
        background: linear-gradient(135deg, #131336 0%, #08081a 100%);
        border: 1px solid rgba(0, 255, 255, 0.4);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    .debris-title {
        color: #00ffff;
        font-size: 17px;
        font-weight: bold;
        margin-bottom: 6px;
    }
    .debris-desc {
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.6;
    }
    .terminal-box {
        background-color: #050511;
        border: 1px solid #00ffff;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        color: #00ffff;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

_, language_column = st.columns([8, 1])
with language_column:
    if st.button("🇹🇷 Türkçe" if english else "🇬🇧 English", use_container_width=True):
        st.session_state.language = "tr" if english else "en"
        st.rerun()

st.title(
    "🪐 INTERACTIVE SPACE TIMELINE & DATA CENTER"
    if english
    else "🪐 İNTERAKTİF UZAY ZAMAN TÜNELİ & VERİ MERKEZİ"
)
st.write(
    "Explore space history, planetary data, and orbital debris by year."
    if english
    else "Uzay tarihini, gezegen verilerini ve yörünge enkazı dağılımını"
    " seçtiğiniz yıla göre inceleyin."
)

veri_tabani = {
    1980: {
        "baslik": "1980: Voyager Geçişleri ve Ozon Tabakasının Keşfi",
        "makale": (
            "Voyager 1 uzay aracı Satürn'e en yakın geçişini tamamlayarak"
            " halkalar ve uydular hakkında devrim niteliğinde veriler"
            " gönderdi. Dünya'da ise stratosfer tabakasındaki ozon incelmesi"
            " (Ozon Deliği) ilk kez bilim insanları tarafından rapor edildi."
        ),
        "gorsel": (
            "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=1200"
        ),
        "cop_detay": [
            {
                "kategori": "Aktif Uydular",
                "oran": 60,
                "aciklama": "Haberleşme ve gözlem amaçlı kontrollü araçlar.",
            },
            {
                "kategori": "Roket Gövdeleri",
                "oran": 30,
                "aciklama": "Boş kalan yakıt tankları.",
            },
            {
                "kategori": "Eski Parçalar",
                "oran": 10,
                "aciklama": "Erken dönem fırlatmalardan kalan adaptörler.",
            },
        ],
        "cop_aciklama": (
            "1980'lerde Alçak Dünya Yörüngesi temizdi; toplam büyük çöp"
            " parçası 4.000'in altındaydı."
        ),
    },
    1990: {
        "baslik": "1990: Hubble Uzay Teleskobu'nun Fırlatılması",
        "makale": (
            "Hubble Uzay Teleskobu yörüngeye yerleştirilerek evrenin"
            " derinliklerinden net fotoğraflar aktarmaya başladı."
        ),
        "gorsel": (
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200"
        ),
        "cop_detay": [
            {
                "kategori": "Aktif Uydular",
                "oran": 50,
                "aciklama": "İletişimi artıran ikinci nesil uydular.",
            },
            {
                "kategori": "Ölü Uydular",
                "oran": 30,
                "aciklama": "Görev süresi dolmuş pasif uydular.",
            },
            {
                "kategori": "Roket Enkazı",
                "oran": 20,
                "aciklama": "Yörünge patlamaları sonucu saçılan hurdalar.",
            },
        ],
        "cop_aciklama": (
            "Yörüngede eski roket kademelerinin birikmesiyle ilk kalabalıklaşma"
            " sinyalleri görüldü."
        ),
    },
    2000: {
        "baslik": "2000: Uluslararası Uzay İstasyonu (ISS) Dönemi",
        "makale": (
            "Uluslararası Uzay İstasyonu'na ilk kalıcı insanlı sefer"
            " gerçekleştirildi; insanlık uzayda kesintisiz yaşam standardına"
            " ulaştı."
        ),
        "gorsel": (
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200"
        ),
        "cop_detay": [
            {
                "kategori": "Aktif Uydular",
                "oran": 45,
                "aciklama": "GPS ve geniş bant veri iletim ağları.",
            },
            {
                "kategori": "Eski Uydular",
                "oran": 35,
                "aciklama": "Yörünge yüksekliği düşen terk edilmiş platformlar.",
            },
            {
                "kategori": "Parçalanma Enkazı",
                "oran": 20,
                "aciklama": "Milimetrik ve santimetrik hurdalar.",
            },
        ],
        "cop_aciklama": (
            "Çöp yoğunluğu 9.000'i aştı ve Kessler Sendromu tartışılmaya"
            " başlandı."
        ),
    },
    2010: {
        "baslik": "2010: Ticari Uzay Uçuşlarının Yükselişi",
        "makale": (
            "Özel uzay şirketleri roket teknolojisinde devrim yaptı. Curiosity"
            " Mars'a başarılı bir şekilde iniş yaptı."
        ),
        "gorsel": (
            "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=1200"
        ),
        "cop_detay": [
            {
                "kategori": "Aktif Uydular",
                "oran": 40,
                "aciklama": "Yüksek çözünürlüklü Dünya gözlem uyduları.",
            },
            {
                "kategori": "Ölü Uydular",
                "oran": 40,
                "aciklama": "Tehdit oluşturan pasif kütleler.",
            },
            {
                "kategori": "Tehlikeli Parçalar",
                "oran": 20,
                "aciklama": "Yüksek hızlı küçük enkaz parçacıkları.",
            },
        ],
        "cop_aciklama": (
            "Çarpışma riskleri artarken aktif temizlik protokolleri"
            " hazırlandı."
        ),
    },
    2020: {
        "baslik": "2020: James Webb Uzay Teleskobu ve Artemis",
        "makale": (
            "James Webb en eski galaksileri görüntüledi. Artemis programı ile"
            " Ay'a dönüş için kritik testler tamamlandı."
        ),
        "gorsel": (
            "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=1200"
        ),
        "cop_detay": [
            {
                "kategori": "Aktif Uydular",
                "oran": 35,
                "aciklama": "Mega takımyıldızlar ile hızla artan filo.",
            },
            {
                "kategori": "Ölü Uydular",
                "oran": 45,
                "aciklama": "Atmosfere girene kadar tehlike saçan kütleler.",
            },
            {
                "kategori": "Roket Artıkları",
                "oran": 20,
                "aciklama": "Çok aşamalı roketlerin bıraktığı metalik halkalar.",
            },
        ],
        "cop_aciklama": (
            "Alçak Dünya Yörüngesi binlerce yeni nesil uydu ile yoğun trafik"
            " kazandı."
        ),
    },
    2026: {
        "baslik": "2026: Çoklu Gezegen Misyonları ve Sürdürülebilirlik Krizi",
        "makale": (
            "Mars'ta mikrobiyal yaşam izleri aranırken, Alçak Dünya"
            " Yörüngesi'nde 35.000'den fazla büyük çöp parçasına ulaşıldı."
        ),
        "gorsel": (
            "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200"
        ),
        "cop_detay": [
            {
                "kategori": "Tehlikeli Büyük Çöpler",
                "oran": 40,
                "aciklama": "Manevra yapmayı zorunlu kılan büyük hurda nesneler.",
            },
            {
                "kategori": "Ölü Uydular",
                "oran": 35,
                "aciklama": "Temizlenme bekleyen eski nesil platformlar.",
            },
            {
                "kategori": "Aktif Ticari Uydular",
                "oran": 25,
                "aciklama": "Küresel internet sağlayan binlerce uydu.",
            },
        ],
        "cop_aciklama": (
            "Yörüngede en yüksek kirlilik seviyesine ulaşıldı; temizleme"
            " uyduları test ediliyor."
        ),
    },
}

haberler = {
    1980: [
        {
            "baslik": "Voyager 1, Satürn'ün yanından geçti",
            "tarih": "12 Kasım 1980",
            "metin": (
                "Voyager 1, Satürn'e yakın geçişi sırasında gezegenin"
                " atmosferini, halkalarını ve uydularını gözlemledi. Yakın"
                " çekimler, Satürn sisteminin beklenenden daha karmaşık"
                " olduğunu ortaya koydu."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=800"
            ),
        },
        {
            "baslik": "Güneş'i izlemek için Solar Maximum Mission",
            "tarih": "14 Şubat 1980",
            "metin": (
                "NASA'nın Solar Maximum Mission uydusu, Güneş'in etkinliğini"
                " ve güneş patlamalarını incelemek üzere fırlatıldı."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800"
            ),
        },
    ],
    1990: [
        {
            "baslik": "Hubble Uzay Teleskobu yörüngeye gönderildi",
            "tarih": "24 Nisan 1990",
            "metin": (
                "Uzay Mekiği Discovery ile fırlatılan Hubble, Dünya"
                " atmosferinin dışından evreni gözlemlemeye başladı."
                " Teleskobun ilk görevleri astronomide yeni bir dönemin"
                " başlangıcı oldu."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800"
            ),
        },
        {
            "baslik": "Ulysses Güneş'i farklı bir açıdan incelemek üzere yola çıktı",
            "tarih": "6 Ekim 1990",
            "metin": (
                "Ulysses uzay aracı, Güneş'in kutup bölgelerini ve güneş"
                " rüzgârını incelemek amacıyla fırlatıldı. Görevi, Güneş'i"
                " yalnızca ekvator düzleminden gözlemleme sınırını aştı."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800"
            ),
        },
    ],
    2000: [
        {
            "baslik": "İlk uzun süreli mürettebat Uluslararası Uzay İstasyonu'na yerleşti",
            "tarih": "2 Kasım 2000",
            "metin": (
                "Expedition 1 ekibinin istasyona ulaşmasıyla ISS'te kesintisiz"
                " insanlı yaşam dönemi başladı. İstasyon, uzun süreli uzay"
                " araştırmaları için uluslararası bir laboratuvara dönüştü."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800"
            ),
        },
        {
            "baslik": "Mars'taki yüzey izleri bilim dünyasında ilgi uyandırdı",
            "tarih": "2000",
            "metin": (
                "Mars Global Surveyor'ın yüksek çözünürlüklü görüntülerinde"
                " görülen bazı yüzey şekilleri, Mars'ta geçmişte su bulunmuş"
                " olabileceğine dair araştırmaları ve tartışmaları"
                " hızlandırdı."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800"
            ),
        },
    ],
    2010: [
        {
            "baslik": "Hayabusa, asteroitten alınan örnekleri Dünya'ya getirdi",
            "tarih": "13 Haziran 2010",
            "metin": (
                "Japonya'nın Hayabusa sondası, Itokawa asteroidinden aldığı"
                " parçacıkları Dünya'ya ulaştırdı. Bu, bir asteroitten"
                " toplanan örneklerin Dünya'ya getirildiği ilk başarılı görev"
                " oldu."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800"
            ),
        },
        {
            "baslik": "Dragon yörüngeye ulaşıp Dünya'ya döndü",
            "tarih": "8 Aralık 2010",
            "metin": (
                "SpaceX'in Dragon kapsülü, yörüngeye çıkıp güvenli biçimde"
                " Dünya'ya dönen ilk özel şirket yapımı uzay aracı oldu."
                " Başarı, ticari uzay taşımacılığı için önemli bir adımdı."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=800"
            ),
        },
    ],
    2020: [
        {
            "baslik": "Crew Dragon astronotları Uluslararası Uzay İstasyonu'na taşıdı",
            "tarih": "30 Mayıs 2020",
            "metin": (
                "NASA'nın Demo-2 göreviyle iki astronot, özel bir şirket"
                " tarafından geliştirilen Crew Dragon kapsülüyle ISS'e"
                " ulaştı. Bu görev, ABD'den insanlı yörünge uçuşlarının"
                " yeniden başlamasını sağladı."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=800"
            ),
        },
        {
            "baslik": "OSIRIS-REx, Bennu asteroidinden örnek topladı",
            "tarih": "20 Ekim 2020",
            "metin": (
                "NASA'nın OSIRIS-REx aracı Bennu yüzeyine kısa süreli temas"
                " ederek örnek topladı. Numune, Dünya'ya dönüş yolculuğunun"
                " ardından 2023'te teslim edildi."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=800"
            ),
        },
        {
            "baslik": "Perseverance Mars yolculuğuna başladı",
            "tarih": "30 Temmuz 2020",
            "metin": (
                "NASA'nın Perseverance gezgini Mars'a fırlatıldı. Görevin"
                " hedefleri arasında Jezero Krateri'ni incelemek ve gelecekte"
                " Dünya'ya getirilebilecek kaya örneklerini toplamak vardı."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800"
            ),
        },
    ],
    2026: [
        {
            "baslik": "Ay keşiflerinde sürdürülebilirliğe odaklanılıyor",
            "tarih": "2026 uzay gündemi",
            "metin": (
                "Ay'a yönelik insanlı ve robotik görev planlarında uzun süreli"
                " keşif, güvenli iniş ve kaynakların sorumlu kullanımı öne"
                " çıkan başlıklar arasında."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?w=800"
            ),
        },
        {
            "baslik": "Yörünge enkazının izlenmesi önemini koruyor",
            "tarih": "2026 uzay gündemi",
            "metin": (
                "Uydu sayısındaki artışla birlikte yörüngedeki nesnelerin"
                " izlenmesi, çarpışma risklerinin azaltılması ve görev dışı"
                " araçların güvenli biçimde yönetilmesi uzay faaliyetlerinin"
                " önemli konuları olmaya devam ediyor."
            ),
            "gorsel": (
                "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800"
            ),
        },
    ],
}

english_data = {
    1980: {
        "baslik": "1980: Voyager Flybys and the Discovery of Ozone Depletion",
        "makale": (
            "Voyager 1 made its closest approach to Saturn, returning "
            "groundbreaking data about its rings and moons. On Earth, "
            "scientists reported the thinning of stratospheric ozone, "
            "known as the ozone hole, for the first time."
        ),
        "cop_aciklama": (
            "Low Earth orbit was relatively clear in the 1980s, with fewer "
            "than 4,000 large debris objects in total."
        ),
        "cop_detay": [
            ("Active Satellites", "Controlled spacecraft used for communications and observation."),
            ("Rocket Bodies", "Empty fuel tanks left in orbit."),
            ("Legacy Fragments", "Adapters left behind by early launches."),
        ],
    },
    1990: {
        "baslik": "1990: The Hubble Space Telescope Launch",
        "makale": (
            "The Hubble Space Telescope was placed in orbit and began "
            "sending clear images of the distant universe."
        ),
        "cop_aciklama": (
            "The accumulation of old rocket stages in orbit marked the "
            "first signs of increasing congestion."
        ),
        "cop_detay": [
            ("Active Satellites", "Second-generation satellites expanded communications."),
            ("Inactive Satellites", "Satellites that had reached the end of their missions."),
            ("Rocket Debris", "Fragments scattered by orbital explosions."),
        ],
    },
    2000: {
        "baslik": "2000: The International Space Station Era",
        "makale": (
            "The first permanent crew arrived at the International Space "
            "Station, beginning humanity's continuous presence in space."
        ),
        "cop_aciklama": (
            "The number of tracked debris objects exceeded 9,000, and "
            "discussion of Kessler syndrome began."
        ),
        "cop_detay": [
            ("Active Satellites", "GPS and broadband data networks."),
            ("Inactive Satellites", "Abandoned spacecraft whose orbits are decaying."),
            ("Fragmentation Debris", "Millimeter- and centimeter-sized fragments."),
        ],
    },
    2010: {
        "baslik": "2010: The Rise of Commercial Spaceflight",
        "makale": (
            "Private space companies transformed rocket technology, while "
            "Curiosity successfully landed on Mars."
        ),
        "cop_aciklama": (
            "As collision risks grew, active debris-removal protocols were prepared."
        ),
        "cop_detay": [
            ("Active Satellites", "High-resolution Earth-observation satellites."),
            ("Inactive Satellites", "Defunct objects posing a threat in orbit."),
            ("Hazardous Fragments", "Small, high-velocity debris particles."),
        ],
    },
    2020: {
        "baslik": "2020: The James Webb Space Telescope and Artemis",
        "makale": (
            "James Webb observed some of the earliest galaxies. The Artemis "
            "program completed critical tests for humanity's return to the Moon."
        ),
        "cop_aciklama": (
            "Thousands of next-generation satellites made Low Earth Orbit "
            "increasingly busy."
        ),
        "cop_detay": [
            ("Active Satellites", "A rapidly growing fleet of mega-constellations."),
            ("Inactive Satellites", "Large objects that remain hazardous until reentry."),
            ("Rocket Remnants", "Metal fragments left by multistage rockets."),
        ],
    },
    2026: {
        "baslik": "2026: Multiplanetary Missions and the Sustainability Challenge",
        "makale": (
            "While missions search for signs of microbial life on Mars, the "
            "number of large debris objects in Low Earth Orbit has topped 35,000."
        ),
        "cop_aciklama": (
            "Orbital pollution has reached a record level, and debris-removal "
            "satellites are being tested."
        ),
        "cop_detay": [
            ("Large Hazardous Debris", "Large pieces of debris that require collision-avoidance maneuvers."),
            ("Inactive Satellites", "Older spacecraft awaiting removal."),
            ("Active Commercial Satellites", "Thousands of satellites providing global internet."),
        ],
    },
}

english_news = {
    1980: [
        (
            "Voyager 1 Flies Past Saturn",
            "November 12, 1980",
            "During its close flyby, Voyager 1 observed Saturn's atmosphere, rings, and moons. The images revealed a more complex Saturn system than expected.",
        ),
        (
            "Solar Maximum Mission Launches to Study the Sun",
            "February 14, 1980",
            "NASA launched the Solar Maximum Mission spacecraft to study solar activity and flares.",
        ),
    ],
    1990: [
        (
            "Hubble Space Telescope Enters Orbit",
            "April 24, 1990",
            "Launched aboard Space Shuttle Discovery, Hubble began observing the universe from beyond Earth's atmosphere. Its first missions opened a new era in astronomy.",
        ),
        (
            "Ulysses Sets Out to Study the Sun from a New Angle",
            "October 6, 1990",
            "Ulysses launched to study the Sun's polar regions and solar wind, going beyond observations limited to the Sun's equatorial plane.",
        ),
    ],
    2000: [
        (
            "First Long-Term Crew Moves Aboard the International Space Station",
            "November 2, 2000",
            "With the arrival of Expedition 1, a continuous human presence began aboard the ISS. The station became an international laboratory for long-duration space research.",
        ),
        (
            "Martian Surface Features Spark Scientific Interest",
            "2000",
            "Some features in high-resolution images from Mars Global Surveyor accelerated research and debate about whether water once existed on Mars.",
        ),
    ],
    2010: [
        (
            "Hayabusa Returns Samples from an Asteroid to Earth",
            "June 13, 2010",
            "Japan's Hayabusa spacecraft delivered particles collected from asteroid Itokawa. It was the first successful mission to return samples from an asteroid.",
        ),
        (
            "Dragon Reaches Orbit and Returns to Earth",
            "December 8, 2010",
            "SpaceX's Dragon became the first privately developed spacecraft to reach orbit and safely return to Earth, an important milestone for commercial spaceflight.",
        ),
    ],
    2020: [
        (
            "Crew Dragon Carries Astronauts to the International Space Station",
            "May 30, 2020",
            "Two astronauts reached the ISS in the privately developed Crew Dragon spacecraft on NASA's Demo-2 mission, restarting crewed orbital launches from the United States.",
        ),
        (
            "OSIRIS-REx Collects a Sample from Asteroid Bennu",
            "October 20, 2020",
            "NASA's OSIRIS-REx briefly touched Bennu's surface to collect a sample, which was delivered to Earth in 2023.",
        ),
        (
            "Perseverance Begins Its Journey to Mars",
            "July 30, 2020",
            "NASA launched the Perseverance rover to explore Jezero Crater and collect rock samples that may one day be returned to Earth.",
        ),
    ],
    2026: [
        (
            "Sustainability Takes Center Stage in Lunar Exploration",
            "2026 space agenda",
            "Plans for crewed and robotic lunar missions emphasize long-term exploration, safe landings, and responsible use of resources.",
        ),
        (
            "Tracking Orbital Debris Remains a Priority",
            "2026 space agenda",
            "As the satellite population grows, tracking objects in orbit, reducing collision risks, and safely managing retired spacecraft remain key challenges.",
        ),
    ],
}

yillar = sorted(veri_tabani.keys())
secilen_yil = st.select_slider(
    (
        "📅 Timeline year (all data updates to this year):"
        if english
        else "📅 Zaman Tüneli Yılı (Tüm Veriler Bu Yıla Göre Güncellenir):"
    ),
    options=yillar,
    value=2020 if 2020 in yillar else yillar[-1],
    key="timeline_year",
)
st.divider()

veri = veri_tabani[secilen_yil]
haber_listesi = haberler[secilen_yil]
if english:
    translation = english_data[secilen_yil]
    veri = {
        **veri,
        "baslik": translation["baslik"],
        "makale": translation["makale"],
        "cop_aciklama": translation["cop_aciklama"],
        "cop_detay": [
            {
                **item,
                "kategori": translated[0],
                "aciklama": translated[1],
            }
            for item, translated in zip(
                veri["cop_detay"], translation["cop_detay"]
            )
        ],
    }
    haber_listesi = [
        {
            **story,
            "baslik": translated[0],
            "tarih": translated[1],
            "metin": translated[2],
        }
        for story, translated in zip(
            haberler[secilen_yil], english_news[secilen_yil]
        )
    ]

tab1, tab2, tab3, tab4 = st.tabs(
    (
        ["🪐 3D System", "🗑️ Space Debris", "📰 News", "💻 Developer"]
        if english
        else ["🪐 3D Sistem", "🗑️ Uzay Çöpleri", "📰 Gazete", "💻 Developer"]
    )
)

with tab1:
    st.markdown(
        "### 🪐 Interactive 3D Solar System"
        if english
        else "### 🪐 İnteraktif 3D Güneş Sistemi"
    )
    simulasyon_yolu = Path(__file__).with_name("simulasyon.html")
    if not simulasyon_yolu.is_file():
        st.error(
            (
                "The 3D simulation file was not found. Place simulasyon.html "
                "in the same folder as WIP.py."
                if english
                else "3D simülasyon dosyası bulunamadı. "
                "simulasyon.html dosyasını WIP.py ile aynı klasöre koyun."
            )
        )
    else:
        simulasyon_html = simulasyon_yolu.read_text(encoding="utf-8")
        simulasyon_html = simulasyon_html.replace(
            "__SELECTED_YEAR__", str(secilen_yil)
        )
        simulasyon_html = simulasyon_html.replace(
            "__LANGUAGE__", "en" if english else "tr"
        )
        st.iframe(simulasyon_html, height=700)

with tab2:
    st.markdown(
        f"### 🗑️ {secilen_yil} Orbital Debris Analysis"
        if english
        else f"### 🗑️ {secilen_yil} Yılı Yörünge Çöpü ve Enkaz Analizi"
    )
    st.write(veri["cop_aciklama"])

    kategoriler = [item["kategori"] for item in veri["cop_detay"]]
    oranlar = [item["oran"] for item in veri["cop_detay"]]
    aciklamalar = [item["aciklama"] for item in veri["cop_detay"]]
    kategori_renkleri = ["#00E5FF", "#A78BFA", "#FFB86B"]
    fig = go.Figure(
        data=[
            go.Pie(
                labels=kategoriler,
                values=oranlar,
                customdata=aciklamalar,
                hole=0.64,
                sort=False,
                direction="clockwise",
                rotation=270,
                textinfo="percent",
                textposition="inside",
                textfont=dict(color="#F8FAFC", size=14, family="Arial"),
                marker=dict(
                    colors=kategori_renkleri,
                    line=dict(color="#080816", width=4),
                ),
                hovertemplate=(
                    "<b>%{label}</b><br>"
                    +
                    (
                        "Debris share: %{percent}<br>"
                        if english
                        else "Enkaz oranı: %{percent}<br>"
                    )
                    + "%{customdata}<extra></extra>"
                ),
                hoverlabel=dict(
                    bgcolor="#101126",
                    bordercolor="#00E5FF",
                    font=dict(color="#F1F5F9", size=14),
                ),
                pull=[0] * len(kategoriler),
            )
        ]
    )
    fig.update_layout(
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(color="#E2E8F0", family="Arial"),
        margin=dict(t=30, b=20, l=10, r=10),
        height=440,
        showlegend=False,
        clickmode="event+select",
        uniformtext_minsize=12,
        uniformtext_mode="hide",
        annotations=[
            dict(
                text=(
                    f"<b>{secilen_yil}</b><br>"
                    +
                    (
                        "<span style='font-size:12px'>DEBRIS DISTRIBUTION</span>"
                        if english
                        else "<span style='font-size:12px'>ENKAZ DAĞILIMI</span>"
                    )
                ),
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(color="#E2E8F0", size=20),
            )
        ],
    )
    etkileisim_kodu = """
    const graph = document.getElementById('{plot_id}');
    const trace = graph.data[0];
    const colors = trace.marker.colors;
    const english = __ENGLISH__;
    let hoveredPoint = null;
    let pinnedPoint = null;

    function showPoint(index) {
      const detail = document.getElementById('debris-detail');
      const detailTitle = document.getElementById('debris-detail-title');
      const detailText = document.getElementById('debris-detail-text');
      if (!detail || !detailTitle || !detailText) return;

      const pulls = trace.labels.map((_, pointIndex) =>
        pointIndex === index ? 0.13 : 0
      );
      Plotly.animate(
        graph,
        [{ data: [{ pull: pulls }], traces: [0] }],
        {
          mode: 'immediate',
          frame: { duration: 360, redraw: false },
          transition: { duration: 360, easing: 'cubic-in-out' }
        }
      );

      if (index === null) {
        detail.classList.remove('is-active');
        detailTitle.textContent = english
          ? 'Explore a debris category'
          : 'Bir enkaz dilimini incele';
        detailText.textContent =
          (english
            ? 'Hover over or tap a slice to see its description.'
            : 'Açıklamayı görmek için dilimin üzerine gel veya dokun.');
        detail.style.borderColor = '#00E5FF';
        return;
      }

      detail.classList.add('is-active');
      const percentage = english
        ? `${trace.values[index]}%`
        : `%${trace.values[index]}`;
      detailTitle.textContent = `${trace.labels[index]} · ${percentage}`;
      detailText.textContent = trace.customdata[index];
      detail.style.borderColor = colors[index];
    }

    graph.on('plotly_hover', event => {
      hoveredPoint = event.points[0].pointNumber;
      showPoint(hoveredPoint);
    });
    graph.on('plotly_unhover', () => {
      hoveredPoint = null;
      showPoint(pinnedPoint);
    });
    graph.on('plotly_click', event => {
      const clickedPoint = event.points[0].pointNumber;
      pinnedPoint = pinnedPoint === clickedPoint ? null : clickedPoint;
      showPoint(pinnedPoint === null ? hoveredPoint : pinnedPoint);
    });

    const slices = Array.from(graph.querySelectorAll('g.slice path'));
    const sliceLabels = Array.from(graph.querySelectorAll('g.slice text'));
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      slices.forEach(slice => {
        slice.style.transformBox = 'fill-box';
        slice.style.transformOrigin = 'center';
        slice.style.transition =
          'opacity 900ms ease, transform 1100ms cubic-bezier(0.2, 0.75, 0.25, 1)';
        slice.style.opacity = '0';
        slice.style.transform = 'scale(0.15)';
      });
      sliceLabels.forEach(label => {
        label.style.transition = 'opacity 700ms ease';
        label.style.opacity = '0';
      });
      requestAnimationFrame(() => {
        slices.forEach((slice, index) => {
          setTimeout(() => {
            slice.style.opacity = '1';
            slice.style.transform = 'scale(1)';
          }, 180 + index * 420);
        });
        sliceLabels.forEach((label, index) => {
          setTimeout(() => { label.style.opacity = '1'; }, 420 + index * 300);
        });
      });
    }
    """
    etkileisim_kodu = etkileisim_kodu.replace(
        "__ENGLISH__", "true" if english else "false"
    )
    grafik_html = pio.to_html(
        fig,
        full_html=False,
        include_plotlyjs="cdn",
        config={
            "displayModeBar": False,
            "responsive": True,
            "scrollZoom": False,
        },
        post_script=etkileisim_kodu,
    )
    st.iframe(
        f"""
        <!DOCTYPE html>
        <html lang="{"en" if english else "tr"}">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                * {{ box-sizing: border-box; }}
                html, body {{
                    margin: 0;
                    padding: 0;
                    background: transparent;
                    font-family: Arial, sans-serif;
                }}
                .debris-chart-frame {{
                    padding: 14px;
                    border: 1px solid rgba(0, 255, 255, 0.45);
                    border-radius: 16px;
                    background: linear-gradient(135deg, #0d0d24 0%, #050511 100%);
                    box-shadow: 0 0 24px rgba(0, 255, 255, 0.12);
                }}
                .debris-detail-card {{
                    margin: 2px 10px 8px;
                    padding: 16px 20px;
                    border: 1px solid #00E5FF;
                    border-radius: 12px;
                    background: linear-gradient(135deg, #131336 0%, #08081a 100%);
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
                    color: #cbd5e1;
                    font: 14px/1.6 Arial, sans-serif;
                    opacity: 0.88;
                    transform: translateY(4px);
                    transition:
                        opacity 0.32s ease,
                        transform 0.38s cubic-bezier(0.2, 0.75, 0.25, 1),
                        border-color 0.32s ease,
                        box-shadow 0.32s ease;
                }}
                .debris-detail-card.is-active {{
                    opacity: 1;
                    transform: translateY(0);
                    box-shadow: 0 0 22px rgba(0, 229, 255, 0.16);
                }}
                .debris-detail-card h3 {{
                    margin: 0 0 5px;
                    color: #00ffff;
                    font-size: 17px;
                }}
                .debris-detail-card p {{ margin: 0; }}
                @media (max-width: 600px) {{
                    .debris-chart-frame {{ padding: 5px; }}
                    .debris-detail-card {{ margin: 0 6px 6px; padding: 12px; }}
                }}
            </style>
        </head>
        <body>
            <section class="debris-chart-frame">
                {grafik_html}
                <div id="debris-detail" class="debris-detail-card">
                    <h3 id="debris-detail-title">
                        {"Explore a debris category" if english else "Bir enkaz dilimini incele"}
                    </h3>
                    <p id="debris-detail-text">
                        {
                            "Hover over or tap a slice to see its description."
                            if english
                            else "Açıklamayı görmek için dilimin üzerine gel veya dokun."
                        }
                    </p>
                </div>
            </section>
        </body>
        </html>
        """,
        height=570,
    )

with tab3:
    st.markdown(
        f"### 📰 Space Chronicle — {secilen_yil}"
        if english
        else f"### 📰 Uzay Kroniği Gazetesi — {secilen_yil}"
    )
    st.caption(
        "Space news and updates from the selected year"
        if english
        else "Seçilen yılın uzay gelişmelerinden haberler"
    )

    for haber in haber_listesi:
        with st.container(border=True):
            resim_kolonu, yazi_kolonu = st.columns([0.9, 1.7], vertical_alignment="center")
            with resim_kolonu:
                st.image(haber["gorsel"], width="stretch")
            with yazi_kolonu:
                st.caption(
                    f"SPACE NEWS  •  {haber['tarih']}"
                    if english
                    else f"UZAY HABERLERİ  •  {haber['tarih']}"
                )
                st.markdown(f"#### {haber['baslik']}")
                st.write(haber["metin"])

with tab4:
    st.markdown(
        f"""
        <section style="
            max-width: 760px;
            margin: 24px auto;
            padding: 30px 34px;
            border: 1px solid rgba(0, 229, 255, 0.48);
            border-radius: 16px;
            background: linear-gradient(135deg, #131336 0%, #08081a 100%);
            box-shadow: 0 0 26px rgba(0, 229, 255, 0.13);
            color: #e2e8f0;
            font-family: Arial, sans-serif;
            text-align: center;
        ">
            <h2 style="
                margin: 0 0 8px;
                color: #00ffff;
                font-family: 'Courier New', monospace;
                letter-spacing: 1px;
            ">Scripter / Developer: <a href="?about=justrubidium" target="_blank" rel="noopener noreferrer" style="color:inherit;text-decoration:none;">JustRubidium</a></h2>
            <div style="
                width: 72px;
                height: 2px;
                margin: 22px auto;
                background: linear-gradient(90deg, #00e5ff, #a78bfa);
                box-shadow: 0 0 12px rgba(0, 229, 255, 0.65);
            "></div>
            <h3 style="
                margin: 0 0 20px;
                color: #67e8f9;
                font-family: 'Courier New', monospace;
                letter-spacing: 0.6px;
            ">{'Thanks For Supports' if english else 'Destekleri İçin Teşekkürler'}</h3>
            <div style="
                display: grid;
                gap: 11px;
                max-width: 460px;
                margin: 0 auto;
            ">
                <a href="https://www.spaceappschallenge.org/2026/find-a-team/aeon-labs/?tab=members" target="_blank" rel="noopener noreferrer" style="
                    padding: 13px 16px;
                    border: 1px solid rgba(167, 139, 250, 0.55);
                    border-radius: 10px;
                    background: rgba(8, 8, 26, 0.72);
                    color: #c4b5fd;
                    font-weight: 700;
                    text-decoration: none;
                    transition: border-color 0.25s ease, background 0.25s ease, transform 0.25s ease;
                " onmouseover="this.style.borderColor='#00e5ff';this.style.background='rgba(0,229,255,0.1)';this.style.transform='translateY(-2px)'" onmouseout="this.style.borderColor='rgba(167, 139, 250, 0.55)';this.style.background='rgba(8, 8, 26, 0.72)';this.style.transform='translateY(0)'">Yağmur Ruze <span style="color:#94a3b8;font-weight:400">({'Team Captain' if english else 'Takım Kaptanı'})</span></a>
                <a href="https://www.spaceappschallenge.org/2026/find-a-team/aeon-labs/?tab=members" target="_blank" rel="noopener noreferrer" style="padding: 11px 16px; border-radius: 10px; color: #dbeafe; text-decoration: none; transition: color 0.25s ease, background 0.25s ease;" onmouseover="this.style.color='#00e5ff';this.style.background='rgba(0,229,255,0.08)'" onmouseout="this.style.color='#dbeafe';this.style.background='transparent'">Beyzanur</a>
                <a href="https://www.spaceappschallenge.org/2026/find-a-team/aeon-labs/?tab=members" target="_blank" rel="noopener noreferrer" style="padding: 11px 16px; border-radius: 10px; color: #dbeafe; text-decoration: none; transition: color 0.25s ease, background 0.25s ease;" onmouseover="this.style.color='#00e5ff';this.style.background='rgba(0,229,255,0.08)'" onmouseout="this.style.color='#dbeafe';this.style.background='transparent'">Hüma</a>
                <a href="https://www.spaceappschallenge.org/2026/find-a-team/aeon-labs/?tab=members" target="_blank" rel="noopener noreferrer" style="padding: 11px 16px; border-radius: 10px; color: #dbeafe; text-decoration: none; transition: color 0.25s ease, background 0.25s ease;" onmouseover="this.style.color='#00e5ff';this.style.background='rgba(0,229,255,0.08)'" onmouseout="this.style.color='#dbeafe';this.style.background='transparent'">Beyza Sami</a>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <section style="
            max-width: 760px;
            margin: 18px auto 28px;
            padding: 24px 30px;
            border: 1px solid rgba(0, 229, 255, 0.35);
            border-radius: 14px;
            background: linear-gradient(135deg, #0d0d24 0%, #050511 100%);
            box-shadow: 0 0 20px rgba(0, 229, 255, 0.09);
            color: #cbd5e1;
            font-family: Arial, sans-serif;
        ">
            <h3 style="
                margin: 0 0 16px;
                color: #00ffff;
                font-family: 'Courier New', monospace;
                letter-spacing: 0.8px;
                text-align: center;
            ">{'Sources' if english else 'Kaynakça'}</h3>
            <ul style="
                display: grid;
                gap: 10px;
                margin: 0;
                padding-left: 20px;
                line-height: 1.55;
            ">
                <li><a href="https://science.nasa.gov/universe/stars/types/" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">NASA Science — Types of Stars</a></li>
                <li><a href="https://science.nasa.gov/universe/stars/" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">NASA Science — Stars</a></li>
                <li><a href="https://science.nasa.gov/universe/glossary/" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">NASA Science — Universe Glossary (Blue Supergiant)</a></li>
                <li><a href="https://tua.gov.tr/tr/blog/evren/supernova-nedir" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">Türkiye Uzay Ajansı — {'What Is a Supernova?' if english else 'Süpernova Nedir?'}</a></li>
                <li><a href="https://bilimgenc.tubitak.gov.tr/makale/gunesten-binlerce-kat-buyuk-yildizlar" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">TÜBİTAK Bilim Genç — {'Stars Thousands of Times Larger Than the Sun' if english else 'Güneş’ten Binlerce Kat Büyük Yıldızlar'}</a></li>
                <li><a href="https://bilimgenc.tubitak.gov.tr/makale/bir-dev-yildizin-yuzeyinde-devasa-boyutlarda-kabarciklar-gozlendi" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">TÜBİTAK Bilim Genç — {'Giant Bubbles Observed on the Surface of a Giant Star' if english else 'Bir Dev Yıldızın Yüzeyinde Devasa Boyutlarda Kabarcıklar Gözlendi'}</a></li>
                <li><a href="https://www.britannica.com/science/star-astronomy" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">Encyclopaedia Britannica — Star (Astronomy)</a></li>
                <li><a href="https://science.nasa.gov/mercury/facts/" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">NASA Science — Mercury Facts</a></li>
                <li><a href="https://science.nasa.gov/mercury/exploration/" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">NASA Science — Mercury Exploration</a></li>
                <li><a href="https://www.esa.int/Science_Exploration/Space_Science/BepiColombo" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">European Space Agency — BepiColombo</a></li>
                <li><a href="https://science.nasa.gov" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">NASA Science — Official Website</a></li>
                <li><a href="https://tua.gov.tr" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">{'Turkish Space Agency — Official Website' if english else 'Türkiye Uzay Ajansı — Resmî Web Sitesi'}</a></li>
                <li><a href="https://bilimgenc.tubitak.gov.tr" target="_blank" rel="noopener noreferrer" style="color:#a5f3fc;">{'TÜBİTAK Bilim Genç — Official Website' if english else 'TÜBİTAK Bilim Genç — Resmî Web Sitesi'}</a></li>
            </ul>
        </section>
        """,
        unsafe_allow_html=True,
    )

#JSTRBDM1
