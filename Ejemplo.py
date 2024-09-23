import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import statsmodels.api as sm



# Generar datos simulados para demostración
np.random.seed(42)
n_periods = 120  # 10 años de datos mensuales
trend = np.linspace(0, 20, n_periods)
seasonal_pattern = 10 + 5 * np.sin(np.linspace(0, 2 * np.pi, n_periods))
noise = np.random.normal(0, 2, n_periods)
data = trend + seasonal_pattern + noise

# Crear un DataFrame con la serie temporal simulada
dates = pd.date_range(start='2010-01-01', periods=n_periods, freq='M')
df = pd.DataFrame({'Date': dates, 'Value': data})
df.set_index('Date', inplace=True)

# Aplicar el modelo de Holt-Winters (multiplicativo por la estacionalidad variable)
model = ExponentialSmoothing(df['Value'], trend='add', seasonal='mul', seasonal_periods=12)
fit_model = model.fit()

# Crear predicciones para 24 meses futuros
forecast = fit_model.forecast(24)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Datos Originales')
plt.plot(fit_model.fittedvalues.index, fit_model.fittedvalues, label='Ajuste del Modelo', color='orange')
plt.plot(forecast.index, forecast, label='Pronóstico', color='green')
plt.title('Modelo Holt-Winters - Ajuste y Pronóstico')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()
