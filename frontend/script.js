async function handleSearch() {
    const query = document.getElementById('search').value.trim();
    if (!query) {
        alert("Please enter a search term.");
        return;
    }

    try {
        const response = await fetch("http://localhost:5000/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ movieName: query }),
        });

        if (response.ok) {
            const data = await response.json();
            showResultsPage(data.movie, data.rating, data.letterboxd);
        } else {
            const errorData = await response.json();
            alert(errorData.error || "An error occurred.");
        }
    } catch (error) {
        console.error("Network error:", error);
        alert("Network error occurred. Try again.");
    }
}