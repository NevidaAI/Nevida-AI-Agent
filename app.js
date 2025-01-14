async function fetchMetrics() {
    const response = await fetch('/api/metrics');
    const data = await response.json();
    document.getElementById('temp').textContent = data.temperature;
    document.getElementById('util').textContent = data.gpu_utilization;
    document.getElementById('power').textContent = data.power_draw;
}

async function optimize() {
    const response = await fetch('/api/optimize', { method: 'POST' });
    const data = await response.json();
    alert(`Optimization Suggestion: ${data.suggestion}`);
}

setInterval(fetchMetrics, 5000);
