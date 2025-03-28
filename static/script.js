document.getElementById("design-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    try {
        const response = await fetch("/generate", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const blob = await response.blob();
            const imageUrl = URL.createObjectURL(blob);

            document.getElementById("generated-image").src = imageUrl;
            document.getElementById("download-button").href = imageUrl;
            document.getElementById("result-section").classList.remove("hidden");
        } else {
            const error = await response.json();
            alert(error.error || "Failed to generate design");
        }
    } catch (error) {
        alert("Network error. Check server logs.");
    }
});
