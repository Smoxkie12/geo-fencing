function getLocation() {
    const btn = document.getElementById('getLocationBtn');
    const checkBtn = document.getElementById('checkLocationBtn');
    const status = document.getElementById('status');
    const results = document.getElementById('results');

    results.classList.remove('show');
    status.className = 'status show loading';
    status.textContent = '⏳ Fetching your location... allow permission if prompted';
    btn.disabled = true;
    checkBtn.disabled = true;

    if (!navigator.geolocation) {
      status.className = 'status show error';
      status.textContent = '❌ Geolocation is not supported by this browser.';
      btn.disabled = false;
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const lat = position.coords.latitude;
        const lng = position.coords.longitude;
        const accuracy = position.coords.accuracy;

        document.getElementById('lat').textContent = lat.toFixed(6);
        document.getElementById('lng').textContent = lng.toFixed(6);
        document.getElementById('accuracy').textContent = `± ${Math.round(accuracy)} m`;

        const badge = document.getElementById('accuracyBadge');
        if (accuracy <= 20) {
          badge.innerHTML = '<span class="accuracy-badge accuracy-good">GOOD</span>';
        } else if (accuracy <= 100) {
          badge.innerHTML = '<span class="accuracy-badge accuracy-medium">MEDIUM</span>';
        } else {
          badge.innerHTML = '<span class="accuracy-badge accuracy-poor">POOR</span>';
        }

        document.getElementById('timestamp').textContent =
          'Captured at ' + new Date(position.timestamp).toLocaleTimeString();

        status.className = 'status show loading';
        status.textContent = '✅ Location captured. Click Save + Check Location to continue.';
        results.classList.add('show');
        btn.disabled = false;
        checkBtn.disabled = false;
      },
      (error) => {
        const checkBtn = document.getElementById('checkLocationBtn');
        status.className = 'status show error';
        let message = '❌ ';
        switch(error.code) {
          case error.PERMISSION_DENIED:
            message += 'Location permission denied. Enable it in browser settings and try again.';
            break;
          case error.POSITION_UNAVAILABLE:
            message += 'Location information unavailable.';
            break;
          case error.TIMEOUT:
            message += 'Request timed out. Try again.';
            break;
          default:
            message += 'An unknown error occurred.';
        }
        status.textContent = message;
        btn.disabled = false;
        checkBtn.disabled = true;
      },
      {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0
      }
    );
  }


  function postLocation() {
    const btn = document.getElementById('checkLocationBtn');
    const status = document.getElementById('status');
    const lat = document.getElementById('lat').textContent;
    const lng = document.getElementById('lng').textContent;
    const accuracy = document.getElementById('accuracy').textContent;

    if (lat === '-' || lng === '-' || accuracy === '-') {
      alert('Please get your location first.');
      return;
    }

    btn.disabled = true;
    status.className = 'status show loading';
    status.textContent = '⏳ Saving and checking location...';

    const data = {
      latitude: parseFloat(lat),
      longitude: parseFloat(lng),
      accuracy: parseInt(accuracy.replace('± ', '').replace(' m', ''), 10),
      timestamp: new Date().toISOString()
    };

    fetch('/api/check-location', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
      if (result.inside) {
        status.className = 'status show loading';
        status.textContent = `✅ Permit: you are ${result.distance_m}m from the office (radius ${result.radius_m}m).`;
      } else {
        status.className = 'status show error';
        status.textContent = `❌ Denied: you are ${result.distance_m}m from the office (radius ${result.radius_m}m).`;
      }
      btn.disabled = false;
    })
    .catch(error => {
      console.error('Error posting location:', error);
      status.className = 'status show error';
      status.textContent = '❌ Failed to save or validate location. Check the server and try again.';
      btn.disabled = false;
    });
  }
