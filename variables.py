data_labels = {
    'p_m2_FE': 'Avg. land rent (€/m2)',
    'pop_density': 'Population density (per km2)',
    'OAD': 'Omgevingsadressendichtheid (adressen per km2)',
    'STED': 'Stedelijkheid (code)',
    'AFS_SUPERM': 'Afstand tot dichtstbijzijnde grote supermarkt (km)',
    'AFS_DAGLMD': 'Afstand tot dichtstbijzijnde overige dagelijkse levensmiddelen (km)',
    'AFS_WARENH': 'Afstand tot dichtstbijzijnde warenhuis (km)',
    'AFS_CAFE': 'Afstand tot dichtstbijzijnde café (km)',
    'AFS_CAFTAR': 'Afstand tot dichtstbijzijnde cafetaria (km)',
    'AFS_HOTEL': 'Afstand tot dichtstbijzijnde hotel (km)',
    'AFS_BSO': 'Afstand tot dichtstbijzijnde buitenschoolse opvang (km)',
    'AFS_KDV': 'Afstand tot dichtstbijzijnde kinderdagverblijf (km)',
    'AFS_BRANDW': 'Afstand tot dichtstbijzijnde brandweerkazerne (km)',
    'AFS_OPRIT': 'Afstand tot dichtstbijzijnde oprit hoofdverkeersweg (km)',
    'AFS_TRNOVS': 'Afstand tot dichtstbijzijnde belangrijk overstapstation (km)',
    'AFS_TREINS': 'Afstand tot dichtstbijzijnde treinstation (km)',
    'AFS_ATTRAC': 'Afstand tot dichtstbijzijnde attractiepark (km)',
    'AFS_BIOS': 'Afstand tot dichtstbijzijnde bioscoop (km)',
    'AFS_MUS': 'Afstand tot museum (km)',
    'AFS_PODIUM': 'Afstand tot dichtstbijzijnde locatie podiumkunsten (km)',
    'AFS_BIBLIO': 'Afstand tot dichtstbijzijnde bibliotheek (km)',
    'AF_IJSBAAN': 'Afstand tot dichtstbijzijnde kunstijsbaan (km)',
    'AFS_POP': 'Afstand tot dichtstbijzijnde poppodium (km)',
    'AFS_SAUNA': 'Afstand tot dichtstbijzijnde sauna (km)',
    'AFS_ZONBNK': 'Afstand tot dichtstbijzijnde zonnebank (km)',
    'AFS_ZWEMB': 'Afstand tot dichtstbijzijnde zwembad (km)',
    'AFS_ONDBAS': 'Afstand tot dichtstbijzijnde basisschool (km)',
    'AFS_ONDHV': 'Afstand tot dichtstbijzijnde school HAVO/VWO (km)',
    'AFS_ONDVMB': 'Afstand tot dichtstbijzijnde school VMBO (km)',
    'AFS_ONDVRT': 'Afstand tot dichtstbijzijnde voortgezet onderwijs (km)',
    'AFS_HAPRAK': 'Afstand tot dichtstbijzijnde huisartsenpraktijk (km)',
    'AFS_ZIEK_E': 'Afstand tot dichtstbijzijnde ziekenhuis excl. Buitenpolikliniek (km)',
    'AFS_ZIEK_I': 'Afstand tot dichtstbijzijnde ziekenhuis incl. buitenpolikliniek (km)',
    'AFS_APOTH': 'Afstand tot dichtstbijzijnde apotheek (km)',
    'AFS_HAPOST': 'Afstand tot dichtstbijzijnde huisartsenpost (km)',
    'AV5_SUPERM': 'Aantal grote supermarkten binnen 5 kilometer (aantal)',
    'AV5_HAPRAK': 'Aantal huisartsenpraktijken binnen 5 kilometer (aantal)',
    'AV5_ONDBAS': 'Aantal basisscholen binnen 5 kilometer (aantal)',
    'AV5_ONDVRT': 'Aantal scholen voortgezet onderwijs binnen 5 kilometer (aantal)',
    'G_ELEK_WON': 'Gemiddeld elektriciteitsverbruik (kWh)',

}

m = [['AFS_BSO',
  'AFS_HAPRAK',
  'AFS_TRNOVS',
  'AFS_ONDHV',
  'AFS_WARENH',
  'AFS_APOTH',
  'AFS_TREINS',
  'AFS_BRANDW',
  'AFS_CAFE',
  'AFS_POP',
  'AFS_KDV',
  'AV5_HAPRAK',
  'AFS_HOTEL',
  'AFS_ONDBAS',
  'AFS_ZONBNK',
  'AFS_CAFTAR',
  'AFS_ONDVRT',
  'AFS_SAUNA',
  'AFS_PODIUM',
  'AV5_ONDBAS',
  'AFS_OPRIT',
  'OAD',
  'AV5_SUPERM',
  'AF_IJSBAAN',
  'AFS_MUS',
  'AFS_ONDVMB',
  'AFS_ZWEMB',
  'AFS_SUPERM',
  'AFS_ATTRAC',
  'AFS_BIOS',
  'AFS_HAPOST',
  'AV5_ONDVRT',
  'AFS_DAGLMD',
  'AFS_BIBLIO',
  'AFS_ZIEK_E',
  'AFS_ZIEK_I',
  'G_ELEK_WON'],
 ['AFS_SUPERM',
  'AFS_OPRIT',
  'AFS_TREINS',
  'AFS_HAPRAK',
  'AFS_ONDBAS',
  'AFS_ONDVRT',
  'AFS_PODIUM',
  'OAD'],
 ['AV5_SUPERM',
  'AFS_OPRIT',
  'AFS_TREINS',
  'AV5_HAPRAK',
  'AV5_ONDBAS',
  'AV5_ONDVRT',
  'AFS_PODIUM',
  'OAD'],
 ['pop_density',
  'AFS_SUPERM',
  'AFS_DAGLMD',
  'AFS_WARENH',
  'AFS_CAFE',
  'AFS_CAFTAR',
  'AFS_HOTEL',
  'AFS_BSO',
  'AFS_KDV',
  'AFS_BRANDW',
  'AFS_OPRIT',
  'AFS_TRNOVS',
  'AFS_TREINS',
  'AFS_ATTRAC',
  'AFS_BIOS',
  'AFS_MUS',
  'AFS_PODIUM',
  'AFS_BIBLIO',
  'AF_IJSBAAN',
  'AFS_POP',
  'AFS_SAUNA',
  'AFS_ZONBNK',
  'AFS_ZWEMB',
  'AFS_ONDBAS',
  'AFS_ONDHV',
  'AFS_ONDVMB',
  'AFS_ONDVRT',
  'AFS_HAPRAK',
  'AFS_ZIEK_E',
  'AFS_ZIEK_I',
  'AFS_APOTH',
  'AFS_HAPOST'],
 ['AFS_SUPERM',
  'AFS_OPRIT',
  'AFS_TREINS',
  'AFS_HAPRAK',
  'AFS_ONDBAS',
  'AFS_ONDVRT',
  'AFS_PODIUM',
  'OAD'],
 ['AV5_SUPERM',
  'AFS_OPRIT',
  'AFS_TREINS',
  'AV5_HAPRAK',
  'AV5_ONDBAS',
  'AV5_ONDVRT',
  'AFS_PODIUM',
  'OAD']]