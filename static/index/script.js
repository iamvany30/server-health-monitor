document.addEventListener('DOMContentLoaded', () => {
    const fetchData = async () => {
        try {
            const response = await fetch('/data');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            
            // Update the elements with fetched data
            updateStatus('cpu', data.cpu_usage);
            updateStatus('disk', data.disk_usage);
            updateStatus('memory', data.memory_usage);
            updateStatus('processes', data.total_processes);
            updateStatus('status', data.status);
            updateTimestamp();
        } catch (error) {
            console.error('Error fetching data:', error);
            document.querySelectorAll('.status .metric-value').forEach(el => el.textContent = 'Error loading data');
            document.getElementById('timestamp').textContent = 'Error loading timestamp';
        }
    };

    const updateStatus = (id, value) => {
        const element = document.querySelector(`#${id} .metric-value`);
        if (element) {
            element.textContent = value !== 'N/A' ? `${value}` : 'N/A';
            element.classList.add('value-update'); // Trigger animation
            setTimeout(() => element.classList.remove('value-update'), 500); // Remove animation class after animation
        }
    };

    const updateTimestamp = () => {
        const timestampElement = document.getElementById('timestamp');
        const now = new Date().toLocaleString();
        timestampElement.textContent = `Last updated: ${now}`;
    };

    // Fetch data initially and then every 10 seconds
    fetchData();
    setInterval(fetchData, 10000);
});