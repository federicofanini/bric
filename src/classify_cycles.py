import pandas as pd
import numpy as np
from typing import Dict, Tuple
import matplotlib.pyplot as plt

def calculate_development_metrics(df: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    """
    Calcola le metriche di sviluppo per ogni paese.
    
    Args:
        df: DataFrame con i dati dei paesi BRIC
        
    Returns:
        Dict con le metriche medie per paese
    """
    metrics = {}
    
    # Calcola le medie per il gruppo BRIC
    bric_avg_growth = df['gdp_growth'].mean()
    bric_avg_hdi = df['hdi'].mean()
    
    # Calcola le medie per ogni paese
    for country in df['country'].unique():
        country_data = df[df['country'] == country]
        metrics[country] = {
            'avg_growth': country_data['gdp_growth'].mean(),
            'avg_hdi': country_data['hdi'].mean(),
            'growth_relative': country_data['gdp_growth'].mean() - bric_avg_growth,
            'hdi_relative': country_data['hdi'].mean() - bric_avg_hdi
        }
    
    return metrics

def classify_development_cycle(metrics: Dict[str, float]) -> Tuple[str, str]:
    """
    Classifica il ciclo di sviluppo di un paese secondo Stewart et al. (2018).
    
    Args:
        metrics: Dizionario con le metriche di sviluppo
        
    Returns:
        Tuple[str, str]: (Classificazione, Motivazione)
    """
    growth_relative = metrics['growth_relative']
    hdi_relative = metrics['hdi_relative']
    
    if growth_relative > 0 and hdi_relative > 0:
        return "Virtuous Cycle", "Alta crescita e alto sviluppo umano rispetto alla media BRIC"
    elif growth_relative > 0 and hdi_relative <= 0:
        return "Growth-Lopsided", "Alta crescita ma basso sviluppo umano rispetto alla media BRIC"
    elif growth_relative <= 0 and hdi_relative > 0:
        return "HD-Lopsided", "Bassa crescita ma alto sviluppo umano rispetto alla media BRIC"
    else:
        return "Vicious Cycle", "Bassa crescita e basso sviluppo umano rispetto alla media BRIC"

def plot_development_typology(metrics: Dict[str, Dict[str, float]], output_path: str):
    """
    Crea il grafico della tipologia di sviluppo.
    
    Args:
        metrics: Dizionario con le metriche per ogni paese
        output_path: Percorso dove salvare il grafico
    """
    plt.figure(figsize=(10, 8))
    
    # Disegna gli assi
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # Colori per ogni tipo di ciclo
    colors = {
        "Virtuous Cycle": "green",
        "Growth-Lopsided": "blue",
        "HD-Lopsided": "orange",
        "Vicious Cycle": "red"
    }
    
    # Plot per ogni paese
    for country, data in metrics.items():
        classification, _ = classify_development_cycle(data)
        plt.scatter(data['growth_relative'], data['hdi_relative'],
                   color=colors[classification], s=100, label=country)
        plt.annotate(country, (data['growth_relative'], data['hdi_relative']),
                    xytext=(5, 5), textcoords='offset points')
    
    # Etichette e titolo
    plt.xlabel('Crescita del PIL relativa alla media BRIC')
    plt.ylabel('HDI relativo alla media BRIC')
    plt.title('Tipologia di Sviluppo dei Paesi BRIC')
    
    # Legenda
    handles = []
    for cycle_type, color in colors.items():
        handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color,
                                markersize=10, label=cycle_type))
    plt.legend(handles=handles, loc='upper left')
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def analyze_cycle_dynamics(df: pd.DataFrame) -> Dict[str, Dict]:
    """
    Analizza le dinamiche del ciclo di sviluppo per ogni paese.
    
    Args:
        df: DataFrame con i dati dei paesi BRIC
        
    Returns:
        Dict con l'analisi dettagliata per ogni paese
    """
    # Calcola le metriche
    metrics = calculate_development_metrics(df)
    
    # Analisi per paese
    analyses = {}
    for country, country_metrics in metrics.items():
        classification, motivation = classify_development_cycle(country_metrics)
        
        analyses[country] = {
            'classification': classification,
            'motivation': motivation,
            'metrics': {
                'avg_growth': country_metrics['avg_growth'],
                'avg_hdi': country_metrics['avg_hdi'],
                'growth_relative': country_metrics['growth_relative'],
                'hdi_relative': country_metrics['hdi_relative']
            },
            'strengths': [],
            'weaknesses': [],
            'recommendations': []
        }
        
        # Analisi dettagliata
        if classification == "Virtuous Cycle":
            analyses[country]['strengths'].append("Performance superiore alla media in entrambi gli indicatori")
            analyses[country]['recommendations'].append("Mantenere le politiche attuali")
        elif classification == "Growth-Lopsided":
            analyses[country]['strengths'].append("Forte performance nella crescita economica")
            analyses[country]['weaknesses'].append("Sviluppo umano inferiore alla media")
            analyses[country]['recommendations'].append("Concentrarsi sul miglioramento dell'HDI")
        elif classification == "HD-Lopsided":
            analyses[country]['strengths'].append("Alto livello di sviluppo umano")
            analyses[country]['weaknesses'].append("Crescita economica inferiore alla media")
            analyses[country]['recommendations'].append("Implementare politiche per stimolare la crescita")
        else:  # Vicious Cycle
            analyses[country]['weaknesses'].append("Performance inferiore alla media in entrambi gli indicatori")
            analyses[country]['recommendations'].append("Interventi strutturali su entrambi i fronti")
    
    return analyses

def generate_cycle_analysis_markdown(analyses: Dict[str, Dict]) -> str:
    """
    Genera un report markdown con l'analisi dei cicli di sviluppo.
    
    Args:
        analyses: Dizionario con le analisi per ogni paese
        
    Returns:
        str: Report in formato markdown
    """
    markdown = "# Analisi dei Cicli di Sviluppo BRIC\n\n"
    
    # Introduzione
    markdown += "## 1. Introduzione\n\n"
    markdown += "Questa analisi classifica i cicli di sviluppo dei paesi BRIC secondo la metodologia di Stewart et al. (2018), "
    markdown += "basandosi sul confronto tra la crescita del PIL pro capite e l'HDI di ogni paese rispetto alla media del gruppo BRIC.\n\n"
    
    # Analisi per paese
    markdown += "## 2. Analisi per Paese\n\n"
    for country, analysis in analyses.items():
        markdown += f"### {country}\n\n"
        markdown += f"**Classificazione**: {analysis['classification']}\n\n"
        markdown += f"**Motivazione**: {analysis['motivation']}\n\n"
        
        # Metriche
        markdown += "**Metriche**:\n"
        markdown += f"- Crescita media del PIL: {analysis['metrics']['avg_growth']:.2f}%\n"
        markdown += f"- HDI medio: {analysis['metrics']['avg_hdi']:.3f}\n"
        markdown += f"- Crescita relativa alla media BRIC: {analysis['metrics']['growth_relative']:.2f}%\n"
        markdown += f"- HDI relativo alla media BRIC: {analysis['metrics']['hdi_relative']:.3f}\n\n"
        
        if analysis['strengths']:
            markdown += "**Punti di Forza**:\n"
            for strength in analysis['strengths']:
                markdown += f"- {strength}\n"
            markdown += "\n"
        
        if analysis['weaknesses']:
            markdown += "**Punti di Debolezza**:\n"
            for weakness in analysis['weaknesses']:
                markdown += f"- {weakness}\n"
            markdown += "\n"
        
        if analysis['recommendations']:
            markdown += "**Raccomandazioni**:\n"
            for rec in analysis['recommendations']:
                markdown += f"- {rec}\n"
            markdown += "\n"
    
    # Conclusioni
    markdown += "## 3. Conclusioni\n\n"
    cycle_counts = {}
    for analysis in analyses.values():
        cycle_type = analysis['classification']
        cycle_counts[cycle_type] = cycle_counts.get(cycle_type, 0) + 1
    
    markdown += "**Distribuzione dei Cicli**:\n"
    for cycle_type, count in cycle_counts.items():
        markdown += f"- {cycle_type}: {count} paesi\n"
    markdown += "\n"
    
    markdown += "### Implicazioni di Policy\n\n"
    markdown += "1. I paesi con cicli virtuosi dovrebbero servire da modello per gli altri\n"
    markdown += "2. I paesi growth-lopsided dovrebbero concentrarsi sul miglioramento dell'HDI\n"
    markdown += "3. I paesi HD-lopsided dovrebbero implementare politiche per stimolare la crescita\n"
    markdown += "4. I paesi con cicli viziosi necessitano di interventi strutturali su entrambi i fronti\n"
    
    return markdown 