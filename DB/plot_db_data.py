data_path = 'DB/data1.db'

def plot_data():
    import sqlite3
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from datetime import datetime

    conn = sqlite3.connect(data_path)
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    data = c.fetchall()
    conn.close()

    samples = range(len(data))
    adcs = [d[1] for d in data]
    temperatures = [d[2] for d in data]
    timestamps = [datetime.strptime(d[3], '%Y-%m-%d %H:%M:%S') for d in data]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

    ax1.plot(samples, adcs, label='ADC', linestyle='-')
    ax1.set_ylabel('ADC Values')
    ax1.legend(loc='upper right')

    ax2.plot(samples, temperatures, label='Temperature', linestyle='--')
    ax2.set_ylabel('Temperature')
    ax2.legend(loc='upper right')

    ax3.plot(samples, timestamps, label='Timestamp', linestyle='-.')
    ax3.set_xlabel('Samples')
    ax3.set_yticks([])  # Remove y-axis labels
    ax3.legend(loc='upper right')

    plt.suptitle('ADC, Temperature, and Timestamp over Samples')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

plot_data()