#!/usr/bin/env python3
"""
One-time backfill of data/nt_ot_citations.json for Mark 11, 13, 14, 15.

Why this exists:
  Mark 1-10 and 12 got OT citations hand-curated into nt_ot_citations.json
  as part of their translation commits. When the ship pipeline matured, that
  manual step silently fell out of the workflow — chapters 11, 13, 14, 15
  shipped with ZERO OT citations recorded in the DB, even though the
  translation notes identified them correctly.

  This script reads the (already-written) translation notes verse-by-verse
  and reproduces them in the structured DB schema used for chapters 1-12.
  Each entry mirrors what the notes already say — no new scholarly claims
  are introduced.

Sources grounding each entry:
  - NA28 marginal references
  - UBS GNT apparatus
  - Beale & Carson, "Commentary on the New Testament Use of the Old Testament"
  - LXX text-form identification in the existing translation notes

Run once:
  python3 scripts/backfill_ot_citations_11_13_14_15.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "nt_ot_citations.json"

# Each entry keyed by "BOOK C:V" matches the existing MRK 1:2 / 1:3 / ... format.
# Type values: 'citation' | 'citation-paraphrase' | 'citation-expanded' |
#              'composite_citation' | 'allusion' | 'composite_allusion'
# greek_matches values: 'LXX' | 'LXX-close' | 'LXX-near-verbatim' | 'LXX-expanded'
#              | 'paraphrase' | 'composite' | 'Aramaic-Targum' | 'MT' | etc.
NEW_ENTRIES = {
    # ══ MARK 11 ══
    "MRK 11:9": {
        "type": "citation",
        "source": "PSA 118:26",
        "greek_matches": "LXX",
        "notes": "Ps 118:26 LXX (Ps 117:26 LXX numbering), verbatim. LXX matches MT (Heb. בָּרוּךְ הַבָּא בְּשֵׁם יְהוָה). Ps 118 is the climax of the Hallel (Pss 113-118) sung at Passover, giving the Triumphal-Entry acclamation its festival-liturgical context. The crowd applies a psalm originally addressed to any pilgrim arriving in the name of YHWH to Jesus specifically — Markan narrative irony. 'The one coming' (ὁ ἐρχόμενος) had become a Second-Temple messianic designation (cf. Matt 11:3, Heb 10:37). Cross-refs: Ps 118:22-23 cited at Mark 12:10-11; Ps 118:26 reprised implicitly at 14:26 (Hallel-singing after the Last Supper).",
    },
    "MRK 11:11": {
        "type": "allusion",
        "source": "MAL 3:1",
        "greek_matches": "thematic",
        "notes": "Jesus's entry-survey-departure pattern (περιβλεψάμενος then return the next day for cleansing) echoes Mal 3:1's judicial-inspection motif: 'the Lord whom you seek will suddenly come to his temple.' Mark frames the temple-cleansing as a considered prophetic-inspection, not impulsive protest. Thematic, not verbal.",
    },
    "MRK 11:17": {
        "type": "composite_citation",
        "sources": ["ISA 56:7", "JER 7:11"],
        "greek_matches": "LXX",
        "notes": "Two OT citations woven via catchword-association (classic gezerah-shavah) on 'house': Isa 56:7 LXX (temple as universal 'house of prayer') + Jer 7:11 LXX (temple as 'den of robbers'). Both in LXX form. Mark UNIQUELY preserves πᾶσιν τοῖς ἔθνεσιν ('for all the nations') — Matt 21:13 and Luke 19:46 omit. This Markan detail grounds the cleansing in Gentile-inclusion concerns (the court-of-the-Gentiles being the space that had been desecrated by commerce), making Mark the most universalist synoptic on this point. Jer 7's 'den of robbers' connotes a safe-haven mentality where religious-performance coexists with injustice, not merely commercial fraud.",
    },

    # ══ MARK 13 ══
    "MRK 13:8": {
        "type": "allusion",
        "source": "ISA 19:2",
        "greek_matches": "LXX-close",
        "notes": "ἔθνος ἐπ' ἔθνος + βασιλεία ἐπὶ βασιλείαν echoes Isa 19:2 LXX and 2 Chr 15:6 LXX (Hanani's oracle on inter-nation conflict as divine judgment). ὠδίν ('birth-pang') is the standard OT-prophetic image for eschatological travail (Isa 13:8, 26:17, 66:7-9; Jer 4:31, 6:24; Mic 4:9-10; Hos 13:13). In Second-Temple Judaism this becomes the technical phrase 'chevlei mashiach' (1 Enoch 62:4; 4 Ezra 4:42; 2 Baruch 29:3ff; 1QH 3:7-12) — a fixed tribulation preceding the Messiah's advent. Mark's Jesus uses this exact register, locating the present crisis as ἀρχή (beginning) of that birth-process.",
    },
    "MRK 13:12": {
        "type": "allusion",
        "source": "MIC 7:6",
        "greek_matches": "LXX-close",
        "notes": "Direct verbal echo of Mic 7:6 LXX ('υἱὸς ἀτιμάζει πατέρα, θυγάτηρ ἐπαναστήσεται ἐπὶ τὴν μητέρα... ἐχθροὶ ἀνδρὸς οἱ ἐν τῷ οἴκῳ αὐτοῦ'). Mark's ἐπαναστήσονται τέκνα ἐπὶ γονεῖς is lexically close. Second-Temple apocalyptic tradition already read Mic 7:6 eschatologically (m. Soṭah 9:15; 1QH; 4 Ezra 6:24). Markan theme: following Jesus divides families (3:31-35, 10:29-30); here the division darkens to family-betrayal-to-death.",
    },
    "MRK 13:14": {
        "type": "composite_citation",
        "sources": ["DAN 9:27", "DAN 11:31", "DAN 12:11"],
        "greek_matches": "LXX",
        "notes": "βδέλυγμα τῆς ἐρημώσεως is drawn from the Daniel triad: Dan 9:27 LXX ('βδέλυγμα τῶν ἐρημώσεων'), Dan 11:31 LXX ('βδέλυγμα ἠφανισμένων'), Dan 12:11 LXX ('βδέλυγμα ἐρημώσεως' — exact match). Original referent: Antiochus IV Epiphanes's 167 BCE temple desecration (altar to Zeus Olympios, swine sacrifices — 1 Macc 1:54-59; 2 Macc 6:2; Josephus Ant. 12.5.4). Mark's Jesus re-applies the Danielic pattern to a future desecration. Candidates: (a) Caligula's 40 CE statue attempt (stopped by assassination); (b) Zealot temple takeover 67 CE; (c) Titus's standards in the temple court 70 CE. The masculine participle ἑστηκότα favors a personal referent, consistent with (a) or (c). The parenthetical 'let the reader understand' is Mark's direct audience signal.",
    },
    "MRK 13:19": {
        "type": "citation",
        "source": "DAN 12:1",
        "greek_matches": "LXX-quasi-verbatim",
        "notes": "Lexically tracks Dan 12:1 LXX ('καὶ ἔσται καιρὸς θλίψεως, θλῖψις οἵα οὐ γέγονεν ἀφ' οὗ γεγένηται ἔθνος ἐπὶ τῆς γῆς ἕως τοῦ καιροῦ ἐκείνου'). Mark substitutes ἀπ' ἀρχῆς κτίσεως ('from the beginning of creation') for Daniel's 'since a nation has existed,' cosmologically broadening. Daniel 12:1 context is the resurrection-announcement, so Mark's borrowing implicitly links the tribulation to eschatological deliverance. θλῖψις is the standard LXX apocalyptic term (Dan 12:1; Zeph 1:15 'ἡμέρα θλίψεως').",
    },
    "MRK 13:22": {
        "type": "allusion",
        "source": "DEU 13:2",
        "greek_matches": "thematic",
        "notes": "Direct thematic echo of Deut 13:2-6 LXX on false prophets with σημεῖα καὶ τέρατα. The Torah principle — that miraculous capacity is NOT a sufficient criterion for prophetic authenticity — grounds Jesus's warning that the elect must test by doctrinal fidelity to the revealed Christ, not by sign-production.",
    },
    "MRK 13:24": {
        "type": "composite_citation",
        "sources": ["ISA 13:10", "JOL 2:10"],
        "greek_matches": "LXX",
        "notes": "Composite pastiche of Day-of-YHWH imagery. Isa 13:10 LXX ('οἱ γὰρ ἀστέρες τοῦ οὐρανοῦ... τὸ φῶς οὐ δώσουσιν, καὶ σκοτισθήσεται τοῦ ἡλίου ἀνατέλλοντος, καὶ ἡ σελήνη οὐ δώσει τὸ φῶς αὐτῆς') — Mark's ἥλιος σκοτισθήσεται + σελήνη οὐ δώσει τὸ φέγγος αὐτῆς tracks this closely. Joel 2:10 LXX ('ὁ ἥλιος καὶ ἡ σελήνη συσκοτάσουσιν') confirms the stock apocalyptic vocabulary. Sun/moon/stars darkening is recurring OT cosmic imagery for YHWH's decisive intervention (not necessarily literal astrophysics); Jesus's audience hears 'the Day of the LORD has arrived.' Ezek 32:7 adds the Egypt-judgment parallel.",
    },
    "MRK 13:25": {
        "type": "composite_citation",
        "sources": ["ISA 34:4", "HAG 2:6"],
        "greek_matches": "LXX",
        "notes": "Isa 34:4 LXX ('πάντες οἱ ἀστέρες πεσοῦνται... καὶ τακήσονται πᾶσαι αἱ δυνάμεις τῶν οὐρανῶν') closely matches Mark's falling-stars + shaken-powers language. Hag 2:6 LXX ('σείσω τὸν οὐρανὸν καὶ τὴν γῆν') supplies the heaven-and-earth-shaken theme (also cited in Heb 12:26). Cosmic upheaval as theophanic signage.",
    },
    "MRK 13:26": {
        "type": "citation",
        "source": "DAN 7:13",
        "greek_matches": "LXX-near-verbatim",
        "notes": "Near-citation of Dan 7:13-14 LXX ('ὡς υἱὸς ἀνθρώπου ἐρχόμενος ἦν καὶ... ἐδόθη αὐτῷ ἐξουσία καὶ τιμὴ βασιλική'). Mark substitutes μετὰ δυνάμεως καὶ δόξης for Daniel's ἐξουσία καὶ τιμή — thematically-identical coronation vocabulary. Mark's most explicit self-identification with Daniel-7's Son of Man up to this point (repeated at 14:62). Directionality is deliberately ambiguous — parousia-to-earth OR ascension-to-throne (Dan 7 originally reads the latter, Acts 1's ascension fits the pattern). ἐν νεφέλαις recurs Markanly (9:7 transfiguration-cloud; here parousia-cloud) — the theophanic medium of YHWH (Exod 13:21, 19:9, 33:9; Num 11:25).",
    },
    "MRK 13:27": {
        "type": "composite_allusion",
        "sources": ["DEU 30:4", "ZEC 2:6", "ISA 11:12", "ISA 27:13"],
        "greek_matches": "LXX",
        "notes": "Composite gathering-of-elect imagery. Zech 2:6 LXX (ἐκ τῶν τεσσάρων ἀνέμων τοῦ οὐρανοῦ συνάξω ὑμᾶς — post-exilic gathering); Deut 30:4 LXX (ἀπ' ἄκρου τοῦ οὐρανοῦ — covenant restoration); Isa 11:12 LXX (συνάξει τοὺς διασπαρέντας — eschatological gathering); Isa 27:13 (trumpet-gathering). Jesus applies the OT exile-gathering pattern to the Son of Man's parousia-gathering of the worldwide church. Elect are no longer just Jewish exiles but globally chosen (cf. v.10). Matt 24:31 reproduces almost verbatim; Luke 21:28 departs.",
    },
    "MRK 13:31": {
        "type": "allusion",
        "source": "ISA 40:8",
        "greek_matches": "thematic",
        "notes": "Jesus claims-for-his-own-words the permanence Isa 40:8 attributes to the word of YHWH ('τὸ δὲ ῥῆμα τοῦ θεοῦ ἡμῶν μένει εἰς τὸν αἰῶνα'). Cf. also Isa 51:6 ('heaven and earth shall pass away, but my salvation shall be forever'). A high-Christology claim preserved by Mark: Jesus's spoken words on par with YHWH's eternal word. Wordplay: γενεὰ αὕτη will not παρέλθῃ (v.30) balanced by οἱ λόγοι μου οὐ μὴ παρελεύσονται (v.31).",
    },

    # ══ MARK 14 ══
    "MRK 14:7": {
        "type": "allusion",
        "source": "DEU 15:11",
        "greek_matches": "thematic",
        "notes": "Jesus does not DISMISS poor-care but INVOKES the verse that establishes Israel's ongoing poor-care obligation. Deut 15:11's full context: 'because there will never cease to be poor in the land, THEREFORE open your hand wide to your brother.' Jesus cites the premise of unending poor-care to justify the UNIQUE moment of this anointing. This saying becomes the scriptural warrant for Christian poor-care-as-continuing-discipline (Acts 4:32-35; 2 Cor 8-9) — precisely because poor-care is NORMAL, extraordinary worship-acts are not in competition with it.",
    },
    "MRK 14:18": {
        "type": "allusion",
        "source": "PSA 41:9",
        "greek_matches": "LXX-echo",
        "notes": "Jesus's 'the one eating with me' directly echoes Ps 41:10 MT / 40:10 LXX — the psalm of the righteous sufferer betrayed by a close friend. Early Christianity read Ps 41 Messianically (John 13:18 cites Ps 41:9/10 explicitly for Judas). Mark's Jesus ALLUDES rather than CITES, letting the echo do the interpretive work. Also foreshadows Ps 22 (cited at 15:24, 15:34) — Mark's Passion is saturated with the Lament Psalms' vocabulary. Meal-betrayal horror: Near-Eastern covenant-of-salt (Num 18:19) and common-table fellowship created a near-inviolable bond; betrayal at the table magnified the moral weight (Qumran 1QS 6.1-5 on table-fellowship discipline).",
    },
    "MRK 14:24": {
        "type": "composite_citation",
        "sources": ["EXO 24:8", "JER 31:31", "ISA 53:12"],
        "greek_matches": "LXX",
        "notes": "Densest single-sentence OT-theological compression in Mark. (1) τὸ αἷμα τῆς διαθήκης = verbatim echo of Exod 24:8 LXX (Moses's Sinai covenant-ratification with sacrificial blood). (2) Jer 31:31's promised 'new covenant' stands behind the claim — 'new' implicit (vs. Luke/1 Cor which make it explicit). (3) ὑπὲρ πολλῶν echoes Isa 53:12 'for the sins of the many' — Jesus the Suffering Servant. Textual decision: SBLGNT's shorter τῆς διαθήκης (without καινῆς) is retained as the harder reading with stronger manuscript support and arguably richer theology (forcing Exod 24 allusion to primary status).",
    },
    "MRK 14:27": {
        "type": "citation",
        "source": "ZEC 13:7",
        "greek_matches": "LXX",
        "notes": "Zech 13:7 LXX form (πατάξω 1sg future) where MT has imperative 2ms. The LXX reading makes God the direct-striker — sharpening the divine-agency of the crucifixion (cf. Isa 53:10 'it pleased the LORD to crush him'). Original Zechariah context: God strikes the shepherd, sheep scatter, but scattering leads to remnant-purification (Zech 13:8-9). Mark applies: Jesus = smitten shepherd; disciples = scattered sheep; implicit Galilean remnant-regathering (v.28). Formally introduced with γέγραπται.",
    },
    "MRK 14:34": {
        "type": "allusion",
        "source": "PSA 42:5",
        "greek_matches": "LXX",
        "notes": "Jesus's complaint-of-soul uses Ps 42:5/11 LXX (41:6/12 LXX numbering) language verbatim: περίλυπος... ψυχή μου. The Psalmist's 'why are you cast down, O my soul?' becomes Jesus's own lament — the Son enters Israel's lament-piety completely. Mark's Passion is saturated with Lament Psalms (Ps 22 at 15:34; Ps 41:10 at 14:18; Ps 42 here; Ps 69 at 15:23, 36). Early church read this as the foundation of Christological-Psalter reading. γρηγορεῖτε command here structurally connects to the closing word of the Olivet Discourse (13:37).",
    },
    "MRK 14:41": {
        "type": "allusion",
        "source": "DAN 7:25",
        "greek_matches": "thematic",
        "notes": "'Son of Man handed over into the hands of...' matches Dan 7:25 LXX 'the saints of the Most High will be given into his hand' (the persecuting beast). Mark inverts apocalyptic-typology: the Son of Man suffers what Daniel's saints suffer — bearing their destiny in himself. Also echoes Mark's own 9:31 second passion-prediction; the prediction now actualizes.",
    },
    "MRK 14:52": {
        "type": "allusion",
        "source": "AMO 2:16",
        "greek_matches": "thematic",
        "notes": "Amos 2:16 MT/LXX: 'even the bravest warrior will flee away naked in that day.' The young-man's naked-flight may enact Amos's judgment-oracle as fulfilled in the disciples' collapse. Literary irony: the same or similar young-man figure reappears at the resurrection (16:5) in a white garment (στολὴ λευκή) — potential Markan reversal pattern (naked-flight at Passion → clothed-glory at Resurrection).",
    },
    "MRK 14:61": {
        "type": "allusion",
        "source": "ISA 53:7",
        "greek_matches": "performative",
        "notes": "Jesus's silence before accusers performatively enacts Isa 53:7 (the Suffering Servant 'like a lamb... silent before her shearers'). Mark presents the Servant via narrative-silence rather than verbal citation. Along with Isa 52:13-53:12, Isa 50 is Mark's silent-servant soundtrack. The high priest's question fuses two Messianic titles — ὁ χριστός (political-messianic) + ὁ υἱὸς τοῦ εὐλογητοῦ (divine-sonship echoing Ps 2:7, 2 Sam 7) — which in first-century Judaism could be separate concepts; Caiaphas bundles them.",
    },
    "MRK 14:62": {
        "type": "composite_citation",
        "sources": ["PSA 110:1", "DAN 7:13"],
        "greek_matches": "LXX-composite",
        "notes": "Mark's Christological climax. Jesus affirms full-title Messianic + Davidic + divine-sonship + Danielic-Son-of-Man + Ps-110-enthroned-Lord in two sentences. Composite citation: Ps 110:1 (ἐκ δεξιῶν... τῆς δυνάμεως, LXX 109:1) + Dan 7:13 (ἐρχόμενον μετὰ τῶν νεφελῶν τοῦ οὐρανοῦ). Same dual-citation appears at 12:36 (Ps 110:1) + 13:26 (Dan 7:13 alluded) + 14:62 (both fused). Three passages form a Markan Christological triad. Directional ambiguity preserved: (a) Second Coming to earth (traditional); (b) Son of Man's ascension to the Ancient of Days (Dan 7 original direction, matching Acts 1 ascension-cloud). Caiaphas reads it as blasphemy (14:63-64) — claim to share God's throne.",
    },
    "MRK 14:65": {
        "type": "allusion",
        "source": "ISA 50:6",
        "greek_matches": "enactment",
        "notes": "Isa 50:6: 'I gave my back to those who strike, and my cheeks to those who pull out the beard; I hid not my face from disgrace and spitting.' Mark's scene is the Servant Song enacted. Prophetic irony: they mock Jesus for not-prophesying, while he has just prophesied (v.62) his coming-in-power — and the prophecy they demand he could fulfill but chooses not to.",
    },

    # ══ MARK 15 ══
    "MRK 15:19": {
        "type": "allusion",
        "source": "ISA 50:6",
        "greek_matches": "thematic",
        "notes": "Roman mock-adoration reprises Isa 50:6 spitting-and-blows on the Servant; also Isa 53:3 (despised and rejected). Three parody-gestures: (1) strike head with reed-scepter (turning scepter into weapon), (2) spit (replacing anointing), (3) kneel (mock-adoration). Each is an antonym of the real royal-ceremony it parodies.",
    },
    "MRK 15:24": {
        "type": "citation",
        "source": "PSA 22:18",
        "greek_matches": "LXX-near-verbatim",
        "notes": "Near-verbatim quote of Ps 22:19 LXX (Ps 21:19 LXX numbering): διαμερίζονται τὰ ἱμάτια ≈ διεμερίσαντο τὰ ἱμάτιά μου; βάλλοντες κλῆρον ≈ ἔβαλον κλῆρον. Mark doesn't tag it with 'it was written,' following his MARKAN CITATION-STRATEGY of echo rather than formal-citation (unlike Matthew's frequent 'in order to fulfill'). Ps 22 is the crucifixion-psalm — its first line is Jesus's cry at v.34 and its motifs permeate Mark 15: mockery by passers-by (v.29 ↔ Ps 22:7), 'save yourself' taunt (v.30 ↔ Ps 22:8), garments divided (v.24 ↔ Ps 22:18), abandonment cry (v.34 ↔ Ps 22:1). The whole psalm is the hermeneutical key.",
    },
    "MRK 15:29": {
        "type": "composite_allusion",
        "sources": ["PSA 22:7", "LAM 2:15"],
        "greek_matches": "verbal-parallel",
        "notes": "Head-wagging mockery verbatim-verbal parallel to Ps 22:7/22:8 LXX (κινοῦντες κεφαλὴν). Lam 2:15 adds head-wagging over Zion imagery. Mark's readers hear the Psalm-of-the-Righteous-Sufferer being enacted by the mockers themselves. The mocking allusion to Jesus's alleged temple-saying (14:58) brings the formal charge into the crucifixion scene. HAPAX: οὐά.",
    },
    "MRK 15:30": {
        "type": "allusion",
        "source": "PSA 22:8",
        "greek_matches": "structural",
        "notes": "Ps 22:8 'he trusts in YHWH, let him deliver him, let him rescue him.' Mark's verbal echo is less direct than Matt 27:43 (which quotes verbatim) but the mockery-structure is identical. Recapitulates the wilderness-temptation pattern ('if you are the Son of God, prove it') in human mouths — Mark's lack of a wilderness-temptation-dialogue scene is supplied by this crucifixion-mockery as climactic temptation.",
    },
    "MRK 15:33": {
        "type": "composite_allusion",
        "sources": ["AMO 8:9", "EXO 10:21"],
        "greek_matches": "thematic",
        "notes": "The 3-hour supernatural midday darkness fulfils OT judgment-theophany motifs: Amos 8:9 ('I will make the sun go down at noon, and darken the earth in broad daylight' — Day-of-YHWH imagery); Exod 10:21-23 (ninth plague — 3 days of darkness before firstborn-death); Deut 28:29 (curse on disobedience). Natural-phenomenon explanations (eclipse, storm) are impossible at Passover (full moon; 3-hour duration). Mark presents it as supernatural.",
    },
    "MRK 15:34": {
        "type": "citation",
        "source": "PSA 22:1",
        "greek_matches": "Aramaic-Targum",
        "notes": "Most-quoted OT verse in the Gospels. Hebrew אֵלִי אֵלִי לָמָה עֲזַבְתָּנִי; Aramaic Targum equivalent approximates Mark's Greek transliteration Ἐλωΐ ἐλωΐ λεμὰ σαβαχθάνι. Mark's ἐγκατέλιπές aligns with the LXX verb elsewhere (direct LXX Ps 21:1 has προσέσχες μοι in the question form — textual complexity noted by scholars). THE CRUX: Is Jesus expressing genuine divine-abandonment or praying Ps 22 as confidence-expression? Both-and: the first line of Ps 22 is a real cry of desolation AND Jewish first-century hermeneutic identifies a psalm by its first line (quoting v.1 evokes the whole Psalm, which ends in vindication and universal worship — Ps 22:27-31). Genuine forsaken-ness + confident trust in the full arc held together.",
    },
    "MRK 15:35": {
        "type": "allusion",
        "source": "MAL 4:5",
        "greek_matches": "thematic",
        "notes": "Phonetic near-miss: Ἐλωΐ (Aramaic 'my God') → Ἠλίας (Elijah). Bystanders either mishear or deliberately distort. Jewish expectation of Elijah's eschatological return (Mal 4:5-6) as Messiah-herald (cf. Mark 9:11-13) makes Elijah a natural wordplay-target. Mark 9:11-13 had already identified John the Baptist as the Elijah-who-has-come — the irony here is that the crowd still LOOKS for Elijah while Messiah-himself dies before them.",
    },
    "MRK 15:36": {
        "type": "allusion",
        "source": "PSA 69:21",
        "greek_matches": "LXX-ὄξος-verbatim",
        "notes": "Ps 69:22 LXX (Ps 68:22 LXX numbering): ἔδωκαν εἰς τὸ βρῶμά μου χολὴν καὶ εἰς τὴν δίψαν μου ἐπότισάν με ὄξος ('they gave me gall for my food, and for my thirst vinegar to drink'). Mark's ὄξος is the verbatim LXX word. The drink here is DIFFERENT from v.23 (wine-with-myrrh, refused). Scholars debate mercy vs mockery; John 19:28-30 frames it as fulfillment of Ps 69:21 tied to Jesus's 'I thirst.' Mark's Thai preserves the ambiguity.",
    },
    "MRK 15:38": {
        "type": "allusion",
        "source": "EXO 26:31",
        "greek_matches": "thematic",
        "notes": "Temple curtain (καταπέτασμα, Exod 26:31-33 construction). Three major interpretive strands (all likely intended): (1) access-now-open — way to God's presence open for all (Heb 10:19-20); (2) judgment on the temple — its cultic role over, 40 years before physical destruction (70 AD); (3) revelatory sign — heavens torn to show who Jesus is. MARKAN INCLUSIO: σχίζω ('torn') binds 1:10 (heavens torn at baptism) with 15:38 (curtain torn at cross) — same verb, same function (revelation of the Son). Possible secondary echo of Isa 25:7 (God swallowing up the veil spread over nations).",
    },
    "MRK 15:43": {
        "type": "allusion",
        "source": "ISA 53:9",
        "greek_matches": "thematic-fulfillment",
        "notes": "Isa 53:9 'they made his grave with the wicked and with the rich in his death.' Joseph of Arimathea, a Sanhedrin member who provides a rich-man's rock-tomb, fulfils this detail of the Servant Song. Mark's spare presentation is theologically weighted: a religious-establishment insider breaks ranks to bury Jesus. Matthew adds 'rich' (27:57), Luke adds 'righteous' and 'had not consented' (23:50-51), John calls him a secret disciple (19:38) — Mark's minimalism lets the Isaiah fulfilment carry the interpretive weight.",
    },
}


def main():
    db = json.loads(DB_PATH.read_text(encoding="utf-8"))
    citations = db["citations"]

    added = 0
    skipped = 0
    for key, entry in NEW_ENTRIES.items():
        if key in citations:
            print(f"  skip (already present): {key}")
            skipped += 1
            continue
        citations[key] = entry
        added += 1

    # Preserve deterministic ordering: sort by book then numeric chapter:verse
    def sort_key(k: str):
        book, ref = k.split(" ")
        ch, v = ref.split(":")
        return (book, int(ch), int(v))

    db["citations"] = {k: citations[k] for k in sorted(citations.keys(), key=sort_key)}
    DB_PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nBackfill complete: +{added} entries, {skipped} skipped (already present).")
    print(f"Total citations now: {len(db['citations'])}")


if __name__ == "__main__":
    main()
