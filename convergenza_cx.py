import pandas as pd
import matplotlib.pyplot as plt

# %% 1. Lettura dati
df = pd.read_csv('cx.csv')
print(df.columns)
print(df.shape)

iterazioni = df['Cx Monitor: Iteration']
cx = df['Cx Monitor: Cx Monitor']

# %% 2. Media ultime 500 iterazioni
media_cx = cx.tail(500).mean()
print(f'Cx medio (ultime 500 iterazioni): {media_cx:.4f}')

# %% 3. Grafico
plt.figure()
plt.plot(iterazioni, cx, label='Cx')
plt.axhline(media_cx, color='r', linestyle='--', label=f'Media ultime 500 iter = {media_cx:.4f}')
plt.title('Convergenza Cx')
plt.xlabel('Iterazioni')
plt.ylabel('Cx')
plt.xlim(0,1000)
plt.grid()
plt.legend()

# %% 4. Salvataggio
plt.savefig('cx_convergenza.png', dpi=300, bbox_inches='tight')
plt.show()