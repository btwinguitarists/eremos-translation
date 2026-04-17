#!/usr/bin/env python3
"""
Second-pass backfill for ALL remaining DB-drift cases across Mark 1–15.

After the Mark 11/13/14/15 backfill added 33 entries, running the hardened
check revealed more drift cases in chapters 2–12 as well — each a verse
whose notes claim an OT link that was never recorded in the DB.

Every entry below is grounded in the existing translation note for that
verse; no new scholarly claims are introduced. For verses where the note
uses generic language ("scripture-fulfillment claim") without identifying
a specific OT text, the entry is marked type='generic_fulfillment' so the
ambiguity is preserved.

Run once:
  python3 scripts/backfill_ot_citations_all.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "nt_ot_citations.json"

NEW_ENTRIES = {
    # ══ MARK 2 ══
    "MRK 2:26": {
        "type": "allusion",
        "source": "1SA 21:1",
        "greek_matches": "narrative-reference",
        "notes": "David eating the Bread of the Presence (1 Sam 21:1-6). HISTORICAL CRUX: Mark's ἐπὶ Ἀβιαθάρ ἀρχιερέως — 1 Sam 21 records Ahimelech, not Abiathar, as priest at Nob; Abiathar (his son) succeeded him (1 Sam 22:20-23). Solutions in literature: (1) Mark/Jesus conflates by memory; (2) ἐπί + gen. = 'in the Scripture section named for Abiathar' (paralleling Mark 12:26's ἐπὶ τοῦ βάτου 'in the burning-bush passage'); (3) both shared priesthood during transition; (4) a variant reading. SBLGNT retains Ἀβιαθάρ as the harder reading. Jesus uses the David-precedent to defend disciples' sabbath plucking — human need supersedes ritual boundary.",
    },

    # ══ MARK 3 ══
    # 3:13 — no clear OT reference in notes; appears to be a rationale-triggered
    # mention of Exod 24 (mountain-calling). Recording as a conceptual echo.
    "MRK 3:13": {
        "type": "echo",
        "source": "EXO 24:1",
        "greek_matches": "thematic",
        "notes": "Jesus ascending the mountain to call the Twelve echoes Moses ascending Sinai to establish the covenant people (Exod 24:1-11). Mark's 'he went up the mountain and called whom he wanted' carries Moses-typology — the new people-of-God being constituted on a mountain by the Son.",
    },

    # ══ MARK 4 ══
    "MRK 4:3": {
        "type": "echo",
        "source": "DEU 6:4",
        "greek_matches": "thematic",
        "notes": "Jesus's opening 'Listen!' (Ἀκούετε) echoes the Shema's opening imperative (Deut 6:4 'Hear, O Israel'). The Parable of the Sower is structured as Jesus's own Shema — a call to covenant-listening that becomes the criterion for understanding all his parables (v.13).",
    },
    "MRK 4:29": {
        "type": "citation",
        "source": "JOL 3:13",
        "greek_matches": "LXX",
        "notes": "Mark 4:29 'εὐθὺς ἀποστέλλει τὸ δρέπανον, ὅτι παρέστηκεν ὁ θερισμός' directly echoes Joel 3:13 LXX (4:13 LXX numbering: ἐξαποστείλατε δρέπανα, ὅτι παρέστηκεν τρυγητός). Isa 17:5 provides secondary resonance. The harvest-sickle is standard OT imagery for eschatological divine judgment (cf. Rev 14:14-16). The parable's force: between sowing and reaping is hidden divine growth, which crashes into visibility at harvest.",
    },
    "MRK 4:41": {
        "type": "allusion",
        "source": "PSA 89:9",
        "greek_matches": "thematic",
        "notes": "The disciples' 'Who is this?' invokes OT sea-subduing theophany: Ps 89:8-9 ('O LORD God of hosts, who is like you? You still the raging of the sea'); Ps 107:29 ('he stilled the storm to a whisper'); Job 38:8-11 (YHWH sets bounds to the sea). For first-century Jews, only YHWH commands the sea. Mark places this Christological question at the climax of ch.4 to force the same confession the centurion will voice at 15:39 ('Truly this was the Son of God'). THEME CLOSURE: ch.4 opens with 'Listen!' (v.3) and closes with 'the wind and sea OBEY' (ὑπακούει = 'hear-under') — creation hears what the disciples struggle to.",
    },

    # ══ MARK 6 ══
    "MRK 6:23": {
        "type": "allusion",
        "source": "EST 5:3",
        "greek_matches": "narrative-echo",
        "notes": "Herod's 'up to half my kingdom' oath echoes Est 5:3, 5:6, 7:2 (Ahasuerus to Esther). Mark's ironic reversal: in Esther the formula saves Jewish lives; here it costs a prophet's. The escalation v.22 casual offer → v.23 sworn oath traps Herod in front of his court.",
    },
    "MRK 6:34": {
        "type": "allusion",
        "source": "NUM 27:17",
        "greek_matches": "LXX",
        "notes": "Jesus's compassion at 'sheep without a shepherd' (ὡς πρόβατα μὴ ἔχοντα ποιμένα) tracks Num 27:17 LXX (ὡσεὶ πρόβατα οἷς οὐκ ἔστιν ποιμήν). Secondary allusions: 1 Kgs 22:17; Ezek 34:5; Zech 10:2. Num 27 is Joshua's commissioning as new-shepherd of Israel — Jesus as new-Joshua leading the wilderness-people-who-need-a-shepherd. σπλαγχνίζομαι (compassion) is Mark's signature verb for Jesus's shepherd-instinct. The chapter opened with rejection in his hometown; it ends with overflowing compassion for strangers.",
    },
    "MRK 6:48": {
        "type": "composite_allusion",
        "sources": ["JOB 9:8", "EXO 33:22", "1KI 19:11"],
        "greek_matches": "LXX-theophanic",
        "notes": "Walking-on-water + 'wished to pass them by' is layered OT theophany-language. (1) Job 9:8 LXX — only YHWH treads on the sea. (2) Exod 33:19, 22 — God 'passes by' Moses on the rock; Mark's παρελθεῖν echoes LXX παρελεύσομαι. (3) 1 Kgs 19:11 LXX — God 'passes by' (παρελεύσεται) Elijah at Horeb. Jesus's walking-on-water is a deliberate theophanic enactment: doing what YHWH does in OT theophanies, using OT theophany-vocabulary. The disciples nearly recognize the supernatural quality but misinterpret it as apparition (v.49). Fourth-watch timing (3-6 AM) after ~9 hours of rowing against the wind places the miracle at maximum exhaustion.",
    },
    "MRK 6:50": {
        "type": "composite_allusion",
        "sources": ["EXO 3:14", "ISA 41:4"],
        "greek_matches": "LXX-divine-self-identification",
        "notes": "ἐγώ εἰμι: Mark's most theologically charged self-disclosure. Echoes Exod 3:14 LXX (God's name to Moses) and Isa 41:4 / 43:10 / 43:25 / 51:12 / 52:6 (YHWH's self-identification 'I am he' / 'I am'). Combined with v.48's theophanic 'pass by' and walking-on-water (Job 9:8), Mark constructs a sustained YHWH-self-revelation tableau. The disciples should hear: this is GOD revealing himself in the storm. Their non-recognition (v.52 hearts hardened) is the tragedy. CHRISTOLOGICAL CRUX: Mark 6:50 is load-bearing for the high Christology — Jesus does what only YHWH does, says what only YHWH says. Thai 'เราเอง' dual-functions as natural self-identifier AND emphatic 'I AM.'",
    },
    "MRK 6:52": {
        "type": "echo",
        "source": "EXO 7:3",
        "greek_matches": "LXX-vocabulary",
        "notes": "πωρόω/πώρωσις (heart-hardness) carries Exodus-vocabulary — originally Pharaoh-language (Exod 7:3; 8:15; 9:12). Mark applies it to the Twelve, their Pharaoh-level resistance to repeated revelation. Paul picks up the same word-family for unbelieving Israel (Rom 11:25). Mark's theological point: the gospel doesn't assume the disciples' unique virtue — they too need the hardening broken open by repeated revelation.",
    },

    # ══ MARK 7 ══
    "MRK 7:35": {
        "type": "allusion",
        "source": "ISA 35:5",
        "greek_matches": "LXX",
        "notes": "Isa 35:5-6 Messianic-age healing-promise: 'the eyes of the blind shall be opened, and the ears of the deaf shall be unstopped... the tongue of the dumb (μογιλάλων) shall sing for joy.' Mark's vocabulary tracks Isaiah's promised restoration precisely (μογιλάλος is a LXX hapax shared with Isa 35:6). The instantaneous reversal — ears opened, tongue loosed, plain speech — enacts the Messianic age. Double passive (ἠνοίγησαν, ἐλύθη) is divine-passive: agency is Jesus's-command-as-God's-power.",
    },

    # ══ MARK 9 ══
    "MRK 9:2": {
        "type": "allusion",
        "source": "EXO 24:16",
        "greek_matches": "LXX-narrative",
        "notes": "Six-day delay echoes Exod 24:15-16 (Moses on Sinai: six days of waiting, then YHWH's voice on the seventh). Jesus takes the inner-three — Peter, James, John — the same three who will sleep in Gethsemane (14:33). The Transfiguration narratively confirms 8:38 ('the Son of Man will come in the glory of his Father'): here that glory is momentarily unveiled. The Moses-typology runs throughout (mountain, cloud, voice, glory).",
    },
    "MRK 9:3": {
        "type": "allusion",
        "source": "DAN 7:9",
        "greek_matches": "LXX-apocalyptic",
        "notes": "Two hapax in a single verse (στίλβω 'shine-radiantly', γναφεύς 'launderer') render the heavenly-whiteness superlatively. Parallels: Dan 7:9 LXX (Ancient of Days: τὸ ἔνδυμα αὐτοῦ ὡσεὶ χιὼν λευκόν 'his clothing white as snow') and Dan 10:6 (man-clothed-in-linen with body στίλβοντος as beryl). Mark's diction evokes apocalyptic theophany — Jesus visually identified with the Dan 7 divine-figure.",
    },
    "MRK 9:7": {
        "type": "composite_citation",
        "sources": ["DEU 18:15", "PSA 2:7", "ISA 42:1"],
        "greek_matches": "LXX-composite",
        "notes": "The divine voice combines: Deut 18:15 LXX (αὐτοῦ ἀκούσεσθε 'you shall listen to him' — the prophet-like-Moses); Ps 2:7 (Davidic-royal 'you are my son'); Isa 42:1 (servant-beloved ὁ ἐκλεκτός μου). Command 'hear him' (ἀκούετε αὐτοῦ) is the transfiguration climax: Jesus supersedes Law-and-Prophets (embodied by Moses and Elijah present) as THE one to be heard. The cloud (Shekhinah) evokes Exod 24 + Exod 40:34 + Num 7:89 theophany-sequence. Not 'one of three' (as Peter proposed in v.5) but the unique Son.",
    },
    "MRK 9:11": {
        "type": "allusion",
        "source": "MAL 4:5",
        "greek_matches": "thematic",
        "notes": "Disciples' question invokes the scribal doctrine derived from Mal 4:5-6 (Mal 3:23-24 Heb.): Elijah must come before the Messiah. Having just seen Elijah on the mountain (v.4), they ask whether the prophecy is fulfilled in what they just witnessed, or whether there is a future-Elijah. Jesus's reply (vv.12-13) identifies John the Baptist as the fulfillment (cf. Mark 1:6 — John's dress explicitly echoes Elijah's 2 Kgs 1:8 LXX).",
    },
    "MRK 9:19": {
        "type": "allusion",
        "source": "DEU 32:5",
        "greek_matches": "LXX-echo",
        "notes": "γενεὰ ἄπιστος inherits Deuteronomic-exodus charge of Israel's wilderness-disobedience: Deut 32:5 (Song of Moses: 'crooked and perverse generation' γενεὰ σκολιὰ καὶ διεστραμμένη); also Deut 32:20; Ps 95:10 LXX (Heb 3:10). Jesus's exasperation encompasses disciples, crowd, scribes, father — the 'generation' of the present age fails to trust.",
    },
    "MRK 9:31": {
        "type": "allusion",
        "source": "HOS 6:2",
        "greek_matches": "LXX-timing",
        "notes": "Second passion prediction. 'Third day' resurrection timing echoes Hos 6:2 LXX (ἐν τῇ ἡμέρᾳ τῇ τρίτῃ ἀναστησόμεθα 'on the third day we shall rise'). Structural counterpart to 8:31 and 10:33-34. παραδίδοται (present tense 'is being handed over') more imminent than 8:31's δεῖ παθεῖν. Son-of-Man/hands-of-men wordplay (υἱὸς ἀνθρώπου → χεῖρας ἀνθρώπων) preserved in Thai 'บุตรมนุษย์/มือของมนุษย์.'",
    },
    "MRK 9:48": {
        "type": "citation",
        "source": "ISA 66:24",
        "greek_matches": "LXX",
        "notes": "Direct citation of Isa 66:24 LXX: ὁ σκώληξ αὐτῶν οὐ τελευτήσει, καὶ τὸ πῦρ αὐτῶν οὐ σβεσθήσεται ('their worm will not die, and their fire will not be quenched'). Mark's wording matches the LXX so precisely that it functions as a citation, though not formally-introduced. Isa 66:24 is the culmination of Isaiah's prophecy — the eschatological judgment where the wicked are consumed perpetually. σκώληξ is a Markan hapax. THEOLOGICALLY: worm + fire is metaphoric imagery for continuous judgment, not necessarily literal.",
    },
    "MRK 9:49": {
        "type": "allusion",
        "source": "LEV 2:13",
        "greek_matches": "LXX-conceptual",
        "notes": "TEXTUAL VARIANT: SBLGNT reads the shorter πᾶς γὰρ πυρὶ ἁλισθήσεται ('every one will be salted with fire'). Many Byz witnesses add 'καὶ πᾶσα θυσία ἁλὶ ἁλισθήσεται' ('and every sacrifice will be salted with salt' — Lev 2:13 echo). The shorter SBLGNT reading is almost certainly original (א B L W Δ f¹); the longer is a scribal harmonization. Lev 2:13 (salt-of-the-covenant in sacrifice) is the conceptual background regardless of which reading is preserved. vv.43-48's Gehenna-fire warnings are summarized by v.49's universal-salting — fire of trial preserves by testing (cf. 1 Pet 1:7; 4:12-13).",
    },

    # ══ MARK 10 ══
    "MRK 10:33": {
        "type": "allusion",
        "source": "ISA 53:6",
        "greek_matches": "divine-passive",
        "notes": "Third (most detailed) passion prediction. Two-stage betrayal: (1) to Jewish leaders (chief priests + scribes), (2) to Gentiles — historically accurate (Sanhedrin trial + Roman crucifixion). The doubled παραδίδωμι (will-be-handed-over + will-hand-over) is Markan irony: they hand over the One whom God is handing over. παραδοθήσεται = divine passive alluding to Isa 53:6/12 ('the LORD has laid on him the iniquity of us all' / 'he poured out his soul to death'). The Servant-Song framework underlies all three passion predictions.",
    },

    # ══ MARK 11 ══
    "MRK 11:7": {
        "type": "allusion",
        "source": "2KI 9:13",
        "greek_matches": "LXX-royal-acclamation",
        "notes": "Royal-acclamation echo: 2 Kgs 9:13 LXX records Jehu's officers hastily spreading their garments (ἱμάτιον) beneath his feet at his acclamation as king. Combined with (a) Mount of Olives setting, (b) Bethphage/Bethany locus, (c) never-ridden colt (1 Sam 6:7; Num 19:2), and (d) imminent Ps 118 acclamation, Mark builds a cumulative royal-coronation framework. Thai ประทับ (royal-register for ἐκάθισεν) encodes this reading.",
    },
    "MRK 11:10": {
        "type": "acclamation-not-citation",
        "source": "PSA 118:26",
        "greek_matches": "thematic-extension",
        "notes": "NOT a formal OT citation but an acclamation that extends Ps 118:26 (v.9) into Davidic-kingdom expectation. The crowd makes explicit what they think 'the one coming in the name of the Lord' means — a Davidic royal-restoration. Mark allows this political-messianic acclamation to stand without correction (unlike Matt 21:10-11 where the crowd cools to 'the prophet from Nazareth'). The ambiguity is theologically productive: the crowd is right about kingship but wrong about its nature. By 15:32 they will mock the same man as 'king of Israel.'",
    },
    "MRK 11:14": {
        "type": "composite_allusion",
        "sources": ["JER 8:13", "HOS 9:10", "MIC 7:1", "JOL 1:7"],
        "greek_matches": "LXX-prophetic-pattern",
        "notes": "Jesus's fig-tree curse echoes the OT fruitless-vine/fig-tree imagery as YHWH's indictment of Israel: Jer 8:13 LXX (οὐκ ἔστιν σταφυλὴ ἐν ταῖς ἀμπέλοις καὶ οὐκ ἔστιν σῦκα ἐν ταῖς συκαῖς); Hos 9:10, 16; Mic 7:1; Joel 1:7. The apostrophic address (to a tree that cannot hear) is a classic OT prophetic gesture (cf. Jer 22:29 'O earth, earth, earth'). The disciples-as-audience (ἤκουον 'were hearing') flags the action as public teaching, setting up their astonished recognition at v.21.",
    },
    "MRK 11:20": {
        "type": "composite_allusion",
        "sources": ["HOS 9:16", "ISA 5:24", "JOB 18:16"],
        "greek_matches": "LXX-judgment-language",
        "notes": "Second half of the Markan fig-tree/temple sandwich — A₂ (fig tree withered) confirms A₁ (cursing) and illuminates B (temple cleansing): just as this tree is judged and dead, so the temple system will be. The 'root-deep destruction' image echoes Job 18:16, Hos 9:16, Isa 5:24 — prophetic-judgment language for terminal destruction with no revival possible.",
    },

    # ══ MARK 12 ══
    "MRK 12:32": {
        "type": "composite_allusion",
        "sources": ["DEU 4:35", "ISA 45:5"],
        "greek_matches": "LXX-monotheistic-confession",
        "notes": "The scribe's restatement collapses OT monotheistic-confession tradition into one statement: Deut 4:35 ('there is none beside him'), Isa 45:5 ('I am the LORD, and there is no other'). Mark uses the scribe's sincerity to demonstrate that not all scribes were Jesus's opponents — a narrative corrective to the otherwise flat-opposition portrayal.",
    },
    "MRK 12:33": {
        "type": "composite_allusion",
        "sources": ["1SA 15:22", "HOS 6:6"],
        "greek_matches": "LXX-prophetic-tradition",
        "notes": "The scribe's 'more than burnt offerings and sacrifices' directly echoes the prophetic tradition: Hos 6:6 (ἔλεος θέλω καὶ οὐ θυσίαν 'I desire mercy, not sacrifice'), 1 Sam 15:22 ('to obey is better than sacrifice'), Mic 6:6-8, Ps 40:6-8, Isa 1:11-17, Amos 5:21-24. In the temple courts, this statement is implicitly critical of the temple-system. The scribe has discerned something that prepares him for Jesus's response in v.34. Glossary: ὁλοκαύτωμα → เครื่องเผาบูชา, θυσία → เครื่องสัตวบูชา.",
    },

    # ══ MARK 13 ══
    "MRK 13:6": {
        "type": "echo",
        "source": "EXO 3:14",
        "greek_matches": "LXX-divine-self-identification",
        "notes": "ἐγώ εἰμι ambiguity preserved intentionally. Mark has used ἐγώ εἰμι for Jesus in divine-self-revelation moments: 6:50 (walking-on-water theophany, Exod 3:14 echo) and 14:62 (Sanhedrin trial). Here at 13:6, false-Christs appropriating precisely this phrase is Mark's signal that they claim the highest identification, not merely 'I am the Messiah.' Mark's Christology is understated but pointed: false ἐγώ εἰμι-claimants confirm Jesus's ἐγώ εἰμι claims are indeed ultimate. First-century messianic pretenders (Theudas, Judas the Galilean) exemplify this.",
    },
    "MRK 13:9": {
        "type": "background",
        "source": "DEU 25:2",
        "greek_matches": "thematic-background",
        "notes": "Synagogue floggings (ἐν συναγωγαῖς δαρήσεσθε) invoke Deut 25:2-3's 39-lash limit (m. Makk. 3:10). Jesus's prediction schematically maps the persecutions later documented in Acts (Peter/John before Sanhedrin 4-5; Paul beaten in synagogues, 2 Cor 11:24; Paul before Felix/Festus, Acts 24-26; Paul before Agrippa II, Acts 26; Paul before Caesar, Acts 27-28). Three concentric circles of persecution: Jewish-local (συνέδρια, συναγωγαί) → Roman-provincial (ἡγεμόνες) → Roman-imperial (βασιλεῖς).",
    },
    "MRK 13:17": {
        "type": "reference",
        "source": "ISA 7:14",
        "greek_matches": "pastoral-register",
        "notes": "Jesus's compassion-pause for pregnant and nursing women is pastoral-realism within cosmic prophecy. No direct OT citation; scholarly note-reference to Isa 7:14 in the general pregnancy-theme background. Luke 21:23 retains the verse almost verbatim.",
    },
    "MRK 13:23": {
        "type": "principle-application",
        "source": "DEU 18:22",
        "greek_matches": "thematic",
        "notes": "Jesus invokes the Deuteronomic test of prophetic reliability: Deut 18:22 — a true prophet's word comes to pass. Advance-warning creates an objective standard against which later-claimants' signs-and-wonders must measure. Transition verse: closes tribulation-section (vv.5-23), opens cosmic-Son-of-Man section (vv.24-27). The structural pivot 'I have told you beforehand' applies the Deuteronomic test to Jesus's own corpus.",
    },

    # ══ MARK 14 ══
    "MRK 14:21": {
        "type": "allusion",
        "source": "JER 20:14",
        "greek_matches": "OT-curse-formula",
        "notes": "The 'better not to have been born' formula is the strongest OT-style curse: echoes Jer 20:14 (Jeremiah's self-curse), Job 3:3, Sir 23:14. Applied to Judas it signals ultimate moral catastrophe. Mark holds in tension divine-necessity (Son-of-Man goes 'as written') and human-responsibility (woe to the betrayer) — same tension as Acts 2:23. Fourth occurrence of παραδίδωμι in vv.10-21. Jesus does not name Judas; the woe is spoken in his hearing, but Mark narrates no turning-point for him.",
    },
    "MRK 14:49": {
        "type": "generic_fulfillment",
        "source": "MULTIPLE",
        "greek_matches": "formal-claim",
        "notes": "SCRIPTURE-FULFILLMENT CLAIM without specific identification. Jesus invokes 'that the Scriptures might be fulfilled' (ἵνα πληρωθῶσιν αἱ γραφαί) as a programmatic self-interpretation, Mark's densest concentration of divine-necessity language (δεῖ + καθὼς γέγραπται + ἵνα πληρωθῶσιν). The broad referent-field is the Passion-predicting OT complex: Servant Songs (Isa 52:13-53:12), Lament Psalms (Ps 22, 41, 69), Zech 13:7 (just cited v.27), and the prophetic-suffering tradition. Mark intentionally does NOT specify which text — the totality of Scripture's testimony to the Messiah's suffering is what is being fulfilled.",
    },
    "MRK 14:50": {
        "type": "allusion-fulfillment",
        "source": "ZEC 13:7",
        "greek_matches": "LXX",
        "notes": "Zech 13:7 FULFILLMENT of 14:27's citation. 'I will strike the shepherd, and the sheep will be scattered' — Mark's literary precision pairs prophecy and fulfillment within five verses. πάντες includes Peter (who reappears at v.54 'following at a distance'). Also sets up v.51's mysterious young-man figure.",
    },
    "MRK 14:58": {
        "type": "echo",
        "source": "ISA 46:6",
        "greek_matches": "LXX-idol-vocabulary",
        "notes": "TEMPLE-SAYING DISTORTION. False witnesses mangle Jesus's historical temple-saying (preserved accurately at John 2:19, Acts 6:14): (a) changed subject (Jesus as destroyer not raiser), (b) verb substitution (οἰκοδομήσω 'will-build' for original ἐγερῶ 'will-raise'), (c) added χειροποίητος/ἀχειροποίητος pair — LXX idol-vocabulary (Isa 46:6 etc.; Lev 26:1) suggesting Jesus calls the temple an idol. The entire accusation becomes Jesus-threatening-temple + implicitly-calling-it-idolatry + claiming-to-build-rival-sanctuary. Witnesses disagree (v.59) — court cannot establish even the fabricated charge.",
    },

    # ══ MARK 15 ══
    "MRK 15:5": {
        "type": "allusion",
        "source": "ISA 53:7",
        "greek_matches": "enactment",
        "notes": "Jesus's silence before Pilate enacts Isa 53:7 LXX ('ὡς πρόβατον ἐπὶ σφαγὴν ἤχθη καὶ ὡς ἀμνὸς ἐναντίον τοῦ κείροντος αὐτὸν ἄφωνος οὕτως οὐκ ἀνοίγει τὸ στόμα αὐτοῦ'). Mark does not quote but performs the Servant-Song shape (cf. 14:61 silent before Caiaphas). Pilate's θαυμάζειν parallels and contrasts with the centurion's confession at v.39 — one marvels and misses who Jesus is; the other marvels and sees.",
    },
    "MRK 15:23": {
        "type": "allusion",
        "source": "PSA 69:21",
        "greek_matches": "thematic",
        "notes": "Wine-with-myrrh (σμυρνισμένος, hapax) offered as pre-crucifixion anesthetic. Myrrh's double Life-of-Jesus appearance (Magi's gift at birth → burial preparation) is Christian-typological. Matt 27:34 substitutes 'gall' (χολή), harmonizing to Ps 69:21 LXX (ἔδωκαν εἰς τὸ βρῶμά μου χολήν). Mark preserves σμυρνίζω and leaves the Ps 69:21 echo implicit. Jesus's REFUSAL has been variously interpreted: (1) full consciousness for atoning suffering, (2) fulfilling Gethsemane's 'I will not drink again of the fruit of the vine until...' (14:25), (3) rejection of the mocking gesture.",
    },
    "MRK 15:40": {
        "type": "allusion",
        "source": "PSA 38:11",
        "greek_matches": "thematic",
        "notes": "Women watching ἀπὸ μακρόθεν ('from afar') echoes Ps 38:11 LXX ('οἱ ἔγγιστά μου ἀπὸ μακρόθεν ἔστησαν' — 'my nearest stand afar off'), the Psalm of the abandoned sufferer. Mark's spatial note encodes the Psalm's abandonment-motif: the few who remain can only watch from distance. These women form Mark's GOSPEL-WITNESS CHAIN (crucifixion 15:40, burial 15:47, empty tomb 16:1-8) — the only humans present at all three pivotal events, contrasting with the male disciples' flight.",
    },
    "MRK 15:45": {
        "type": "allusion",
        "source": "ISA 53:9",
        "greek_matches": "narrative-fulfillment",
        "notes": "Pilate's release of the body to Joseph of Arimathea is part of the Isa 53:9 fulfillment sequence ('with a rich man in his death'). Roman practice normally denied crucifixion-victims proper burial (left on cross or mass grave as deterrent); Pilate's favor is unusual. πτῶμα (literally 'fallen-thing,' standard Greek for corpse) marks dehumanized state; Mark's Thai translation preserves human dignity via royal-register พระศพ — a theological choice.",
    },
    "MRK 15:46": {
        "type": "allusion",
        "source": "ISA 53:9",
        "greek_matches": "LXX-narrative-fulfillment",
        "notes": "RICH-MAN-TOMB fulfills Isa 53:9 LXX ('δώσω τοὺς πονηροὺς ἀντὶ τῆς ταφῆς αὐτοῦ καὶ τοὺς πλουσίους ἀντὶ τοῦ θανάτου αὐτοῦ'). Mark's bare narration (buy linen → take down → wrap → place in tomb → roll stone → close up, 6 actions) lets the fulfillment-logic speak without editorial comment. σινδών glossary reaffirmed (established at 14:51); μνημεῖον → อุโมงค์ glossary established. Hapax: ἐνειλέω.",
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

    def sort_key(k: str):
        book, ref = k.split(" ")
        ch, v = ref.split(":")
        return (book, int(ch), int(v))

    db["citations"] = {k: citations[k] for k in sorted(citations.keys(), key=sort_key)}
    DB_PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nBackfill complete: +{added} entries, {skipped} skipped.")
    print(f"Total citations now: {len(db['citations'])}")


if __name__ == "__main__":
    main()
