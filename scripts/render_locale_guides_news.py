#!/usr/bin/env python3
"""One-off renderer: locale guides.html and news.html from English sources."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GUIDES_BLOCKS = {
    "pl": {
        "lang": "pl",
        "title": "Playbook Sugargoo Spreadsheet | Workflow agenta | sugargoo spreadsheet",
        "desc": "Przewodnik do sugargoo spreadsheet: zasady portfela, QC magazynowe, próbna waga, ryzyko celne, ubezpieczenie i zwroty—wszystko po wklejeniu linku do Sugargoo.",
        "og_desc": "Po użyciu sugargoo spreadsheet te workflowy tłumaczą saldo Sugargoo, QC, rehearsal i wysyłkę.",
        "bc_home": "Strona główna",
        "bc_guides": "Poradniki",
        "skip": "Przejdź do treści",
        "brand_aria": "Strona główna sugargoo spreadsheet",
        "nav_aria": "Główne",
        "home": "Strona główna",
        "all_cat": "Wszystkie kategorie",
        "guides": "Poradniki",
        "spreadsheet": "Arkusz",
        "contact": "Kontakt",
        "news": "Aktualności",
        "lang_aria": "Wybierz język",
        "breadcrumb_aria": "Ścieżka nawigacji",
        "hero_h1": "Po sugargoo spreadsheet: co dzieje się wewnątrz Sugargoo",
        "hero_lead": """          Kopiowanie linku z <strong>sugargoo spreadsheet</strong> to dopiero pierwszy krok. Saldo,
          liczniki magazynowe, QC, konsolidacja i linie międzynarodowe działają przez
          <strong>Sugargoo</strong>. Ten playbook tłumaczy hałaśliwe fragmenty zakupów przez agenta na
          listy kontrolne—zawsze weryfikuj liczby na żywym koncie.""",
        "master_h2": "Notatki z pola: płatności, magazyn, QC, forwarding, cło i przypadki brzegowe",
        "master_p": """          Traktuj te sekcje jak towarzysza „co teraz?” do sugargoo spreadsheet. Nie zastępują
          wsparcia Sugargoo, ale pokazują, jak kupujący zwykle przeżywają każdy etap.""",
        "toc_nav_aria": "Sekcje przewodnika",
        "toc_label": "Przejdź do tematu",
        "toc_items": [
            "Ładowanie portfela Sugargoo",
            "Zwroty i wypłaty",
            "Liczniki przechowywania w magazynie",
            "Luki w śledzeniu",
            "Szacunkowa vs próbna waga",
            "Zatrzymania celne",
            "QC magazynowe w praktyce",
            "Uszkodzenia i wady po dostawie",
            "Kompromisy ubezpieczenia",
            "Kategorie ograniczone",
            "Problemy z płatnością",
            "Podatki importowe i cła",
            "Łączenie, rehearsal, wybór linii",
            "Promocje i zaproszenia",
        ],
        "sections": [
            (
                "Ładowanie portfela Sugargoo",
                """            Sugargoo działa na prepaid dla większości zakupów. Doładuj portfel metodami, które Sugargoo
            wymienia dla twojego kraju—karty, portfele lub opcje regionalne.""",
                [
                    "Doładuj przed flash sale, żeby krajowe przekazy nie stanęły.",
                    "Niektóre procesory rozliczają od razu; inne potrzebują dnia bankowego lub dwóch.",
                    "Zapisuj zrzuty ekranu, dopóki księga nie pokaże poprawnej kwoty.",
                ],
                None,
            ),
            (
                "Zwroty i wypłaty",
                """            Korzystaj z natywnych narzędzi zwrotu lub wypłaty w Sugargoo. Ścieżki różnią się według
            pierwotnej metody płatności i lokalnych przepisów.""",
                [
                    "Nigdy nie żądaj zwrotów przez tę stronę marketingową—tylko w Sugargoo.",
                    "Środki często wracają tym samym kanałem, którym zapłaciłeś.",
                    "Liczy się kilka dni roboczych na rozliczenie u operatora płatności.",
                ],
                None,
            ),
            (
                "Liczniki przechowywania w magazynie",
                """            Po dostawie krajowej towar leży w magazynie Sugargoo, dopóki nie wyślesz go międzynarodowo.
            Obowiązuje <strong>darmowe okno przechowywania</strong>—sprawdź aktualną politykę Sugargoo co do liczby godzin.""",
                [
                    "Wyślij lub skonsoliduj, zanim zacznie się płatne przechowywanie.",
                    "Porzucone paczki mogą być utylizowane według polityki—ustaw przypomnienia w kalendarzu.",
                ],
                "Wskazówka: łącz dopiero po pozytywnym QC—nie ma sensu scalać rzeczy, które i tak odrzucisz.",
            ),
            (
                "Luki w śledzeniu",
                """            Międzynarodowe śledzenie często się zatrzymuje: kolejki lotnicze, kolejki celne lub partnerzy
            ostatniej mili, którzy skanują paczki paczkami.""",
                [
                    "Porównaj długość przestoju z SLA przewoźnika dla danej linii.",
                    "Cło może trzymać paczki bez aktualizacji—cierpliwość plus dokumentacja.",
                    "Eskaluj przez Sugargoo, jeśli przekraczasz podany termin.",
                ],
                None,
            ),
            (
                "Szacunkowa vs próbna waga",
                """            Wyceny często używają <strong>szacunkowej wagi</strong> przed rehearsal. Po zapakowaniu
            <strong>rzeczywista waga</strong> (a czasem waga objętościowa) ustala końcowe porto.""",
                [
                    "Nadpłata często wraca na saldo.",
                    "Rehearsal może zmniejszyć objętość przy gabarytowych rzeczach.",
                ],
                None,
            ),
            (
                "Zatrzymania celne",
                """            Służby graniczne mogą kontrolować, skanować lub opodatkować paczki. Zatrzymanie nie zawsze
            oznacza konfiskatę.""",
                [
                    "Podawaj prawdę, jeśli proszą o faktury lub dokumenty.",
                    "Niektóre linie omijają wybrane kategorie—czytaj notatki przy linii.",
                    "Sprawdź lokalny limit bezclłowy zanim wyślesz.",
                ],
                None,
            ),
            (
                "QC magazynowe w praktyce",
                """            Fotografowie Sugargoo robią zdjęcia tego, co przyszło—inaczej niż lśniące foty sprzedawcy
            z wiersza sugargoo spreadsheet.""",
                [
                    "Przybliż etykiety, szwy i sylwetkę.",
                    "Poproś o zwrot lub wymianę, póki Sugargoo trzyma towar.",
                    "Po zatwierdzeniu wysyłki opcje się zwężają—wybieraj rozważnie.",
                ],
                None,
            ),
            (
                "Uszkodzenia i wady po dostawie",
                """            Jeśli paczka jest zmiażdżona lub przedmiot nie przechodzi kontroli, sfotografuj wszystko:
            karton zewnętrzny, etykiety i wadę.""",
                [
                    "Otwieraj tickety w Sugargoo w opublikowanych terminach.",
                    "Wyniki zależą od ubezpieczenia, zasad sprzedawcy i odpowiedzialności przewoźnika.",
                    "Redaktorzy sugargoo spreadsheet nie mogą nadpisać decyzji w sprawie.",
                ],
                None,
            ),
            (
                "Kompromisy ubezpieczenia",
                """            Opcjonalne ubezpieczenie może pokryć stratę lub uszkodzenie w transporcie. Limity i wyłączenia
            różnią się według linii.""",
                [
                    "Wysokowartościowe hauly zwykle uzasadniają składkę.",
                    "Czytaj wyłączenia (np. zajęcie przez cło).",
                    "Składaj roszczenia w Sugargoo według ich listy dowodów.",
                ],
                None,
            ),
            (
                "Kategorie ograniczone",
                """            Baterie, płyny, repliki lub podróbki mogą łamać zasady Sugargoo lub kraju, nawet jeśli ogłoszenie
            wciąż jest online.""",
                [
                    "Sprawdź listę zakazanych Sugargoo przed wysyłką.",
                    "Zapytaj wsparcie, jeśli kategoria jest na granicy.",
                ],
                None,
            ),
            (
                "Problemy z płatnością",
                """            Banki i portfele odrzucają obciążenia przez antyfraud, limity lub compliance regionalny.""",
                [
                    "Sprawdź datę ważności karty, kod pocztowy i monity 3-D Secure.",
                    "Użyj drugiej metody, jeśli Sugargoo to pozwala.",
                    "Duże pierwsze doładowania mogą wymagać dodatkowej weryfikacji tożsamości.",
                ],
                None,
            ),
            (
                "Podatki importowe i cła",
                """            Zwykle jesteś importerem—VAT, cło lub opłaty brokerskie mogą obowiązywać.""",
                [
                    "Sprawdź progi de minimis i stawki dla kategorii lokalnie.",
                    "Przewoźnicy czasem przedpłacają cła i fakturują przy dostawie.",
                ],
                None,
            ),
            (
                "Łączenie, rehearsal, wybór linii",
                """            Połącz wiele zakupów w jedną paczkę, zrób rehearsal dla dokładnej wagi, potem wybierz linię
            zgodnie z tolerancją ryzyka.""",
                [
                    "Łącz dopiero gdy każdy przedmiot przejdzie QC magazynowe.",
                    "Rehearsal może kosztować niewielką opłatę, ale zaoszczędzi na końcowej linii.",
                    "Balansuj tanio, szybko i bezpiecznie—wybierz to, co najważniejsze.",
                ],
                None,
            ),
            (
                "Promocje i zaproszenia",
                """            Sugargoo czasem oferuje kupony, bonusy polecające lub eventy sezonowe—czytaj drobny druk w aplikacji.""",
                [
                    "Nadużywanie promocji może zablokować konta.",
                    "Kwalifikacja zawsze według Sugargoo.",
                ],
                None,
            ),
        ],
        "footer_note": """          Łączenie sugargoo spreadsheet z infrastrukturą agenta Sugargoo utrzymuje szybkie odkrywanie,
          a zakupy pozostają w ochronie Sugargoo. Ta mikrostrona nie sprzedaje towaru ani nie obsługuje płatności.""",
        "cta_hub": "Przeglądaj hub arkusza",
        "cta_home": "Wróć na stronę główną",
        "related_h2": "Więcej zasobów sugargoo spreadsheet",
        "rel_news_t": "Aktualności i changelog",
        "rel_news_s": "Przypomnienia QC, alerty martwych linków i zmiany w hubie.",
        "rel_contact_t": "Społeczność",
        "rel_contact_s": "Discord: opinie o arkuszu, haul'e i Q&amp;A kupujących.",
        "rel_hub_t": "Skrót do huba",
        "rel_hub_s": "Od razu do żywego huba sugargoo spreadsheet.",
        "footer_line": "sprzedawcy platformy Sugargoo",
    },
}

# Spanish
GUIDES_BLOCKS["es"] = {
    **{k: v for k, v in GUIDES_BLOCKS["pl"].items() if k not in ("lang", "sections", "toc_items", "hero_lead", "master_h2", "master_p", "footer_note")},
    "lang": "es",
    "title": "Playbook Sugargoo Spreadsheet | Flujo del agente | sugargoo spreadsheet",
    "desc": "Guía complementaria al sugargoo spreadsheet: reglas de cartera, QC de almacén, peso de ensayo, riesgo aduanero, seguro y reembolsos—todo tras pegar un enlace en Sugargoo.",
    "og_desc": "Tras usar el sugargoo spreadsheet, estos flujos explican saldo Sugargoo, QC, ensayo y envío.",
    "bc_home": "Inicio",
    "bc_guides": "Guías",
    "skip": "Saltar al contenido",
    "brand_aria": "Inicio sugargoo spreadsheet",
    "nav_aria": "Principal",
    "home": "Inicio",
    "all_cat": "Todas las categorías",
    "guides": "Guías",
    "spreadsheet": "Hoja",
    "contact": "Contacto",
    "news": "Noticias",
    "lang_aria": "Seleccionar idioma",
    "breadcrumb_aria": "Migas de pan",
    "hero_h1": "Después del sugargoo spreadsheet: qué pasa dentro de Sugargoo",
    "hero_lead": """          Copiar un enlace del <strong>sugargoo spreadsheet</strong> es solo el primer paso. Cartera,
          temporizadores de almacén, QC, consolidación y líneas internacionales pasan por
          <strong>Sugargoo</strong>. Este playbook traduce las partes ruidosas de comprar con agente en
          listas de comprobación—verifica siempre los números en tu cuenta en vivo.""",
    "master_h2": "Notas de campo: pagos, almacén, QC, reenvío, aduanas y casos límite",
    "master_p": """          Piensa en estas secciones como el compañero «¿y ahora qué?» del sugargoo spreadsheet. No sustituyen
          al soporte de Sugargoo, pero explican cómo los compradores suelen vivir cada etapa.""",
        "toc_nav_aria": "Secciones de la guía",
        "toc_label": "Ir a un tema",
    "toc_items": [
        "Cargar tu cartera Sugargoo",
        "Reembolsos y retiradas",
        "Temporizadores de almacén",
        "Lagunas de seguimiento",
        "Peso estimado vs ensayo",
        "Retenciones aduaneras",
        "QC de almacén en detalle",
        "Daños y defectos a la llegada",
        "Compromisos del seguro",
        "Categorías restringidas",
        "Problemas de pago",
        "Impuestos de importación y aranceles",
        "Combinaciones, ensayo y elección de línea",
        "Promos e invitaciones",
    ],
    "sections": [
        (
            "Cargar tu cartera Sugargoo",
            """            Sugargoo funciona con saldo prepago para la mayoría de compras. Carga la cartera con los métodos
            que Sugargoo liste para tu país—tarjetas, monederos u opciones regionales.""",
            [
                "Carga antes de ventas flash para que el reenvío nacional no se pare.",
                "Algunos procesadores liquidan al instante; otros necesitan un día bancario o dos.",
                "Guarda capturas hasta que el libro refleje el importe correcto.",
            ],
            None,
        ),
        (
            "Reembolsos y retiradas",
            """            Usa las herramientas nativas de reembolso o retirada de Sugargoo. Las rutas varían según el método
            de pago original y la normativa local.""",
            [
                "Nunca pidas reembolsos por este sitio de marketing—solo dentro de Sugargoo.",
                "El dinero suele volver por el mismo canal con el que pagaste.",
                "Cuenta unos días hábiles para que los procesadores concilien.",
            ],
            None,
        ),
        (
            "Temporizadores de almacén",
            """            Tras la entrega nacional, tu artículo permanece en almacén Sugargoo hasta que envíes
            internacionalmente. Aplica una <strong>ventana de almacén gratis</strong>—consulta la política
            actual de Sugargoo para las horas exactas.""",
            [
                "Envía o consolida antes de que empiece el almacén de pago.",
                "Los paquetes abandonados pueden desecharse según política—pon recordatorios en el calendario.",
            ],
            "Consejo: combina solo después de pasar QC—no tiene sentido fusionar artículos que podrías rechazar.",
        ),
        (
            "Lagunas de seguimiento",
            """            El seguimiento internacional a menudo se pausa: colas aéreas, colas aduaneras o socios de última
            milla que escanean paquetes en lote.""",
            [
                "Compara la duración de la parada con el SLA del transportista para esa línea.",
                "Aduanas puede retener paquetes sin actualizaciones—paciencia y documentación.",
                "Escala vía Sugargoo si superas la ventana indicada.",
            ],
            None,
        ),
        (
            "Peso estimado vs ensayo",
            """            Las cotizaciones suelen usar <strong>peso estimado</strong> antes del ensayo. Tras embalar,
            el <strong>peso real</strong> (y a veces el volumétrico) fija el porte final.""",
            [
                "El sobrepago a menudo se acredita al saldo.",
                "El ensayo puede reducir volumen en artículos voluminosos.",
            ],
            None,
        ),
        (
            "Retenciones aduaneras",
            """            Las autoridades pueden inspeccionar, escanear o gravar paquetes. Una retención no siempre es
            decomiso.""",
            [
                "Declara con veracidad si piden facturas o documentos.",
                "Algunas líneas evitan ciertas categorías—lee las notas de la línea.",
                "Conoce el margen libre de aranceles de tu país antes de enviar.",
            ],
            None,
        ),
        (
            "QC de almacén en detalle",
            """            Los fotógrafos de Sugargoo capturan lo que llegó—distinto de las fotos del vendedor en una fila
            del sugargoo spreadsheet.""",
            [
                "Amplía etiquetas, costuras y silueta.",
                "Pide devolución o cambio mientras Sugargoo retenga el artículo.",
                "Tras aprobar el envío, las opciones se reducen—elige con cuidado.",
            ],
            None,
        ),
        (
            "Daños y defectos a la llegada",
            """            Si la caja llega aplastada o el artículo no pasa inspección, fotografía todo: cartón exterior,
            etiquetas y el defecto.""",
            [
                "Abre tickets en Sugargoo dentro de sus plazos publicados.",
                "Los resultados dependen del seguro, reglas del vendedor y responsabilidad del transportista.",
                "Los editores del sugargoo spreadsheet no pueden anular decisiones de casos.",
            ],
            None,
        ),
        (
            "Compromisos del seguro",
            """            El seguro opcional puede cubrir pérdida o daño en tránsito. Topes y exclusiones varían por línea.""",
            [
                "Los hauls de alto valor suelen justificar la prima.",
                "Lee exclusiones (p. ej. decomiso aduanero).",
                "Presenta reclamaciones en Sugargoo con su lista de pruebas.",
            ],
            None,
        ),
        (
            "Categorías restringidas",
            """            Pilas, líquidos, réplicas o falsificaciones pueden violar reglas de Sugargoo o del país aunque
            el anuncio siga online.""",
            [
                "Contrasta la lista de prohibidos de Sugargoo antes de enviar.",
                "Pregunta al soporte si la categoría es dudosa.",
            ],
            None,
        ),
        (
            "Problemas de pago",
            """            Bancos y monederos rechazan cargos por fraude, límites o cumplimiento regional.""",
            [
                "Verifica caducidad de tarjeta, código postal de facturación y avisos 3-D Secure.",
                "Usa un segundo método si Sugargoo lo permite.",
                "Las primeras cargas grandes pueden requerir verificación extra de identidad.",
            ],
            None,
        ),
        (
            "Impuestos de importación y aranceles",
            """            Sueles ser el importador—IVA, aranceles u honorarios de gestión pueden aplicar.""",
            [
                "Investiga umbrales de minimis y tipos por categoría localmente.",
                "Los transportistas a veces prepagan aranceles y te facturan al entregar.",
            ],
            None,
        ),
        (
            "Combinaciones, ensayo y elección de línea",
            """            Fusiona varias compras en un solo paquete, haz ensayo para peso preciso, luego elige una línea
            que encaje con tu tolerancia al riesgo.""",
            [
                "Combina solo cuando cada artículo pase QC de almacén.",
                "El ensayo puede costar una pequeña tarifa pero ahorra en la línea final.",
                "Equilibra barato, rápido y seguro—prioriza lo que más importe.",
            ],
            None,
        ),
        (
            "Promos e invitaciones",
            """            Sugargoo a veces ofrece cupones, bonos de referidos o eventos de temporada—lee la letra pequeña en la app.""",
            [
                "Abusar de promos puede bloquear cuentas.",
                "La elegibilidad la decide siempre Sugargoo.",
            ],
            None,
        ),
    ],
    "footer_note": """          Emparejar un sugargoo spreadsheet con las vías de agente de Sugargoo mantiene el descubrimiento rápido
          mientras las compras quedan bajo las protecciones de Sugargoo. Este micrositio no vende inventario ni
          procesa pagos.""",
    "cta_hub": "Ver hub de la hoja",
    "cta_home": "Volver al inicio",
    "related_h2": "Más recursos sugargoo spreadsheet",
    "rel_news_t": "Noticias y changelog",
    "rel_news_s": "Recordatorios QC, alertas de enlaces rotos y ajustes del hub.",
    "rel_contact_t": "Comunidad",
    "rel_contact_s": "Discord: feedback del sheet, hauls y preguntas de compradores.",
    "rel_hub_t": "Atajo al hub",
    "rel_hub_s": "Entra directo al hub vivo del sugargoo spreadsheet.",
    "footer_line": "comerciantes de la plataforma Sugargoo",
}

# German - abbreviated copy using same structure as PL/ES for remaining keys
GUIDES_BLOCKS["de"] = {
    **GUIDES_BLOCKS["es"],
    "lang": "de",
    "title": "Sugargoo Spreadsheet Playbook | Agenten-Workflow | sugargoo spreadsheet",
    "desc": "Begleitguide zum sugargoo spreadsheet: Wallet-Regeln, Lager-QC, Rehearsal-Gewicht, Zollrisiko, Versicherung und Erstattungen—alles nach dem Einfügen eines Links bei Sugargoo.",
    "og_desc": "Nach dem sugargoo spreadsheet erklären diese Workflows Sugargoo-Guthaben, QC, Rehearsal und Versand.",
    "bc_home": "Startseite",
    "bc_guides": "Ratgeber",
    "skip": "Zum Inhalt springen",
    "brand_aria": "Startseite sugargoo spreadsheet",
    "nav_aria": "Hauptnavigation",
    "home": "Startseite",
    "all_cat": "Alle Kategorien",
    "guides": "Ratgeber",
    "spreadsheet": "Tabelle",
    "contact": "Kontakt",
    "news": "Neuigkeiten",
    "lang_aria": "Sprache wählen",
    "breadcrumb_aria": "Brotkrümel",
    "hero_h1": "Nach dem sugargoo spreadsheet: was in Sugargoo passiert",
    "hero_lead": """          Einen Link aus dem <strong>sugargoo spreadsheet</strong> zu kopieren ist nur Schritt eins. Guthaben,
          Lager-Timers, QC, Konsolidierung und internationale Linien laufen über
          <strong>Sugargoo</strong>. Dieses Playbook übersetzt laute Agent-Kaufteile in Checklisten—Zahlen immer
          mit dem Live-Konto abgleichen.""",
    "master_h2": "Feldnotizen: Zahlungen, Lager, QC, Weiterleitung, Zoll und Sonderfälle",
    "master_p": """          Diese Abschnitte sind der «und jetzt?»-Begleiter zum sugargoo spreadsheet. Sie ersetzen nicht den
          Sugargoo-Support, erklären aber typische Käufererfahrungen pro Stufe.""",
        "toc_nav_aria": "Abschnitte des Ratgebers",
        "toc_label": "Zu einem Thema springen",
    "toc_items": [
        "Sugargoo-Wallet laden",
        "Erstattungen & Auszahlungen",
        "Lagertimer",
        "Tracking-Lücken",
        "Geschätztes vs. Rehearsal-Gewicht",
        "Zollstopps",
        "Lager-QC im Detail",
        "Ankunftsschäden & Mängel",
        "Versicherungs-Abwägungen",
        "Eingeschränkte Kategorien",
        "Zahlungsprobleme",
        "Einfuhrsteuern & Zölle",
        "Kombis, Rehearsal, Linienwahl",
        "Promos & Einladungen",
    ],
    "sections": [
        (
            "Sugargoo-Wallet laden",
            """            Sugargoo nutzt für die meisten Käufe Prepaid-Guthaben. Lade das Wallet mit den Methoden, die Sugargoo
            für dein Land auflistet—Karten, Wallets oder regionale Optionen.""",
            [
                "Vor Flash-Sales aufladen, damit inländische Weiterleitung nicht stockt.",
                "Manche Prozessoren buchen sofort; andere brauchen einen Banktag oder zwei.",
                "Screenshots speichern, bis das Ledger den richtigen Betrag zeigt.",
            ],
            None,
        ),
        (
            "Erstattungen & Auszahlungen",
            """            Nutze Sugargoos native Erstattungs- oder Auszahlungstools. Wege unterscheiden sich nach ursprünglicher
            Zahlungsmethode und lokaler Regulierung.""",
            [
                "Niemals Erstattungen über diese Marketing-Site—nur in Sugargoo.",
                "Geld kehrt oft über denselben Kanal zurück, mit dem du zahltest.",
                "Einige Werktage für die Abstimmung der Prozessoren einplanen.",
            ],
            None,
        ),
        (
            "Lagertimer",
            """            Nach inländischer Zustellung liegt der Artikel im Sugargoo-Lager, bis du international versendest.
            Es gilt ein <strong>kostenfreies Lagerfenster</strong>—Sugargoos aktuelle Policy zu Stunden prüfen.""",
            [
                "Versenden oder konsolidieren, bevor kostenpflichtiges Lager beginnt.",
                "Verwaiste Pakete können laut Policy verworfen werden—Kalender-Erinnerungen setzen.",
            ],
            "Tipp: erst nach bestandenem QC kombinieren—keinen Sinn, Artikel zu bündeln, die du ablehnen könntest.",
        ),
        (
            "Tracking-Lücken",
            """            Internationales Tracking pausiert oft: Flug-Rückstände, Zoll-Warteschlangen oder Last-Mile-Partner,
            die Pakete batch-scannen.""",
            [
                "Stopp-Länge mit Carrier-SLA für diese Linie vergleichen.",
                "Zoll kann Pakete ohne Updates halten—Geduld plus Unterlagen.",
                "Über Sugargoo eskalieren, wenn du das angegebene Fenster sprengst.",
            ],
            None,
        ),
        (
            "Geschätztes vs. Rehearsal-Gewicht",
            """            Angebote nutzen oft <strong>geschätztes Gewicht</strong> vor Rehearsal. Nach dem Packen setzen
            <strong>Ist-Gewicht</strong> (und manchmal Volumengewicht) das Endporto.""",
            [
                "Überzahlung wird oft dem Guthaben gutgeschrieben.",
                "Rehearsal kann Volumen bei sperrigen Teilen reduzieren.",
            ],
            None,
        ),
        (
            "Zollstopps",
            """            Grenzbehörden können Pakete prüfen, scannen oder besteuern. Ein Stopp bedeutet nicht immer Beschlagnahme.""",
            [
                "Bei Rechnungen oder IDs wahrheitsgemäß angeben.",
                "Manche Linien meiden Kategorien—Liniennotizen lesen.",
                "Freigrenze deines Landes vor Versand kennen.",
            ],
            None,
        ),
        (
            "Lager-QC im Detail",
            """            Sugargoos Fotografen zeigen, was ankam—anders als glatte Verkäuferfotos in einer sugargoo spreadsheet-Zeile.""",
            [
                "Labels, Nähte und Silhouette vergrößern.",
                "Rückgabe oder Umtausch anfragen, solange Sugargoo den Artikel hält.",
                "Nach Versandfreigabe werden Optionen weniger—sorgfältig wählen.",
            ],
            None,
        ),
        (
            "Ankunftsschäden & Mängel",
            """            Wenn die Box zerquetscht ist oder der Artikel die Prüfung nicht besteht, alles fotografieren: Außenkarton,
            Labels und den Mangel.""",
            [
                "Tickets innerhalb der Sugargoo-Fristen öffnen.",
                "Ergebnisse hängen von Versicherung, Verkäuferregeln und Carrier-Haftung ab.",
                "sugargoo spreadsheet-Redakteure können Case-Entscheidungen nicht überstimmen.",
            ],
            None,
        ),
        (
            "Versicherungs-Abwägungen",
            """            Optionale Versicherung kann Verlust oder Transportschaden decken. Deckel und Ausschlüsse unterscheiden sich pro Linie.""",
            [
                "Hochwertige Hauls rechtfertigen oft die Prämie.",
                "Ausschlüsse lesen (z. B. Zollbeschlagnahme).",
                "Ansprüche bei Sugargoo mit deren Nachweisliste einreichen.",
            ],
            None,
        ),
        (
            "Eingeschränkte Kategorien",
            """            Batterien, Flüssigkeiten, Repliken oder Fakes können Sugargoo- oder Landesregeln verletzen, auch wenn ein Listing noch online ist.""",
            [
                "Sugargoos Verbotsliste vor Versand abgleichen.",
                "Support fragen, wenn die Grenze unscharf wirkt.",
            ],
            None,
        ),
        (
            "Zahlungsprobleme",
            """            Banken und Wallets lehnen Abbuchungen wegen Fraud-Trigger, Limits oder regionaler Compliance ab.""",
            [
                "Kartenablauf, Rechnungs-PLZ und 3-D-Secure prüfen.",
                "Zweite Methode nutzen, wenn Sugargoo es erlaubt.",
                "Große Erstlads können Extra-ID-Checks brauchen.",
            ],
            None,
        ),
        (
            "Einfuhrsteuern & Zölle",
            """            Du bist typischerweise Importeur—MwSt., Zoll oder Brokergebühren können anfallen.""",
            [
                "De-minimis-Schwellen und Kategorientarife lokal recherchieren.",
                "Carrier zahlen manchmal Zoll vor und stellen dir bei Lieferung in Rechnung.",
            ],
            None,
        ),
        (
            "Kombis, Rehearsal, Linienwahl",
            """            Mehrere Käufe zu einem Paket zusammenführen, Rehearsal für genaues Gewicht, dann Linie nach Risikotoleranz wählen.""",
            [
                "Erst kombinieren, wenn jedes Teil Lager-QC bestanden hat.",
                "Rehearsal kann kleine Gebühr kosten, spart aber auf der Endlinie.",
                "Billig, schnell, sicher abwägen—priorisieren, was zählt.",
            ],
            None,
        ),
        (
            "Promos & Einladungen",
            """            Sugargoo hat gelegentlich Coupons, Referral-Boni oder Saison-Events—Kleingedrucktes in der App lesen.""",
            [
                "Promo-Missbrauch kann Konten sperren.",
                "Berechtigung entscheidet immer Sugargoo.",
            ],
            None,
        ),
    ],
    "footer_note": """          sugargoo spreadsheet mit Sugargoos Agent-Schienen zu koppeln hält Discovery schnell, während Käufe in Sugargoos
          Schutz bleiben. Diese Microsite verkauft kein Inventar und verarbeitet keine Zahlungen.""",
    "cta_hub": "Hub der Tabelle durchsuchen",
    "cta_home": "Zurück zur Startseite",
    "related_h2": "Weitere sugargoo spreadsheet-Ressourcen",
    "rel_news_t": "Neuigkeiten & Changelog",
    "rel_news_s": "QC-Hinweise, tote-Link-Alerts und Hub-Anpassungen.",
    "rel_contact_t": "Community",
    "rel_contact_s": "Discord: Sheet-Feedback, Haul-Talk und Käufer-Q&A.",
    "rel_hub_t": "Hub-Shortcut",
    "rel_hub_s": "Direkt in den Live-sugargoo spreadsheet-Hub.",
    "footer_line": "Händler der Sugargoo-Plattform",
}

GUIDES_BLOCKS["pt"] = {
    **GUIDES_BLOCKS["de"],
    "lang": "pt-PT",
    "title": "Playbook Sugargoo Spreadsheet | Fluxo do agente | sugargoo spreadsheet",
    "desc": "Guia complementar ao sugargoo spreadsheet: regras de carteira, QC de armazém, peso de ensaio, risco alfandegário, seguro e reembolsos—tudo depois de colares um link na Sugargoo.",
    "og_desc": "Depois de usares o sugargoo spreadsheet, estes fluxos explicam saldo Sugargoo, QC, ensaio e envio.",
    "bc_home": "Início",
    "bc_guides": "Guias",
    "skip": "Saltar para o conteúdo",
    "brand_aria": "Início sugargoo spreadsheet",
    "nav_aria": "Principal",
    "home": "Início",
    "all_cat": "Todas as categorias",
    "guides": "Guias",
    "spreadsheet": "Folha",
    "contact": "Contacto",
    "news": "Notícias",
    "lang_aria": "Selecionar idioma",
    "breadcrumb_aria": "Navegação estrutural",
    "hero_h1": "Depois do sugargoo spreadsheet: o que acontece dentro da Sugargoo",
    "hero_lead": """          Copiar um link do <strong>sugargoo spreadsheet</strong> é só o primeiro passo. Saldo,
          temporizadores de armazém, QC, consolidação e linhas internacionais passam pela
          <strong>Sugargoo</strong>. Este playbook traduz as partes ruidosas de comprar com agente em
          listas de verificação—confirma sempre os números na tua conta em tempo real.""",
    "master_h2": "Notas de campo: pagamentos, armazém, QC, reencaminhamento, alfândega e casos limite",
    "master_p": """          Vê estas secções como o companheiro «e agora?» do sugargoo spreadsheet. Não substituem o
          suporte Sugargoo, mas explicam como os compradores costumam viver cada etapa.""",
    "toc_nav_aria": "Secções do guia",
    "toc_label": "Ir para um tópico",
    "toc_items": [
        "Carregar a carteira Sugargoo",
        "Reembolsos e levantamentos",
        "Temporizadores no armazém",
        "Lacunas de rastreio",
        "Peso estimado vs ensaio",
        "Retenções alfandegárias",
        "QC de armazém a fundo",
        "Danos e defeitos à chegada",
        "Compromissos do seguro",
        "Categorias restritas",
        "Problemas de pagamento",
        "Impostos de importação e direitos",
        "Combinações, ensaio e escolha de linha",
        "Promos e convites",
    ],
    "sections": [
        (
            "Carregar a carteira Sugargoo",
            """            A Sugargoo usa saldo pré-pago na maioria das compras. Carrega a carteira com os métodos que a Sugargoo
            lista para o teu país—cartões, carteiras digitais ou opções regionais.""",
            [
                "Carrega antes de saldos-relâmpago para o reencaminhamento nacional não parar.",
                "Alguns processadores liquidam na hora; outros precisam de um ou dois dias bancários.",
                "Guarda capturas até o extrato reflectir o valor correcto.",
            ],
            None,
        ),
        (
            "Reembolsos e levantamentos",
            """            Usa as ferramentas nativas de reembolso ou levantamento na Sugargoo. Os caminhos variam conforme o método
            de pagamento original e a regulamentação local.""",
            [
                "Nunca peças reembolsos através deste site de marketing—só dentro da Sugargoo.",
                "O dinheiro costuma voltar pelo mesmo canal com que pagaste.",
                "Conta com alguns dias úteis para os processadores reconciliarem.",
            ],
            None,
        ),
        (
            "Temporizadores no armazém",
            """            Após a entrega nacional, o artigo fica no armazém Sugargoo até enviares internacionalmente. Há uma
            <strong>janela de armazém gratuita</strong>—consulta a política actual da Sugargoo para o número exacto de horas.""",
            [
                "Envia ou consolida antes de começar armazém pago.",
                "Encomendas abandonadas podem ser descartadas conforme política—usa lembretes no calendário.",
            ],
            "Dica: combina só depois de passar o QC—não faz sentido fundir artigos que possas rejeitar.",
        ),
        (
            "Lacunas de rastreio",
            """            O rastreio internacional páusa muitas vezes: filas aéreas, filas alfandegárias ou parceiros de última milha
            que escaneiam encomendas em lote.""",
            [
                "Compara a duração da paragem com o SLA da transportadora para essa linha.",
                "Alfândega pode segurar encomendas sem actualizações—paciência e documentação.",
            ],
            None,
        ),
        (
            "Peso estimado vs ensaio",
            """            As cotações usam muitas vezes <strong>peso estimado</strong> antes do ensaio. Depois de embalar, o
            <strong>peso real</strong> (e por vezes o volumétrico) define o porte final.""",
            [
                "O excesso de pagamento é muitas vezes creditado no saldo.",
                "O ensaio pode reduzir volume em artigos volumosos.",
            ],
            None,
        ),
        (
            "Retenções alfandegárias",
            """            As autoridades podem inspeccionar, digitalizar ou tributar encomendas. Uma retenção nem sempre é apreensão.""",
            [
                "Declara com verdade se pedirem facturas ou documentos.",
                "Algumas linhas evitam certas categorias—lê as notas da linha.",
                "Conhece o limiar isento do teu país antes de enviar.",
            ],
            None,
        ),
        (
            "QC de armazém a fundo",
            """            Os fotógrafos da Sugargoo mostram o que chegou—diferente das fotos do vendedor numa linha do sugargoo spreadsheet.""",
            [
                "Amplia etiquetas, costuras e silhueta.",
                "Pede devolução ou troca enquanto a Sugargoo segura o artigo.",
                "Depois de aprovares o envio, as opções estreitam—escolhe com cuidado.",
            ],
            None,
        ),
        (
            "Danos e defeitos à chegada",
            """            Se a caixa chega esmagada ou o artigo falha inspecção, fotografa tudo: cartão exterior, etiquetas e o defeito.""",
            [
                "Abre tickets na Sugargoo dentro das janelas publicadas.",
                "Os resultados dependem do seguro, regras do vendedor e responsabilidade da transportadora.",
                "Os editores do sugargoo spreadsheet não podem sobrepor decisões de casos.",
            ],
            None,
        ),
        (
            "Compromissos do seguro",
            """            O seguro opcional pode cobrir perda ou dano em trânsito. Limites e exclusões variam por linha.""",
            [
                "Hauls de alto valor normalmente justificam o prémio.",
                "Lê exclusões (ex.: apreensão alfandegária).",
                "Apresenta reclamações na Sugargoo com a lista de provas deles.",
            ],
            None,
        ),
        (
            "Categorias restritas",
            """            Pilhas, líquidos, réplicas ou contrafacções podem violar regras Sugargoo ou do país mesmo que o anúncio ainda esteja online.""",
            [
                "Cruza a lista de proibidos Sugargoo antes de enviar.",
                "Pergunta ao suporte se a categoria é limítrofe.",
            ],
            None,
        ),
        (
            "Problemas de pagamento",
            """            Bancos e carteiras recusam cobranças por fraude, limites ou conformidade regional.""",
            [
                "Verifica validade do cartão, código postal de facturação e avisos 3-D Secure.",
                "Usa um segundo método se a Sugargoo permitir.",
                "Primeiras cargas grandes podem exigir verificação extra de identidade.",
            ],
            None,
        ),
        (
            "Impostos de importação e direitos",
            """            Normalmente és o importador—IVA, direitos ou taxas de desalfandegamento podem aplicar-se.""",
            [
                "Investiga limiares de minimis e taxas por categoria localmente.",
                "Transportadoras por vezes pré-pagam direitos e facturam-te na entrega.",
            ],
            None,
        ),
        (
            "Combinações, ensaio e escolha de linha",
            """            Junta várias compras numa encomensa, faz ensaio para peso correcto, depois escolhe uma linha que corresponda à tua tolerância a risco.""",
            [
                "Combina só depois de cada artigo passar QC de armazém.",
                "O ensaio pode custar uma taxa pequena mas poupa na linha final.",
                "Equilibra barato, rápido e seguro—prioriza o que mais importa.",
            ],
            None,
        ),
        (
            "Promos e convites",
            """            A Sugargoo ocasionalmente oferece cupões, bónus de referência ou eventos de época—lê a letra pequena na app.""",
            [
                "Abusar de promos pode bloquear contas.",
                "A elegibilidade decide sempre a Sugargoo.",
            ],
            None,
        ),
    ],
    "footer_note": """          Emparelhar um sugargoo spreadsheet com as vias de agente Sugargoo mantém a descoberta rápida enquanto as compras
          ficam nas protecções Sugargoo. Este microsite não vende inventário nem processa pagamentos.""",
    "cta_hub": "Ver hub da folha",
    "cta_home": "Voltar ao início",
    "related_h2": "Mais recursos sugargoo spreadsheet",
    "rel_news_t": "Notícias e changelog",
    "rel_news_s": "Lembretes QC, alertas de links mortos e ajustes do hub.",
    "rel_contact_t": "Comunidade",
    "rel_contact_s": "Discord: feedback da folha, hauls e Q&A de compradores.",
    "rel_hub_t": "Atalho ao hub",
    "rel_hub_s": "Entra directamente no hub vivo sugargoo spreadsheet.",
    "footer_line": "comerciantes da plataforma Sugargoo",
}


def build_guides_html(locale: str, prefix: str) -> str:
    b = GUIDES_BLOCKS[locale]
    lang_links = []
    for href, label, lang_attr, is_cur in (
        ("/guides.html", "EN", "en", False),
        ("/pl/guides.html", "PL", "pl", locale == "pl"),
        ("/pt/guides.html", "PT", "pt-PT", locale == "pt"),
        ("/es/guides.html", "ES", "es", locale == "es"),
        ("/de/guides.html", "DE", "de", locale == "de"),
    ):
        cur = ' aria-current="page"' if is_cur else ""
        lang_links.append(f'            <a href="{href}"{cur} lang="{lang_attr}">{label}</a>')
    lang_menu_html = "\n".join(lang_links)
    parts = [p.strip() for p in b["title"].split("|")]
    og_title = " | ".join(parts[:2]) if len(parts) >= 2 else b["title"]
    toc_ol = "\n".join(
        f'            <li><a href="#g{i}">{b["toc_items"][i - 1]}</a></li>'
        for i in range(1, 15)
    )
    sections_html = []
    for i, (title, para, bullets, tip) in enumerate(b["sections"], start=1):
        lis = "\n".join(f"            <li>{x}</li>" for x in bullets)
        tip_block = ""
        if tip:
            tip_block = f'\n          <p class="guides-tip">\n            {tip}\n          </p>'
        sections_html.append(
            f"""        <section class="guide-section" id="g{i}">
          <h3>
            <span class="guide-num" aria-hidden="true">{i}</span>
            {title}
          </h3>
          <p>
{para}
          </p>
          <ul>
{lis}
          </ul>{tip_block}
        </section>"""
        )
    sections_joined = "\n\n".join(sections_html)

    return f"""<!DOCTYPE html>
<html lang="{b["lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" type="image/png" href="../images/flame-icon.png" sizes="225x225" />
    <link rel="icon" type="image/png" href="../images/favicon-32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="../images/favicon-16.png" sizes="16x16" />
    <link rel="apple-touch-icon" href="../images/apple-touch-icon.png" />
    <title>
      {b["title"]}
    </title>
    <meta
      name="description"
      content="{b["desc"]}"
    />
    <link rel="canonical" href="https://sugargooospreadsheet.com/{prefix}guides.html" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://sugargooospreadsheet.com/{prefix}guides.html" />
    <meta
      property="og:title"
      content="{og_title}"
    />
    <meta
      property="og:description"
      content="{b["og_desc"]}"
    />
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{b["bc_home"]}",
            "item": "https://sugargooospreadsheet.com/{prefix.rstrip("/")}/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{b["bc_guides"]}",
            "item": "https://sugargooospreadsheet.com/{prefix}guides.html"
          }}
        ]
      }}
    </script>
    <link rel="alternate" hreflang="en" href="https://sugargooospreadsheet.com/guides.html" />
    <link rel="alternate" hreflang="pl" href="https://sugargooospreadsheet.com/pl/guides.html" />
    <link rel="alternate" hreflang="pt-PT" href="https://sugargooospreadsheet.com/pt/guides.html" />
    <link rel="alternate" hreflang="es" href="https://sugargooospreadsheet.com/es/guides.html" />
    <link rel="alternate" hreflang="de" href="https://sugargooospreadsheet.com/de/guides.html" />
    <link rel="alternate" hreflang="x-default" href="https://sugargooospreadsheet.com/guides.html" />
    <link rel="stylesheet" href="../styles.css" />
  </head>
  <body>
    <a class="skip-link" href="#main">{b["skip"]}</a>
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="/{prefix.rstrip("/")}/" aria-label="{b["brand_aria"]}">
          <img
            class="brand-logo"
            src="../images/logo.png"
            width="200"
            height="40"
            alt="Sugargoo"
            decoding="async"
          />
          <span class="brand-text">sugargoo spreadsheet</span>
        </a>
        <nav aria-label="{b["nav_aria"]}">
          <ul>
            <li><a href="/{prefix.rstrip("/")}/">{b["home"]}</a></li>
            <li class="has-sub">
              <button type="button" aria-expanded="false" aria-haspopup="true">
                {b["all_cat"]}
              </button>
              <div class="submenu" role="menu">
                <a href="https://maisonlooks.com/en/c/shoes" role="menuitem">Shoes</a>
                <a href="https://maisonlooks.com/en/c/jackets" role="menuitem">Jackets</a>
                <a href="https://maisonlooks.com/en/c/clothing" role="menuitem">Hoodies / Sweaters</a>
                <a href="https://maisonlooks.com/en/c/t-shirts" role="menuitem">T-Shirts</a>
                <a href="https://maisonlooks.com/en/c/clothing" role="menuitem">Pants / Shorts</a>
                <a href="https://maisonlooks.com/en/products" role="menuitem">Bags</a>
                <a href="https://maisonlooks.com/en/c/headwear" role="menuitem">Headwear</a>
                <a href="https://maisonlooks.com/en/c/accessories" role="menuitem">Accessories</a>
                <a href="https://maisonlooks.com/en/c/electronics" role="menuitem">Electronics</a>
                <a href="https://maisonlooks.com/en/c/perfume" role="menuitem">Perfume</a>
                <a href="https://maisonlooks.com/en/products" role="menuitem">Jersey</a>
                <a href="https://maisonlooks.com/en/products" role="menuitem">Other</a>
              </div>
            </li>
            <li><a href="guides.html" aria-current="page">{b["guides"]}</a></li>
            <li><a href="spreadsheet.html">{b["spreadsheet"]}</a></li>
            <li><a href="contact.html">{b["contact"]}</a></li>
            <li><a href="news.html">{b["news"]}</a></li>
          </ul>
        </nav>
        <div class="header-end">
        <div class="header-cta">
          <a
            class="btn btn-primary"
            href="https://maisonlooks.com/?utm_source=sugargooospreadsheet"
            >sugargoo spreadsheet</a
          >
        </div>
        <nav class="language-switcher has-lang" aria-label="{b["lang_aria"]}">
          <button type="button" class="lang-globe-btn" aria-haspopup="true" aria-expanded="false" aria-label="{b["lang_aria"]}">
            <svg class="lang-globe-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <circle cx="12" cy="12" r="10" />
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
            </svg>
          </button>
                    <div class="lang-menu" role="menu">
{lang_menu_html}
          </div>
        </nav>
        </div>
      </div>
    </header>

    <main class="guides-page" id="main">
      <nav class="page-breadcrumbs" aria-label="{b["breadcrumb_aria"]}">
        <a href="/{prefix.rstrip("/")}/">{b["bc_home"]}</a>
        <span aria-hidden="true">/</span>
        <span>{b["bc_guides"]}</span>
      </nav>
      <header class="guides-hero">
        <h1>{b["hero_h1"]}</h1>
        <p class="guides-lead">
{b["hero_lead"]}
        </p>
      </header>

      <article class="guides-master">
        <h2>
          {b["master_h2"]}
        </h2>
        <p>
{b["master_p"]}
        </p>

        <nav class="guides-toc" aria-label="{b["toc_nav_aria"]}">
          <strong>{b["toc_label"]}</strong>
          <ol>
{toc_ol}
          </ol>
        </nav>

{sections_joined}

        <p class="guides-footer-note">
{b["footer_note"]}
        </p>

        <div class="guides-cta">
          <a
            class="btn btn-primary"
            href="https://maisonlooks.com/?utm_source=sugargooospreadsheet"
            >{b["cta_hub"]}</a
          >
          <a class="btn btn-ghost" href="/{prefix.rstrip("/")}/">{b["cta_home"]}</a>
        </div>
        <section class="related-links-block" aria-labelledby="guides-related">
          <h2 id="guides-related">{b["related_h2"]}</h2>
          <div class="related-links-grid">
            <a class="related-link-card" href="news.html">
              <strong>{b["rel_news_t"]}</strong>
              <span>{b["rel_news_s"]}</span>
            </a>
            <a class="related-link-card" href="contact.html">
              <strong>{b["rel_contact_t"]}</strong>
              <span>{b["rel_contact_s"]}</span>
            </a>
            <a class="related-link-card" href="spreadsheet.html">
              <strong>{b["rel_hub_t"]}</strong>
              <span>{b["rel_hub_s"]}</span>
            </a>
          </div>
        </section>
      </article>
    </main>

    <footer class="site-footer">
      <div class="footer-inner">
        <p>
          © <span id="y"></span> sugargoo spreadsheet — {b["footer_line"]}.
        </p>
        <div class="footer-links">
          <a href="/{prefix.rstrip("/")}/">{b["home"]}</a>
          <a href="contact.html">{b["contact"]}</a>
        </div>
      </div>
    </footer>
    <script>
      document.getElementById("y").textContent = new Date().getFullYear();
    </script>
  </body>
</html>
"""


def _news_lang_menu(locale: str) -> str:
    links = []
    for href, label, lang_attr, cur in (
        ("/news.html", "EN", "en", False),
        ("/pl/news.html", "PL", "pl", locale == "pl"),
        ("/pt/news.html", "PT", "pt-PT", locale == "pt"),
        ("/es/news.html", "ES", "es", locale == "es"),
        ("/de/news.html", "DE", "de", locale == "de"),
    ):
        ac = ' aria-current="page"' if cur else ""
        links.append(f'            <a href="{href}"{ac} lang="{lang_attr}">{label}</a>')
    return "\n".join(links)


# fmt: off
NEWS_BLOCKS = {
    "pl": {
        "lang": "pl",
        "in_lang": "pl",
        "title": "Changelog Sugargoo Spreadsheet | Notatki | sugargoo spreadsheet",
        "desc": "Changelog dla sugargoo spreadsheet: zmiany w hubie, przypomnienia QC, czyszczenie martwych linków i workflow—oficjalne zasady pozostają na sugargoo.com/help.",
        "og_title": "Changelog Sugargoo Spreadsheet | Notatki",
        "og_desc": "Co zmieniło się w naszym ekosystemie sugargoo spreadsheet—to nadal nie zastępuje wsparcia Sugargoo.",
        "schema_name": "Sugargoo Spreadsheet — aktualności",
        "schema_desc": "Changelog dla czytelników sugargoo spreadsheet: hub, nawyki QC i przypomnienia workflow.",
        "bc_home": "Strona główna",
        "bc_news": "Aktualności",
        "skip": "Przejdź do treści",
        "brand_aria": "Strona główna sugargoo spreadsheet",
        "nav_aria": "Główne",
        "home": "Strona główna",
        "all_cat": "Wszystkie kategorie",
        "guides": "Poradniki",
        "spreadsheet": "Arkusz",
        "contact": "Kontakt",
        "news": "Aktualności",
        "lang_aria": "Wybierz język",
        "breadcrumb_aria": "Ścieżka nawigacji",
        "h1": "Changelog sugargoo spreadsheet",
        "intro": """        Notatki dla osób śledzących nasz <strong>sugargoo spreadsheet</strong>.
        Kwestie portfela, sporów i polityki nadal należą do
        <a href="https://sugargoo.com/help" target="_blank" rel="noopener noreferrer">Sugargoo Help</a>.""",
        "footer_discord": """        <a href="https://discord.gg/9hrqg53zgs" target="_blank" rel="noopener noreferrer"
          >Discord</a>
        ·
        <a href="guides.html">Workflow w poradnikach Sugargoo</a>""",
        "related_h2": "Dalej: sugargoo spreadsheet",
        "rel_home_t": "Strona główna",
        "rel_home_s": "Pozycjonowanie, FAQ i mapa kategorii dla sugargoo spreadsheet.",
        "rel_guides_t": "Playbook",
        "rel_guides_s": "Portfel, QC, forwarding, cło—po wklejeniu linków do Sugargoo.",
        "rel_hub_t": "Skrót do huba",
        "rel_hub_s": "Wejdź do żywej bazy powiązanej z tą stroną sugargoo spreadsheet.",
        "footer_line": "sprzedawcy platformy Sugargoo",
        "articles": [
            ("2026-04-08", "8 kwietnia 2026", "Przebudowa tekstów: unikalny messaging sugargoo spreadsheet", None, "Przepisaliśmy tę mikrostronę od zera, żeby brzmiała jak nasz własny playbook—a nie kopia innych arkuszy agenta. Słowa kluczowe wciąż celują w <strong>sugargoo spreadsheet</strong>, ale zdania, FAQ i poradniki są świeżo napisane dla kupujących przez Sugargoo.", None, None),
            ("2026-04-05", "5 kwietnia 2026", "Kurtki + sneakers: kolumny przesunięte", None, "Sezonowy popyt się zmienił, więc przełożyliśmy zakładki kurtek i trainerów w hubie MaisonLooks. Mniej zduplikowanych sylwetek, jaśniejsze notatki „batch vs batch” w każdej kolumnie sugargoo spreadsheet.", None, None),
            ("2026-04-02", "2 kwietnia 2026", "QC magazynowe wciąż ważniejsze niż screeny z wiersza", "sugargoo-spreadsheet-qc.html", "Świeży wyjaśniacz: dlaczego zdjęcia sprzedawcy w arkuszu to tylko podpowiedź, a zestaw magazynowy Sugargoo to brama akceptacji. Przeczytaj przed wiosennymi haulami.", "sugargoo-spreadsheet-qc.html", "Otwórz przewodnik QC →"),
            ("2026-03-29", "29 marca 2026", "Etykieta portfela i ticketów", None, "Szybkie przypomnienie: nieudane doładowania, timing zwrotów i blokady kont to wyłącznie tematy Sugargoo. Oznacz nas na Discordzie przy problemach z arkuszem; otwieraj tickety Sugargoo przy pieniądzach na platformie.", None, None),
            ("2026-03-26", "26 marca 2026", "Protokół martwych linków", "sugargoo-spreadsheet-dead-links.html", "Sprzedawcy podmieniają URL-e z dnia na dzień. Opisujemy, jak oznaczamy nieaktualne wiersze i jak kupujący mogą pomóc utrzymać wiarygodność sugargoo spreadsheet.", "sugargoo-spreadsheet-dead-links.html", "Artykuł o martwych linkach →"),
            ("2026-03-22", "22 marca 2026", "Kolumny planowania FX lekko popchnięte", None, "Planowane kwoty USD przesunęły się po zmianach kursów. To wciąż rzędu wielkości—kurs przy kasie Sugargoo zawsze wygrywa.", None, None),
            ("2026-03-18", "18 marca 2026", "Filtry runnerów dopracowane", None, "Retro runner vs tech runner filtrują się osobno, żeby hub sugargoo spreadsheet nie mieszał niepowiązanych podeszw.", None, None),
            ("2026-03-14", "14 marca 2026", "Cisza celna ≠ przechwycenie", None, "Międzynarodowe skany często stają. Jeśli przekraczasz SLA przewoźnika, eskaluj przez Sugargoo—nie przez ten changelog.", None, None),
            ("2026-03-09", "9 marca 2026", "Zrób rehearsal zanim obwinisz arkusz", "sugargoo-spreadsheet-shipping-weight.html", "Łączone haul'e potrzebują danych z rehearsal—niespodzianki objętościowe biją niespodzianki wagowe.", "sugargoo-spreadsheet-shipping-weight.html", "Waga wysyłki — pogłębienie →"),
            ("2026-03-04", "4 marca 2026", "Wątek Discord „QC receipts”", None, "Tygodniowy przypięty wątek porównuje foty kupujących ze zdjęciami magazynowymi—tylko edukacja, nie oficjalne QC.", None, None),
            ("2026-02-28", "28 lutego 2026", "Miniatury huba lazy-load v2", None, "Szybszy pierwszy render na mobilnych siatkach. Jeśli assety wiszą, to zwykle sieć—nie zepsuty wiersz sugargoo spreadsheet.", None, None),
        ],
    },
    "es": {
        "lang": "es",
        "in_lang": "es",
        "title": "Changelog Sugargoo Spreadsheet | Notas | sugargoo spreadsheet",
        "desc": "Changelog para sugargoo spreadsheet: ajustes del hub, recordatorios QC, barridos de enlaces muertos y notas de flujo—las políticas oficiales siguen en sugargoo.com/help.",
        "og_title": "Changelog Sugargoo Spreadsheet | Notas",
        "og_desc": "Qué cambió en nuestro ecosistema sugargoo spreadsheet—sigue sin sustituir al soporte Sugargoo.",
        "schema_name": "Sugargoo Spreadsheet — noticias",
        "schema_desc": "Changelog para lectores de sugargoo spreadsheet: hub, hábitos QC y recordatorios de flujo.",
        "bc_home": "Inicio",
        "bc_news": "Noticias",
        "skip": "Saltar al contenido",
        "brand_aria": "Inicio sugargoo spreadsheet",
        "nav_aria": "Principal",
        "home": "Inicio",
        "all_cat": "Todas las categorías",
        "guides": "Guías",
        "spreadsheet": "Hoja",
        "contact": "Contacto",
        "news": "Noticias",
        "lang_aria": "Seleccionar idioma",
        "breadcrumb_aria": "Migas de pan",
        "h1": "Changelog de sugargoo spreadsheet",
        "intro": """        Notas para quienes siguen nuestro <strong>sugargoo spreadsheet</strong>.
        Cartera, disputas y política siguen en
        <a href="https://sugargoo.com/help" target="_blank" rel="noopener noreferrer">Sugargoo Help</a>.""",
        "footer_discord": """        <a href="https://discord.gg/9hrqg53zgs" target="_blank" rel="noopener noreferrer"
          >Discord</a>
        ·
        <a href="guides.html">Guías de flujo Sugargoo</a>""",
        "related_h2": "Sigue explorando sugargoo spreadsheet",
        "rel_home_t": "Inicio",
        "rel_home_s": "Posicionamiento, FAQ y mapa de categorías para sugargoo spreadsheet.",
        "rel_guides_t": "Playbook",
        "rel_guides_s": "Cartera, QC, reenvío, aduanas—después de pegar enlaces en Sugargoo.",
        "rel_hub_t": "Atajo al hub",
        "rel_hub_s": "Entra a la base de datos viva enlazada desde este sitio sugargoo spreadsheet.",
        "footer_line": "comerciantes de la plataforma Sugargoo",
        "articles": [
            ("2026-04-08", "8 de abril de 2026", "Renovación de textos: mensajes únicos de sugargoo spreadsheet", None, "Reescribimos este micrositio de arriba abajo para que suene como nuestro playbook—no como un espejo de otras hojas de agente. Las keywords siguen apuntando a <strong>sugargoo spreadsheet</strong>, pero frases, FAQ y guías están redactadas de nuevo para compradores Sugargoo.", None, None),
            ("2026-04-05", "5 de abril de 2026", "Carril outerwear + zapatillas reordenado", None, "La demanda estacional cambió, así que reorganizamos pestañas de chaquetas y trainers en el hub MaisonLooks. Menos siluetas duplicadas y notas «batch vs batch» más claras en cada carril del sugargoo spreadsheet.", None, None),
            ("2026-04-02", "2 de abril de 2026", "El QC de almacén sigue ganando a capturas de fila", "sugargoo-spreadsheet-qc.html", "Nuevo artículo: por qué las fotos del vendedor en la hoja son pistas, mientras el set de almacén de Sugargoo es la puerta de aprobación. Léelo antes de tus hauls de primavera.", "sugargoo-spreadsheet-qc.html", "Abrir guía QC →"),
            ("2026-03-29", "29 de marzo de 2026", "Etiqueta de cartera y tickets", None, "Recordatorio: top-ups fallidos, tiempos de reembolso y bloqueos de cuenta son temas solo de Sugargoo. Menciónanos en Discord por la hoja; abre tickets Sugargoo por dinero en la plataforma.", None, None),
            ("2026-03-26", "26 de marzo de 2026", "Protocolo de enlaces muertos", "sugargoo-spreadsheet-dead-links.html", "Los vendedores rotan URLs de la noche a la mañana. Documentamos cómo marcamos filas obsoletas y cómo los compradores pueden ayudar a mantener confiable el sugargoo spreadsheet.", "sugargoo-spreadsheet-dead-links.html", "Leer artículo de enlaces muertos →"),
            ("2026-03-22", "22 de marzo de 2026", "Columnas de planificación FX ajustadas", None, "Las cifras de planificación USD se movieron ligeramente con el tipo de cambio. Siguen siendo orientativas—el tipo en checkout de Sugargoo manda.", None, None),
            ("2026-03-18", "18 de marzo de 2026", "Filtros de runners afinados", None, "Retro runner vs tech runner ahora filtran por separado para que el hub sugargoo spreadsheet no mezcle suelas no relacionadas.", None, None),
            ("2026-03-14", "14 de marzo de 2026", "Silencio aduanero ≠ decomiso", None, "Los escaneos internacionales a menudo se pausan. Si superas el SLA del transportista, escala vía Sugargoo—no vía este changelog.", None, None),
            ("2026-03-09", "9 de marzo de 2026", "Haz ensayo antes de culpar a la hoja", "sugargoo-spreadsheet-shipping-weight.html", "Los hauls combinados necesitan datos de ensayo—las sorpresas de volumen ganan a las de gramos.", "sugargoo-spreadsheet-shipping-weight.html", "Profundizar en peso de envío →"),
            ("2026-03-04", "4 de marzo de 2026", "Hilo Discord «QC receipts»", None, "Hilo fijado semanal que compara fotos de compradores vs almacén—solo educación, no QC oficial.", None, None),
            ("2026-02-28", "28 de febrero de 2026", "Miniaturas del hub lazy-load v2", None, "Primer pintado más rápido en grillas móviles. Si los assets tardan, suele ser red—no una fila rota del sugargoo spreadsheet.", None, None),
        ],
    },
    "de": {
        "lang": "de",
        "in_lang": "de",
        "title": "Sugargoo Spreadsheet Changelog | Feldnotizen | sugargoo spreadsheet",
        "desc": "Händler-Changelog für sugargoo spreadsheet: Hub-Anpassungen, QC-Hinweise, tote-Link-Sweeps und Workflow-Notizen—offizielle Policies bleiben auf sugargoo.com/help.",
        "og_title": "Sugargoo Spreadsheet Changelog | Feldnotizen",
        "og_desc": "Was sich in unserem sugargoo spreadsheet-Ökosystem geändert hat—kein Ersatz für Sugargoo-Support.",
        "schema_name": "Sugargoo Spreadsheet — Neuigkeiten",
        "schema_desc": "Changelog für sugargoo spreadsheet-Leser: Hub-Notizen, QC-Gewohnheiten und Workflow-Erinnerungen.",
        "bc_home": "Startseite",
        "bc_news": "Neuigkeiten",
        "skip": "Zum Inhalt springen",
        "brand_aria": "Startseite sugargoo spreadsheet",
        "nav_aria": "Hauptnavigation",
        "home": "Startseite",
        "all_cat": "Alle Kategorien",
        "guides": "Ratgeber",
        "spreadsheet": "Tabelle",
        "contact": "Kontakt",
        "news": "Neuigkeiten",
        "lang_aria": "Sprache wählen",
        "breadcrumb_aria": "Brotkrümel",
        "h1": "sugargoo spreadsheet Changelog",
        "intro": """        Händler-Notizen für alle, die unser <strong>sugargoo spreadsheet</strong> verfolgen.
        Wallet, Streitfälle und Policy gehören weiterhin in den
        <a href="https://sugargoo.com/help" target="_blank" rel="noopener noreferrer">Sugargoo Help</a>.""",
        "footer_discord": """        <a href="https://discord.gg/9hrqg53zgs" target="_blank" rel="noopener noreferrer"
          >Discord</a>
        ·
        <a href="guides.html">Sugargoo-Workflow-Ratgeber</a>""",
        "related_h2": "Mehr zum sugargoo spreadsheet",
        "rel_home_t": "Startseite",
        "rel_home_s": "Positionierung, FAQs und Kategoriemap für das sugargoo spreadsheet.",
        "rel_guides_t": "Playbook",
        "rel_guides_s": "Wallet, QC, Weiterleitung, Zoll—nach dem Einfügen von Links bei Sugargoo.",
        "rel_hub_t": "Hub-Shortcut",
        "rel_hub_s": "Springe in die Live-Datenbank, die von dieser sugargoo spreadsheet-Site verlinkt ist.",
        "footer_line": "Händler der Sugargoo-Plattform",
        "articles": [
            ("2026-04-08", "8. April 2026", "Text-Overhaul: eigenes sugargoo spreadsheet Messaging", None, "Wir haben diese Microsite komplett neu geschrieben, damit sie wie unser eigenes Playbook klingt—nicht wie andere Agent-Tabellen. Keywords zielen weiter auf <strong>sugargoo spreadsheet</strong>, aber Sätze, FAQs und Ratgeber sind frisch für Sugargoo-Käufer formuliert.", None, None),
            ("2026-04-05", "5. April 2026", "Outerwear- + Sneaker-Spuren neu gewichtet", None, "Saisonale Nachfrage verschob sich, daher haben wir Jacket- und Trainer-Tabs im MaisonLooks-Hub umgestellt. Weniger doppelte Silhouetten, klarere „Batch vs. Batch“-Notizen in jeder Spur des sugargoo spreadsheet.", None, None),
            ("2026-04-02", "2. April 2026", "Lager-QC schlägt weiterhin Zeilen-Screenshots", "sugargoo-spreadsheet-qc.html", "Neuer Erklärer: Warum Verkäuferfotos in der Tabelle nur Hinweise sind, während Sugargoos Lager-Set das Freigabe-Tor ist. Lesen vor Frühjahrs-Hauls.", "sugargoo-spreadsheet-qc.html", "QC-Leitfaden öffnen →"),
            ("2026-03-29", "29. März 2026", "Wallet- & Ticket-Etikette", None, "Kurz erinnert: fehlgeschlagene Top-ups, Erstattungs-Timing und Kontosperren sind nur Sugargoo-Themen. Markiere uns auf Discord bei Sheet-Problemen; öffne Sugargoo-Tickets für Geld auf der Plattform.", None, None),
            ("2026-03-26", "26. März 2026", "Protokoll für tote Links", "sugargoo-spreadsheet-dead-links.html", "Verkäufer rotieren URLs über Nacht. Wir dokumentieren, wie veraltete Zeilen markiert werden und wie Käufer dem sugargoo spreadsheet vertrauen helfen.", "sugargoo-spreadsheet-dead-links.html", "Artikel zu toten Links →"),
            ("2026-03-22", "22. März 2026", "FX-Planungsspalten leicht verschoben", None, "USD-Planungszahlen haben sich nach Währungsschwankungen leicht bewegt. Es bleiben Größenordnungen—der Sugargoo-Checkout-Kurs gewinnt immer.", None, None),
            ("2026-03-18", "18. März 2026", "Runner-Filter verschärft", None, "Retro- vs. Tech-Runner-Chips filtern jetzt getrennt, damit der sugargoo spreadsheet-Hub keine fremden Sohlen mischt.", None, None),
            ("2026-03-14", "14. März 2026", "Zoll-Stille ≠ Beschlagnahme", None, "Internationale Scans pausieren oft. Wenn du die Carrier-SLA sprengst, eskalieren über Sugargoo—nicht über dieses Changelog.", None, None),
            ("2026-03-09", "9. März 2026", "Rehearsal bevor du die Tabelle beschuldigst", "sugargoo-spreadsheet-shipping-weight.html", "Kombi-Hauls brauchen Rehearsal-Daten—Volumen-Überraschungen schlagen Gramm-Überraschungen.", "sugargoo-spreadsheet-shipping-weight.html", "Versandgewicht vertiefen →"),
            ("2026-03-04", "4. März 2026", "Discord-Thread „QC receipts“", None, "Wöchentlicher angehefteter Thread vergleicht Käuferfotos vs. Lager—nur Bildung, kein offizielles QC.", None, None),
            ("2026-02-28", "28. Februar 2026", "Hub-Thumbnails Lazy-Load v2", None, "Schnelleres erstes Rendering auf mobilen Grids. Wenn Assets hängen, meist Netzwerk—keine kaputte sugargoo spreadsheet-Zeile.", None, None),
        ],
    },
    "pt": {
        "lang": "pt-PT",
        "in_lang": "pt-PT",
        "title": "Changelog Sugargoo Spreadsheet | Notas | sugargoo spreadsheet",
        "desc": "Changelog do sugargoo spreadsheet: ajustes no hub, lembretes QC, limpezas de links mortos e notas de fluxo—as políticas oficiais ficam em sugargoo.com/help.",
        "og_title": "Changelog Sugargoo Spreadsheet | Notas",
        "og_desc": "O que mudou no nosso ecossistema sugargoo spreadsheet—continua a não substituir o suporte Sugargoo.",
        "schema_name": "Sugargoo Spreadsheet — notícias",
        "schema_desc": "Changelog para leitores do sugargoo spreadsheet: notas de hub, hábitos QC e lembretes de fluxo.",
        "bc_home": "Início",
        "bc_news": "Notícias",
        "skip": "Saltar para o conteúdo",
        "brand_aria": "Início sugargoo spreadsheet",
        "nav_aria": "Principal",
        "home": "Início",
        "all_cat": "Todas as categorias",
        "guides": "Guias",
        "spreadsheet": "Folha",
        "contact": "Contacto",
        "news": "Notícias",
        "lang_aria": "Selecionar idioma",
        "breadcrumb_aria": "Navegação estrutural",
        "h1": "Changelog do sugargoo spreadsheet",
        "intro": """        Notas para quem segue o nosso <strong>sugargoo spreadsheet</strong>.
        Carteira, disputas e política continuam no
        <a href="https://sugargoo.com/help" target="_blank" rel="noopener noreferrer">Sugargoo Help</a>.""",
        "footer_discord": """        <a href="https://discord.gg/9hrqg53zgs" target="_blank" rel="noopener noreferrer"
          >Discord</a>
        ·
        <a href="guides.html">Guias de fluxo Sugargoo</a>""",
        "related_h2": "Explora mais o sugargoo spreadsheet",
        "rel_home_t": "Início",
        "rel_home_s": "Posicionamento, FAQs e mapa de categorias para o sugargoo spreadsheet.",
        "rel_guides_t": "Playbook",
        "rel_guides_s": "Carteira, QC, reencaminhamento, alfândega—depois de colares links na Sugargoo.",
        "rel_hub_t": "Atalho ao hub",
        "rel_hub_s": "Entra na base de dados ao vivo ligada a este site sugargoo spreadsheet.",
        "footer_line": "comerciantes da plataforma Sugargoo",
        "articles": [
            ("2026-04-08", "8 de abril de 2026", "Renovação de texto: mensagens únicas sugargoo spreadsheet", None, "Reescrevemos este microsite de alto a baixo para soar como o nosso playbook—não um espelho de outras folhas de agente. As keywords continuam a visar <strong>sugargoo spreadsheet</strong>, mas frases, FAQs e guias foram redigidos de novo para compradores Sugargoo.", None, None),
            ("2026-04-05", "5 de abril de 2026", "Carris outerwear + sapatilhas repostos", None, "A procura sazonal mudou, por isso reorganizámos separadores de casacos e trainers no hub MaisonLooks. Menos silhuetas duplicadas e notas «batch vs batch» mais claras em cada carril do sugargoo spreadsheet.", None, None),
            ("2026-04-02", "2 de abril de 2026", "QC de armazém continua a bater capturas de linha", "sugargoo-spreadsheet-qc.html", "Novo artigo: porque as fotos do vendedor na folha são pistas, enquanto o conjunto de armazém Sugargoo é a porta de aprovação. Lê antes dos hauls de primavera.", "sugargoo-spreadsheet-qc.html", "Abrir guia QC →"),
            ("2026-03-29", "29 de março de 2026", "Etiqueta de carteira e tickets", None, "Lembrete: top-ups falhados, tempos de reembolso e bloqueios de conta são só tema Sugargoo. Menciona-nos no Discord para a folha; abre tickets Sugargoo para dinheiro na plataforma.", None, None),
            ("2026-03-26", "26 de março de 2026", "Protocolo de links mortos", "sugargoo-spreadsheet-dead-links.html", "Os vendedores rodam URLs de um dia para o outro. Documentamos como marcamos linhas obsoletas e como os compradores ajudam a manter o sugargoo spreadsheet fiável.", "sugargoo-spreadsheet-dead-links.html", "Ler artigo de links mortos →"),
            ("2026-03-22", "22 de março de 2026", "Colunas de planeamento FX ajustadas", None, "Os valores USD de planeamento moveram-se ligeiramente com o câmbio. Continuam ordens de grandeza—a taxa no checkout Sugargoo manda.", None, None),
            ("2026-03-18", "18 de março de 2026", "Filtros de runners apertados", None, "Retro runner vs tech runner filtram separadamente para o hub sugargoo spreadsheet não misturar solas não relacionadas.", None, None),
            ("2026-03-14", "14 de março de 2026", "Silêncio alfandegário ≠ apreensão", None, "Os rastreios internacionais pausam muitas vezes. Se ultrapassares o SLA da transportadora, escala via Sugargoo—não via este changelog.", None, None),
            ("2026-03-09", "9 de março de 2026", "Faz ensaio antes de culpar a folha", "sugargoo-spreadsheet-shipping-weight.html", "Hauls combinados precisam de dados de ensaio—surpresas de volume ganham a surpresas de gramas.", "sugargoo-spreadsheet-shipping-weight.html", "Aprofundar peso de envio →"),
            ("2026-03-04", "4 de março de 2026", "Tópico Discord «QC receipts»", None, "Tópico semanal fixo compara fotos de compradores vs armazém—só educação, não QC oficial.", None, None),
            ("2026-02-28", "28 de fevereiro de 2026", "Miniaturas do hub lazy-load v2", None, "Primeira pintura mais rápida em grelhas móveis. Se os assets atrasam, costuma ser rede—não uma linha partida do sugargoo spreadsheet.", None, None),
        ],
    },
}
# fmt: on


def _news_article_html(a: tuple) -> str:
    iso, label, title, title_href, body, cta_href, cta_text = a
    if title_href:
        h2 = f"""          <h2>
            <a href="{title_href}">{title}</a>
          </h2>"""
    else:
        h2 = f"          <h2>{title}</h2>"
    cta = ""
    if cta_href and cta_text:
        cta = f"""          <p class="news-item-link">
            <a href="{cta_href}">{cta_text}</a>
          </p>"""
    return f"""        <article class="news-item">
          <time datetime="{iso}">{label}</time>
{h2}
          <p>
            {body}
          </p>
{cta}
        </article>"""


def build_news_html(locale: str, prefix: str) -> str:
    b = NEWS_BLOCKS[locale]
    articles_html = "\n\n".join(_news_article_html(a) for a in b["articles"])
    parts = [p.strip() for p in b["title"].split("|")]
    og_title = " | ".join(parts[:2]) if len(parts) >= 2 else b["title"]
    return f"""<!DOCTYPE html>
<html lang="{b["lang"]}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" type="image/png" href="../images/flame-icon.png" sizes="225x225" />
    <link rel="icon" type="image/png" href="../images/favicon-32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="../images/favicon-16.png" sizes="16x16" />
    <link rel="apple-touch-icon" href="../images/apple-touch-icon.png" />
    <title>{b["title"]}</title>
    <meta
      name="description"
      content="{b["desc"]}"
    />
    <link rel="canonical" href="https://sugargooospreadsheet.com/{prefix}news.html" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://sugargooospreadsheet.com/{prefix}news.html" />
    <meta property="og:title" content="{og_title}" />
    <meta
      property="og:description"
      content="{b["og_desc"]}"
    />
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "{b["schema_name"]}",
        "url": "https://sugargooospreadsheet.com/{prefix}news.html",
        "inLanguage": "{b["in_lang"]}",
        "dateModified": "2026-04-08",
        "description": "{b["schema_desc"]}"
      }}
    </script>
    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "{b["bc_home"]}",
            "item": "https://sugargooospreadsheet.com/{prefix.rstrip("/")}/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{b["bc_news"]}",
            "item": "https://sugargooospreadsheet.com/{prefix}news.html"
          }}
        ]
      }}
    </script>
    <link rel="alternate" hreflang="en" href="https://sugargooospreadsheet.com/news.html" />
    <link rel="alternate" hreflang="pl" href="https://sugargooospreadsheet.com/pl/news.html" />
    <link rel="alternate" hreflang="pt-PT" href="https://sugargooospreadsheet.com/pt/news.html" />
    <link rel="alternate" hreflang="es" href="https://sugargooospreadsheet.com/es/news.html" />
    <link rel="alternate" hreflang="de" href="https://sugargooospreadsheet.com/de/news.html" />
    <link rel="alternate" hreflang="x-default" href="https://sugargooospreadsheet.com/news.html" />
    <link rel="stylesheet" href="../styles.css" />
  </head>
  <body>
    <a class="skip-link" href="#main">{b["skip"]}</a>
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="/{prefix.rstrip("/")}/" aria-label="{b["brand_aria"]}">
          <img
            class="brand-logo"
            src="../images/logo.png"
            width="200"
            height="40"
            alt="Sugargoo"
            decoding="async"
          />
          <span class="brand-text">sugargoo spreadsheet</span>
        </a>
        <nav aria-label="{b["nav_aria"]}">
          <ul>
            <li><a href="/{prefix.rstrip("/")}/">{b["home"]}</a></li>
            <li class="has-sub">
              <button type="button" aria-expanded="false" aria-haspopup="true">
                {b["all_cat"]}
              </button>
              <div class="submenu" role="menu">
                <a href="https://maisonlooks.com/en/c/shoes" role="menuitem">Shoes</a>
                <a href="https://maisonlooks.com/en/c/jackets" role="menuitem">Jackets</a>
                <a href="https://maisonlooks.com/en/c/clothing" role="menuitem">Hoodies / Sweaters</a>
                <a href="https://maisonlooks.com/en/c/t-shirts" role="menuitem">T-Shirts</a>
                <a href="https://maisonlooks.com/en/c/clothing" role="menuitem">Pants / Shorts</a>
                <a href="https://maisonlooks.com/en/products" role="menuitem">Bags</a>
                <a href="https://maisonlooks.com/en/c/headwear" role="menuitem">Headwear</a>
                <a href="https://maisonlooks.com/en/c/accessories" role="menuitem">Accessories</a>
                <a href="https://maisonlooks.com/en/c/electronics" role="menuitem">Electronics</a>
                <a href="https://maisonlooks.com/en/c/perfume" role="menuitem">Perfume</a>
                <a href="https://maisonlooks.com/en/products" role="menuitem">Jersey</a>
                <a href="https://maisonlooks.com/en/products" role="menuitem">Other</a>
              </div>
            </li>
            <li><a href="guides.html">{b["guides"]}</a></li>
            <li><a href="spreadsheet.html">{b["spreadsheet"]}</a></li>
            <li><a href="contact.html">{b["contact"]}</a></li>
            <li><a href="news.html" aria-current="page">{b["news"]}</a></li>
          </ul>
        </nav>
        <div class="header-end">
        <div class="header-cta">
          <a
            class="btn btn-primary"
            href="https://maisonlooks.com/?utm_source=sugargooospreadsheet"
            >sugargoo spreadsheet</a
          >
        </div>
        <nav class="language-switcher has-lang" aria-label="{b["lang_aria"]}">
          <button type="button" class="lang-globe-btn" aria-haspopup="true" aria-expanded="false" aria-label="{b["lang_aria"]}">
            <svg class="lang-globe-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <circle cx="12" cy="12" r="10" />
              <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
            </svg>
          </button>
          <div class="lang-menu" role="menu">
{_news_lang_menu(locale)}
          </div>
        </nav>
        </div>
      </div>
    </header>

    <main class="news-page" id="main">
      <nav class="page-breadcrumbs" aria-label="{b["breadcrumb_aria"]}">
        <a href="/{prefix.rstrip("/")}/">{b["bc_home"]}</a>
        <span aria-hidden="true">/</span>
        <span>{b["bc_news"]}</span>
      </nav>
      <h1>{b["h1"]}</h1>
      <p class="news-intro">
{b["intro"]}
      </p>

      <div class="news-list">
{articles_html}
      </div>

      <p class="news-intro" style="margin-top: 2rem; margin-bottom: 0; border: none; padding: 0">
{b["footer_discord"]}
      </p>
      <section class="related-links-block" aria-labelledby="news-related">
        <h2 id="news-related">{b["related_h2"]}</h2>
        <div class="related-links-grid">
          <a class="related-link-card" href="/{prefix.rstrip("/")}/">
            <strong>{b["rel_home_t"]}</strong>
            <span>{b["rel_home_s"]}</span>
          </a>
          <a class="related-link-card" href="guides.html">
            <strong>{b["rel_guides_t"]}</strong>
            <span>{b["rel_guides_s"]}</span>
          </a>
          <a class="related-link-card" href="spreadsheet.html">
            <strong>{b["rel_hub_t"]}</strong>
            <span>{b["rel_hub_s"]}</span>
          </a>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="footer-inner">
        <p>
          © <span id="y"></span> sugargoo spreadsheet — {b["footer_line"]}.
        </p>
        <div class="footer-links">
          <a href="/{prefix.rstrip("/")}/">{b["home"]}</a>
          <a href="contact.html">{b["contact"]}</a>
        </div>
      </div>
    </footer>
    <script>
      document.getElementById("y").textContent = new Date().getFullYear();
    </script>
  </body>
</html>
"""


def main() -> None:
    for loc, pref in [("pl", "pl/"), ("es", "es/"), ("de", "de/"), ("pt", "pt/")]:
        (ROOT / pref / "guides.html").write_text(build_guides_html(loc, pref), encoding="utf-8")
        print("wrote", ROOT / pref / "guides.html")
        (ROOT / pref / "news.html").write_text(build_news_html(loc, pref), encoding="utf-8")
        print("wrote", ROOT / pref / "news.html")


if __name__ == "__main__":
    main()