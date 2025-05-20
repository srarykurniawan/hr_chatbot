function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value;
    if (!message) return;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
        .then(res => res.json())
        .then(data => {
            const chatArea = document.getElementById("chatArea");
            chatArea.innerHTML += `<div><strong>Anda:</strong> ${message}</div>`;
            chatArea.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div><hr>`;
            input.value = "";
        });
}