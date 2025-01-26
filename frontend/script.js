const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

sendButton.addEventListener("click", () => {
    const message = messageInput.value.trim();
    if (message) {
        const newMessage = document.createElement("div");
        newMessage.textContent = `You: ${message}`;
        messagesDiv.appendChild(newMessage);
        messageInput.value = "";

        // Simulate a bot reply
        setTimeout(() => {
            const botReply = document.createElement("div");
            botReply.textContent = "Bot: Thanks for your message!";
            botReply.style.color = "blue";
            messagesDiv.appendChild(botReply);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }, 1000);
    }
});
