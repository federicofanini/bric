import seaborn as sns
import matplotlib.pyplot as plt
import os

def ensure_output_dir():
    os.makedirs('figures', exist_ok=True)

def plot_time_series(df, column, title, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(df['year'], df[column], marker='o')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(f'figures/{filename}.png')
    plt.close()

def plot_scatter(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['gdp_growth'], df['hdi'])
    plt.xlabel('GDP Growth Rate')
    plt.ylabel('HDI')
    plt.title('GDP Growth vs HDI')
    plt.grid(True)
    plt.savefig('figures/scatter.png')
    plt.close()

def plot_heatmap(df):
    plt.figure(figsize=(10, 8))
    corr = df[['gdp_growth', 'hdi', 'education_expenditure', 'health_expenditure']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix')
    plt.savefig('figures/correlation.png')
    plt.close()

def plot_quadrant(df):
    plt.figure(figsize=(10, 6))
    plt.axhline(y=df['hdi'].mean(), color='r', linestyle='--', alpha=0.3)
    plt.axvline(x=df['gdp_growth'].mean(), color='r', linestyle='--', alpha=0.3)
    plt.scatter(df['gdp_growth'], df['hdi'])
    
    for i, row in df.iterrows():
        plt.annotate(str(int(row['year'])), 
                    (row['gdp_growth'], row['hdi']),
                    xytext=(5, 5), textcoords='offset points')
    
    plt.xlabel('GDP Growth Rate')
    plt.ylabel('HDI')
    plt.title('GDP Growth vs HDI Quadrant Analysis')
    plt.grid(True)
    plt.savefig('figures/quadrant.png')
    plt.close()
