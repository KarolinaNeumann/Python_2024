# zkouska vyhledani subjektu jabuk neumann - nalezeno 15 subjektu - vypis struktury 1. zaznamu

data = {
        'pocetCelkem': 15, 
        'ekonomickeSubjekty': 
            [
                {
                'ico': '01625616', 
                'obchodniJmeno': 'Jakub Neumann',
                'sidlo': 
                    {
                    'kodStatu': 'CZ',
                    'nazevStatu': 'Česká republika',
                    'kodKraje': 27, 
                    'nazevKraje': 'Středočeský kraj',
                    'kodOkresu': 3211,
                    'nazevOkresu': 'Příbram',
                    'kodObce': 540901, 
                    'nazevObce': 'Nový Knín',
                    'kodUlice': 527475,
                    'nazevUlice': 'Na Smíchově',
                    'cisloDomovni': 233,
                    'kodCastiObce': 107638,
                    'nazevCastiObce': 'Nový Knín',
                    'kodAdresnihoMista': 22927468,
                    'psc': 26203,
                    'textovaAdresa': 'Na Smíchově 233, 26203 Nový Knín',
                    'typCisloDomovni': '1',
                    'standardizaceAdresy': True
                     },
                'pravniForma': '101',
                'financniUrad': '063',
                'datumVzniku': '2013-04-22',
                'datumAktualizace': '2023-08-09',
                'icoId': '01625616', 
                'adresaDorucovaci': 
                    {
                    'radekAdresy1': 'Na Smíchově 233', 
                    'radekAdresy2': '26203 Nový Knín'
                    },
                'seznamRegistraci':
                    {
                    'stavZdrojeVr': 'NEEXISTUJICI',
                    'stavZdrojeRes': 'AKTIVNI', 
                    'stavZdrojeRzp': 'AKTIVNI', 
                    'stavZdrojeNrpzs': 'NEEXISTUJICI', 
                    'stavZdrojeRpsh': 'NEEXISTUJICI', 
                    'stavZdrojeRcns': 'NEEXISTUJICI', 
                    'stavZdrojeSzr': 'NEEXISTUJICI', 
                    'stavZdrojeDph': 'NEEXISTUJICI', 
                    'stavZdrojeSd': 'NEEXISTUJICI', 
                    'stavZdrojeIr': 'NEEXISTUJICI', 
                    'stavZdrojeCeu': 'NEEXISTUJICI', 
                    'stavZdrojeRs': 'NEEXISTUJICI', 
                    'stavZdrojeRed': 'NEEXISTUJICI'
                    }, 
                'primarniZdroj': 'rzp',
                'dalsiUdaje': 
                    [
                        {
                        'obchodniJmeno': 
                            [
                                {
                                'obchodniJmeno': 'Jakub Neumann', 
                                'primarniZaznam': True
                                }
                            ], 
                        'sidlo': 
                            [
                                {
                                'sidlo': 
                                    {
                                    'kodStatu': 'CZ',
                                    'nazevStatu': 'Česká republika',
                                    'kodKraje': 27, 
                                    'nazevKraje': 'Středočeský kraj',
                                    'kodOkresu': 3211, 
                                    'nazevOkresu': 'Příbram',
                                    'kodObce': 540901, 
                                    'nazevObce': 'Nový Knín', 
                                    'kodUlice': 527475, 
                                    'nazevUlice': 'Na Smíchově',
                                    'cisloDomovni': 233, 
                                    'kodCastiObce': 107638, 
                                    'nazevCastiObce': 'Nový Knín',
                                    'kodAdresnihoMista': 22927468,
                                    'psc': 26203,
                                    'textovaAdresa': 'Na Smíchově 233, 26203 Nový Knín',
                                    'typCisloDomovni': '1', 
                                    'standardizaceAdresy': True
                                    }, 
                                'primarniZaznam': True
                                }
                            ], 
                            'pravniForma': '101', 
                            'datovyZdroj': 'res'
                        }, 
                        {'obchodniJmeno': 
                            [   
                                {
                                'obchodniJmeno': 'Jakub Neumann', 
                                'primarniZaznam': True
                                }
                            ], 
                        'sidlo': 
                            [
                                {'sidlo': 
                                    {
                                    'kodStatu': 'CZ', 
                                    'nazevStatu': 'Česká republika', 
                                    'kodKraje': 27, 
                                    'nazevKraje': 'Středočeský kraj', 
                                    'kodOkresu': 3211, 
                                    'nazevOkresu': 'Příbram', 
                                    'kodObce': 540901, 
                                    'nazevObce': 'Nový Knín', 
                                    'kodUlice': 527475, 
                                    'nazevUlice': 'Na Smíchově', 
                                    'cisloDomovni': 233, 
                                    'kodCastiObce': 107638, 
                                    'nazevCastiObce': 'Nový Knín', 
                                    'kodAdresnihoMista': 22927468, 
                                    'psc': 26203, 
                                    'textovaAdresa': 'Na Smíchově 233, 26203 Nový Knín', 
                                    'typCisloDomovni': '1', 
                                    'standardizaceAdresy': True
                                    }, 
                                'primarniZaznam': True
                                }
                            ], 
                        'pravniForma': '101', 
                        'datovyZdroj': 'rzp'
                        }
                    ], 
                'czNace': ['01493', '309', '32', '43120', '461', '471', '63910', '6820', '7490']
                },          
                #dalsi subj {'ico': '05959845'}
            ]
        }

print(data["ekonomickeSubjekty"][0]["ico"])
print(data["ekonomickeSubjekty"][0]["obchodniJmeno"])