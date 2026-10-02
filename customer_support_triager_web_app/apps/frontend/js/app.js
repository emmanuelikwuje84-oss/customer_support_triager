const form = document.getElementById("ticket-form");
const domainSelect = document.getElementById("domain");

async function loadDomains() {
    try {
        const response = await fetch("/api/organizations/");

        if (!response.ok) {
            throw new Error("Could not load domains.");
        }

        const domains = await response.json();

        domainSelect.innerHTML = "";

        domains.forEach((domain) => {
            const option = document.createElement("option");
            option.value = domain.id;
            option.textContent = domain.name;
            domainSelect.appendChild(option);
        });
    } catch (error) {
        domainSelect.innerHTML =
            '<option value="">Unable to load domains</option>';
        console.error(error);
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const button = form.querySelector("button");
    button.disabled = true;
    button.textContent = "Analyzing...";

    const data = {
        customer_name: document.getElementById("customer-name").value.trim(),
        domain: domainSelect.value,
        complaint: document.getElementById("complaint").value.trim(),
    };

    try {
        const response = await fetch("/api/tickets/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data),
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Something went wrong.");
        }

        document.getElementById("ticket-id").textContent = result.ticket_id;
        document.getElementById("department").textContent = result.department;
        document.getElementById("intent").textContent = result.intent;
        document.getElementById("urgency").textContent = result.urgency;
        document.getElementById("sentiment").textContent = result.sentiment;
        document.getElementById("route").textContent = result.route;
        document.getElementById("response").textContent =
            result.suggested_response;

        document.getElementById("result").classList.remove("hidden");
    } catch (error) {
        alert(error.message);
    } finally {
        button.disabled = false;
        button.textContent = "Submit Ticket";
    }
});

loadDomains();
