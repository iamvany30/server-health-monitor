function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cpu').innerText = 'CPU Usage: ' + data.cpu_usage + '%';
            document.getElementById('disk').innerText = 'Disk Usage: ' + data.disk_usage + '%';
            document.getElementById('memory').innerText = 'Memory Usage: ' + data.memory_usage + '%';
            document.getElementById('processes').innerText = 'Total Processes: ' + data.total_processes;
            document.getElementById('status').innerText = 'Status: ' + data.status;
            document.getElementById('timestamp').innerText = 'Updated: ' + new Date().toLocaleString();
        });
}
setInterval(fetchData, 2000);

// Добавляем класс js-enabled к body при загрузке JavaScript
document.body.classList.add('js-enabled');