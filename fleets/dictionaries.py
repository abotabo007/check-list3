
ins = '''CREATE TABLE IF NOT EXISTS inspections
               (i_id INTEGER PRIMARY KEY, c_id INTEGER NOT NULL,
               u_id INTEGER NOT NULL, v_id INTEGER NOT NULL, miles INTEGER NOT NULL,
               next_oil INTEGER NOT NULL, next_1 INTEGER, next_2 INTEGER, date TEXT NOT NULL,
               first_name TEXT, last_name TEXT,
               leak_sign INTEGER, leak_sign_t TEXT, leak_sign_b BLOB,
               tires_inflated INTEGER, tires_inflated_t TEXT, tires_inflated_b BLOB,
               windows_clean INTEGER, windows_clean_t TEXT, windows_clean_b BLOB,
               doors_open INTEGER, doors_open_t TEXT, doors_open_b BLOB,
               oil_level INTEGER, oil_level_t TEXT, oil_level_b BLOB,
               coolant_level INTEGER, coolant_level_t TEXT, coolant_level_b BLOB,
               brake_fluid INTEGER, brake_fluid_t TEXT, brake_fluid_b BLOB,
               transmission_fluid INTEGER, transmission_fluid_t TEXT, transmission_fluid_b BLOB,
               steering_fluid INTEGER, steering_fluid_t TEXT, steering_fluid_b BLOB,
               battery_corrosion INTEGER, battery_corrosion_t TEXT, battery_corrosion_b BLOB,
               windshield_fluid INTEGER, windshield_fluid_t TEXT, windshield_fluid_b BLOB,
               hoses INTEGER, hoses_t TEXT, hoses_b BLOB,
               belts INTEGER, belts_t TEXT, belts_b BLOB,
               interior_clean INTEGER, interior_clean_t TEXT, interior_clean_b BLOB,
               rear_compartment INTEGER, rear_compartment_t TEXT, rear_compartment_b BLOB,
               seatbelts INTEGER, seatbelts_t TEXT, seatbelts_b BLOB,
               mirrors INTEGER, mirrors_t TEXT, mirrors_b BLOB,
               brakes INTEGER, brakes_t TEXT, brakes_b BLOB,
               heater INTEGER, heater_t TEXT, heater_b BLOB,
               ac INTEGER, ac_t TEXT, ac_b BLOB,
               fuel INTEGER, fuel_t TEXT, fuel_b BLOB,
               warning_lights INTEGER, warning_lights_t TEXT, warning_lights_b BLOB,
               door_locks INTEGER, door_locks_t TEXT, door_locks_b BLOB,
               seats INTEGER, seats_t TEXT, seats_b BLOB,
               windows INTEGER, windows_t TEXT, windows_b BLOB,
               fleft_turn INTEGER, fleft_turn_t TEXT, fleft_turn_b BLOB,
               fright_turn INTEGER, fright_turn_t TEXT, fright_turn_b BLOB,
               rleft_turn INTEGER, rleft_turn_t TEXT, rleft_turn_b BLOB,
               rright_turn INTEGER, rright_turn_t TEXT, rright_turn_b BLOB,
               high_beam INTEGER, high_beam_t TEXT, high_beam_b BLOB,
               low_beams INTEGER, low_beams_t TEXT, low_beams_b BLOB,
               reverse_lights INTEGER, reverse_lights_t TEXT, reverse_lights_b BLOB,
               emergency_flashers INTEGER, emergency_flashers_t TEXT, emergency_flashers_b BLOB,
               trailer_connection INTEGER, trailer_connection_t TEXT, trailer_connection_b BLOB,
               harness INTEGER, harness_t TEXT, harness_b BLOB,
               glasses INTEGER, glasses_t TEXT, glasses_b BLOB,
               face_shield INTEGER, face_shield_t TEXT, face_shield_b BLOB,
               hard_hat INTEGER, hard_hat_t TEXT, hard_hat_b BLOB,
               gloves INTEGER, gloves_t TEXT, gloves_b BLOB,
               sleeves INTEGER, sleeves_t TEXT, sleeves_b BLOB,
               shoes INTEGER, shoes_t TEXT, shoes_b BLOB,
               ladders_racks INTEGER, ladders_racks_t TEXT, ladders_racks_b BLOB,
               boom_control INTEGER, boom_control_t TEXT, boom_control_b BLOB,
               hose_leaks INTEGER, hose_leaks_t TEXT, hose_leaks_b BLOB,
               hydraulics_leaks INTEGER, hydraulics_leaks_t TEXT, hydraulics_leaks_b BLOB,
               basket INTEGER, basket_t TEXT, basket_b BLOB,
               extra1 INTEGER, extra1_t TEXT, extra1_b BLOB,
               extra2 INTEGER, extra2_t TEXT, extra2_b BLOB,
               extra3 INTEGER, extra3_t TEXT, extra3_b BLOB,
               extra4 INTEGER, extra4_t TEXT, extra4_b BLOB,
               extra5 INTEGER, extra5_t TEXT, extra5_b BLOB,
               extra6 INTEGER, extra6_t TEXT, extra6_b BLOB,
               extra7 INTEGER, extra7_t TEXT, extra7_b BLOB,
               extra8 INTEGER, extra8_t TEXT, extra8_b BLOB,
               extra9 INTEGER, extra9_t TEXT, extra9_b BLOB,
               extra10 INTEGER, extra10_t TEXT, extra10_b BLOB,
               extra11 INTEGER, extra11_t TEXT, extra11_b BLOB,
               extra12 INTEGER, extra12_t TEXT, extra12_b BLOB,
               extra13 INTEGER, extra13_t TEXT, extra13_b BLOB,
               extra14 INTEGER, extra14_t TEXT, extra14_b BLOB,
               extra15 INTEGER, extra15_t TEXT, extra15_b BLOB,
               extra16 INTEGER, extra16_t TEXT, extra16_b BLOB,
               extra17 INTEGER, extra17_t TEXT, extra17_b BLOB,
               extra18 INTEGER, extra18_t TEXT, extra18_b BLOB,
               extra19 INTEGER, extra19_t TEXT, extra19_b BLOB,
               extra20 INTEGER, extra20_t TEXT, extra20_b BLOB,
               extra21 INTEGER, extra21_t TEXT, extra21_b BLOB,
               extra22 INTEGER, extra22_t TEXT, extra22_b BLOB,
               extra23 INTEGER, extra23_t TEXT, extra23_b BLOB,
               extra24 INTEGER, extra24_t TEXT, extra24_b BLOB,
               extra25 INTEGER, extra25_t TEXT, extra25_b BLOB,
               extra26 INTEGER, extra26_t TEXT, extra26_b BLOB,
               extra27 INTEGER, extra27_t TEXT, extra27_b BLOB,
               extra28 INTEGER, extra28_t TEXT, extra28_b BLOB,
               extra29 INTEGER, extra29_t TEXT, extra29_b BLOB,
               extra30 INTEGER, extra30_t TEXT, extra30_b BLOB,
               extra31 INTEGER, extra31_t TEXT, extra31_b BLOB,
               extra32 INTEGER, extra32_t TEXT, extra32_b BLOB,
               extra33 INTEGER, extra33_t TEXT, extra33_b BLOB,
               extra34 INTEGER, extra34_t TEXT, extra34_b BLOB,
               extra35 INTEGER, extra35_t TEXT, extra35_b BLOB,
               extra36 INTEGER, extra36_t TEXT, extra36_b BLOB,
               extra37 INTEGER, extra37_t TEXT, extra37_b BLOB,
               extra38 INTEGER, extra38_t TEXT, extra38_b BLOB,
               extra39 INTEGER, extra39_t TEXT, extra39_b BLOB,
               extra40 INTEGER, extra40_t TEXT, extra40_b BLOB,
               FOREIGN KEY (c_id) REFERENCES companys (id) ON DELETE CASCADE
               ON UPDATE NO ACTION, FOREIGN KEY (u_id) REFERENCES users (u_id) ON DELETE NO ACTION
               ON UPDATE NO ACTION, FOREIGN KEY (v_id) REFERENCES vehicles (v_id) ON DELETE CASCADE
               ON UPDATE NO ACTION)'''

c1 = [
    ["borsa_documenti", "borsa_documenti_t", "borsa_documenti_b", "Borsa documenti"],
    ["blocchetto_viaggio", "blocchetto_viaggio_t", "blocchetto_viaggio_b", "Blocchetto di viaggio"],
    ["tariffario", "tariffario_t", "tariffario_b", "Tariffario"],
    ["scheda_carburante", "scheda_carburante_t", "scheda_carburante_b", "Scheda carburante"],
    ["schede_118", "schede_118_t", "schede_118_b", "Schede 118"],
    ["carlina", "carlina_t", "carlina_b", "Carlina"],
    ["navigatore", "navigatore_t", "navigatore_b", "Navigatore"],
    ["carta_circola_fotocopia", "carta_circola_fotocopia_t", "carta_circola_fotocopia_b", "Carta circola (fotocopia)"],
    ["cartello_fuori_servizio", "cartello_fuori_servizio_t", "cartello_fuori_servizio_b", "Cartello \"Fuori servizio\""],
    ["elenco_dotazione_ambulanza", "elenco_dotazione_ambulanza_t", "elenco_dotazione_ambulanza_b", "Elenco dotazione ambulanza"],
    ["tagliando_assicurazione", "tagliando_assicurazione_t", "tagliando_assicurazione_b", "Tagliando assicurazione"],
    ["cert_idoneita_asl_fotocopia", "cert_idoneita_asl_fotocopia_t", "cert_idoneita_asl_fotocopia_b", "Cert. idoneità ASL (fotocopia)"],
    ["giubbotto_alta_visibilita", "giubbotto_alta_visibilita_t", "giubbotto_alta_visibilita_b", "Giubbotto alta visibilità"],
    ["triangolo", "triangolo_t", "triangolo_b", "Triangolo"],
    ["estintore_cabina", "estintore_cabina_t", "estintore_cabina_b", "Estintore cabina"],
    ["torcia", "torcia_t", "torcia_b", "Torcia"],
    ["guanti_da_lavoro", "guanti_da_lavoro_t", "guanti_da_lavoro_b", "Guanti da lavoro"],
    ["cassetta_porta_attrezzi", "cassetta_porta_attrezzi_t", "cassetta_porta_attrezzi_b", "Cassetta porta attrezzi"],
    ["gel_battericida_lavamani", "gel_battericida_lavamani_t", "gel_battericida_lavamani_b", "Gel battericida lavamani"],
    ["taglia_s", "taglia_s_t", "taglia_s_b", "Taglia S"],
    ["taglia_m", "taglia_m_t", "taglia_m_b", "Taglia M"],
    ["taglia_l", "taglia_l_t", "taglia_l_b", "Taglia L"],
    ["taglia_xl", "taglia_xl_t", "taglia_xl_b", "Taglia XL"],
    ["cassetti", "cassetti_t", "cassetti_b", "Cassetti"],
    ["forbici_garze", "forbici_garze_t", "forbici_garze_b", "Forbici garze"],
    ["garze_non_sterili_10x10", "garze_non_sterili_10x10_t", "garze_non_sterili_10x10_b", "Garze non sterili 10x10"],
    ["garze_non_sterili_30x30", "garze_non_sterili_30x30_t", "garze_non_sterili_30x30_b", "Garze non sterili 30x30"],
    ["garze_sterili", "garze_sterili_t", "garze_sterili_b", "Garze sterili"],
    ["rasoio", "rasoio_t", "rasoio_b", "Rasoio"],
    ["laccio_emostatico", "laccio_emostatico_t", "laccio_emostatico_b", "Laccio emostatico"],
    ["tellino_sterile", "tellino_sterile_t", "tellino_sterile_b", "Tellino sterile"],
    ["nastrotela", "nastrotela_t", "nastrotela_b", "Nastrotela"],
    ["cerotti_medicati_scatola", "cerotti_medicati_scatola_t", "cerotti_medicati_scatola_b", "Cerotti medicati in scatola"],
    ["bende_orlate_medie", "bende_orlate_medie_t", "bende_orlate_medie_b", "Bende orlate medie"],
    ["bende_orlate_grandi", "bende_orlate_grandi_t", "bende_orlate_grandi_b", "Bende orlate grandi"],
    ["benda_auto_adesiva_grande", "benda_auto_adesiva_grande_t", "benda_auto_adesiva_grande_b", "Benda auto-adesiva grande"],
    ["benda_auto_adesiva_piccola", "benda_auto_adesiva_piccola_t", "benda_auto_adesiva_piccola_b", "Benda auto-adesiva piccola"],
    ["disinfettante_cutaneo", "disinfettante_cutaneo_t", "disinfettante_cutaneo_b", "Disinfettante cutaneo"],
    ["acqua_ossigenata", "acqua_ossigenata_t", "acqua_ossigenata_b", "Acqua ossigenata"],
    ["ghiaccio_istantaneo", "ghiaccio_istantaneo_t", "ghiaccio_istantaneo_b", "Ghiaccio istantaneo in pacco"],
    ["ghiaccio_spray", "ghiaccio_spray_t", "ghiaccio_spray_b", "Ghiaccio spray in bomboletta"],
    ["coperta_isotermica", "coperta_isotermica_t", "coperta_isotermica_b", "Coperta isotermica"],
    ["siringhe", "siringhe_t", "siringhe_b", "Siringhe"],
    ["cavo_12v_aspiratore", "cavo_12v_aspiratore_t", "cavo_12v_aspiratore_b", "Cavo 12 V aspiratore"],
    ["forbici_robin", "forbici_robin_t", "forbici_robin_b", "Forbici Robin"],
    ["piastre_adulto", "piastre_adulto_t", "piastre_adulto_b", "Piastre adulto"],
    ["piastre_pediatriche", "piastre_pediatriche_t", "piastre_pediatriche_b", "Piastre pediatriche"],
    ["lenzuolo_sterile", "lenzuolo_sterile_t", "lenzuolo_sterile_b", "Lenzuolo sterile"],
    ["rasoio_monouso", "rasoio_monouso_t", "rasoio_monouso_b", "Rasoio monouso"],
    ["manuale_istruzioni", "manuale_istruzioni_t", "manuale_istruzioni_b", "Manuale istruzioni"],
    ["aspiratore_fisso", "aspiratore_fisso_t", "aspiratore_fisso_b", "Aspiratore fisso"],
    ["aspiratore_portatile", "aspiratore_portatile_t", "aspiratore_portatile_b", "Aspiratore portatile"],
    ["sacchetti_scorta", "sacchetti_scorta_t", "sacchetti_scorta_b", "Sacchetti di scorta"],
    ["ventilatore_polmonare", "ventilatore_polmonare_t", "ventilatore_polmonare_b", "Ventilatore polmonare"],
    ["frigorifero", "frigorifero_t", "frigorifero_b", "Frigorifero"],
    ["collari_diverse_misure", "collari_diverse_misure_t", "collari_diverse_misure_b", "Collari diverse misure"],
    ["barella_principale", "barella_principale_t", "barella_principale_b", "Barella principale"],
    ["coperta", "coperta_t", "coperta_b", "Coperta"],
    ["barella_atraumatica", "barella_atraumatica_t", "barella_atraumatica_b", "Barella atraumatica"],
    ["cinghie_cucchiaio", "cinghie_cucchiaio_t", "cinghie_cucchiaio_b", "Cinghie cucchiaio"],
    ["telo_portafetiti", "telo_portafetiti_t", "telo_portafetiti_b", "Telo portafetiti"],
    ["set_infettivi", "set_infettivi_t", "set_infettivi_b", "Set infettivi"],
    ["ked", "ked_t", "ked_b", "KED"],
    ["sedia_portantina", "sedia_portantina_t", "sedia_portantina_b", "Sedia portantina"],
    ["elmetto_antine_occhiali", "elmetto_antine_occhiali_t", "elmetto_antine_occhiali_b", "Elmetto antine con occhiali"],
    ["occhiali_protettivi", "occhiali_protettivi_t", "occhiali_protettivi_b", "Occhiali protettivi"],
    ["mascherine_chirurgiche", "mascherine_chirurgiche_t", "mascherine_chirurgiche_b", "Mascherine chirurgiche"],
    ["estintore_2kg", "estintore_2kg_t", "estintore_2kg_b", "Estintore 2 kg"],
    ["multipresa_mobile", "multipresa_mobile_t", "multipresa_mobile_b", "Multipresa mobile (ciabatta)"],
    ["bombolino_o2_vista", "bombolino_o2_vista_t", "bombolino_o2_vista_b", "Bombolino O2 da 3 L. a vista"],
    ["rilevatore_monossido", "rilevatore_monossido_t", "rilevatore_monossido_b", "Rilevatore monossido"],
    ["asse_spinale_adulti", "asse_spinale_adulti_t", "asse_spinale_adulti_b", "Asse Spinale Adulti"],
    ["asse_spinale", "asse_spinale_t", "asse_spinale_b", "Asse spinale"],
    ["base_fermacapo", "base_fermacapo_t", "base_fermacapo_b", "Base fermacapo"],
    ["cuscini_fermacapo", "cuscini_fermacapo_t", "cuscini_fermacapo_b", "Cuscini fermacapo"],
    ["ragno", "ragno_t", "ragno_b", "Ragno"],
    ["cinghie_fermacapo", "cinghie_fermacapo_t", "cinghie_fermacapo_b", "Cinghie fermacapo"],
    ["asse_spinale_pediatrica", "asse_spinale_pediatrica_t", "asse_spinale_pediatrica_b", "Asse Spinale Pediatrica"],
    ["steccobende_piccola", "steccobende_piccola_t", "steccobende_piccola_b", "Steccobende Piccola"],
    ["steccobende_media", "steccobende_media_t", "steccobende_media_b", "Steccobende Media"],
    ["steccobende_grande", "steccobende_grande_t", "steccobende_grande_b", "Steccobende Grande"],
    ["sondino_nero_ch10", "sondino_nero_ch10_t", "sondino_nero_ch10_b", "Nero CH 10"],
    ["sondino_bianco_ch12", "sondino_bianco_ch12_t", "sondino_bianco_ch12_b", "Bianco CH 12"],
    ["sondino_verde_ch14", "sondino_verde_ch14_t", "sondino_verde_ch14_b", "Verde CH 14"],
    ["sondino_arancio_ch16", "sondino_arancio_ch16_t", "sondino_arancio_ch16_b", "Arancio CH 16"],
    ["sondino_rosso_ch18", "sondino_rosso_ch18_t", "sondino_rosso_ch18_b", "Rosso CH 18"],
    ["sondino_giallo_ch20", "sondino_giallo_ch20_t", "sondino_giallo_ch20_b", "Giallo CH 20"],
    ["maschera_ossigeno_adulto_reservoir", "maschera_ossigeno_adulto_reservoir_t", "maschera_ossigeno_adulto_reservoir_b", "Adulto con reservoir"],
    ["maschera_ossigeno_adulto_senza_reservoir", "maschera_ossigeno_adulto_senza_reservoir_t", "maschera_ossigeno_adulto_senza_reservoir_b", "Adulto senza reservoir"],
    ["maschera_ossigeno_pediatrico_reservoir", "maschera_ossigeno_pediatrico_reservoir_t", "maschera_ossigeno_pediatrico_reservoir_b", "Pediatrico con reservoir"],
    ["maschera_ossigeno_pediatrico_senza_reservoir", "maschera_ossigeno_pediatrico_senza_reservoir_t", "maschera_ossigeno_pediatrico_senza_reservoir_b", "Pediatrico senza reservoir"],
    ["tubo_raccordo_o2", "tubo_raccordo_o2_t", "tubo_raccordo_o2_b", "Tubo raccordo O2"],
    ["occhialini_o2", "occhialini_o2_t", "occhialini_o2_b", "Occhialini O2"],
    ["padella", "padella_t", "padella_b", "Padella"],
    ["pappagallo", "pappagallo_t", "pappagallo_b", "Pappagallo"],
    ["bacinella", "bacinella_t", "bacinella_b", "Bacinella"],
    ["spruzzino_disinfettante", "spruzzino_disinfettante_t", "spruzzino_disinfettante_b", "Spruzzino disinfettante"],
    ["carta", "carta_t", "carta_b", "Carta"],
    ["contenitore_taglienti", "contenitore_taglienti_t", "contenitore_taglienti_b", "Contenitore taglienti"],
    ["sacchetti_rifiuti", "sacchetti_rifiuti_t", "sacchetti_rifiuti_b", "Sacchetti rifiuti"],
    ["telli_sterili", "telli_sterili_t", "telli_sterili_b", "Telli sterili"],
    ["clamp", "clamp_t", "clamp_b", "Clamp"],
    ["metalline_baby", "metalline_baby_t", "metalline_baby_b", "Metalline baby"],
    ["metallina_adulti", "metallina_adulti_t", "metallina_adulti_b", "Metallina adulti"],
    ["aspiramico", "aspiramico_t", "aspiramico_b", "Aspiramico"],
    ["sonda_saturimetro_pediatrico", "sonda_saturimetro_pediatrico_t", "sonda_saturimetro_pediatrico_b", "Sonda saturimetro pediatrico"],
    ["sonda_saturimetro_neonatale", "sonda_saturimetro_neonatale_t", "sonda_saturimetro_neonatale_b", "Sonda saturimetro neonatale"],
    ["batteria_di_scorta", "batteria_di_scorta_t", "batteria_di_scorta_b", "Batteria di scorta"],
    ["fonendo_baby", "fonendo_baby_t", "fonendo_baby_b", "Fonendo baby"],
    ["bracciale_pressione", "bracciale_pressione_t", "bracciale_pressione_b", "Bracciale pressione"],
    ["sfigmomanometro_baby", "sfigmomanometro_baby_t", "sfigmomanometro_baby_b", "Sfigmomanometro baby"],
    ["pallone_ambu", "pallone_ambu_t", "pallone_ambu_b", "Pallone Ambu"],
    ["reservoir_per_ambu", "reservoir_per_ambu_t", "reservoir_per_ambu_b", "Reservoir per Ambu"],
    ["filtro_per_ambu", "filtro_per_ambu_t", "filtro_per_ambu_b", "Filtro per Ambu"],
    ["tubo_raccordo_o2_per_ambu", "tubo_raccordo_o2_per_ambu_t", "tubo_raccordo_o2_per_ambu_b", "Tubo di raccordo O2 per Ambu"],
    ["maschera_piccola_per_ambu", "maschera_piccola_per_ambu_t", "maschera_piccola_per_ambu_b", "Maschera piccola per Ambu"],
    ["cannula_guedel_bianca_1", "cannula_guedel_bianca_1_t", "cannula_guedel_bianca_1_b", "Cannula Guedel bianca (1)"],
    ["cannula_guedel_nera_0", "cannula_guedel_nera_0_t", "cannula_guedel_nera_0_b", "Cannula Guedel nera (0)"],
    ["cannula_guedel_blu_00", "cannula_guedel_blu_00_t", "cannula_guedel_blu_00_b", "Cannula Guedel blu (00)"],
    ["cannula_guedel_rosa_000", "cannula_guedel_rosa_000_t", "cannula_guedel_rosa_000_b", "Cannula Guedel rosa (000)"],
    ["siringa_singola", "siringa_singola_t", "siringa_singola_b", "Siringa"],
    ["frusta_principale", "frusta_principale_t", "frusta_principale_b", "Frusta principale"],
    ["frusta_derivazioni", "frusta_derivazioni_t", "frusta_derivazioni_b", "Frusta derivazioni"],
    ["saturimetro_monitor", "saturimetro_monitor_t", "saturimetro_monitor_b", "Saturimetro"],
    ["cavo_test", "cavo_test_t", "cavo_test_b", "Cavo test"],
    ["elettrodi", "elettrodi_t", "elettrodi_b", "Elettrodi"],
    ["piastre_monitor", "piastre_monitor_t", "piastre_monitor_b", "Piastre"],
    ["elettrodi_di_scorta", "elettrodi_di_scorta_t", "elettrodi_di_scorta_b", "Elettrodi di scorta"],
    ["carta_scorta", "carta_scorta_t", "carta_scorta_b", "Carta scorta"],
    ["gel_monitor", "gel_monitor_t", "gel_monitor_b", "Gel"],
    ["set_arti", "set_arti_t", "set_arti_b", "Set arti"],
    ["sacco_mano", "sacco_mano_t", "sacco_mano_b", "Sacco mano"],
    ["sacca_braccio", "sacca_braccio_t", "sacca_braccio_b", "Sacca braccio"],
    ["sacca_gamba", "sacca_gamba_t", "sacca_gamba_b", "Sacca gamba"],
    ["ghiaccio_sterile", "ghiaccio_sterile_t", "ghiaccio_sterile_b", "Ghiaccio sterile"],
    ["garze_30x30", "garze_30x30_t", "garze_30x30_b", "Garze 30x30"],
    ["cerotti", "cerotti_t", "cerotti_b", "Cerotti"],
    ["benda_tela", "benda_tela_t", "benda_tela_b", "Benda tela"],
    ["telo_sterile_allumin_60x80", "telo_sterile_allumin_60x80_t", "telo_sterile_allumin_60x80_b", "Telo sterile allumin. 60x80"],
    ["metalline", "metalline_t", "metalline_b", "Metalline"],
    ["fisiologiche_da_infusione", "fisiologiche_da_infusione_t", "fisiologiche_da_infusione_b", "Fisiologiche da infusione"],
    ["fisiologiche_da_lavaggio", "fisiologiche_da_lavaggio_t", "fisiologiche_da_lavaggio_b", "Fisiologiche da lavaggio"],
    ["sacchetto_vomito", "sacchetto_vomito_t", "sacchetto_vomito_b", "Sacchetto vomito"],
    ["teli_barella", "teli_barella_t", "teli_barella_b", "Teli barella"],
    ["traversa_monouso", "traversa_monouso_t", "traversa_monouso_b", "Traversa monouso"],
    ["sacca_medicazione_verde", "sacca_medicazione_verde_t", "sacca_medicazione_verde_b", "Sacca Medicazione Verde"],
    ["nastro_carta", "nastro_carta_t", "nastro_carta_b", "Nastro carta"],
    ["nastro_telato", "nastro_telato_t", "nastro_telato_b", "Nastro telato"],
    ["guanti_sterili", "guanti_sterili_t", "guanti_sterili_b", "Guanti sterili"],
    ["cerotti_in_scatola_medicati", "cerotti_in_scatola_medicati_t", "cerotti_in_scatola_medicati_b", "Cerotti in scatola medicati"],
    ["forbici_piccole", "forbici_piccole_t", "forbici_piccole_b", "Forbici piccole"],
    ["pallone_ambu_adulto", "pallone_ambu_adulto_t", "pallone_ambu_adulto_b", "Pallone Ambu"],
    ["reservoir_per_ambu_adulto", "reservoir_per_ambu_adulto_t", "reservoir_per_ambu_adulto_b", "Reservoir per Ambu"],
    ["filtro_per_ambu_adulto", "filtro_per_ambu_adulto_t", "filtro_per_ambu_adulto_b", "Filtro per Ambu"],
    ["tubo_raccordo_o2_per_ambu_adulto", "tubo_raccordo_o2_per_ambu_adulto_t", "tubo_raccordo_o2_per_ambu_adulto_b", "Tubo di raccordo O2 per Ambu"],
    ["maschera_piccola_per_ambu_adulto", "maschera_piccola_per_ambu_adulto_t", "maschera_piccola_per_ambu_adulto_b", "Maschera piccola per Ambu"],
    ["maschera_media_per_ambu_adulto", "maschera_media_per_ambu_adulto_t", "maschera_media_per_ambu_adulto_b", "Maschera media per Ambu"],
    ["maschera_grande_per_ambu_adulto", "maschera_grande_per_ambu_adulto_t", "maschera_grande_per_ambu_adulto_b", "Maschera grande per Ambu"],
    ["maschera_con_reservoir_o2", "maschera_con_reservoir_o2_t", "maschera_con_reservoir_o2_b", "Maschera con reservoir O2"],
    ["cannula_guedel_bianca_1_adulto", "cannula_guedel_bianca_1_adulto_t", "cannula_guedel_bianca_1_adulto_b", "Cannula Guedel bianca (1)"],
    ["cannula_guedel_gialla_2", "cannula_guedel_gialla_2_t", "cannula_guedel_gialla_2_b", "Cannula Guedel gialla (2)"],
    ["cannula_guedel_verde_3", "cannula_guedel_verde_3_t", "cannula_guedel_verde_3_b", "Cannula Guedel verde (3)"],
    ["cannula_guedel_arancio_4", "cannula_guedel_arancio_4_t", "cannula_guedel_arancio_4_b", "Cannula Guedel arancio (4)"],
    ["cannula_guedel_azzurra_5", "cannula_guedel_azzurra_5_t", "cannula_guedel_azzurra_5_b", "Cannula Guedel azzurra (5)"],
    ["termometro", "termometro_t", "termometro_b", "Termometro"],
    ["fonendo", "fonendo_t", "fonendo_b", "Fonendo"],
    ["bracciale_pressione_monitor", "bracciale_pressione_monitor_t", "bracciale_pressione_monitor_b", "Bracciale pressione"],
    ["sfigmomanometro", "sfigmomanometro_t", "sfigmomanometro_b", "Sfigmomanometro"],
    ["fonendoscopio", "fonendoscopio_t", "fonendoscopio_b", "Fonendoscopio"],
    ["batterie_di_scorta", "batterie_di_scorta_t", "batterie_di_scorta_b", "Batterie di scorta"],
    ["sondino_bianco_ch12", "sondino_bianco_ch12_t", "sondino_bianco_ch12_b", "Bianco CH 12"],
    ["sondino_verde_ch14", "sondino_verde_ch14_t", "sondino_verde_ch14_b", "Verde CH 14"],
    ["sondino_arancio_ch16", "sondino_arancio_ch16_t", "sondino_arancio_ch16_b", "Arancio CH 16"],
    ["sondino_rosso_ch18", "sondino_rosso_ch18_t", "sondino_rosso_ch18_b", "Rosso CH 18"],
    ["sondino_giallo_ch20", "sondino_giallo_ch20_t", "sondino_giallo_ch20_b", "Giallo CH 20"],
    ["set_scasso", "set_scasso_t", "set_scasso_b", "Set scasso"],
    ["badile", "badile_t", "badile_b", "Badile"],
    ["catene_da_neve", "catene_da_neve_t", "catene_da_neve_b", "Catene da neve (su 210 in cabina)"],
    ["bombolino_o2_di_scorta", "bombolino_o2_di_scorta_t", "bombolino_o2_di_scorta_b", "Bombolino O2 da 3 L. di scorta"],
]