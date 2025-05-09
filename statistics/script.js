document.getElementById("jobForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const skills = document.getElementById("skills").value.split(',').map(s => s.trim().toLowerCase());
    const location = document.getElementById("location").value.trim();

    const response = await fetch("/recommend", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ skills, location })
    });

    const jobs = await response.json();
    const results = document.getElementById("results");
    results.innerHTML = "<h2>Recommended Jobs</h2>";

    if (jobs.length === 0) {
        results.innerHTML += "<p>No matching jobs found.</p>";
    } else {
        jobs.forEach(job => {
            results.innerHTML += `<p><strong>${job.title}</strong> - ${job.location} (Match Score: ${job.score})</p>`;
        });
    }
});
