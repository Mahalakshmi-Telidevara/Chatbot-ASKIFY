function toggleChatbox() {
    const modal = document.getElementById('chatbot-modal');
    if (modal.style.display === 'none' || modal.classList.contains('hidden')) {
      modal.style.display = 'flex'; // Open chatbox
      modal.classList.remove('hidden');
    } else {
      modal.style.display = 'none'; // Close chatbox
      modal.classList.add('hidden');
    }
  }

function sendMessage() {
  var userInput = document.getElementById('user-input').value;
  if (userInput.trim() !== '') {
      var chatLog = document.getElementById('chat-log');
      
      // Append user message to chat
      var userMessage = document.createElement('div');
      userMessage.classList.add('user-message');
      userMessage.textContent = "You: " + userInput;
      chatLog.appendChild(userMessage);

      // Send the message to Flask server
      fetch('http://127.0.0.1:5000/chat', {  // Use full URL with localhost
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({message: userInput}),  // Key should match Flask code
      })
      .then(response => {
          if (!response.ok) {
              throw new Error("Network response was not ok");
          }
          return response.json();
      })
      .then(data => {
          var botMessage = document.createElement('div');
          botMessage.classList.add('bot-message');
          botMessage.textContent = "Askify: " + data.response;
          chatLog.appendChild(botMessage);
          document.getElementById('user-input').value = '';
          chatLog.scrollTop = chatLog.scrollHeight;  // Auto scroll
      })
      .catch(error => {
          var errorMessage = document.createElement('div');
          errorMessage.classList.add('bot-message');
          errorMessage.textContent = "Askify: Sorry, there was an error connecting to the server.";
          chatLog.appendChild(errorMessage);
          console.error('Error:', error);
      });
  }
}