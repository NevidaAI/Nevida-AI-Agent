async function fetchHistory() {
    const response = await fetch('/api/history');
    const data = await response.json();
    const table = document.getElementById('history-table');
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.timestamp}</td>
            <td>${row.temperature}</td>
            <td>${row.gpu_utilization}</td>
            <td>${row.power_draw}</td>
        `;
        table.appendChild(tr);
    });
}
