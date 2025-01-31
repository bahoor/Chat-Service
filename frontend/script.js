document.addEventListener("DOMContentLoaded", function() {
    // Fetch and display messages when the page is loaded
    fetchMessages();

    // Handle form submission
    const form = document.getElementById("message-form");
    form.addEventListener("submit", async function(event) {
        event.preventDefault();

        // Get the input values
        const sender = document.getElementById("sender").value;
        const content = document.getElementById("content").value;

        // Prepare message data
        const message = {
            sender: sender,
            content: content
        };

        // Send the message to the backend
        await sendMessage(message);

        // Clear the input fields
        document.getElementById("sender").value = "";
        document.getElementById("content").value = "";

        // Fetch and display updated messages
        fetchMessages();
    });
});

// Function to fetch and display all messages
async function fetchMessages() {
    try {
        // Fetch messages from the backend
        const response = await fetch("http://localhost:8000/message");
        if (!response.ok) throw new Error("Failed to fetch messages");

        const messages = await response.json(); // Convert response to JSON

        const messagesContainer = document.getElementById("messages");
        messagesContainer.innerHTML = ""; // Clear existing messages before displaying new ones

        // Display each message
        messages.forEach(message => {
            const messageElement = document.createElement("div");
            messageElement.classList.add("message");
            messageElement.innerHTML = `<strong>${message.sender}:</strong> ${message.content}`;
            messagesContainer.appendChild(messageElement);
        });
    } catch (error) {
        console.error("Error fetching messages:", error);
    }
}

// Function to send a new message to the backend
async function sendMessage(message) {
    try {
        const response = await fetch("http://localhost:8000/message", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(message)
        });
        if (!response.ok) throw new Error("Failed to send message");

        const newMessage = await response.json();
        console.log("Message sent:", newMessage);
    } catch (error) {
        console.error("Error sending message:", error);
    }
}
