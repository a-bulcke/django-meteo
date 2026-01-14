// Fonction pour créer un graphique
function createChart(canvasId, label, apiUrl, borderColor, backgroundColor) {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById(canvasId).getContext('2d');
            const mesures = data.donnees;
 
            if (mesures.length === 0) {
                ctx.fillText('Aucune donnée disponible', 10, 20);
                return;
            }
 
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: mesures.map(m => {
                        const date = new Date(m.timestamp);
                        return date.toLocaleTimeString('fr-FR', {
                            hour: '2-digit',
                            minute: '2-digit'
                        });
                    }),
                    datasets: [{
                        label: label,
                        data: mesures.map(m => m.valeur),
                        borderColor: borderColor,
                        backgroundColor: backgroundColor,
                        tension: 0.4,
                        fill: true,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        pointBackgroundColor: borderColor,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: false,
                            title: {
                                display: true,
                                text: label
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Erreur lors du chargement du graphique:', error));
}
 
// Créer le graphique de température au chargement
document.addEventListener('DOMContentLoaded', function() {
    createChart(
        'temperatureChart',
        'Température (°C)',
        '/api/mesures/temperature/',
        'rgb(255, 99, 132)',
        'rgba(255, 99, 132, 0.1)'
    );
    // TODO : Ajouter les appels createChart pour pression et humidité
});
 
// Actualiser les données toutes les 30 secondes
setInterval(() => location.reload(), 30000);
