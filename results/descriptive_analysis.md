# Descriptive Analysis of BRIC Data

## 1. Basic Statistics

### By Country

#### Brazil

|       |    year | gdp_per_capita | gdp_growth |       hdi | education_expenditure | health_expenditure |     gcf |
| :---- | ------: | -------------: | ---------: | --------: | --------------------: | -----------------: | ------: |
| count |      39 |              1 |         39 |        39 |                    19 |                 19 |      20 |
| mean  | 2009.67 |        6817.78 |    1.48942 |  0.720923 |                5.2911 |            8.47739 | 18.5013 |
| std   |  5.8189 |            nan |    2.72574 | 0.0315498 |              0.895716 |           0.588337 | 2.42895 |
| min   |    2000 |        6817.78 |    -4.3064 |     0.668 |               3.75037 |            7.73638 | 14.6256 |
| 25%   |    2005 |        6817.78 |  0.0770005 |     0.696 |               4.67484 |            8.02334 | 17.1178 |
| 50%   |    2010 |        6817.78 |    1.78204 |     0.722 |                5.6488 |            8.33457 | 18.3272 |
| 75%   |  2014.5 |        6817.78 |    3.04696 |    0.7525 |               5.95598 |            8.80308 | 20.7656 |
| max   |    2019 |        6817.78 |    6.62783 |     0.764 |               6.32048 |            9.61449 | 21.8263 |

#### China

|       |    year | gdp_per_capita | gdp_growth |       hdi | education_expenditure | health_expenditure |     gcf |
| :---- | ------: | -------------: | ---------: | --------: | --------------------: | -----------------: | ------: |
| count |      35 |              0 |         35 |        35 |                    15 |                 15 |      20 |
| mean  | 2010.57 |            nan |    8.36588 |  0.698086 |               3.69751 |            4.54547 | 42.1344 |
| std   | 5.41939 |            nan |    2.22029 | 0.0529013 |              0.654281 |           0.505617 | 3.80449 |
| min   |    2000 |            nan |    5.57532 |     0.586 |               2.39191 |            3.67491 |  33.573 |
| 25%   |  2006.5 |            nan |    6.42074 |     0.662 |               3.59573 |            4.20337 | 40.2372 |
| 50%   |    2011 |            nan |     7.6386 |     0.706 |               4.02442 |            4.56585 | 42.8223 |
| 75%   |    2015 |            nan |    9.40817 |     0.741 |               4.12057 |            4.95892 | 45.4732 |
| max   |    2019 |            nan |    13.6358 |     0.775 |               4.29789 |            5.35028 | 46.6601 |

#### India

|       |    year | gdp_per_capita | gdp_growth |       hdi | education_expenditure | health_expenditure |     gcf |
| :---- | ------: | -------------: | ---------: | --------: | --------------------: | -----------------: | ------: |
| count |      36 |              1 |         36 |        36 |                    16 |                 16 |      20 |
| mean  | 2010.06 |        756.704 |    5.12342 |  0.574194 |               3.80343 |            3.49875 | 34.4777 |
| std   | 5.81105 |            nan |    1.67674 | 0.0489949 |              0.429384 |           0.375107 |  4.4887 |
| min   |    2000 |        756.704 |    1.61413 |      0.49 |               3.14285 |               2.86 | 25.6773 |
| 25%   |    2005 |        756.704 |    3.95314 |     0.532 |                3.3714 |              3.265 | 30.6926 |
| 50%   |  2010.5 |        756.704 |     6.0058 |     0.579 |                 3.871 |               3.55 | 34.1455 |
| 75%   |    2015 |        756.704 |    6.31341 |     0.619 |               4.15037 |               3.76 | 38.5664 |
| max   |    2019 |        756.704 |    6.97395 |     0.638 |               4.37693 |               4.03 | 41.9508 |

#### Russia

|       |    year | gdp_per_capita | gdp_growth |       hdi | education_expenditure | health_expenditure |     gcf |
| :---- | ------: | -------------: | ---------: | --------: | --------------------: | -----------------: | ------: |
| count |      39 |              1 |         39 |        39 |                    19 |                 19 |      20 |
| mean  | 2009.56 |        5323.67 |    3.61879 |  0.793308 |               3.84774 |            5.14211 | 22.1399 |
| std   | 5.90181 |            nan |     4.2997 | 0.0323502 |               0.43701 |            0.28834 | 1.86005 |
| min   |    2000 |        5323.67 |   -7.82775 |     0.733 |               2.93979 |               4.76 | 18.6938 |
| 25%   |  2004.5 |        5323.67 |    1.53351 |    0.7655 |               3.70411 |               4.92 | 20.8907 |
| 50%   |    2010 |        5323.67 |    4.17698 |     0.797 |                3.7931 |               5.16 | 22.2698 |
| 75%   |  2014.5 |        5323.67 |    6.80661 |    0.8205 |               3.94007 |               5.33 | 23.3555 |
| max   |    2019 |        5323.67 |    10.4637 |     0.839 |               4.68991 |               5.65 | 25.5012 |

### Interpretazione delle Statistiche di Base

#### Differenze tra Paesi

- **HDI**: Russia mostra il valore più alto (0.793), seguito da Brazil (0.721), China (0.698) e India (0.574)
- **GDP Growth**: China ha la crescita media più alta (8.37%), seguita da India (5.12%), Russia (3.62%) e Brazil (1.49%)
- **Spesa Pubblica**:
  - Brazil spende di più in educazione (5.29%) e salute (8.48%)
  - Russia ha spese moderate (3.85% educazione, 5.14% salute)
  - China e India hanno spese più basse, specialmente in salute

#### Variabilità

- **GDP Growth**: Russia mostra la maggiore volatilità (std dev 4.30), mentre India la minore (1.68)
- **HDI**: Tutti i paesi mostrano bassa variabilità (std dev < 0.06), indicando cambiamenti graduali
- **Spesa Pubblica**: Relativamente stabile nel tempo, con variazioni minime

## 2. Correlation Analysis

|                       | gdp_growth |       hdi | education_expenditure | health_expenditure |
| :-------------------- | ---------: | --------: | --------------------: | -----------------: |
| gdp_growth            |          1 | -0.297434 |             -0.621236 |           -0.56074 |
| hdi                   |  -0.297434 |         1 |              0.301438 |            0.39292 |
| education_expenditure |  -0.621236 |  0.301438 |                     1 |           0.735343 |
| health_expenditure    |   -0.56074 |   0.39292 |              0.735343 |                  1 |

### Interpretazione delle Correlazioni

#### Relazioni Chiave

- **GDP Growth vs HDI**: Correlazione negativa (-0.297) → suggerisce che la crescita non si traduce immediatamente in sviluppo umano
- **Spesa Pubblica**:
  - Forte correlazione positiva tra educazione e salute (0.735)
  - Correlazioni negative con GDP growth, specialmente per educazione (-0.621)
  - Correlazioni positive con HDI, più forte per salute (0.393)

#### Implicazioni

- La spesa pubblica sembra avere un trade-off con la crescita nel breve periodo
- L'HDI è più correlato con la spesa in salute che con quella in educazione
- Le correlazioni suggeriscono effetti ritardati tra crescita e sviluppo umano

## 3. Time Series Analysis

### Brazil

#### gdp_growth

- Mean: 1.49
- Std Dev: 2.73
- Trend (slope): -0.1916

#### hdi

- Mean: 0.72
- Std Dev: 0.03
- Trend (slope): 0.0054

### China

#### gdp_growth

- Mean: 8.37
- Std Dev: 2.22
- Trend (slope): -0.2712

#### hdi

- Mean: 0.70
- Std Dev: 0.05
- Trend (slope): 0.0097

### India

#### gdp_growth

- Mean: 5.12
- Std Dev: 1.68
- Trend (slope): 0.0607

#### hdi

- Mean: 0.57
- Std Dev: 0.05
- Trend (slope): 0.0084

### Russia

#### gdp_growth

- Mean: 3.62
- Std Dev: 4.30
- Trend (slope): -0.4496

#### hdi

- Mean: 0.79
- Std Dev: 0.03
- Trend (slope): 0.0054

### Interpretazione delle Serie Temporali

#### Trend di Crescita

- **Declino Generale**: Brazil, China e Russia mostrano trend negativi nella crescita
- **India**: Unica eccezione con trend positivo (0.0607)
- **Volatilità**: Russia mostra la maggiore variabilità nella crescita

#### Trend HDI

- **Miglioramento Costante**: Tutti i paesi mostrano trend positivi nell'HDI
- **Ritmo di Crescita**:
  - China mostra il miglioramento più rapido (0.0097/anno)
  - India segue con 0.0084/anno
  - Brazil e Russia con 0.0054/anno

#### Implicazioni

- La crescita economica rallenta mentre l'HDI continua a migliorare
- Suggerisce un potenziale disaccoppiamento tra crescita economica e sviluppo umano.
- I paesi potrebbero essere entrati in una fase di maturità economica

## 4. Distribution Analysis

### gdp_growth

- Skewness: -0.50
- Kurtosis: 0.76
- Shapiro-Wilk test p-value: 0.0124

### hdi

- Skewness: -0.56
- Kurtosis: -0.50
- Shapiro-Wilk test p-value: 0.0001

### education_expenditure

- Skewness: 0.77
- Kurtosis: 0.24
- Shapiro-Wilk test p-value: nan

### health_expenditure

- Skewness: 0.71
- Kurtosis: -0.83
- Shapiro-Wilk test p-value: nan

### Interpretazione delle Distribuzioni

#### GDP Growth

- Distribuzione leggermente asimmetrica a sinistra (skewness -0.50)
- Curtosi positiva (0.76) → code più pesanti della normale
- Test di Shapiro-Wilk significativo (p=0.0124) → non normalità

#### HDI

- Asimmetria negativa (-0.56) → concentrazione verso valori alti
- Curtosi negativa (-0.50) → distribuzione più piatta della normale
- Forte non normalità (p=0.0001)

#### Spesa Pubblica

- Educazione: asimmetria positiva (0.77) → alcuni valori alti
- Salute: asimmetria positiva (0.71) ma curtosi negativa (-0.83)
- Distribuzioni relativamente simmetriche ma non normali

#### Implicazioni

- Le distribuzioni non normali suggeriscono la necessità di modelli robusti
- L'asimmetria nelle distribuzioni indica potenziali outlier
- La non normalità potrebbe influenzare l'interpretazione dei test statistici

## 5. Conclusioni Generali

### Principali Risultati

1. **Divergenza Crescita-Sviluppo**:

   - La crescita economica rallenta mentre l'HDI continua a migliorare
   - Suggerisce un potenziale disaccoppiamento tra crescita economica e sviluppo umano.
2. **Pattern di Spesa**:

   - Brazil spende di più in welfare
   - China e India hanno spese più basse ma crescono più velocemente
   - Russia mostra un approccio intermedio
3. **Stabilità vs Crescita**:

   - I paesi con crescita più stabile (India) mostrano miglioramenti più graduali
   - I paesi con maggiore volatilità (Russia) hanno HDI più alto ma crescita instabile

### Limiti e Considerazioni

- Dati mancanti in alcune variabili (es. gdp_per_capita)
- Periodo di osservazione relativamente breve
- Potenziali problemi di non normalità nelle distribuzioni

### Prospettive Future

- Monitorare il decoupling tra crescita e sviluppo umano
- Investigare il ruolo della spesa pubblica nel lungo periodo
- Considerare l'impatto delle politiche specifiche per paese
