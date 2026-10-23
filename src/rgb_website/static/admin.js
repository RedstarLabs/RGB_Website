const form = document.querySelector("#admin-form");
const tokenInput = document.querySelector("#admin-token");
const message = document.querySelector("#admin-message");

function showMessage(text, error = false) {
  message.textContent = text;
  message.classList.toggle("error", error);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const token = tokenInput.value;
  showMessage("Export wird vorbereitet …");
  try {
    const response = await fetch("/api/admin/export", {
      headers: { "X-Admin-Token": token },
    });
    if (!response.ok) {
      showMessage(
        response.status === 401
          ? "Authentifizierung fehlgeschlagen."
          : "Der Export ist derzeit nicht verfügbar.",
        true,
      );
      return;
    }
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = "responses.csv";
    link.click();
    URL.revokeObjectURL(url);
    showMessage("Export wurde heruntergeladen.");
  } catch {
    showMessage("Netzwerkfehler. Der Export wurde nicht erstellt.", true);
  } finally {
    tokenInput.value = "";
  }
});
