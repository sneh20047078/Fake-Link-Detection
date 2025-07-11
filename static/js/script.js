lucide.createIcons();

// tsParticles Background
tsParticles.load("tsparticles", {
    fullScreen: { enable: false },
    background: { color: "#0a0a23" },
    particles: {
        number: { value: 50 },
        size: { value: 3 },
        color: { value: "#ffffff" },
        opacity: { value: 0.3 },
        move: { enable: true, speed: 1 },
        links: { enable: true, color: "#888", opacity: 0.2 }
    }
});

// --- Model Selection Logic ---
const modelSelectionGrid = document.getElementById('modelSelectionGrid');
const selectedModelInput = document.getElementById('selectedModelInput');
const modelCards = document.querySelectorAll('.model-card');

modelCards.forEach(card => {
    card.addEventListener('click', () => {
        modelCards.forEach(c => {
            c.classList.remove('ring-2', 'ring-blue-400');
            const badge = c.querySelector('.selected-badge');
            if (badge) badge.remove();
        });
        card.classList.add('ring-2', 'ring-blue-400');
        const newBadge = document.createElement('span');
        newBadge.className = 'selected-badge inline-block mt-2 bg-blue-600 text-white text-xs px-2 py-1 rounded';
        newBadge.textContent = 'Selected';
        card.appendChild(newBadge);
        const selectedModel = card.getAttribute('data-model');
        selectedModelInput.value = selectedModel;
    });
});

// --- Prediction Text Typing Effect ---
if (typeof prediction !== 'undefined') {
    const predEl = document.getElementById("predictionText");
    let i = 0;
    if (prediction && predEl) {
        const typingInterval = setInterval(() => {
            if (i < prediction.length) {
                predEl.textContent += prediction.charAt(i);
                i++;
            } else {
                clearInterval(typingInterval);
            }
        }, 80);
    }
}

// --- FIXED: Sound Toggle Logic ---
const soundToggle = document.getElementById('soundToggle');
const bgMusic = document.getElementById('bgMusic');

soundToggle.addEventListener('click', () => {
    // Toggle music playback
    if (bgMusic.paused) {
        bgMusic.play().catch(e => console.error("Audio play failed:", e));
        // Set the button's HTML to the "playing" icon placeholder
        soundToggle.innerHTML = '<i data-lucide="volume-2" class="w-6 h-6"></i>';
    } else {
        bgMusic.pause();
        // Set the button's HTML to the "muted" icon placeholder
        soundToggle.innerHTML = '<i data-lucide="volume-x" class="w-6 h-6"></i>';
    }
    // Tell Lucide to process the new icon placeholder inside the button
    lucide.createIcons();
}); 

// --- Report Modal Logic ---
const showReportBtn = document.getElementById('showReportBtn');
const reportModal = document.getElementById('reportModal');
const closeReportBtn = document.getElementById('closeReportBtn');

let chartDrawn = false;
let perLinkChartDrawn = false;

if (showReportBtn && reportModal && closeReportBtn) {
  showReportBtn.addEventListener('click', function() {
    reportModal.classList.remove('hidden');
    if (!chartDrawn && typeof Chart !== 'undefined') {
      const ctx = document.getElementById('accuracyChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: modelNames,
          datasets: [
            {
              label: 'Accuracy',
              data: accuracies,
              backgroundColor: 'rgba(54, 162, 235, 0.6)'
            },
            {
              label: 'Precision',
              data: precisions,
              backgroundColor: 'rgba(255, 206, 86, 0.6)'
            },
            {
              label: 'Recall',
              data: recalls,
              backgroundColor: 'rgba(75, 192, 192, 0.6)'
            },
            {
              label: 'F1-score',
              data: f1s,
              backgroundColor: 'rgba(153, 102, 255, 0.6)'
            }
          ]
        },
        options: {
          responsive: true,
          scales: {
            y: { beginAtZero: true, max: 1 }
          }
        }
      });
      chartDrawn = true;
    }
    if (typeof perLinkModelNames !== 'undefined' && !perLinkChartDrawn && document.getElementById('perLinkChart')) {
      const ctx2 = document.getElementById('perLinkChart').getContext('2d');
      new Chart(ctx2, {
        type: 'bar',
        data: {
          labels: perLinkModelNames,
          datasets: [{
            label: 'Prediction Probability',
            data: perLinkProbabilities,
            backgroundColor: 'rgba(255, 99, 132, 0.6)'
          }]
        },
        options: {
          responsive: true,
          scales: {
            y: { beginAtZero: true, max: 1 }
          }
        }
      });
      perLinkChartDrawn = true;
    }
  });
  closeReportBtn.addEventListener('click', function() {
    reportModal.classList.add('hidden');
  });
} 