const task = document.getElementById("task");
const inputText = document.getElementById("inputText");
const submitBtn = document.getElementById("submitBtn");
const result = document.getElementById("result");
const loading = document.getElementById("loading");


submitBtn.addEventListener("click", async () => {
    const text = inputText.value.trim();

    if (!text) {
        result.textContent = "Please enter some content first.";
        return;
    }

    const selectedTask = task.value;

    let endpoint = "";

    if (selectedTask === "qa") {
        endpoint = "/qa";
    } else if (selectedTask === "explain") {
        endpoint = "/explain";
    } else if (selectedTask === "quiz") {
        endpoint = "/quiz";
    } else if (selectedTask === "summarize") {
        endpoint = "/summarize";
    } else if (selectedTask === "learn") {
        endpoint = "/learn/recommendations";
    }

    loading.classList.remove("hidden");
    result.textContent = "";

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        if (Array.isArray(data.result)) {
            result.textContent = JSON.stringify(data.result, null, 2);
        } else {
            result.textContent = data.result;
        }

    } catch (error) {
        result.textContent = "Error: " + error.message;
    } finally {
        loading.classList.add("hidden");
    }
});