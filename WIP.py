from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio
import streamlit as st


st.set_page_config(
    page_title="İnteraktif Uzay Zaman Tüneli & Veri Platformu",
    page_icon="🪐",
    layout="wide",
)

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

st.title("🪐 İNTERAKTİF UZAY ZAMAN TÜNELİ & VERİ MERKEZİ")
st.write(
    "Uzay tarihini, gezegen verilerini ve yörünge enkazı dağılımını"
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

yillar = sorted(veri_tabani.keys())
secilen_yil = st.select_slider(
    "📅 Zaman Tüneli Yılı (Tüm Veriler Bu Yıla Göre Güncellenir):",
    options=yillar,
    value=2020 if 2020 in yillar else yillar[-1],
)
st.divider()

veri = veri_tabani[secilen_yil]
tab1, tab2, tab3, tab4 = st.tabs(
    ["🪐 3D Sistem", "🗑️ Uzay Çöpleri", "📰 Gazete", "💻 Developer"]
)

with tab1:
    st.markdown("### 🪐 İnteraktif 3D Güneş Sistemi")
    simulasyon_yolu = Path(__file__).with_name("simulasyon.html")
    if not simulasyon_yolu.is_file():
        st.error(
            "3D simülasyon dosyası bulunamadı. "
            "simulasyon.html dosyasını WIP.py ile aynı klasöre koyun."
        )
    else:
        simulasyon_html = simulasyon_yolu.read_text(encoding="utf-8")
        simulasyon_html = simulasyon_html.replace(
            "__SELECTED_YEAR__", str(secilen_yil)
        )
        st.iframe(simulasyon_html, height=700)

with tab2:
    st.markdown(f"### 🗑️ {secilen_yil} Yılı Yörünge Çöpü ve Enkaz Analizi")
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
                    "Enkaz oranı: %{percent}<br>"
                    "%{customdata}"
                    "<extra></extra>"
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
                    "<span style='font-size:12px'>ENKAZ DAĞILIMI</span>"
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
        detailTitle.textContent = 'Bir enkaz dilimini incele';
        detailText.textContent =
          'Açıklamayı görmek için dilimin üzerine gel veya dokun.';
        detail.style.borderColor = '#00E5FF';
        return;
      }

      detail.classList.add('is-active');
      detailTitle.textContent =
        `${trace.labels[index]} · %${trace.values[index]}`;
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
        <html lang="tr">
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
                    <h3 id="debris-detail-title">Bir enkaz dilimini incele</h3>
                    <p id="debris-detail-text">
                        Açıklamayı görmek için dilimin üzerine gel veya dokun.
                    </p>
                </div>
            </section>
        </body>
        </html>
        """,
        height=570,
    )

with tab3:
    st.markdown(f"### 📰 Uzay Kroniği Gazetesi — {secilen_yil}")
    st.caption("Seçilen yılın uzay gelişmelerinden haberler")

    for haber in haberler[secilen_yil]:
        with st.container(border=True):
            resim_kolonu, yazi_kolonu = st.columns([0.9, 1.7], vertical_alignment="center")
            with resim_kolonu:
                st.image(haber["gorsel"], width="stretch")
            with yazi_kolonu:
                st.caption(f"UZAY HABERLERİ  •  {haber['tarih']}")
                st.markdown(f"#### {haber['baslik']}")
                st.write(haber["metin"])

with tab4:
    st.markdown("This Site Maded By JustRubidium")
